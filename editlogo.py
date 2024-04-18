from openai import OpenAI
client = OpenAI()

response = client.images.create_variation(
  model="dall-e-2",
  image=open("image_path", "rb"), #EDIT PATH
  n=1,
  size="1024x1024"
)

image_url = response.data[0].url

import requests
from PIL import Image
from io import BytesIO

image_data = requests.get(image_url).content

image = Image.open(BytesIO(image_data))

image.show()