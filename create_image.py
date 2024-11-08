import secrets

from openai import OpenAI

client = OpenAI(api_key=secrets.api_key)

prompt = "The Open GL book cover where the world is made out of Lego pieces."

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
)

print(response.data[0].url)