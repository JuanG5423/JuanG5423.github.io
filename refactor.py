import os

def remove_filler(filename : str) -> str:
    split = filename.find("___")
    #rename the file to the first part of the filename
    return filename[:split]

#remove filler on all files in the objectproperties directory
for filename in os.listdir("docs/objectproperties"):
    os.rename("docs/objectproperties/" + filename, "docs/objectproperties/" + remove_filler(filename) + ".html")

