from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder

def get_qa_prompt(data: str, user_id: int):
    qa_system_prompt = f"""
    You are an AI assistant specializing in forex algorithmic trading analysis and finance, having background about the trade and the forex algorithmic trading context.

    Your function is to analyze trading strategies, provide expert insights on trading performance and metrics, and answer questions based on given context.

    Answer the question and provide a detailed and insightful answer based on the retrieved trading metrics and the account summary: ({data})

    Always strive for accuracy and clarity in your responses, and acknowledging any limitations when necessary.

    If you don’t know the answer, just say that you don’t know. Use three sentences maximum and keep the answer concise, yet informative.

    The user ID is {user_id}.

    {{context}}
    """

    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", qa_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    return qa_prompt

def get_contextualize_q_prompt():
    contextualize_q_system_prompt = """
    Given a chat history and the latest user question
    which might reference context in the chat history, formulate a standalone question
    which can be understood without the chat history. Do NOT answer the question,
    just reformulate it if needed and otherwise return it as is.
    """

    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    return contextualize_q_prompt
