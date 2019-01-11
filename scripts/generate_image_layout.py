"""
Automates the HTML (Jekyll form) creation for media.html, so
that the images do not have to be manually inserted into it.
"""

import os


def generate_list(relative_path):
    """
    Generates a list of image names
    """
    current_path = os.path.dirname(__file__)    
    file_path = os.path.relpath(relative_path, current_path)    
    filenames = os.listdir(file_path)
    image_names = list()
    for _, filename in enumerate(filenames):
        image_names.append(filename)
    return image_names

def format_names(image_names, relative_path):
    """
    Formats the image names into the Jekyll format wanted
    """
    top_text = "---\nlayout: media\ntitle: Media\nimages:\n"
    bottom_text = "---"
    output = top_text
    for _, image in enumerate(image_names):
	image_name = extract_title(image)
	output += "  - image_path: {}\n    title: {}\n".format(relative_path + image, image_name) 
    output += bottom_text
    return output

def extract_title(image):
    """
    Makes titles from filenames
    """
    name = str()
    for _, char in image:
        if char == "-":
            break
        elif char == "_":
            char = " "
        name += char
    name = name.title()
    return name

def main(input_path, output_path):
    """
    The input path is where Python can find the folder.
    The output path is where the generated html can find the folder.
    """
    image_names = generate_list(input_path)
    output = format_names(image_names, output_path)

if __name__ == "__main__":
    main("../img/media/", "./img/media/")
