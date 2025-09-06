def write_and_append(filename):
    # Step 1: Take user input and write to file
    data = input("Enter text to write to the file: ")
    with open(filename, "w") as file:
        file.write(data + "\n")
    print(f"Data successfully written to {filename}.")

    extra_data = input("Enter additional text to append: ")
    with open(filename, "a") as file:
        file.write(extra_data + "\n")
    print("Data successfully appended.")

    print(f"\nFinal content of {filename}:")
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())

write_and_append("output.txt")
