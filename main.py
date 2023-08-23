from PIL import Image
import requests
import io


def process_image():
    # Open the image file
    with open('image.jpeg', 'rb') as f:
        img = Image.open(f)

        # Get the dimensions of the image
        width, height = img.size

        # Check if the image is vertical
        is_vertical = height > width

        # If the image is not vertical, rotate it
        if not is_vertical:
            img = img.transpose(Image.ROTATE_270)

        # Convert the image to bytes
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='JPEG')
        img_bytes.seek(0)

        r = requests.post(
            "https://api.deepai.org/api/image-editor",
            files={
                'image': ('image.jpeg', img_bytes),
                'text': open('text.txt', 'rb'),
            },
            headers={'api-key': '415fcf85-9478-4ecc-9ee3-79bfd328f346'}
        )

        # Get the URL of the generated image from the API response
        image_url = r.json().get('output_url')

        # Download the image data from the URL
        image_data = requests.get(image_url).content

        # Save the image data to a file
        with open('output1.jpeg', 'wb') as f:
            f.write(image_data)


process_image()