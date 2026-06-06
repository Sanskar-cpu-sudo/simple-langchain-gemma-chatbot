# 🤖 LangChain Gemma Chatbot

A simple AI chatbot built using **LangChain**, **Streamlit**, and **Ollama** with the **Gemma 2B** model.

## 🚀 Features

* Interactive chatbot interface using Streamlit
* Powered by Google's Gemma 2B model through Ollama
* Uses LangChain for prompt management and response generation
* LangSmith integration for tracing and monitoring
* Simple and easy-to-understand project structure

## 🛠️ Technologies Used

* Python
* Streamlit
* LangChain
* Ollama
* Gemma 2B
* Python Dotenv
* LangSmith

## 📂 Project Structure

```text
langchain-gemma-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env (not uploaded)
```

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Sanskar-cpu-sudo/simple-langchain-gemma-chatbot.git
cd simple-langchain-gemma-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Ollama

Download and install Ollama from:

https://ollama.com

### 4. Pull the Gemma Model

```bash
ollama pull gemma:2b
```

### 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=LangChain-Gemma-Chatbot
```

## ▶️ Running the Application

Start Ollama:

```bash
ollama serve
```

Run the Streamlit app:

```bash
streamlit run app.py
```

Open the URL shown in the terminal (usually http://localhost:8501).

## 📸 Screenshot

Add a screenshot of your application here.



## 🎯 Future Improvements

* Chat history support
* Multiple model selection
* Dark mode UI
* File upload support
* Voice input and output
* Conversation memory

## 👨‍💻 Author

Created by Sanskar Petkar


