from app.memory.chat_memory import (
    add_message,
    get_recent
)

from app.memory.summary_memory import (
    get_summary,
    update_summary
)

from app.llm.groq_client import ask_llm


def save_conversation(
    user_message,
    assistant_message
):

    add_message(
        "user",
        user_message
    )

    add_message(
        "assistant",
        assistant_message
    )

    messages = get_recent()

    if len(messages) >= 10:

        prompt = f"""
Summarize the conversation.

Conversation:

{messages}

Keep:
- user facts
- project status
- important decisions

Remove:
- greetings
- small talk
"""

        summary = ask_llm(
            prompt
        )

        update_summary(
            summary
        )