from functions import BaseFunctions
import json
import sys
import time


def animate_pilu_fill():
    logo = [
        "████  ██  █     █  █",
        "█  █  ██  █     █  █",
        "████  ██  █     █  █",
        "█     ██  █     █  █",
        "█     ██  ████  ████"
    ]

    shades = [' ', '░', '▒', '▓', '█']
    for _ in range(len(logo)):
        print()

    total_steps = 15

    for step in range(total_steps + 1):
        sys.stdout.write(f'\x1b[{len(logo)}A')

        for row_idx, row_str in enumerate(logo):
            inv_row = (len(logo) - 1) - row_idx

            fill_level = step - (inv_row * 2)

            if fill_level < 0:
                char_to_use = shades[0]
            elif fill_level >= len(shades) - 1:
                char_to_use = shades[4]
            else:
                char_to_use = shades[fill_level]

            animated_row = ""
            for char in row_str:
                if char == '█':
                    animated_row += char_to_use
                else:
                    animated_row += ' '

            sys.stdout.write('\x1b[2K')
            print(animated_row)

        time.sleep(0.19)
animate_pilu_fill()

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
    elif command_path_list[0].lower() == "delete" or command_path_list[0].lower() == "rf":
        try:
            functions.delete(command_path_list[1])
        except IndexError:
            print("please specify a file to read.")
    elif command_path_list[0].lower() == "clear":
            functions.clear()

    else:
        print(f"Command '{command_path_list[0]}' does not exist.")
