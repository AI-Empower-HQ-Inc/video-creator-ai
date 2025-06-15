import os

def get_image_sequence(image_dir):
    return sorted([
        os.path.join(image_dir, f)
        for f in os.listdir(image_dir)
        if f.endswith(('.png', '.jpg', '.jpeg'))
    ])