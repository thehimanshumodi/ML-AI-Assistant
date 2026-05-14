# 🤖 ML Knowledge Assistant (RAG-Based Application)

A production-grade **Retrieval-Augmented Generation (RAG)** application that answers Machine Learning questions using semantic search (FAISS) and Groq LLM for fast, accurate, low-hallucination responses.

> Built and deployed end-to-end by **Himanshu Modi** — containerized with Docker and hosted on AWS EC2.

---

## 🌐 Live Demo

| Platform | URL | Status |
|----------|-----|--------|
| **AWS EC2 (Primary)** | [http://54.235.238.223:8501](http://54.235.238.223:8501) | ✅ Live |
| **Streamlit Cloud (Mirror)** | [https://thehimanshumodi-ml-ai-assistant-app-m04cql.streamlit.app/](https://thehimanshumodi-ml-ai-assistant-app-m04cql.streamlit.app/) | ✅ Live |

---

## 🚀 Features

- 🔎 **Semantic Search** using FAISS vector database
- 📚 **Retrieval-Augmented Generation (RAG)** — reduces hallucination by grounding answers in retrieved documents
- 💬 **Clean interactive chat UI** built with Streamlit
- 📄 **Context-aware answers** from embedded ML documents
- 🔐 **Secure API key handling** using environment variables
- 🐳 **Dockerized** — runs identically on any machine or server
- ☁️ **Cloud deployed** on AWS EC2 — live 24/7

---

## 🏗️ Tech Stack

| Category | Tools |
|----------|-------|
| **Frontend** | Streamlit |
| **LLM Framework** | LangChain |
| **Language Model** | Groq LLM (llama-3.3-70b-versatile) |
| **Vector Database** | FAISS |
| **Embeddings** | Sentence Transformers (HuggingFace) |
| **Containerization** | Docker |
| **Cloud Hosting** | AWS EC2 (t2.micro, Ubuntu 22.04) |
| **Language** | Python 3.10 |

---

## 📂 Project Structure

```
ML-AI-Assistant/
│
├── app.py              # Main Streamlit application (chat UI)
├── llm.py              # RAG pipeline — generate_answer()
├── retriever.py        # FAISS semantic search logic
├── ingest.py           # PDF ingestion & FAISS index creation
├── config.py           # Configuration & environment variables
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker container configuration
├── .dockerignore       # Files excluded from Docker build
├── faiss_index/        # Stored FAISS vector index
├── chunks.pkl          # Saved document chunks
├── .streamlit/         # Streamlit theme configuration
└── README.md
```

---

## ⚙️ How It Works

```
User Question
      │
      ▼
  Embed Question
  (Sentence Transformers)
      │
      ▼
  FAISS Semantic Search
  (find relevant chunks)
      │
      ▼
  Retrieved Context
      │
      ▼
  Groq LLM (llama-3.3-70b)
  generates answer using context
      │
      ▼
  Final Answer (low hallucination)
```

1. PDF documents are loaded, cleaned, and split into chunks
2. Each chunk is converted into vector embeddings
3. Embeddings are stored in a FAISS vector database
4. When a user asks a question:
   - The question is embedded
   - Relevant chunks are retrieved from FAISS
   - Groq LLM generates an answer using retrieved context
5. This architecture **reduces hallucination** and improves factual accuracy

---

## 🐳 Docker Deployment

### Prerequisites
- Docker installed ([docker.com](https://docker.com))
- Groq API key ([console.groq.com](https://console.groq.com))

### Run with Docker

**Step 1 — Clone the repository:**
```bash
git clone https://github.com/thehimanshumodi/ML-AI-Assistant.git
cd ML-AI-Assistant
```

**Step 2 — Create your .env file:**
```bash
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

**Step 3 — Build the Docker image:**
```bash
docker build -t ml-ai-assistant .
```

**Step 4 — Run the container:**
```bash
docker run -p 8501:8501 --env-file .env ml-ai-assistant
```

**Step 5 — Open in browser:**
```
http://localhost:8501
```

---

## ☁️ AWS EC2 Deployment

This project is deployed on **AWS EC2 (t2.micro)** running Ubuntu 22.04 LTS.

### Deployment Architecture

```
User Browser
      │
      │ HTTP Request
      ▼
AWS EC2 (t2.micro)
Ubuntu 22.04 LTS
      │
      │ Port 8501
      ▼
Docker Container
ml-ai-assistant:latest
      │
      ├── Streamlit App
      ├── LangChain + FAISS
      └── Groq LLM API
```

### EC2 Setup Steps

**1. Launch EC2 instance (t2.micro — free tier)**

**2. Install Docker on EC2:**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu
```

**3. Copy project to EC2:**
```bash
scp -i "key.pem" -r ./ML-AI-Assistant ubuntu@YOUR_EC2_IP:~/ML-AI-Assistant
```

**4. Build and run on EC2:**
```bash
cd ~/ML-AI-Assistant
docker build -t ml-ai-assistant .
docker run -d -p 8501:8501 --env-file .env ml-ai-assistant
```

**5. Access live app:**
```
http://YOUR_EC2_PUBLIC_IP:8501
```

### Security Group Configuration
| Type | Protocol | Port | Source |
|------|----------|------|--------|
| SSH | TCP | 22 | Your IP |
| Custom TCP | TCP | 8501 | 0.0.0.0/0 |
| HTTP | TCP | 80 | 0.0.0.0/0 |

---

## 🛠️ Local Installation (Without Docker)

**Step 1 — Clone:**
```bash
git clone https://github.com/thehimanshumodi/ML-AI-Assistant.git
cd ML-AI-Assistant
```

**Step 2 — Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**Step 3 — Install dependencies:**
```bash
pip install -r requirements.txt
```

**Step 4 — Create .env file:**
```
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

**Step 5 — Run:**
```bash
streamlit run app.py
```

---

## 🧠 Example Use Cases

- Understanding Machine Learning fundamentals
- Concept clarification from ML textbooks
- Academic assistance and study tool
- Knowledge-base Q&A system
- Portfolio project demonstrating RAG + Cloud deployment

---

## 📈 Future Improvements

- [ ] Hybrid search (BM25 + Embeddings)
- [ ] Reranking models
- [ ] User document upload feature
- [ ] Chat memory support
- [ ] AWS S3 for model artifact storage
- [ ] CI/CD pipeline with GitHub Actions
- [ ] Migration to scalable vector databases (Pinecone / Weaviate)
- [ ] Custom domain with HTTPS (AWS Route 53 + SSL)

---

## 👨‍💻 Author

**Himanshu Modi**
B.Tech. Information Technology | MLV Textile and Engineering College, Bhilwara

- 📧 modihimanshu66@gmail.com
- 💼 [linkedin.com/in/himanshu-modi-dev](https://linkedin.com/in/himanshu-modi-dev)
- 🐙 [github.com/thehimanshumodi](https://github.com/thehimanshumodi)

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
