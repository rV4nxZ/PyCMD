import os
import readline

# CAT

def cat(file):
    try:
        with open(file, "r") as f:
            read = f.read()
            print(read)
    except FileNotFoundError:
        print(f"ERROR: File '{file}' not found.")
    
    except Exception as e:
        print(e)

# LS

def ls(path="."):
    try:
        files = os.listdir(path)
        for file in files:
            print("-", file)
    except FileNotFoundError:
        print(f"ERROR: Directory '{path}' not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for directory '{path}'.")
    except Exception as e:
        print(f"ERROR: {e}")

# CD

def cd(path):
    try:
        os.chdir(path)
    except FileNotFoundError or WindowsError:
        print(f"ERROR: Directory '{path}' not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for directory '{path}'.")
    except Exception as e:
        print(f"ERROR: {e}")

def complete_cd(text, state):
    dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
    matches = [d for d in dirs if d.startswith(text)]
    if state < len(matches):
        return matches[state]
    else:
        return None

readline.set_completer_delims(' \t\n')
readline.parse_and_bind("tab: complete")
readline.set_completer(complete_cd)

# CLEAR

def clear():
    os.system("cls")

# ECHO

def echo(text):
    print(text)

# MKDIR

def mkdir(folder):
    try:
        os.mkdir(folder)
    except FileExistsError:
        print(f"ERROR: Directory '{folder}' already exists.")
    except FileNotFoundError:
        print(f"ERROR: Directory '{folder}' not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for directory '{folder}'.")
    except Exception as e:
        print(f"ERROR: {e}")

# RMDIR

def rmdir(folder):
    try:
        os.rmdir(folder)
    except FileNotFoundError:
        print(f"ERROR: Directory '{folder}' not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for directory '{folder}'.")
    except Exception as e:
        print(f"ERROR: {e}")