# Install APK Backend
from pathlib import Path
import subprocess
import os
import shutil
import time
import threading

baseFolder = os.getcwd()
# win = chr(92)

def extract(location,platform):
    if platform == "Windows":
        s = subprocess.Popen(['apktool','d','-f',location],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)

def install(location,mode,filename,platform,tmpfile):
    os.chdir('decompile')
    base = os.getcwd()
    win = "\\"
    if platform == "Windows":
        if mode == 1:
            s = subprocess.Popen(['adb','install',location],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            (out,err) = s.communicate()
            print("===Install APK===")
            print(f"Install Out : {out.decode()}")
            print(f"Install Err : {err.decode()}")
            print("=================")
            os.chdir(baseFolder)
            if b'Success' in out:
                with open(tmpfile,"w") as files:
                    files.write("1")
            else:
                with open(tmpfile,"w") as files:
                    files.write("2")
        else:
            locationAPKS = base+win+filename+".out"+win+"unknown"
            extract(location,platform)
            time.sleep(0.7)
            if Path(locationAPKS).exists():
                os.chdir(locationAPKS)
                fileList = os.listdir()
                apkList = [x for x in fileList if x.endswith("apk")]
                installCommand = ['adb','install-multiple']
                for i in apkList:
                    installCommand.append(i)
                s = subprocess.Popen(installCommand,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
                (out,err) = s.communicate()
                print("===Install APKS===")
                print(f"Install Out : {out.decode()}")
                print(f"Install Err : {err.decode()}")
                print("=================")
                os.chdir(baseFolder)
                # shutil.rmtree(base+win+filename+".out")
                if b'Success' in out or b'extracted' in err:
                    with open(tmpfile,"w") as files:
                        files.write("1")
                else:
                    with open(tmpfile,"w") as files:
                        files.write("2")

def realInstall(location,mode,filename,platform,tmpfile):
    t1 = threading.Thread(target=install,args=(location,mode,filename,platform,tmpfile,))
    t1.start()