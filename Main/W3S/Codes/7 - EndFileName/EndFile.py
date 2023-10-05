# 7. Write a Python program that accepts a filename
# from the user and prints the extension of the file.

file = input("Escreva o nome completo do seu arquivo: ").strip()
file_extension = file.split('.')[1]
print(f"Sua extensão de arquivo é: {file_extension}")


# Outros modos de fazer:
# import pathlib
# file = str(input("Escreva o nome completo do seu arquivo: ").strip())
# file_extension = pathlib.Path(file).suffix
# print("Sua extensão de arquivo é: ", file_extension)

# filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print("The extension of the file is : " + repr(f_extns[-1]))
