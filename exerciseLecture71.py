import datetime

r"""
This creates an empty file.
"""

filename = datetime.datetime.now()
filename = filename.strftime("%Y-%m-%d-%H-%M")
# Create an empty file
def create_file():
    """This is the function that creates an empty file"""
    with open(filename,"w") as file:
        file.write("")

print(filename)
create_file()
