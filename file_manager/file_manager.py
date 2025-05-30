import os

def read_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found at path {file_path}")
    
    with open(file_path, 'r') as file:
        return file.read()

def main():
    try:
        # Simulate trying to read a non-existent file
        content = read_file("/tmp/processing/data.json")
        print(content)
    except FileNotFoundError as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    main()
