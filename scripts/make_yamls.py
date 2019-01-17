"""
Automates the HTML (Jekyll form) creation for media.html, so
that the images do not have to be manually inserted into it.
"""
import os

def htmlify(filename):
    return (filename[:-3] + ".html")


def main(input_path, output_path):
    """
    The input path is where Python can find the folder.
    The output path is where the generated html can find the folder.
    """
    current_path = os.path.dirname(__file__)
    file_path = os.path.relpath(input_path, current_path)  
    file_path_2 = os.path.relpath(output_path, current_path)  
    html_filename = str()
    yaml_str = str()
    for file in os.listdir(file_path):
        if file.endswith(".md"):
            html_filename = htmlify(file)
            md_path = file_path + "/" + file
            html_path = file_path + "/" + html_filename
            with open(md_path,"r") as input_file:
                lines = input_file.readlines()
                for i in range(0, 4):
                    yaml_str += lines[i]
                yaml_str += "layout: post\n---\n"
            with open(html_path, 'r') as original:
                data = original.read()
            with open(html_path, 'w') as modified:
                modified.write(yaml_str + data)
            yaml_str = str()

if __name__ == "__main__":
    main("../_posts/", "../_posts/")
