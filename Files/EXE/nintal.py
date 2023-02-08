from sys import *


def open_file(filename:str):
    if ".n" == filename:
        data = open(filename,'r').read()
        return data
    else:
        raise CannotRun



def parse(filecontents):
    fl = ""
    if "print" in filecontents:
        fl = filecontents.replace('print', '')
        fl  = fl.replace("\n",'')
        fl = fl.replace("\"", "")
        if ";" in fl:
            if " ; " in fl:
                fl = fl.replace(' ; ','\n')
            elif "; " in fl:
                fl = fl.replace('; ', '\n')

    if fl is not None:
        fl = fl[1:]
        fl = fl[:-1]
        return fl
    else:
        return ""
    


def run():
    data = open_file(argv[1])
    print(parse(data))



class CannotRun:
    def __init__(self) -> None:
        print("Sorry, but could'nt run the file!")



if __name__ == '__main__':
    run()
