# 📝 AI-powered Text Preprocessing App

A **Streamlit application** that leverages **LangChain + Google Gemini** for intelligent text preprocessing.  
The app removes formatting, identifies headlines, extracts key elements (dates, names, locations, statistics), and detects the input text’s language.  

---

## 🚀 Features

- 🔄 **Whitespace & Formatting Cleanup** – Removes excessive spacing and cleans text.  
- 📰 **Headline Detection** – Separates headline from body content.  
- 📌 **Key Information Extraction** – Pulls out dates, names, locations, and statistics.  
- 🌍 **Language Detection** – Supports multilingual text input.  
- 🎨 **Streamlit UI** – Interactive web app for easy text processing.  

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – UI framework  
- [LangChain](https://www.langchain.com/) – Prompt orchestration  
- [Google Gemini API](https://ai.google.dev/) – LLM backend (`langchain_google_genai`)  
- [Pydantic](https://docs.pydantic.dev/) – Structured output validation  
- [dotenv](https://pypi.org/project/python-dotenv/) – Environment variable management  

---

## ⚙️ Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/text-preprocessing-app.git
   cd text-preprocessing-app
