import base64


def encode_image(full_path):
    with open(full_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
