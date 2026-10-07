# GenAI API Calling & Text Generation

A beginner-friendly Python project to understand **API keys, environment variables, LLM API calls, and text generation** using multiple providers.

### Supported Providers

- OpenAI
- Google Gemini
- Ollama

---

## 🚀 Project Roadmap

```text
Project Setup
     ↓
Virtual Environment
     ↓
Git & GitHub
     ↓
.env + API Keys
     ↓
genai_1.py → Configuration
     ↓
genai_provider.py → API Calls
     ↓
chatbot.py → User Interface
     ↓
OpenAI / Gemini / Ollama
     ↓
Generated Text
```

---

## 1. Project Setup

Create and enter the project folder:

```powershell
mkdir GenAi-Practice
cd GenAi-Practice
```

Create virtual environment:

```powershell
python -m venv venv
```

Activate on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again.

Install dependencies:

```powershell
pip install python-dotenv requests openai google-genai
```

Save dependencies:

```powershell
pip freeze > requirements.txt
```

---

## 2. Git Setup

Initialize Git:

```bash
git init
```

Configure Git:

```bash
git config --global user.name "Aamir"
git config --global user.email "your-email@example.com"
```

Check:

```bash
git status
```

---

## 3. Environment Variables

Create a file named:

```text
.env
```

Example:

```env
LLM_PROVIDER=openai
SYSTEM_PROMPT=You are a helpful AI assistant.

OPENAI_API_KEY=your_api_key
OPENAI_MODEL=your_model

GEMINI_API_KEY=your_api_key
GEMINI_MODEL=your_model

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=your_model
```

### What is `.env`?

`.env` stores configuration and sensitive values such as API keys separately from the Python code.

Instead of:

```python
OPENAI_API_KEY = "secret-key"
```

we use:

```python
os.getenv("OPENAI_API_KEY")
```

---

## 4. `.gitignore`

Create `.gitignore`:

```gitignore
.env
venv/
__pycache__/
```

`.gitignore` tells Git which files should **not be tracked or pushed to GitHub**.

- `.env` → contains secrets
- `venv/` → local Python environment
- `__pycache__/` → Python cache

**Never push your real API key to GitHub.**

---

# 5. Project Structure

```text
GenAi-Practice/
│
├── .env
├── .gitignore
├── requirements.txt
├── genai_1.py
├── genai_provider.py
├── chatbot.py
├── README.md
└── venv/
```

---

# 6. `genai_1.py` — Configuration

This file loads values from `.env`.

```python
import os
from dotenv import load_dotenv

load_dotenv()

PROVIDER = os.getenv("LLM_PROVIDER", "openai")

SYSTEM_PROMPT = os.getenv(
    "SYSTEM_PROMPT",
    "You are a helpful AI assistant."
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
```

### Main purpose

```text
.env
 ↓
load_dotenv()
 ↓
os.getenv()
 ↓
Python Configuration
```

It provides:

- Provider
- API keys
- Model names
- System prompt
- Ollama URL

---

# 7. `genai_provider.py` — API Functions

This file contains separate functions for communicating with LLM providers:

```text
ask_openai()
ask_gemini()
ask_ollama()
```

### OpenAI

```python
def ask_openai(message):

    client = OpenAI(
        api_key=genai_1.OPENAI_API_KEY
    )

    response = client.responses.create(
        model=genai_1.OPENAI_MODEL,
        instructions=genai_1.SYSTEM_PROMPT,
        input=message
    )

    return response.output_text
```

Flow:

```text
Message
 ↓
OpenAI Client
 ↓
API Request
 ↓
Model
 ↓
Generated Text
```

### Gemini

```python
def ask_gemini(message):

    client = genai.Client(
        api_key=genai_1.GEMINI_API_KEY
    )

    response = client.models.generate_content(
        model=genai_1.GEMINI_MODEL,
        contents=message,
        config={
            "system_instruction": genai_1.SYSTEM_PROMPT
        }
    )

    return response.text
```

### Ollama

Ollama can run models locally, so the application communicates with its local HTTP server:

```text
Python
 ↓
http://localhost:11434
 ↓
Ollama
 ↓
Local Model
 ↓
Response
```

It uses `requests.post()` to send the message to:

```text
/api/chat
```

---

# 8. `chatbot.py` — Main Application

`chatbot.py` provides the user interface.

It:

1. Checks the configuration
2. Identifies the selected provider
3. Takes user input
4. Calls the correct provider function
5. Displays the response

The main function is:

```python
ask_llm(message)
```

It selects the provider:

```python
if genai_1.PROVIDER == "openai":
    return ask_openai(message)

elif genai_1.PROVIDER == "gemini":
    return ask_gemini(message)

else:
    return ask_ollama(message)
```

Provider is controlled through `.env`:

```env
LLM_PROVIDER=openai
```

or:

```env
LLM_PROVIDER=gemini
```

or:

```env
LLM_PROVIDER=ollama
```

---

# 9. Run the Project

Activate environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Run:

```powershell
python chatbot.py
```

Example:

```text
========================================
      Simple GenAI CLI Chatbot
========================================

Provider: openai
Model: your-model

You: What is Machine Learning?

Assistant: Machine learning is...
```

Commands:

```text
/help    → Show help
/exit    → Exit chatbot
```

---

# 10. GitHub Push

Check files:

```bash
git status
```

Add files:

```bash
git add .
```

Commit:

```bash
git commit -m "Initial GenAI API project"
```

Connect GitHub repository:

```bash
git remote add origin YOUR_GITHUB_REPOSITORY_URL
```

Rename branch:

```bash
git branch -M main
```

Push:

```bash
git push -u origin main
```

Make sure `.env` and `venv/` are not pushed.

---

# 🔄 Complete Architecture

```text
                    .env
                     ↓
                genai_1.py
                Configuration
                     ↓
                chatbot.py
                User Input
                     ↓
                 ask_llm()
                     ↓
          ┌──────────┼──────────┐
          ↓          ↓          ↓
       OpenAI      Gemini     Ollama
          ↓          ↓          ↓
       Cloud API  Cloud API  Local API
          └──────────┼──────────┘
                     ↓
              Generated Text
                     ↓
                   User
```

## 🎯 What You Learn

- Python virtual environments
- `.env` and environment variables
- API key management
- `.gitignore`
- Git & GitHub
- OpenAI API calling
- Gemini API calling
- Ollama local API calling
- Multi-provider LLM architecture
- Building a simple GenAI chatbot

### Core Concept

```text
Prompt → API → LLM Model → Response → Generated Text
```

---
