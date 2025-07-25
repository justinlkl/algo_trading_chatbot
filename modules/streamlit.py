import os
import streamlit as st
from modules.llm_model import (
    initialize_cohere_llm_model,   
)
from modules.data_parser import load_url, load_csv
from modules.vectorstore import get_retriever
from constant import COHERE_API_KEY
from modules.prompt import get_contextualize_q_prompt, get_qa_prompt
from modules.memory_chain import memory_chain
from modules.full_chain import ask_question
from modules.config_parser import ConfigParser
from langchain.globals import set_debug
from langchain_core.chat_history import InMemoryChatMessageHistory
import time
import pandas as pd

set_debug(True)
# Formatting the front page
st.set_page_config(page_title=" AI Chatbot🌱", layout="wide", page_icon="🌲")

st.markdown(
    """
<style>

.stApp {
    background-color: #f0f4f8;
}


[data-testid="stChatMessage"] {
    background-color: white !important;
    border-radius: 15px !important;
    padding: 15px !important;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1) !important;
    margin-bottom: 15px !important;
    transition: all 0.3s ease !important;
}

[data-testid="stChatMessage"]:hover {
    box-shadow: 0 5px 15px rgba(0,0,0,0.1) !important;
}

[data-testid="stSidebar"] {
    background-color: #ffffff;
    padding: 2rem;
    border-right: 1px solid #e0e0e0;
}

.stTextInput > div > div > input {
    border-radius: 20px;
    padding: 10px 15px;
    border: 2px solid #4CAF50;
    transition: all 0.3s ease;
}

.stTextInput > div > div > input:focus {
    border-color: #45a049;
    box-shadow: 0 0 0 2px rgba(76, 175, 80, 0.2);
}

.stButton > button {
    border-radius: 20px;
    padding: 10px 25px;
    background-color: #4CAF50;
    color: white;
    border: none;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background-color: #45a049;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.1 {
    color: #2E7D32;
    font-weight: bold;
}


@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.fade-in {
    animation: fadeIn 0.5s ease-out;
    padding-bottom: 10px; !important;
}

</style>
""",
    unsafe_allow_html=True,
)


# Useful Functions
def clear_cache():
    # Delete all the items in Session state
    for key in st.session_state.keys():
        del st.session_state[key]


def get_user_data(user_id: int):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    data_path = f"./data/user_id={user_id}/account_stat_summary.csv"
    data = pd.read_csv(data_path)
    return data


# Initialize value
if "chat_questions" not in st.session_state:
    st.session_state["chat_questions"] = []
if "chat_responses" not in st.session_state:
    st.session_state["chat_responses"] = []
if "memory" not in st.session_state:
    st.session_state["memory"] = InMemoryChatMessageHistory()
if "retriever" not in st.session_state:
    # load data
    docs = []
    get_config_file = ConfigParser().get_config()
    url_webpage_list = get_config_file["url_webpage_list"]
    for url in url_webpage_list:
        doc = load_url(url)
        docs.extend(doc)
    # create retriever
    retriever = get_retriever(docs, COHERE_API_KEY)
    st.session_state["retriever"] = retriever
if "llm" not in st.session_state:
    st.session_state["llm"] = initialize_cohere_llm_model()
if "user_id" not in st.session_state:
    st.session_state["user_id"] = 1


# create chain
contextualize_q_prompt = get_contextualize_q_prompt()
data = get_user_data(st.session_state["user_id"])
qa_prompt = get_qa_prompt(data, st.session_state["user_id"])
rag_chain_with_history = memory_chain(
    st.session_state.llm,
    st.session_state.retriever,
    qa_prompt,
    contextualize_q_prompt,
    st.session_state.memory,
)


with st.sidebar:
    st.markdown(
        '<h1 class="fade-in"> AI Chatbot </h1>', unsafe_allow_html=True
    )
    st.image("./assets/logo.png", use_column_width=True)
    st.markdown("It is the demo of  AI Chatbot.")
    st.markdown("---")
    user_choice = st.radio("Select the user:", ["User 1", "User 2"])
    if user_choice == "User 1":
        st.session_state["user_id"] = 1
        contextualize_q_prompt = get_contextualize_q_prompt()
        data = get_user_data(st.session_state["user_id"])
        qa_prompt = get_qa_prompt(data, st.session_state["user_id"])
        rag_chain_with_history = memory_chain(
            st.session_state.llm,
            st.session_state.retriever,
            qa_prompt,
            contextualize_q_prompt,
            st.session_state.memory,
        )
    else:
        st.session_state["user_id"] = 2
        contextualize_q_prompt = get_contextualize_q_prompt()
        data = get_user_data(st.session_state["user_id"])
        qa_prompt = get_qa_prompt(data, st.session_state["user_id"])
        rag_chain_with_history = memory_chain(
            st.session_state.llm,
            st.session_state.retriever,
            qa_prompt,
            contextualize_q_prompt,
            st.session_state.memory,
        )
    if st.button("Reset Chat", key="reset"):
        clear_cache()
    st.markdown("---")

st.markdown(
    '<h2 class="fade-in">Welcome to  AI Assistant</h2>',
    unsafe_allow_html=True,
)
st.dataframe(data, use_container_width=True, hide_index=True)

welcome_msg = (
    "Hi, I am your friendly  AI Chatbot. How may I assist you today?"
)
with st.chat_message("assistant", avatar="🌳"):
    st.markdown(f'<div class="fade-in">{welcome_msg}</div>', unsafe_allow_html=True)

# React to user input and save to history
if query := st.chat_input("Say Something..."):

    for chat_question, bot_response in zip(
        st.session_state["chat_questions"], st.session_state["chat_responses"]
    ):
        with st.chat_message("user", avatar="👤"):
            st.markdown(
                f'<div class="fade-in">{chat_question}</div>', unsafe_allow_html=True
            )
        with st.chat_message("assistant", avatar="🌳"):
            st.markdown(
                f'<div class="fade-in">{bot_response}</div>', unsafe_allow_html=True
            )

    with st.chat_message("user", avatar="👤"):

        st.markdown(query)
        st.session_state.chat_questions.append(query)

    # Generate the bot's response
    with st.chat_message("assistant", avatar="🌳"):
        with st.spinner("Wait for it..."):
            bot_response = ask_question(query, rag_chain_with_history)
        full_response = ""
        message_placeholder = st.empty()
        for chunk in bot_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(
                f'<div class="fade-in">{full_response}▌</div>',
                unsafe_allow_html=True,
            )
        message_placeholder.markdown(bot_response)
        st.session_state.chat_responses.append(bot_response)
