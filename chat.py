import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

messages = [
    {"role": "system", "content": "你是一个耐心的编程学习助手，回答尽量简短。"},
]

while True:
    user_input = input("你：")
    if user_input in ("exit", "quit"):
        print("再见！")
        break

    messages.append({"role": "user", "content": user_input})

    resp = client.chat.completions.create(
        model="deepseek-flash",
        messages=messages,
    )
    answer = resp.choices[0].message.content
    print("AI：", answer)

    messages.append({"role": "assistant", "content": answer})
