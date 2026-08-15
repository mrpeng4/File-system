from functions import BaseFunctions
import json

functions = BaseFunctions()

with open("User_data.pilu", "r") as data:
    userdata = json.load(data)

if userdata != {}:
    functions.login()
else:
    functions.signup()

print("please be aware this is in it's beta stages so it may have some bugs\n")

while functions.turn_off != True:
    command_path_list = functions.input_command()
    if command_path_list[0].lower() == "listfiles" or command_path_list[0].lower() == "ls":
        functions.listfiles()
    elif command_path_list[0].lower() == "gointo" or command_path_list[0].lower() == "cd":
        try:
            functions.gointo(command_path_list[1])
        except IndexError:
            print("please specify a folder to gointo.")

    elif command_path_list[0].lower() == "off" or command_path_list[0].lower() == "qe":
        functions.off()
    elif command_path_list[0].lower() == "goback" or command_path_list[0].lower() == "bc":
        functions.goback()
    elif command_path_list[0].lower() == "makefolder" or command_path_list[0].lower() == "mkf":
        try:
            functions.make_folder(command_path_list[1])
        except IndexError:
            print("please specify a folder to make.")
    elif command_path_list[0].lower() == "makefile" or command_path_list[0].lower() == "mkfl":
        try:
            functions.makefile(command_path_list[1], command_path_list[2])
        except IndexError:
            print("please specify a file to make or a filetype of the file.")
    elif command_path_list[0].lower() == "write" or command_path_list[0].lower() == "w":
        try:
            functions.addtext(command_path_list[1])
        except IndexError:
            print("please specify a file to edit.")
    elif command_path_list[0].lower() == "overwrite" or command_path_list[0].lower() == "or":
        try:
            functions.ortext(command_path_list[1])
        except IndexError:
            print("please specify a file to edit.")
    elif command_path_list[0].lower() == "read" or command_path_list[0].lower() == "rd":
        try:
            functions.readfile(command_path_list[1])
        except IndexError:
            print("please specify a file to read.")

    else:
        print(f"Command '{command_path_list[0]}' does not exist.")