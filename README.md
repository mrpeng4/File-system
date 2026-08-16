# Start up!

<img width="1200" height="634" alt="Screen Recording 2026-08-16 at 11 59 41 AM" src="https://github.com/user-attachments/assets/bae16e6d-dd0b-45bd-a37b-84866a46a57b" />

# Virtual File System CLI

A lightweight, terminal-based file system simulator written in Python. This application emulates standard operating system directory structures, file creation, reading, and editing operations while persisting all data to JSON-formatted `.pilu` system files.

## Project Summary

A Python-based virtual file system CLI application that simulates full directory structures and file management within custom JSON storage files. Features local user authentication, directory navigation, custom file editor with save/exit shortcuts, folder creation, reading, appending, and overwriting for over 40 distinct plain text and code file extensions.

## Features

- User Authentication: Local user signup and login stored securely in User_data.pilu.
- Directory Navigation: Move through virtual nested directories using path commands.
- File Management: Create folders, create files with custom extensions, view contents, append text, and overwrite files.
- Interactive File Editor: Multi-line terminal-based text editor supporting line-by-line input, saving, and exiting.
- Persistent Storage: Automatically syncs all virtual file system changes to Root.pilu.

## How to Use

### 1. Authentication
- On initial launch, if no account details exist in `User_data.pilu`, you will be prompted to sign up by creating a username and password.
<img width="828" height="468" alt="ScreenRecording2026-08-16at10 02 41PM-ezgif com-video-to-gif-converter" src="https://github.com/user-attachments/assets/b4ab442c-bbec-49d6-89ca-3512186971f0" />

- On subsequent launches, enter your credentials at the prompt to log in.
<img width="828" height="458" alt="ezgif com-gif-maker" src="https://github.com/user-attachments/assets/f79940d7-8283-4c3c-bafd-ab44697a176e" />


### 2. Command Execution
Commands are entered at the `:>` terminal prompt. Command arguments are space-separated.

Example sequence:
- `mkf Projects` (Creates a directory named Projects)
- `cd Root/Projects` (Navigates into the Projects directory)
- `mkfl script py` (Creates a Python file named script.py)

### 3. Interactive Text Editor
When creating a file with editing enabled, or when using the `write` or `overwrite` commands, you enter interactive edit mode:
- Lines are entered one by one at the `~` prompt.
- Type `:save` on a new line and press Enter to save changes and return to the main interface.
- Type `:exit` on a new line and press Enter to cancel editing and exit without saving changes.

## Command Reference

| Command | Alias | Syntax | Description |
| :--- | :--- | :--- | :--- |
| listfiles | ls | ls | Displays all files and folders in the current directory. |
<img width="1200" height="664" alt="listfiles_func" src="https://github.com/user-attachments/assets/a8a57f15-6fdb-4521-90fe-c35e5a242ca1" />

| Command | Alias | Syntax | Description |
| :--- | :--- | :--- | :--- |
| gointo | cd | cd  path | Navigates into the specified folder or path (e.g., cd Root/Documents). |
<img width="1200" height="664" alt="gointo_func" src="https://github.com/user-attachments/assets/550ac78c-9eb2-48bd-b998-b6fd35234d8d" />

| Command | Alias | Syntax | Description |
| :--- | :--- | :--- | :--- |
| goback | bc | bc | Returns to the parent directory. |
<img width="1200" height="664" alt="goback_func" src="https://github.com/user-attachments/assets/c987498d-ce4d-4f08-a478-3fbf1bbba084" />

| Command | Alias | Syntax | Description |
| :--- | :--- | :--- | :--- |
| makefolder | mkf | mkf  folder_name | Creates a new subfolder in the current directory. |
<img width="1200" height="664" alt="Makefolder_func" src="https://github.com/user-attachments/assets/728f1d44-96e6-486b-8c68-fca211b7510e" />

| Command | Alias | Syntax | Description |
| :--- | :--- | :--- | :--- |
| makefile | mkfl | mkfl  filename  extension | Creates a file with the specified extension and offers immediate editing. |
<img width="1200" height="664" alt="Makefile_func" src="https://github.com/user-attachments/assets/f0bea4e0-b738-40a8-a470-107ae9ac8272" />

| Command | Alias | Syntax | Description |
| :--- | :--- | :--- | :--- |
| read | rd | rd  filename | Displays the text content of a specified file. |
<img width="828" height="458" alt="ezgif com-video-to-gif-converter" src="https://github.com/user-attachments/assets/5cc1204e-e70f-4885-8c70-a772061f518f" />

| Command | Alias | Syntax | Description |
| :--- | :--- | :--- | :--- |
| write | w | w  filename | Appends new lines of text to an existing file using the interactive editor. |
<img width="828" height="458" alt="ezgif com-video-to-gif-converter-2" src="https://github.com/user-attachments/assets/7696c78c-6872-409e-8311-d4520aee7988" />

| Command | Alias | Syntax | Description |
| :--- | :--- | :--- | :--- |
| overwrite | or | or  filename | Overwrites the entire content of an existing file using the interactive editor. |
<img width="1200" height="664" alt="overwrite_func" src="https://github.com/user-attachments/assets/edf8f77f-ee81-481d-a120-ca86fb05c2ce" />

| Command | Alias | Syntax | Description |
| :--- | :--- | :--- | :--- |
| delete | rf | delete  filename | Deletes the file you gave if the file is in the current directory|
<img width="1200" height="664" alt="delete_func" src="https://github.com/user-attachments/assets/157b8bbb-d0cf-47c5-b912-16e0c0c1ddab" />

| Command | Alias | Syntax | Description |
| :--- | :--- | :--- | :--- |
| clear | no alias | clear | Clears the terminal window, I mean like it just adds like 50 new line so you won't see the previous ones 😅 sorry that was the only option.|
<img width="1200" height="664" alt="clear_func" src="https://github.com/user-attachments/assets/22606550-9693-4fd6-979e-6cf9cbf6ccf8" />

| Command | Alias | Syntax | Description |
| :--- | :--- | :--- | :--- |
| off | qe | off | Exits the virtual file system application. |
<img width="1200" height="664" alt="off_func" src="https://github.com/user-attachments/assets/4328cf28-89fd-4302-8bd9-a88218d8ebf2" />

## Supported File Extensions

File creation supports extensions up to 8 characters in length. Text editing operations are restricted to supported file types listed below:

| Category | Supported Extensions |
| :--- | :--- |
| Plain Text & Documentation | `.txt`, `.md`, `.markdown`, `.rst`, `.log`, `.nfo`, `.lic` |
| Data & Configurations | `.json`, `.jsonl`, `.csv`, `.tsv`, `.yaml`, `.yml`, `.xml`, `.toml`, `.ini`, `.env`, `.conf`, `.config`, `.properties` |
| Web & Stylesheets | `.html`, `.htm`, `.css`, `.scss`, `.sass`, `.less`, `.svg` |
| Code & Scripts | `.py`, `.pyw`, `.js`, `.jsx`, `.ts`, `.tsx`, `.c`, `.h`, `.cpp`, `.hpp`, `.cs`, `.java`, `.kt`, `.rs`, `.go`, `.swift`, `.php`, `.rb`, `.lua`, `.sh`, `.bat`, `.cmd`, `.ps1`, `.sql` |

## Naming Rules and Constraints

| Constraint Type | Rule |
| :--- | :--- |
| Invalid Characters | File and folder names must not contain `.`, `/`, or `\` |
| Extension Length | File extensions must be between 1 and 8 characters long |
| User Credentials | Usernames and passwords cannot contain spaces or be left blank |
| Directory Navigation | Path strings should begin with `Root/` when navigating relative to system root |

## File Structure

- `main.py`: Main application entry point and command loop.
- `functions.py`: Class implementation containing file system logic, authentication, and editor routines.
- `Root.pilu`: JSON database file storing virtual files and folder structure.
- `User_data.pilu`: JSON store holding authentication credentials.

## [>] Installation & Setup Guide

### Prerequisites
* **macOS**: Python 3 installed (check with `python3 --version` in Terminal. Install via [python.org](https://www.python.org/) or `brew install python` if needed).
* **Windows**: Python 3.x installed and added to your system `PATH`.

---

### Option 1: Automatic One-Line Installation (Recommended)

Open your terminal or PowerShell and run the command matching your operating system:

| Operating System | Terminal Command |
| :--- | :--- |
| **macOS / Linux** | `curl -fsSL https://raw.githubusercontent.com/mrpeng4/File-system/main/install.sh \| bash` |
| **Windows (PowerShell)** | `iwr -useb https://raw.githubusercontent.com/mrpeng4/File-system/main/install.ps1 \| iex` |

> **macOS Note**: The script uses `sudo` to create `/usr/local/bin/pilu`, so macOS may prompt you for your admin password during installation.  
> **Windows Note**: If PowerShell blocks script execution, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` first, then run the installer script ;)

#### Verify Installation
Restart your Terminal or PowerShell window and type:

```bash
pilu
```
### Uninstallation

If you ever want to remove `pilu` and all of its virtual files from your machine, run the command for your operating system:

**macOS / Linux (Terminal)**
This command deletes the hidden application folder and removes the terminal shortcut:
```bash
rm -rf "$HOME/Library/Application Support/pilu" && sudo rm -f /usr/local/bin/pilu
```
**Windows (Powershell)**
```bash
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\pilu"
```
# Forget Password
Incase you forgot your password you can type forget in both entries during login to trigger the forget function which makes you type you the security questions you 
entered when you signed up and if they are correct you sign up again replacing your original password and username. No data is lost.

<img width="828" height="468" alt="ezgif com-video-to-gif-converter" src="https://github.com/user-attachments/assets/9ee44076-0729-477b-a0d5-36867958fd71" />
