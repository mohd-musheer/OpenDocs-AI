from groq import Groq

from app.config import (
    GROQ_API_KEY,
    MODEL_NAME
)

client = Groq(
    api_key=GROQ_API_KEY
)


def ask_llm(prompt: str):

    print("\n" + "=" * 80)
    print("PROMPT SIZE")
    print("=" * 80)

    print(
        f"{len(prompt)} chars"
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = (
        response
        .choices[0]
        .message
        .content
    )

    return answer