import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import pickle
import re

def clean_text(text):
    # Remove Table of Contents lines
    if "Table of Contents" in text:
        return ""

    # Remove lines with lots of dots (......)
    text = re.sub(r"\.{3,}", "", text)

    # Remove page numbers like "vii", "1", etc. alone on line
    text = re.sub(r"^\s*\d+\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*[ivxlcdm]+\s*$", "", text, flags=re.MULTILINE)

    # Remove very short useless lines
    lines = text.split("\n")
    lines = [line for line in lines if len(line.strip()) > 20]

    blacklist_keywords = [
    "table of contents",
    "preface",
    "copyright",
    "isbn"
    ]

    if any(word in text.lower() for word in blacklist_keywords):
     return ""

    return "\n".join(lines)

def ingest_documents(pdf_path, department="general"):
    
    """
    Loads PDF, splits into chunks, creates embeddings,
    and stores in FAISS vector database.
    """
        
    # 1️⃣ Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    for doc in documents:
        doc.page_content = clean_text(doc.page_content)

    # 2️⃣ Add metadata
    for doc in documents:
        doc.metadata["department"] = department
        doc.metadata["source_file"] = os.path.basename(pdf_path)

    # 3️⃣ Chunking strategy (enterprise-level tuning)
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150,
    separators=["\n\n", "\n", ".", " ", ""]
)

    chunks = text_splitter.split_documents(documents)
    
    # Save chunks for BM25
    with open("chunks.pkl", "wb") as f:
        pickle.dump(documents, f)

    print(f"Total Chunks Created: {len(chunks)}")

    # 4️⃣ Create embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # 5️⃣ Store in FAISS
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # 6️⃣ Save locally
    vectorstore.save_local("faiss_index")

    print("Vector store saved successfully!")


if __name__ == "__main__":
    ingest_documents("data/Introduction to Machine Learning with Python ( PDFDrive.com )-min.pdf", department="HR")