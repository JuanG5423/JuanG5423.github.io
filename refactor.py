import os

def remove_filler(filename : str) -> str:
    split = filename.find("_")
    #rename the file to the first part of the filename
    return filename[:split]

#remove filler on all files in the classes directory
for filename in os.listdir("docs/classes"):
    os.rename("docs/classes/" + filename, "docs/classes/" + remove_filler(filename) + ".html")

