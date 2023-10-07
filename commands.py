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

# RM

def rm(file):
    try:
        os.remove(file)
    except FileNotFoundError:
        print(f"ERROR: File '{file}' not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for file '{file}'.")
    except Exception as e:
        print(f"ERROR: {e}")

# RENAME

def rename(old, new):
    try:
        os.rename(old, new)
    except FileNotFoundError:
        print(f"ERROR: File '{old}' not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for file '{old}'.")
    except Exception as e:
        print(f"ERROR: {e}")

# HELP

def help():
    print("Commands:")
    print("  cat <file> - print file contents")
    print("  cd <path> - change directory")
    print("  clear - clear screen")
    print("  echo <text> - print text")
    print("  exit - exit shell")
    print("  help - print this help")
    print("  ls - list directory contents")
    print("  mkdir <folder> - create directory")
    print("  rename <old> <new> - rename file")
    print("  rm <file> - remove file")
    print("  rmdir <folder> - remove directory")
    print("  set <var> <value> - set environment variable")
    print("  unset <var> - unset environment variable")
    print("  whoami - print current user")

# SET

def set(var, value):
    try:
        os.environ[var] = value
    except Exception as e:
        print(f"ERROR: {e}")

# UNSET

def unset(var):
    try:
        del os.environ[var]
    except Exception as e:
        print(f"ERROR: {e}")

# WHOAMI

def whoami():
    print(os.getenv("USERNAME"))

# PATH

def path():
    print(os.getenv("PATH"))

# PWD

def pwd():
    print(os.getcwd())

# CP

def cp(old, new):
    try:
        with open(old, "r") as f:
            read = f.read()
            with open(new, "w") as f2:
                f2.write(read)
    except FileNotFoundError:
        print(f"ERROR: File '{old}' not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for file '{old}'.")
    except Exception as e:
        print(f"ERROR: {e}")

# MV

def mv(old, new):
    try:
        os.rename(old, new)
    except FileNotFoundError:
        print(f"ERROR: File '{old}' not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for file '{old}'.")
    except Exception as e:
        print(f"ERROR: {e}")

# DATE

def date():
    import datetime
    print(datetime.datetime.now())

# GREP

def grep(file, pattern):
    try:
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                if pattern in line:
                    print(line)
    except FileNotFoundError:
        print(f"ERROR: File '{file}' not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for file '{file}'.")
    except Exception as e:
        print(f"ERROR: {e}")

# FIND

def find(path, pattern):
    try:
        files = os.listdir(path)
        for file in files:
            if pattern in file:
                print(file)
    except FileNotFoundError:
        print(f"ERROR: Directory '{path}' not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for directory '{path}'.")
    except Exception as e:
        print(f"ERROR: {e}")

# TREE

def tree(path="."):
    try:
        files = os.listdir(path)
        for file in files:
            print(file)
            if os.path.isdir(file):
                tree(file)
    except FileNotFoundError:
        print(f"ERROR: Directory '{path}' not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for directory '{path}'.")
    except Exception as e:
        print(f"ERROR: {e}")

# CHMOD

def chmod(file, mode):
    try:
        os.chmod(file, mode)
    except FileNotFoundError:
        print(f"ERROR: File '{file}' not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for file '{file}'.")
    except Exception as e:
        print(f"ERROR: {e}")

# CHOWN

def chown(file, user):
    try:
        os.chown(file, user)
    except FileNotFoundError:
        print(f"ERROR: File '{file}' not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for file '{file}'.")
    except Exception as e:
        print(f"ERROR: {e}")

# HISTORY

def history():
    try:
        with open("history.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                print(line)
    except FileNotFoundError:
        print(f"ERROR: File 'history.txt' not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for file 'history.txt'.")
    except Exception as e:
        print(f"ERROR: {e}")

# ZIP

def zip(file, zip):
    try:
        import zipfile
        with zipfile.ZipFile(zip, "w") as zip_file:
            zip_file.write(file)
    except FileNotFoundError:
        print(f"ERROR: File '{file}' not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for file '{file}'.")
    except Exception as e:
        print(f"ERROR: {e}")

# UNZIP

def unzip(zip, path):
    try:
        import zipfile
        with zipfile.ZipFile(zip, "r") as zip_file:
            zip_file.extractall(path)
    except FileNotFoundError:
        print(f"ERROR: File '{zip}' not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for file '{zip}'.")
    except Exception as e:
        print(f"ERROR: {e}")

# PYTHON

def python(file):
    try:
        import subprocess
        subprocess.run(["python", file])
    except FileNotFoundError:
        print(f"ERROR: File '{file}' not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for file '{file}'.")
    except Exception as e:
        print(f"ERROR: {e}")

# PING

def ping(host):
    try:
        import subprocess
        subprocess.run(["ping", host])
    except FileNotFoundError:
        print(f"ERROR: Host '{host}' not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for host '{host}'.")
    except Exception as e:
        print(f"ERROR: {e}")

# IFCONFIG

def ifconfig():
    try:
        import subprocess
        subprocess.run(["ipconfig"])
    except FileNotFoundError:
        print(f"ERROR: ipconfig not found.")
    except PermissionError:
        print(f"ERROR: Permission denied for ipconfig.")
    except Exception as e:
        print(f"ERROR: {e}")