import os

def remove_filler(filename : str) -> str:
    split = filename.find("___")
    #rename the file to the first part of the filename
    return filename[:split]

#remove filler on all files in the dataproperties directory
for filename in os.listdir("docs/dataproperties"):
    os.rename("docs/dataproperties/" + filename, "docs/dataproperties/" + remove_filler(filename) + ".html")

