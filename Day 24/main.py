#to print the text in the file - open read and print close 
file = open("my_txt_file.txt")
contents = file.read()
print(contents)
file.close()

#to write this text into the text file
#  in the place of the already existing files
with open("my_txt_file.txt",mode="w") as file:
    file.write("Na nala iruken nee...?")

#add this text to the existing text without deleting them 
with open("my_txt_file.txt",mode="a") as file:
    file.write("\n I am Great. Thanks for asking.")

#to create a new file with new text 
with open("new_file.txt",mode = "w") as file:
    file.write("New Text..")