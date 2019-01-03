# 2381 Robotics

# Installation
1. Get git.
2. ```git clone``` this repo
3. Get ruby.
4. ```gem install``` bundle
5. ```gem install``` jekyll
6. ```bundle install``` in the folder.
7. ```bundle exec jekyll serve``` to start a local server.

# Editing this repo

The _layouts folder contains general layouts that you can include in the top configuration thing of every html file.
The img folder has all the images.
The posts folder has something that I need to figure out (I feel like it's doing nothing atm).
The _posts folder is where individual posts go.
The _include folder has the equivalent of components I guess like head, navbar, and footer.
The assets folder contains a bunch of assets and the .scss file in the _sass folder points to that folder.
The individual html things that you need to edit are in the root directory.
Note the html files in the root directory are not full html files. They are used to generate an actual html file.
After running bundle exec jekyll serve, the generated files go in _site.

## Posts

Go to the _posts folder and make a new file with the naming scheme shown below:
```YYYY-MM-DD-title-name.html```

Configure the below:
```yaml
---
author: "author_name"
layout: post
title:  "Generic Title"
subtitle: "Generic Subtitle"
date:   2018-09-01 23:00:00 -0500
background: '/img/posts/YYYY-MM-DD-title-name.jpg'
---
```
Note the image you put in /img/posts/ has the same naming scheme as the post
Also note that the time is 24 hour time. If you write the post in another time zone other than EST, change -0500 accordingly (this is RFC822 time)


