import requests

def download_image(image_url):
    response = requests.get(image_url)
    with open('image.jpg', 'wb') as file:
        file.write(response.content)
    print('Download Completed')

prompt = 'Create a detailed illustration of The entire image should be...'
width = 1216
height = 1574
seed = 867413420
model = 'flux'

image_url = f"https://pollinations.ai/p/{prompt}?width={width}&height={height}&seed={seed}&model={model}"

download_image(image_url)


import pollinations as ai

model_obj = ai.Model()

image = model_obj.generate(
    prompt=f'Create a detailed illustration of The entire image should be... {ai.realistic}',
    model=ai.flux,
    width=1216,
    height=1574,
    seed=867413420
)
image.save('image-output.jpg')

print(image.url)

