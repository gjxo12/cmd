import os
import sys
import subprocess
from pathlib import Path


class branchEnum():
    def __init__(self, branch1, branch2, branch3):
        self.branch1 = branch1
        self.branch2 = branch2
        self.branch3 = branch3


def move(argv: str):
    print(f'{argv}')
    os.chdir(argv)

    if not Path(argv).is_dir():
        print(f'error....')

    proc = subprocess.Popen('cd ', shell=True, stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    out, err = proc.communicate()
    print(str(out.decode()))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Insufficient arguments")
        sys.exit()

    enter_path = os.getcwd()
    print(enter_path)
    root_path = os.path.abspath("..")
    print(root_path)
    branch = branchEnum(sys.argv[1], sys.argv[2], sys.argv[3])
    print(branch.branch1)

    for i in sys.argv[1:]:
        move(root_path + '\\' + i)


    print("Subprocess...........")

