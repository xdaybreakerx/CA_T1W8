readme_file = open("readme.txt", "r+")


readme_file.write("I don't know what to write \n")

readme_file.write("Writing at end")

print(readme_file.read())


readme_file.close()