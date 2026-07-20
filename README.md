# 📄 AI Document Q&A Assistant

An AI-powered Document Question Answering Assistant built using **FastAPI**, **Streamlit**, **Gemini API**, and **ChromaDB**. Upload documents in multiple formats and ask natural language questions. The application retrieves the most relevant document chunks using semantic search and generates accurate answers using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 📄 Upload multiple documents
  - PDF
  - DOCX
  - TXT
  - JSON

- 🔍 Semantic document search using Gemini Embeddings

- 🤖 Retrieval-Augmented Generation (RAG)

- 💬 Ask questions about uploaded documents

- 🌍 General AI questions supported when documents don't contain relevant information

- 📚 Source citation showing document name and chunk

- ⚡ FastAPI REST API

- 🎨 Streamlit Chat Interface

- 🗂️ Document Management
  - Upload documents
  - List uploaded documents
  - Delete documents

- 🐳 Dockerized Application

- 🔄 GitHub Actions CI Pipeline

---

# 🏗 Architecture

```

                User

                  │

                  ▼

         Streamlit Frontend

                  │

                  ▼

            FastAPI Backend

                  │

        ┌─────────┴─────────┐

        ▼                   ▼

 Gemini Embedding API   Gemini LLM API

        │

        ▼

      ChromaDB

        │

        ▼

 Uploaded Documents

```

---

## 🛠 Tech Stack

### Backend

- FastAPI
- Python

### Frontend

- Streamlit

### AI

- Google Gemini API
- Gemini Embeddings
- Retrieval-Augmented Generation (RAG)

### Vector Database

- ChromaDB

### DevOps

- Docker
- Docker Compose
- GitHub Actions

---

# 📁 Project Structure

```text
doc-qa-assistant/

├── app/
│   ├── api/
│   ├── models/
│   ├── services/
│   ├── data/
│   └── main.py
│
├── frontend/
│   └── streamlit_app.py
│
├── tests/
│
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/doc-qa-assistant.git

cd doc-qa-assistant
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env`

```env
GEMINI_API_KEY=YOUR_API_KEY
API_URL=http://127.0.0.1:8000
```

---

# Run Backend

```bash
uvicorn app.main:app --reload
```

Backend

```
http://127.0.0.1:8000/docs
```

---

# Run Frontend

```bash
streamlit run frontend/streamlit_app.py
```

Frontend

```
http://localhost:8501
```

---

# Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/upload` | Upload documents |
| POST | `/chat` | Ask questions |
| GET | `/documents` | List uploaded documents |
| DELETE | `/documents/{filename}` | Delete document |

---

# Future Improvements

- User Authentication
- Chat History Database
- Conversation Memory
- Hybrid Search
- OCR Support
- Image Upload
- Audio Upload
- Multi-user Support
- Streaming Responses
- Cloud Storage Integration

---

# Screenshots

Add screenshots of:

- Upload page
- Chat interface
- Source citations
- Docker running
- Swagger UI

---

# License

MIT License