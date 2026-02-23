# 🤖 ML Knowledge Assistant (RAG-Based Application)

A Retrieval-Augmented Generation (RAG) application built using Streamlit, LangChain, FAISS, and OpenAI.

This project allows users to ask questions about Machine Learning concepts, and the system retrieves relevant information from embedded documents before generating accurate, context-aware responses.

It is designed as a portfolio-ready academic project demonstrating modern LLM + Vector Database integration.

---

## 🚀 Features

- 🔎 Semantic Search using FAISS  
- 📚 Retrieval-Augmented Generation (RAG)  
- 💬 Clean interactive UI built with Streamlit  
- 📄 Context-aware answers from PDF documents  
- 🔐 Secure API key handling using environment variables  
- ☁️ Easily deployable on Streamlit Cloud  

---

## 🏗️ Tech Stack

- **Frontend:** Streamlit  
- **LLM Framework:** LangChain  
- **Vector Database:** FAISS  
- **Embeddings:** OpenAI / Sentence Transformers  
- **Language Model:** OpenAI GPT  

---

## 📂 Project Structure


rag-ml-assistant/
│
├── app.py # Main Streamlit application
├── llm.py # RAG pipeline logic
├── ingest.py # PDF ingestion & FAISS index creation
├── requirements.txt # Project dependencies
├── faiss_index/ # Stored FAISS vector index
├── .gitignore
└── README.md


---

## ⚙️ How It Works

1. PDF documents are loaded and cleaned.
2. Text is split into meaningful chunks.
3. Each chunk is converted into embeddings.
4. Embeddings are stored inside a FAISS vector database.
5. When a user asks a question:
   - The question is embedded.
   - Relevant chunks are retrieved from FAISS.
   - The LLM generates an answer using retrieved context.

This architecture reduces hallucination and improves factual accuracy.

---

## 🧠 Example Use Cases

- Understanding Machine Learning fundamentals  
- Concept clarification from textbooks  
- Academic assistance tool  
- Knowledge-base Q&A system  
- Portfolio project demonstrating RAG architecture  

---

## 🛠️ Local Installation Guide

### 1️⃣ Clone the Repository


git clone https://github.com/YOUR_USERNAME/rag-ml-assistant.git

cd rag-ml-assistant


(Replace `YOUR_USERNAME` with your GitHub username)

---

### 2️⃣ Install Dependencies


pip install -r requirements.txt


---

### 3️⃣ Add Environment Variable

Create a `.env` file in the root directory:


OPENAI_API_KEY=your_api_key_here


⚠️ Do NOT commit `.env` to GitHub.

---

### 4️⃣ Run the Application


streamlit run app.py


The app will start locally in your browser.

---

## ☁️ Deployment (Streamlit Cloud)

1. Push your code to GitHub  
2. Go to https://streamlit.io/cloud  
3. Click **New App**  
4. Select your repository  
5. Choose `app.py` as the main file  
6. Add your environment variable in:

App Settings → Secrets


OPENAI_API_KEY="your_api_key_here"


7. Deploy 🚀  

---

## 🔐 Security Best Practices

- `.env` file is excluded using `.gitignore`  
- API keys are never pushed to GitHub  
- Secrets are configured securely on the deployment platform  

---

## 📈 Future Improvements

- Hybrid search (BM25 + Embeddings)  
- Reranking models  
- User document upload feature  
- Chat memory support  
- Dockerized deployment  
- Migration to scalable vector databases (Pinecone / Weaviate)  

---

## 👨‍💻 Author

**Himanshu Modi**  
Machine Learning Enthusiast  

Built as an academic + portfolio-ready RAG project.

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

