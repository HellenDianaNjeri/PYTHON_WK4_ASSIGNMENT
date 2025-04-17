# error_handling_lab.py

# Step 1: Ask the user for a filename
filename = input("Enter the name of the file you want to open: ")

print(f"\nYou entered: {filename}") 

try:
    # Step 2: Try to open and read the file
    with open(filename, 'r') as file:  # Use the entered filename
        content = file.read()
        print(content)

except FileNotFoundError:
    print(f"\n❌ The file '{filename}' was not found. Please check the file path and try again.")

except PermissionError:
    print("\n❌ You do not have permission to read the file.")

except Exception as e:
    print("\n⚠️ An unexpected error occurred.")
    print(e)
