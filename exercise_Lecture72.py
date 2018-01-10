import datetime

r"""
This creates an file from three files file[1-3].txt and creates a file with
the name as a time stamp 2017-11-01-13-57-39-170965.txt  and all contents of the files.
"""

filename = datetime.datetime.now()
filename = filename.strftime("%Y-%m-%d-%H-%M-%S-%f")
# Create an empty file
def create_file():
    """
    This is the function that creates an the file with a given file name.
    it then appends the file[1-3].txt first line into that file.
    """
    if  not filename:
        return
    with open(filename,"w") as file:
        for i in range(1,4):
            t_f = open("file" + str(i) +".txt","r")
            fcont = t_f.read()
            t_f.close()
            file.write(str(fcont)+"\n")


print(filename)
create_file()
