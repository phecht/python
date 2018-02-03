'''Modifies the HOSTS_PATH file.
takes the '''
import time
from datetime import datetime as dt

HOSTS_PATH = r"hosts"
REDIRECT = "127.0.0.1"
WEBSITE_LIST = ["www.facebook.com", "facebook.com", "twitter.com"]
BLOCK_ADDER = " #BLOCK_ADD"

def make_string_line(website):
    ''' Takes the website and makes the line to put in or take out of a file.'''
    return REDIRECT + " " + website + BLOCK_ADDER


def write_file(file_name):
    ''' addlines to file_name.'''
    with open(file_name, 'r+') as file:
        content = file.read()

        for website in WEBSITE_LIST:
            addline = make_string_line(website)
            if addline in content:
                pass
            else:
                file.write(addline + "\n")


def remove_lines_from_file(file_name):
    ''' Removes lines from file_name. '''
    with open(file_name, "r+") as file:
        content = file.readlines()
        file.seek(0)
        file.truncate()

        for line in content:
            # if line from makeStringLine is the line, don't print it back.
            # website is a created variable from website_list. Created for each
            # entry in website_list.
            if not BLOCK_ADDER in line:
                file.write(line)
                print("writing:"+line)
            else:
                print("Not writing:"+ line)

while True:
    print("Waiting 1...")
    time.sleep(2)
    print(dt.now().hour)
    if 2 <= dt.now().hour <= 7:
        print("Adding...")
        write_file(HOSTS_PATH)
    else:
        print("Removing...")
        remove_lines_from_file(HOSTS_PATH)

    print("Waiting 2...")
    time.sleep(2)
