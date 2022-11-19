# Basic Utils Menu
import subprocess

def deviceChecking():
    s = subprocess.check_output(["adb","devices"]).decode().replace('\n\n','\r\n')
    if(len(s)<30):
        return 1
    else:
        return s.split("\r\n")[1].split('\t')[0]
