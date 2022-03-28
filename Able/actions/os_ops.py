import os
import subprocess as sp

paths = {
    'foldverse': "C:\\Users\\minec\\Documents\\Unreal Projects\\FoldverseThree\\FoldverseThree.uproject"
}


def open_project():
    os.startfile(paths['foldverse'])


def open_cmd():
    os.system('start cmd')


def open_calculator():
    sp.Popen(paths['calculator'])
