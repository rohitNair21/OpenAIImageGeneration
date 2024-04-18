from openai import OpenAI
client = OpenAI()

response = client.images.edit((
  model="dall-e-2",
  image=open("ORIGINAL_IMAGE", "rb"), #LOGO TO BE CHANGED
  mask=open("mask.png", "rb"), #MASK (EX. ERASE CURRENT IMAGE AREA)
  prompt="A sunlit indoor lounge area with a pool containing a flamingo",
  n=1,
  size="1024x1024",
))

image_url = response.data[0].url

import requests
from PIL import Image
from io import BytesIO

image_data = requests.get(image_url).content

image = Image.open(BytesIO(image_data))

image.show()