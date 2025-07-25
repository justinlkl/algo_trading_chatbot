# Forex Algorithmic Trading Chatbot Prompts

This module defines prompt templates for a forex algorithmic trading AI assistant using LangChain's `ChatPromptTemplate` and `MessagesPlaceholder`. These prompts are designed to guide the language model in providing expert insights and concise answers based on trading data and user queries.

## Functions

### `get_qa_prompt(data: str, user_id: int)`

Creates a system prompt for the AI assistant to:
- Analyze trading strategies and metrics.
- Provide detailed, insightful, and concise answers based on the provided trading data (`data`) and user ID (`user_id`).
- Limit responses to three sentences and acknowledge limitations when necessary.
- Use chat history and user input for context.

**Parameters:**
- `data` (str): Trading metrics and account summary to be referenced in answers.
- `user_id` (int): The user's identifier, included in the prompt for context.

**Returns:**  
A `ChatPromptTemplate` for question-answering.

---

### `get_contextualize_q_prompt()`

Creates a system prompt instructing the AI to:
- Reformulate the latest user question into a standalone question, using chat history for context.
- Avoid answering the question, only rephrasing it if necessary.

**Returns:**  
A `ChatPromptTemplate` for contextualizing user questions.

---

## Example Usage

```python
from modules.prompt import get_qa_prompt, get_contextualize_q_prompt

qa_prompt = get_qa_prompt(data="account metrics here", user_id=1)
contextualize_q_prompt = get_contextualize_q_prompt()

## Dependencies

- langchain_core.prompts.ChatPromptTemplate
- langchain_core.prompts.MessagesPlaceholder

For more details, see modules/prompt.py# algo_trading_chatbot
