import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from retriever import retrieve_documents

load_dotenv()

MAX_CONTEXT_LENGTH = 4000

# 🧠 Store conversation history
chat_history = []

def generate_answer(query):

    global chat_history

    # 1️⃣ Retrieve documents
    docs = retrieve_documents(query, k=5)

    context = ""
    total_length = 0
    filtered_docs = []

    for i, doc in enumerate(docs):
        chunk_text = doc.page_content

        if total_length + len(chunk_text) > MAX_CONTEXT_LENGTH:
            break

        context += f"\n[Source {i+1}]\n{chunk_text}\n"
        total_length += len(chunk_text)
        filtered_docs.append(doc)

    # 2️⃣ Initialize LLM
    llm = ChatGroq(
        model_name=os.getenv("GROQ_MODEL"),
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    # 3️⃣ Build messages
    messages = [
        SystemMessage(
    content="""
You are a professional machine learning assistant.

Use only the provided context to answer clearly and concisely.
Do not mention source numbers in the answer.
Do not say "according to the source".

If information is not found, say:
"I don't have enough information in the provided documents."
"""
)
    ]

    # Add previous chat history
    messages.extend(chat_history)

    # Add current user query with context
    messages.append(
        HumanMessage(
            content=f"""
Context:
{context}

Question:
{query}"""
        )
    )

    # 4️⃣ Generate response
    response = llm.invoke(messages)

    # 5️⃣ Save to memory
    chat_history.append(HumanMessage(content=query))
    chat_history.append(AIMessage(content=response.content))

    return response.content, filtered_docs


if __name__ == "__main__":
    while True:
        user_query = input("\nAsk: ")

        if user_query.lower() == "exit":
            break

        answer, sources = generate_answer(user_query)

        print("\nAnswer:\n")
        print(answer)