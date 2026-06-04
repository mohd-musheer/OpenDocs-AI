# OpenDocs-AI

OpenDocs-AI is a Dockerized Vectorless RAG documentation assistant.

It automatically:

1. Crawls documentation websites
2. Extracts content
3. Converts content into Markdown
4. Builds PageIndex document trees
5. Retrieves relevant documentation sections
6. Uses an LLM (Groq) to answer questions grounded in documentation

Unlike traditional RAG systems, OpenDocs-AI does not require embeddings or vector databases.

---

# Features

### Documentation Crawling

Automatically crawl documentation websites from a configuration file.

Supported examples:

* FastAPI
* LangGraph
* LangChain
* React
* Kubernetes
* Internal company documentation

---

### Vectorless Retrieval

Uses PageIndex document trees instead of embeddings.

Benefits:

* No vector database
* Lower storage requirements
* Faster indexing
* Lower infrastructure cost

---

### Multi-Source Support

Load multiple documentation sources using:

```json
[
  {
    "name": "fastapi",
    "url": "https://fastapi.tiangolo.com"
  },
  {
    "name": "langgraph",
    "url": "https://langchain-ai.github.io/langgraph/"
  }
]
```

---

### Memory Support

Includes:

* Session Memory
* Chat Memory
* Summary Memory
* User Profile Memory

---

### Web Interface

Includes a browser-based chat interface.

---

### REST API

Ask questions through HTTP endpoints.

---

# Architecture

```text
sources.json
      ↓
Crawler
      ↓
Raw JSON
      ↓
Markdown Conversion
      ↓
PageIndex Builder
      ↓
PageIndex Trees
      ↓
Retriever
      ↓
Groq LLM
      ↓
Answer
```

---

# Project Structure

```text
OpenDocs-AI
│
├── app
│   ├── agent
│   ├── api
│   ├── crawler
│   ├── llm
│   ├── memory
│   ├── pageindex_engine
│   ├── static
│   ├── templates
│   ├── bootstrap.py
│   ├── config.py
│   └── main.py
│
├── data
│   ├── raw
│   ├── markdown
│   ├── pageindex
│   └── memory
│
├── sources.json
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

---

# Data Flow

## Step 1: Documentation Crawling

Reads:

```text
sources.json
```

Example:

```json
[
  {
    "name": "fastapi",
    "url": "https://fastapi.tiangolo.com"
  }
]
```

Downloads documentation pages and stores them as:

```text
data/raw/*.json
```

---

## Step 2: Markdown Conversion

Converts:

```text
data/raw/*.json
```

into:

```text
data/markdown/*.md
```

---

## Step 3: PageIndex Generation

Converts:

```text
data/markdown/*.md
```

into:

```text
data/pageindex/*.json
```

These files contain structured documentation trees used for retrieval.

---

## Step 4: Retrieval

When a user asks a question:

```text
What is FastAPI?
```

OpenDocs-AI:

1. Searches PageIndex trees
2. Finds matching nodes
3. Sends relevant context to Groq
4. Returns an answer

---

# Configuration

## Groq API Key

Create a Groq API key.

Set environment variable:

```bash
GROQ_API_KEY=your_key_here
```

---

## Sources Configuration

Create:

```text
sources.json
```

Example:

```json
[
  {
    "name": "fastapi",
    "url": "https://fastapi.tiangolo.com"
  },
  {
    "name": "langgraph",
    "url": "https://langchain-ai.github.io/langgraph/"
  }
]
```

---

# Local Development

## Clone Repository

```bash
git clone https://github.com/mohdmusheer/OpenDocs-AI.git

cd OpenDocs-AI
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Bootstrap

Creates:

```text
raw
markdown
pageindex
```

```bash
python -m app.bootstrap
```

---

## Run Application

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

# Docker

## Build Image

```bash
docker build -t opendocs-ai .
```

Verify:

```bash
docker images
```

---

# Docker Hub

Docker Hub Username:

```text
mohdmusheer
```

Tag image:

```bash
docker tag opendocs-ai mohdmusheer/opendocs-ai:latest
```

Push:

```bash
docker login

docker push mohdmusheer/opendocs-ai:latest
```

---

# Pull Image

```bash
docker pull mohdmusheer/opendocs-ai:latest
```

---

# Run Container

## Windows

```bash
docker run ^
-p 8000:8000 ^
-e GROQ_API_KEY=YOUR_GROQ_API_KEY ^
-v %cd%\sources.json:/app/sources.json ^
-v %cd%\data:/app/data ^
mohdmusheer/opendocs-ai:latest
```

---

## Linux

```bash
docker run \
-p 8000:8000 \
-e GROQ_API_KEY=YOUR_GROQ_API_KEY \
-v $(pwd)/sources.json:/app/sources.json \
-v $(pwd)/data:/app/data \
mohdmusheer/opendocs-ai:latest
```

---

# API

## Ask Question

Endpoint:

```http
POST /ask
```

Request:

```json
{
  "question": "What is FastAPI?"
}
```

Response:

```json
{
  "answer": "FastAPI is a modern, high-performance Python web framework..."
}
```

---

# Troubleshooting

## No Documents Found

Delete:

```text
data/pageindex
```

Then rebuild:

```bash
python -m app.bootstrap
```

---

## Empty Answers

Verify:

```text
data/pageindex
```

contains generated files.

Check retrieval logs.

---

## Groq Error

Verify:

```bash
echo %GROQ_API_KEY%
```

or

```bash
echo $GROQ_API_KEY
```

---

# Future Improvements

* Source citations
* Hybrid retrieval
* Incremental indexing
* Authentication
* Multi-user support
* Background indexing jobs
* Docker Compose
* Kubernetes deployment
* Source management UI

---

# License

MIT License

---

# Author

Mohd Musheer

GitHub:
https://github.com/mohd-musheer
