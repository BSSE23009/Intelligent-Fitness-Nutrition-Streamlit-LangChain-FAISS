# 💪 Fitness, Nutrition & Motivation AI

This project is a Streamlit web app powered by LangChain agents and RAG (Retrieval-Augmented Generation). It can answer questions about workouts, meals, motivation, and the *Starting Strength* book. Users provide their own API keys using a `.env` file.

---

## Features

1. Personalized workout recommendations
2. Nutrition and meal guidance
3. Instant motivational messages
4. RAG-based answers from the *Starting Strength* book
5. Chat interface with AI agents

---

## Requirements

1. Docker
2. `.env` file with your own API keys (OpenAI, Pinecone if using)

---

## Setup

### Step 1: Clone the repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### Step 2: Create `.env` file

```ini
OPENAI_API_KEY=your_openai_key_here
PINECONE_API_KEY=your_pinecone_key_here
```

### Step 3: Build Docker image

```bash
docker build -t fitness_app .
```

### Step 4: Run Docker container

```bash
docker run --env-file .env -p 8501:8501 fitness_app
```

Open your browser and go to [http://localhost:8501](http://localhost:8501) to access the app.

---

Made by **Manan Ch**
