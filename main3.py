import urllib.request
import shutil
import minecraft_launcher_lib
import subprocess
from minecraft_launcher_lib.utils import get_minecraft_directory
import tkinter as tk
from pathlib import Path

minecraft_directory = get_minecraft_directory().replace('minecraft', 'Starlauncher')
mods_directory = Path(minecraft_directory + '/versions/1.18.2-forge-40.2.4/')
version = '1.18.2'
forge_version = '1.18.2-40.2.4'
#проверка версии
if minecraft_launcher_lib.forge.is_forge_version_valid(forge_version):
    print("its exists")
else:
    print(minecraft_launcher_lib.forge.list_forge_versions())

# загрузка модпака
url = 'https://github.com/Banstra/modsDabloon/releases/download/mods/mods.zip'
Filecheck = Path('mods.zip')

try:
    if Filecheck.is_file():
        shutil.unpack_archive('mods.zip', mods_directory)
        print('unpacked in: ', mods_directory)
    else:
        filehandle = urllib.request.urlretrieve(url, 'mods.zip')
        print('downloading...')
except(Exception ):
    print(Exception)
#shutil.unpack_archive('mods.zip', minecraft_directory)

#UI и запуск игры
def get_input():
    username = entry.get()
    return username


root = tk.Tk()
root.geometry("360x200")
root.title("StarSolar")

# Create an Entry widget
entry = tk.Entry(root)
entry.pack()

label = tk.Label(root, text="StarSolar", font=('Arial', 20))
label.pack(padx=20, pady=20)

minecraft_launcher_lib.forge.install_forge_version(forge_version, minecraft_directory)
# minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=minecraft_directory)

options = {
    'username': get_input(),
    'uuid': '',
    'token': ''
}


def Launch():
    subprocess.call(
        #minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=minecraft_directory,options=options))
        minecraft_launcher_lib.command.get_minecraft_command(version=minecraft_launcher_lib.forge.forge_to_installed_version(forge_version), minecraft_directory=minecraft_directory, options=options))


# Create a button to get the input
button = tk.Button(root, text="Launch", command=Launch)
button.pack()

root.mainloop()


