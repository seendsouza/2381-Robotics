"""
Automates the HTML (Jekyll form) creation for media.html, so
that the images do not have to be manually inserted into it.
"""
import os
import curses

counter = int()
blog_properties = list()

class BlogPost():
    def __init__(self, title, author, date, text):
        self.title = title
        self.author = author
        self.date = date
        self.text = text

def remove_header(line):
    return line

def check_line(line, counter):
    print(line)
    print(line.find("title: "))
    if line.startswith("title:"):
        counter += 1
        blog_properties.append(instance.Blog_Post())
        blog_properties[counter].title = remove_header(line)
    elif line.startswith("author: "):
        blog_properties[counter].author = remove_header(line)
    elif line.startswith("date: "):
        blog_properties[counter].date = remove_header(line)
    else:
        blog_properties[counter].text += line
    return counter

def main(input_path, output_path):
    """
    The input path is where Python can find the folder.
    The output path is where the generated html can find the folder.
    """
    current_path = os.path.dirname(__file__)
    file_path = os.path.relpath(input_path, current_path)  
    counter = -1
    with open(file_path,"r") as input_file:
        while True:
            line = input_file.readline() 
            line = line.rstrip()
            counter = check_line(str(line), counter)
            if not line:
                break
    print(blog_properties)
    """
    # get the curses screen window
    screen = curses.initscr()
    # turn off input echoing
    curses.noecho()
    # respond to keys immediately (don't wait for enter)
    curses.cbreak()
    # map arrow keys to special values
    screen.keypad(True)
    i = 0
    try:
        while True: 
            char = screen.getch()
            if i == (len(blog_properties)-1):
                break
            if char == ord('q'):
                break
            elif char == curses.KEY_RIGHT:
                print(blog_properties[i])
                i += 1
    finally:
        # shut down cleanly
        curses.nocbreak()
        screen.keypad(0)
        curses.echo()
        curses.endwin() 
    """

if __name__ == "__main__":
    main("./engineering_notebook.md", "../_posts/")
