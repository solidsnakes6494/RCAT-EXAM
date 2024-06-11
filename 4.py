def read_file(f):
    try:
        with open(f, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{f}' not found.")
        return None

f = "gaurav.txt" 
file_content = read_file(f)
if file_content is not None:
    print("File content:")
    print(file_content)
"""
OUTPUT
Error: File 'gaurav.txt' not found.
"""
