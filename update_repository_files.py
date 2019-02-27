import os
import ftplib

d = {1: "experimental",
     2: "developers",
     3: "go-developers",
     4: "optional",
     5: "developers-optional",
     6: "go-developers-optional",
     7: "rc-optional",
     8: "testing",
     9: "go-testing",
     10: "rc",
     11: "critical"}


def create_direcrory():
    for key, val in d.items():
        print(key, ".", val)
    try:
        user_input = int(input("Choose your option: (example 1)>"))
        return d[user_input]
    except Exception as e:
        print("Error", e.__doc__)
        exit(1)


def create_files_directory(user_input):
    for file in os.listdir(path="."):
        if file.endswith(".deb"):
            f = open(os.path.join(file) + "." + user_input, "tw", encoding='utf-8')
            f.close()


def search_file():
    for filename in os.listdir(path="."):
        if filename.endswith(".deb") or (filename.split('.')[-2]) == 'deb':
            yield filename


def open_directory(filename):
    ftp = ftplib.FTP('ftp', 'login', 'pass')
    ftp.cwd('/repo-channel')
    f = open(filename, "rb")
    ftp.storbinary('STOR ' + filename, f)
    f.close()
    ftp.retrlines('NLST')
    ftp.quit()
    # os.remove(filename)


create_files_directory(create_direcrory())
search_file()
mygenerator = search_file()
for filename in mygenerator:
    open_directory(filename)
