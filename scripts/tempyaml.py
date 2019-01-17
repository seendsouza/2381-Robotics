import yaml

stream = open("test", "r")
docs = yaml.load_all(stream)
for doc in docs:
    for k,v in doc.items():
        print k, "->", v
    print "\n",
