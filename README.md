# 🤖 Smart AI Interviewer

An **Agentic AI-powered Interview Preparation Platform** built using **Streamlit**, **LangChain**, and **Ollama (LLaMA 3)**.
This app helps candidates analyze their resume against a job description, generate interview questions, get mock interview feedback, and evaluate job fit — all **locally** using an LLM.

---

## ✨ Features

* 📄 Upload **Resume & Job Description** (TXT / PDF)
* 🧠 Resume & JD Parsing Agent
* ❓ Interview Question Generator Agent
* 🗣 Mock Interview Feedback Agent (STAR method)
* 📊 Job Suitability Score Agent
* 🦙 Runs **100% locally** using Ollama (LLaMA 3)

---

## 🛠 Tech Stack

* **Python 3.10 (Recommended)**
* **Streamlit** – UI
* **LangChain** – Agent orchestration
* **Ollama** – Local LLM runtime
* **LLaMA 3** – Language model
* **PyPDF** – PDF text extraction

---

## ✅ Prerequisites

### 1️⃣ Install Python (IMPORTANT)

Use **Python 3.10.13** for best stability.

👉 Download: [https://www.python.org/downloads/release/python-31013/](https://www.python.org/downloads/release/python-31013/)

During installation:

* ✅ Check **Add Python to PATH**

Verify:

```bash
python --version
```

Expected:

```text
Python 3.10.13
```

---

### 2️⃣ Install Ollama

👉 Download & install Ollama:

```
https://ollama.com
```

Pull the LLaMA 3 model:

```bash
ollama pull llama3
```

Verify model:

```bash
ollama list
```

> ⚠️ Note: Ollama runs in the background automatically.
> Do NOT run `ollama serve` if it is already running.

---

## 📁 Project Setup

### 3️⃣ Clone / Open Project Folder

```bash
cd F:\Smart AI Interviewer
```

---

### 4️⃣ Create Virtual Environment (venv)

```bash
python -m venv venv
```

Activate venv:

**Windows (PowerShell):**

```bash
venv\Scripts\activate
```

You should see:

```text
(venv)
```

---

### 5️⃣ Install Required Python Libraries

```bash
pip install --upgrade pip
pip install streamlit langchain langchain-ollama langchain-core pypdf
```

Verify installation:

```bash
python -c "import streamlit, langchain, pypdf"
```

---

## ▶️ Run the Application

⚠️ **IMPORTANT:** Do NOT use `python App.py`

Run Streamlit correctly:

```bash
streamlit run App.py
```

The app will open automatically in your browser 🌐

---

## 🧪 Common Issues & Fixes

### ❌ `model 'llama3' not found`

**Fix:**

```bash
ollama pull llama3
```

---

### ❌ `missing ScriptRunContext`

**Cause:** Running app using `python App.py`

**Fix:**

```bash
streamlit run App.py
```

---

### ❌ Port 11434 already in use

This means Ollama is already running ✅
No action needed.

To restart Ollama manually:

```bash
taskkill /IM ollama.exe /F
ollama serve
```

---

## 📌 Recommended Versions

| Tool   | Version   |
| ------ | --------- |
| Python | 3.10.13 ✅ |
| Ollama | Latest    |
| Model  | llama3    |

---

## 🚀 Future Enhancements

* 📈 ATS score visualization
* 🎤 Voice-based mock interviews
* 📄 Export reports as PDF
* 🌐 Cloud deployment
* 🎛 Model switcher (Mistral, Phi, etc.)

---

## 👨‍💻 Author

**Vittal Yakari**
AI / ML Engineer | Python Developer

---

✅ *Built for stable, local, and privacy-friendly AI interview preparation.*
