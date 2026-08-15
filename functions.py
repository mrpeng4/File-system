import json
import time
import os

class BaseFunctions:
    def __init__(self):
        with open("Root.pilu", "r+") as path:
            self.system = json.load(path)
            self.current_path = self.system
            self.path_names = []
            self.turn_off = False
            self.special_char = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "{", "}", "[", "]", "<", ">", "/", "\\"]
            self.special_char = [".","/","\\"]
            self.EDITABLE_EXTENSIONS = [
    # Plain Text & Documentation
    ".txt", ".md", ".markdown", ".rst", ".log", ".nfo", ".lic",

    # Data & Configurations
    ".json", ".jsonl", ".csv", ".tsv", ".yaml", ".yml", ".xml",
    ".toml", ".ini", ".env", ".conf", ".config", ".properties",

    # Web & Stylesheets
    ".html", ".htm", ".css", ".scss", ".sass", ".less", ".svg",

    # Code & Scripts
    ".py", ".pyw", ".js", ".jsx", ".ts", ".tsx", ".c", ".h",
    ".cpp", ".hpp", ".cs", ".java", ".kt", ".rs", ".go", ".swift",
    ".php", ".rb", ".lua", ".sh", ".bat", ".cmd", ".ps1", ".sql"
]

    def check_slash_infront(self, path:str):
        path_list = path.split("/")
        if "" not in path_list:
            return True
        else:
            return False

    def textedit_or(self, file):
        try:
            self.current_path[file]
        except KeyError:
            print("this file does not exists in the folder")
        else:
            print(f"--- Editing '{file}' ---")
            print("Type your text below. Type ':save' on a new line to finish & save.\n")
            lines = []

            while True:
                line = input("~ ")

                if line.strip() == ":exit":
                    try:
                        return self.current_path[file]
                    except KeyError:
                        print("this file does not exists in the folder")
                    break

                if line.strip() == ":save":
                    return "\n".join(lines)
                lines.append(line)

    def textedit_add(self, file):
        try:
            self.current_path[file]
        except KeyError:
            print("this file does not exists in the folder")
        else:
            print(f"--- Editing '{file}' ---")
            print("Type your text below. Type ':save' on a new line to finish & save.\n")

            lines = self.current_path[file].split("\n") if self.current_path[file] else []
            for line in lines:
                print(f"~ {line}")

            while True:
                line = input("~ ")

                if line.strip() == ":exit":
                    try:
                        return self.current_path[file]
                    except KeyError:
                        print("this file does not exists in the folder")
                    break

                if line.strip() == ":save":
                    break
                lines.append(line)
            return "\n".join(lines)

    def makefile(self, file_name, file_type):
        filename = file_name.strip()
        filetype = file_type.strip()
        filetype_dot = "." + filetype
        if 0 < len(filetype) <= 8:
            if filename != "":
                file = filename + "." + file_type
                carry_on = True
                for symbol in self.special_char:
                    if symbol in filename:
                        print(f"\"{symbol}\" this character is not allowed in a file name.")
                        carry_on = False
                        break

                if carry_on:
                    if filetype_dot in self.EDITABLE_EXTENSIONS:
                        edit_y_n = input(f"do you want to edit the {filetype} file right now?\nEnter Yes or No: ")
                        if edit_y_n.lower().strip() == "yes":
                            text = self.textedit_or(file)
                            self.current_path[file] = text
                            with open("Root.pilu", "w") as data:
                                json.dump(self.system, data, indent=4)
                        else:
                            self.current_path[file] = ""
                            with open("Root.pilu", "w") as data:
                                json.dump(self.system, data, indent=4)
                    else:
                        print("we only support specific types of file types of filetypes\nsorry the rest are in development :(")
                        filetypes_inquire = input("type Yes to see the supported filetypes else type No: ")
                        if filetypes_inquire.lower().strip() == "yes":
                            print(self.EDITABLE_EXTENSIONS)
                        else:
                            pass
            else:
                print("please provide a filename")
        else:
            print("The length of a the extension\ncan't be more than 8 letters or less than 0")

    def addtext(self, file):
        try:
            self.current_path[file]
        except KeyError:
            print("this file does not exists in the folder")
        else:
            full_text = self.textedit_add(file)
            self.current_path[file] = full_text
            with open("Root.pilu", "w") as data:
                json.dump(self.system, data, indent=4)

    def ortext(self, file):
        try:
            self.current_path[file]
        except KeyError:
            print("this file does not exists in the folder")
        else:
            full_text = self.textedit_or(file)
            self.current_path[file] = full_text
            with open("Root.pilu", "w") as data:
                json.dump(self.system, data, indent=4)

    def readfile(self, file):
        try:
            self.current_path[file]
        except KeyError:
            print(f"this {file} does not exists in the folder")
        else:
            if type(self.current_path[file]) != dict:
                print(self.current_path[file])
            else:
                print(f"you are trying to read a Folder {file} and not a File.")

    def make_folder(self, foldername):
        folder_name = foldername.strip()
        if foldername != "":
            carry_on = True
            for symbol in self.special_char:
                if symbol in folder_name:
                    print(f"\"{symbol}\" this character is not allowed in a folder name.")
                    carry_on = False
                    break

            if carry_on:
                self.current_path[folder_name] = {}
                with open("Root.pilu", "w") as data:
                    json.dump(self.system, data, indent=4)
            else:
                print("no folder created.")
        else:
            print("please specify a folder to make.")

    def input_command(self):
        the_line_typed_by_the_user = input(":> ")
        command_list = the_line_typed_by_the_user.split(" ")
        return command_list

    def gointo(self, folder_user):
        if self.check_slash_infront(folder_user):

                folder_list = folder_user.split("/")
                if folder_list[0] == "Root":
                    self.current_path = self.system
                    folder_list = folder_list[1:]
                    self.path_names = []

                for folder in folder_list:
                    try:
                        if type(self.current_path[folder]) != dict:
                            print(f"this {folder} does not exists")
                            break
                        else:
                            self.path_names.append(folder)
                            self.current_path = self.current_path[folder]
                            print(f"Went into {folder}")
                    except KeyError:
                        print(f"This folder {folder} does not exists")

        else:
            print("You didn't specify a folder to go into :(, or try removing\nthe / in front of the path you provided")

    def clear_terminal(self):
        os.environ.setdefault('TERM', 'xterm-256color')
        os.system('cls' if os.name == 'nt' else 'clear')

    def signup(self):
        print("it seems like you don't have an account please make one\nplease fill in these details:")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        if username != "" and password != "":
            if " " not in username and " " not in password:

                user_data = {
                    "username": username,
                    "password": password,
                }
                with open("User_data.pilu", "w") as data:
                    json.dump(user_data, data)
                self.clear_terminal()
                print("Your data has been saved!")
                time.sleep(2)
                self.clear_terminal()
            else:
                self.clear_terminal()
                print("No spaces allowed in the username or the password")
                self.signup()
        else:
            self.clear_terminal()
            print("Please enter valid details don't leave anything blank")
            self.signup()

    def login(self):
        print("Please login")
        with open("User_data.pilu", "r") as data:
            user_data = json.load(data)
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        if username != "" and password != "":
            if user_data["username"] == username and user_data["password"] == password:
                self.clear_terminal()
                print("login successful!")
                time.sleep(2)
                self.clear_terminal()
            else:
                self.clear_terminal()
                print("Wrong username or password.")
                self.login()
        else:
            self.clear_terminal()
            print("Please enter valid details don't leave anything blank")
            self.login()

    def goback(self):
        try:
            self.path_names.pop(-1)
        except IndexError:
            print("you are already in the Root folder")
        else:
            self.current_path = self.system
            if self.path_names != []:

                print(f"you went back into {self.path_names[-1]}")
                for names in self.path_names:
                    self.current_path = self.current_path[names]
            else:
                print("you are in the Root folder")

    def off(self):
        self.turn_off = True

    def listfiles(self):
        if self.current_path != {}:
            for files in self.current_path:
                print(files)
        else:
            print("there are no files in the Root folder to list :(")

