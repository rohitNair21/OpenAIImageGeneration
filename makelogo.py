from openai import OpenAI

client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt="a white siamese cat",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url

import requests
from PIL import Image
from io import BytesIO

image_data = requests.get(image_url).content

image = Image.open(BytesIO(image_data))

image.show()
