from openai import OpenAI

client = OpenAI(
    base_url="https://unermined-bridgette-transempirical.ngrok-free.dev/v1",
    api_key="token",
)

completion = client.chat.completions.create(
    model="/scratch/yinx/custom_models/Qwen3-Coder-30B-A3B-Instruct",
    messages=[
        {"role": "user", "content": "Hello from Kalinda!"},
    ],
)


print(completion.choices[0].message)
