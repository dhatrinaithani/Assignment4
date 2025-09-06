def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading file content:\n")
            for line_num, line in enumerate(file, start=1):
                print(f"Line {line_num}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

read_file("sample.txt")
