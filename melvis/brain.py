from openai import OpenAI
from melvis.config import OPENAI_API_KEY, USER_NAME

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_melvis(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": f"You are Melvis, a helpful AI assistant built for {USER_NAME}. Be concise and useful."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content