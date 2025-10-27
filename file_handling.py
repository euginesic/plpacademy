file=open('stack.py', 'r')
data=file.read()
print(data)

#modified data
modified_data=data.upper()
print(modified_data)

#file handling
try:
    
    file=open('stack.py', 'r')
    content=file.read()
    print(content)

except FileNotFoundError:
    print("file not found!")   

try:
    enter=input("enter file name: ")
    if enter=="stack.py":
        file=open(enter, 'r')
        content=file.read()
        print(content)
    else:
        print("file not found!")
except FileNotFoundError:
    print("file does not exist!")



