
# Create a new file and write data to it
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test.\n")

print("Data has been written to the file.")




# Read data from an existing file
with open("example.txt", "r") as file:
    data = file.read()

print("Data read from the file:")
print(data)


# Append data to an existing file
with open("example.txt", "a") as file:
    file.write("Appending more data.\n")

print("Data has been appended to the file.")


