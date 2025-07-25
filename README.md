# 🌱 AI Chatbot for Forex Algorithmic Trading

This is a Retrieval-Augmented Generation (RAG) chatbot designed to assist users with forex algorithmic trading insights. It leverages LangChain, Cohere, and Hugging Face models to retrieve and generate insightful responses using custom trading data and relevant web resources.

---

## 🚀 Features

- 💬 Conversational chatbot with memory
- 📈 Forex trading strategy analysis
- 🔍 RAG-powered retrieval from online resources and CSV data
- 🌐 Multi-model support (Cohere, Hugging Face endpoints)
- 📊 Streamlit-based user interface

---

## 🧠 How It Works

1. **Document Loading**  
   Loads forex-related resources from URLs or CSVs using `WebBaseLoader` and `CSVLoader`.

2. **Text Splitting & Embedding**  
   Splits and embeds documents using Cohere embeddings for retrieval.

3. **Vector Store & Retrieval**  
   Stores vectors in ChromaDB and retrieves relevant context during Q&A.

4. **LLM Invocation**  
   Uses Cohere or Hugging Face models for context-aware generation.

5. **Prompt Templates**  
   Custom prompts for QA and contextualized question reformulation.

---

## 📁 Project Structure

```text
.
├── config/
│   └── config.yaml              # Contains a list of URLs
├── data/                        # User trading data
├── assets/                      # App logo
├── modules/                     # Custom logic modules
│   ├── config_parser.py
│   ├── constant.py
│   ├── data_parser.py
│   ├── full_chain.py
│   ├── llm_model.py
│   ├── memory_chain.py
│   ├── prompt.py
│   ├── splitter.py
│   └── vectorstore.py
├── streamlit.py                 # Streamlit UI app
├── requirements.txt
└── README.md
```


## ⚙️ Configuration

Update the URL sources in `./config/config.yaml`:

```yaml
url_webpage_list:
  - https://example.com/forex1
  - https://example.com/forex2 
```
Make sure to place user CSVs in:
./data/user_id=<id>/account_stat_summary.csv

⸻

## 🔐 API Keys

Set these environment variables or replace them in constant.py:
	•	HUGGINGFACE_API_KEY
	•	COHERE_API_KEY

⸻

## 🖥️ Run the App

1. Install dependencies
   
```yaml
pip install -r requirements.txt
```

2. Launch Streamlit
```yaml
streamlit run streamlit.py
```

## 🧪 Supported Models
	•	Cohere
	•	Mistral-7B (Hugging Face)
	•	BERT / RoBERTa (Q&A)

⸻

## 📝 Notes
	•	Chat memory is handled in-session using LangChain’s InMemoryChatMessageHistory.
	•	Prompts are tailored for financial/forex analysis—editable in prompt.py.

⸻

## 📸 Sample UI

A clean and interactive chatbot UI styled with CSS animations and Streamlit components.

⸻

## 📃 License

This project is for educational and demonstration purposes.
