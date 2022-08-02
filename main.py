import os
import sys
import subprocess
from pathlib import Path

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_path = sys.argv[2]
    if len(sys.argv) < 3:
        print("Insufficient arguments")
        sys.exit()

    cur_path = Path(__file__).parent.resolve()
    print(cur_path)
    test = os.getcwd()
    print(test)
    os.chdir("..")
    aPath = ""
    bPath = ""
    cPath = ""
    proc = subprocess.Popen('cd & echo %cd% & echo a & echo b', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = proc.communicate()
    print(str(out.decode()))