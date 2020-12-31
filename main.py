# images converter to PNG
import os
from PIL import Image


def convert_to_png(images_folder, output_folder):
    # creating output_folder if it doesnt exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    #    looping through filenames in images_folder
    for filename in os.listdir(images_folder):
        img = Image.open(f'{images_folder}{filename}')  # open image file
        img.thumbnail((500, 500))  # modifying image file
        clean_name = os.path.splitext(filename)[0] # removing image extension
        img.save(f'{output_folder}{clean_name}.png', 'png')  # saving image with new png extension
        print(f'{clean_name}.png saved!')


if __name__ == '__main__':
    convert_to_png('images/', 'my_folder/')
