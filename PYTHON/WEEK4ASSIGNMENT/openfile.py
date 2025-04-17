with open("example.txt","r") as file:
    file =file.read()
    print(file)

modified_file=file.lower()

with open("output.txt","w") as file:
    file.write(modified_file)
    print("File modified successfully")