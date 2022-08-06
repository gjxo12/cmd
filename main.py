import os
import sys
import subprocess
from pathlib import Path


def move():
    proc = subprocess.Popen('cd ', shell=True, stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    out, err = proc.communicate()
    print(str(out.decode()))


def movesst(argv: str):
    print(f'{argv}  ddddd')
    os.chdir(argv)
    if Path(argv).is_dir():
        print(f'{Path(argv)}  경로 있음')
    move()


def moveLib(argv: str):
    print(f'{argv}  ddddd')
    os.chdir(argv)
    move()


def moveEnter(argv: str):
    print(f'{argv}  ddddd')
    os.chdir(argv)
    move()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_path = sys.argv[2]
    if len(sys.argv) < 3:
        print("Insufficient arguments")
        sys.exit()

    cur_path = Path(__file__).parent.resolve()
    test = os.getcwd()
    test = os.path.abspath("..")

    moveLibsst(test + '\\' + sys.argv[1])
    #moveLibanalysis(test + '\\' + sys.argv[2])
    #moveEnterprise(test + '\\' + sys.argv[3])
    print("Subprocess...........")
    # proc = subprocess.Popen('cd & echo %cd% & echo a & echo b', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    # out, err = proc.communicate()
    # print(str(out.decode()))
