import os
def rename_files():
    file_list = os.listdir(r"F:\picture\rename")
    print(file_list)
    saved_path = os.getcwd()
    print("Current work direction is "+saved_path)
    os.chdir(r"F:\picture\rename")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "x_"))
    os.chdir(saved_path)
rename_files()
