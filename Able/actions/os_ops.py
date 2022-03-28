import os
import subprocess as sp

paths = {
    'discord': "C:\\Users\\wchurchill_bnsstuden\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe"
}


def open_discord():
    os.startfile(paths['discord'])


def open_cmd():
    os.system('start cmd')


def open_calculator():
    sp.Popen(paths['calculator'])
