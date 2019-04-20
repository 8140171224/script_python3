from sys import argv

script, filename = argv

txt = open(filename) 

print(f"Here's your file name {filename}:\n\n\n\n\n\n\n")
print(txt.read())

print("Type the filename again:\n\n\n")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())
