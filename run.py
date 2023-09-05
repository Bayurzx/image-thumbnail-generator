import os
from PIL import Image


def create_thumbnails(source_dir, target_dir, size=(128, 128)):
    # Ensure the target directory exists; create it if it doesn't.
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # List all files in the source directory.
    files = os.listdir(source_dir)

    for file in files:
        # Check if the file is an image (you can add more image extensions as needed).
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Construct the full paths for the source and target images.
            source_path = os.path.join(source_dir, file)
            target_path = os.path.join(target_dir, file)

            # Open the source image and create a thumbnail.
            try:
                image = Image.open(source_path)
                thumbnail = image.resize(size)
                thumbnail.save(target_path)
                print(f"Thumbnail created for {file}")
            except Exception as e:
                print(f"Failed to process {file}: {str(e)}")


if __name__ == "__main__":
    source_directory = "C:\\Users\\USER\\Desktop\\adebayoomolumo.website\\portfolio\\arter\\img\\works\\ML_K8s"
    thumbnail_directory = "C:\\Users\\USER\\Desktop\\adebayoomolumo.website\\portfolio\\arter\\img\\works\\ML_K8s\\thumbnail"
    
    create_thumbnails(source_directory, thumbnail_directory)

