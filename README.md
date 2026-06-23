# 🔍 ResearchGPT

ResearchGPT is an AI-powered research assistant that helps users generate research reports, blog articles, and LinkedIn posts using real-time web search and generative AI.

---

## 🚀 Features

* AI Research Report Generation
* Real-Time Web Search using Tavily
* Blog Article Generation
* LinkedIn Post Generation
* PDF Export
* Source Citation Display
* Clean Streamlit Interface
* LangChain Integration

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI & LLM

* Google Gemini 2.5 Flash
* LangChain

### Search Engine

* Tavily Search API

### PDF Generation

* ReportLab

---

## 📂 Project Structure

```text
ResearchGPT/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
│
├── services/
│   ├── search_service.py
│   ├── research_service.py
│   ├── blog_service.py
│   ├── linkedin_service.py
│   └── pdf_service.py
│
└── screenshots/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd ResearchGPT
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
TAVILY_API_KEY=YOUR_TAVILY_API_KEY
```

### Run Application

```bash
streamlit run app.py
```

---

## 🔄 Application Workflow

```text
User
 ↓
Streamlit UI
 ↓
Tavily Search
 ↓
LangChain
 ↓
Gemini AI
 ↓
Research Report
 ↓
Blog / LinkedIn Post / PDF
```

---

## 📸 Screenshots

Add screenshots here after running the application:

* Home Screen
* Research Report
* Blog Generator
* LinkedIn Generator

---

## 🎯 Future Improvements

* Research History
* Multi-Agent Workflow
* Authentication
* Database Integration
* Export to DOCX
* Email Sharing

---

## 👩‍💻 Author

Swati Shinde

AI • Blockchain • Full-Stack Development
