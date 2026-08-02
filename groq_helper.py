import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_llm(question):
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    response = completion.choices[0].message.content

    response = response.replace("```sql", "")
    response = response.replace("```", "")
    response = response.strip()

    return response