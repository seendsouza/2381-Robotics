"""
Automates the HTML (Jekyll form) creation for media.html, so
that the images do not have to be manually inserted into it.
"""

import os

def 

def main(input_path, output_path):
    """
    The input path is where Python can find the folder.
    The output path is where the generated html can find the folder.
    """
    with open(input_path,"r") as input_file:
        while True:
            line = input_file.readline()
            if not line:
                break


if __name__ == "__main__":
    main("./", "../_posts/")
