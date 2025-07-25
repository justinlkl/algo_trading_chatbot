from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

# A complete question-answering chain
def create_full_chain(llm, retriever, qa_prompt, contextualize_q_prompt):
    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt
    )
    qa_chain = create_stuff_documents_chain(llm, qa_prompt)
    retrieval_chain = create_retrieval_chain(history_aware_retriever, qa_chain)
    return retrieval_chain

# Takes a query and outputs the invoked chain
def ask_question(query, rag_chain_with_history):
    return rag_chain_with_history.invoke(
        {"input": query}, config={"configurable": {"session_id": "foo"}}
    )["answer"]

# def create_full_chain(retriever):
#     llm = initialize_cohere_llm_model()
#     qa_prompt = get_qa_prompt()
#     contextualize_q_prompt = get_contextualize_q_prompt()
#     basic_chain = rag_chain(retriever, qa_prompt, llm)
#     full_chain = memory_chain(llm, contextualize_q_prompt, basic_chain)
#     return full_chain
