"""
Automates the HTML (Jekyll form) creation for media.html, so
that the images do not have to be manually inserted into it.
"""
import os
import yaml
from pprint import pformat
import datetime

def check_line(line, counter):
    if line.find("---") == 0:
        counter += 1
    return counter

def format_date(unformatted):
    formatted = unformatted.split()[0]
    return formatted

def format_title(unformatted):
    formatted = str()
    for char in unformatted:
        if char == " ":
            char = "-"
        formatted += char
    return formatted

def main(input_path, output_path):
    """
    The input path is where Python can find the folder.
    The output path is where the generated html can find the folder.
    """
    current_title = str()
    current_date = str()
    yaml_str = str()
    yaml_dict = dict()
    current_path = os.path.dirname(__file__)
    file_path = os.path.relpath(input_path, current_path)  
    file_path_2 = os.path.relpath(output_path, current_path)  
    counter = 1
    line_no_init = 0
    line_no_final = int()
    with open(file_path,"r") as input_file:
        lines = input_file.readlines()
        for i, line in enumerate(lines): 
            counter = check_line(str(line), counter)
            if counter == 1 and line.find("---") == -1:
                yaml_str += line
            elif counter % 2 == 0:
                continue
            elif counter == 3:
                line_no_final = i - 1
                yaml_gen = yaml.load_all(yaml_str)
                for _, item in enumerate(yaml_gen):
                    yaml_dict = item
                current_title = format_title(yaml_dict["title"])
                current_date = format_date(yaml_dict["date"])
                full_path = file_path_2 + "/" + current_date + "-" + current_title + ".md"
                with open(full_path,"w") as blog_file:
                    for j in range(line_no_init, line_no_final):
                        blog_file.write(lines[j])
                line_no_init = i
                counter = 1

if __name__ == "__main__":
    main("./engineering_notebook.md", "../_posts/")
