# import pathlib

# file = str(input("Escreva o nome completo do seu arquivo: ").strip())
# file_extension = pathlib.Path(file).suffix
# print("Sua extensão de arquivo é: ", file_extension)

file = input("Escreva o nome completo do seu arquivo: ").strip()
file_extension = file.split('.')[1]
print(f"Sua extensão de arquivo é: {file_extension}")

# filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print("The extension of the file is : " + repr(f_extns[-1]))
