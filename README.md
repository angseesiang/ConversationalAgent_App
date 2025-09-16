# 🤖 Conversational Agent

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](#)
[![Flask](https://img.shields.io/badge/Flask-lightgrey)](#)
[![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-green)](#)
[![PyTorch](https://img.shields.io/badge/PyTorch-red)](#)

This project implements a **conversational AI chatbot** powered by GPT-2, with support for basic text preprocessing, evaluation metrics, and a Flask API for interaction.  
Unit tests are provided to ensure functionality.

---

## 📖 Contents

- `conversational_model.py` – Core GPT-2 conversational model  
- `app.py` – Flask application serving chatbot responses  
- `index.html` – Simple frontend for chatting with the bot  
- `data_preprocessor.py` – Utility for loading and preprocessing data  
- `evaluator.py` – Computes accuracy, precision, recall, and F1-score  
- `test_app.py` – Unit tests for the Flask app  
- `requirements.txt` – Project dependencies  
- `url.txt` – Repository reference  

---

## 🚀 How to Use

### 1) Clone this repository

```bash
git clone https://github.com/angseesiang/ConversationalAgent_App.git
cd ConversationalAgent_App
```

### 2) Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Linux / macOS
venv\Scripts\activate      # On Windows
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Start the chatbot server

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser and chat with the bot.  
You can also use the provided `index.html` for a simple UI.

### 5) Run unit tests

```bash
python -m unittest test_app.py
```

This will validate the `/chat` endpoint and ensure the chatbot responds correctly.

---

## 🛠️ Requirements

- Python 3.9+  
- Flask  
- PyTorch  
- Hugging Face Transformers  
- Pandas  
- Scikit-learn  

All dependencies are listed in `requirements.txt`.

---

## 📌 Notes

- The chatbot uses GPT-2 (`gpt2`) for generating responses.  
- API supports both **POST JSON** (`{"message": "Hello"}`) and a frontend chat UI (`index.html`).  
- Preprocessing and evaluation modules can be extended for downstream tasks.  

---

## 📜 License

This project is for **educational purposes only**.
