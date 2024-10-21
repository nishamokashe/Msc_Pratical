''' Write/Append text into the file and display '''

def write_to_file(file_name, text, mode='a'):
    # Writing or appending text to the file
    with open(file_name, mode) as file:
        file.write(text + '\n')  # Writing the text and adding a new line at the end

def read_file(file_name):
    # Reading the file content and displaying it
    with open(file_name, 'r') as file:
        content = file.read()
    return content

# File name to write/append to
file_name = 'example.txt'

# Example text to write/append to the file
text_to_write = "This is a new line of text."

# Writing/appending text to the file
write_to_file(file_name, text_to_write, mode='a')  # 'a' for append mode, 'w' for write mode

# Reading and displaying the file content
print("File contents:")
print(read_file(file_name))
