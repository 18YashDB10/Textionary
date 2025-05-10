# 🧠 Textionary

**Textionary** is a Streamlit-powered web application that lets you “chat” with any plain-text file. Simply upload a `.txt` document, ask questions in natural language, and see context-aware answers generated on the fly using Google’s Gemini LLM and LangChain.

👉 **Live Demo:** https://textionary.onrender.com/

---

## 📋 Table of Contents

1. [Features](#-features)  
2. [Tech Stack](#-tech-stack)  
3. [Project Structure](#-project-structure)  
4. [Getting Started](#-getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Clone & Install](#clone--install)  
   - [Environment Variables](#environment-variables)  
   - [Run Locally](#run-locally)  
5. [How It Works](#-how-it-works)  
6. [Usage](#-usage)  
7. [Future Improvements](#-future-improvements)  
8. [License](#-license)  

---

## 🚀 Features

- **Streamlit UI**: Intuitive chat interface with file uploader and message history.  
- **File Chunking**: Splits large text into 1,000-character chunks for efficient retrieval.  
- **Vector Store**: Persists embeddings in a Chroma DB under `db_store/chroma_db_romeo_juliet/`.  
- **Retrieval**: Fetches top-3 most relevant chunks via semantic similarity.  
- **LLM Integration**: Uses Google Gemini 2.0 (via `langchain_google_genai`) for both embeddings and chat generation.  
- **Typing Effect**: Simulated “typing” animation in chat responses.  
- **Session State**: Maintains full conversation history across interactions.  
- **Celebration**: Streams balloons on each successful assistant response.  

---

## 🛠️ Tech Stack

- **Frontend / App Framework**: Streamlit  
- **LLM & Embeddings**: Google Generative AI (Gemini 2.0 Flash + embeddings-001)  
- **Orchestration**: LangChain (document loaders, text splitters, prompt templates)  
- **Vector Database**: Chroma (via `langchain_chroma`)  
- **Environment**: Python 3.x, `.env` for secrets  
- **Deployment**: Render (https://textionary.onrender.com/)  

---

## 📁 Project Structure

```
.
├── Custom Chat.py         # Streamlit app entrypoint
├── utils.py               # Vector-store creation & retrieval functions
├── db_store/              # Persists Chroma embeddings
│   └── chroma_db_romeo_juliet/
├── requirements.txt       # Python dependencies
├── .env.example           # Example env vars (see below)
└── README.md              # This file
```

---

## ⚙️ Getting Started

### Prerequisites

- **Python 3.8+**  
- A Google Cloud project with access to the Generative AI API (Gemini)  
- [Render](https://render.com/) account (if you want to redeploy)  

### Clone & Install

```bash
git clone https://github.com/18YashDB10/Textionary.git
cd Textionary
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### Environment Variables

Create & Copy to `.env` and fill in your credentials:

```dotenv
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_API_PROJECT=your_google_project_id
```

_Streamlit will auto-load `.env` via `python-dotenv`._

### Run Locally

```bash
streamlit run "Custom Chat.py"
```

Then open `http://localhost:8501` in your browser.

---

## 🤖 How It Works

1. **Upload**: User uploads a `.txt` file via `st.file_uploader`.  
2. **Persist**: The file is saved to a temporary path.  
3. **Embed & Store**:  
   - `utils.create_vector_store(tmp_file_path)`  
   - Loads text with `TextLoader`  
   - Splits into 1,000-character chunks (`CharacterTextSplitter`)  
   - Embeds via `GoogleGenerativeAIEmbeddings`  
   - Persists in a Chroma DB folder.  
4. **Retrieve**:  
   - On each query, `utils.get_similar_docs(query)` loads the same DB, retrieves the top 3 chunks.  
5. **Prompting**:  
   - The app wraps retrieved chunks and user question into a prompt via `ChatPromptTemplate`.  
6. **Generate**:  
   - Sends prompt to Gemini 2.0 Flash (`ChatGoogleGenerativeAI`), returns a text answer.  
7. **Display**:  
   - Shows the answer word-by-word with a typing effect, then “balloons” celebration.  
   - All messages are stored in `st.session_state.messages` for chat history.  

---

## 💬 Usage

1. **Upload** your `.txt` file (up to a few MB).  
2. **Type** a question in the “What is up?” input box.  
3. **Read** the assistant’s streamed answer.  
4. **Repeat** as needed—your past conversation remains visible.  

Example queries:

- “Summarize the main arguments.”  
- “What are the key dates mentioned?”  
- “Find all occurrences of the word ‘character.’”  

---

## 🔮 Future Improvements

- 📄 Support for **PDF**, **DOCX**, and other formats  
- 🔍 Adjustable **number of returned chunks** (`k` parameter)  
- 🔐 **User authentication** and per-user DB isolation  
- 📱 **Responsive UI** for mobile devices  
- 📂 **Multi‐file chat** & **history export**  

---



© 2025 Yash Deepak Bambore · [GitHub Repository](https://github.com/18YashDB10/Textionary)
