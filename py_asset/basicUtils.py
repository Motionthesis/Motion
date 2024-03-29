# Basic Utils Backend
import os
import subprocess
import threading
import time


def deviceChecking():
    s = subprocess.check_output(["adb","devices"],shell=True).decode().replace('\n\n','\r\n')
    if(len(s)<30):
        return 1
    else:
        return s.split("\r\n")[1].split('\t')[0]

#Need Adjusting if Won't Work in Linux or MacOS
"""
    Frida List -> SEMUA
"""
def fridaList():
    s = subprocess.Popen(['frida-ps','-Uaij'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
    (out,err) = s.communicate()
    return out

"""
    ActiveList -> Ada PID Only
"""
def activeList():
    s = subprocess.Popen(['frida-ps','-Uaj'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
    (out,err) = s.communicate()
    return out

"""
    Uninstall APP
"""
def uninstall(packageName):
    s = subprocess.Popen(['adb','uninstall',packageName],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
    (out,err) = s.communicate()
    return out

"""
    Spawn Shell
"""
def spawnShell():
    os.system("start cmd /c adb shell")

"""
    Screenshoot
"""
def screenshot():
    ts = time.strftime('%Y%m%d_%H%M%S', time.localtime())
    s = subprocess.Popen(['adb','shell','screencap','-p','/sdcard/Download/'+str(ts)+'.png'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True).wait()
    p = subprocess.Popen(['adb','pull','/sdcard/Download/'+str(ts)+'.png','screenshot/'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True).wait()
    d = subprocess.Popen(['adb','shell','rm','/sdcard/Download/'+str(ts)+'.png'],shell=True).wait()
    if s == 1:
        return "1";
    else:
        return str(ts)+'.png'

# Patch Smali
def patchXML(filename,tmpfile):
    with open(filename,"r") as files: # Baca Inputan File Smali
        smali = files.readlines() # Baca Semua Linenya
    injectPosition = 0 # Variable Injection 0
    for i in range (len(smali)):
        if '# virtual methods' in smali[i]:
            injectPosition = i+3
            break
    payload = \
    """
    const/4 v0, 0x1\n
    const-string v1, "Motion - No Integrity Check"\n
    invoke-static {p0, v1, v0}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;\n
    move-result-object v0\n
    invoke-virtual {v0}, Landroid/widget/Toast;->show()V\n    
    """
    value = ''.join(smali[:injectPosition]) + payload + ''.join(smali[injectPosition:]) # Ambil Depan + Payload + Belakang
    with open(filename,"w") as files: # Smali File
        files.write(value)
    with open(tmpfile,"w") as files: # Ngecheck Udah Kelar Apa Belum
        files.write("2")

def realpatchXML(filename,tmpfile):
    t1 = threading.Thread(target=patchXML,args=(filename,tmpfile,))
    t1.start()

#Decompile
def decompile(fileLocation,base,tmpFile):
    tmpbase = base+"\\decompile"
    os.chdir(tmpbase)
    s = subprocess.Popen(['apktool','d','-f',fileLocation],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
    (out,err) = s.communicate()
    # print("===Decompile===")
    # print(f"Decompile Out : {out.decode()}")
    # print(f"Decompile Err : {err}")
    # print("===============")
    if b'continue' in out:
        with open(tmpFile,"w") as files:
            files.write("1")
    os.chdir(base)

def realDecompile(fileLocation,base,tmpFile):
    t1 = threading.Thread(target=decompile,args=(fileLocation,base,tmpFile,))
    t1.start()

#Recompile
def recompile(fileLocation,tmpFile):
    s = subprocess.Popen(['apktool','b','--use-aapt2',fileLocation],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
    out,err = s.communicate()
    # print("===Recompile===")
    # print(f"Recompile Out : {out.decode()}")
    # print(f"Recompile Err : {err}")
    # print("===============")
    if b"Built apk" in out:
        with open(tmpFile,"w") as files:
            files.write("1")

def realRecompile(fileLocation,tmpfile):
    t1 = threading.Thread(target=recompile,args=(fileLocation,tmpfile))
    t1.start()
    
def checkFrida():
    retval = deviceChecking()
    if retval == 1:
        return 3
    else:
        s = subprocess.Popen(['adb','shell','ps | grep frida'],shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        out,err = s.communicate()
        if b"frida" in out:
            return 1
        else:
            return 2