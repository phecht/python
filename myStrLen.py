def my_string_length(myString):
    if type(myString) == str:
        return len(myString)
    elif type(myString) == float:
        return "Float, no string!"
    else:
        return "Not a string!"
  
ASTRING = input("Enter a string:")
print(my_string_length(ASTRING))
print(my_string_length(10))
