# APKS -> APK Backend
import xml.etree.ElementTree as ET
import subprocess
import os
import shutil
import yaml
import threading

locate = ""

def cleanXML():
    root = ET.parse("AndroidManifest.xml").getroot()
    for child in root:
        if "application" in child.tag:
            try:
                child.attrib.pop("{http://schemas.android.com/apk/res/android}extractNativeLibs")
            except KeyError:
                # print("extractNativeLibs Not Found")
                pass
            try:
                child.attrib.pop("{http://schemas.android.com/apk/res/android}isSplitRequired")
            except KeyError:
                # print("isSplit Not Found")
                pass
            try:
                child.attrib.pop("{http://schemas.android.com/apk/res/android}localeConfig")
            except KeyError:
                pass
    open("AndroidManifest.xml","wb").write(ET.tostring(root))

def extract(location):
    s = subprocess.Popen(['apktool','d','-f',location],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
    out,err = s.communicate()

def cgFolder(location):
    global locate
    os.chdir(location)
    os.chdir("unknown")
    locate = os.getcwd()

def moveFile(file,system,basefile):
    tmplist = [x for x in file if not x.startswith(basefile)]
    for i in tmplist:
        for root,dirs,files in os.walk(i):
            for name in dirs:
                try:
                    os.makedirs(locate+system+basefile+system+os.path.join(root, name).replace(i+system,''))
                except FileExistsError:
                    pass
            for name in files:
                try :
                    fd  = os.open(locate+system+basefile+system+os.path.join(root,name).replace(i+system,''),os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                    with os.fdopen(fd, 'wb') as f:
                        with open(os.path.join(root,name),'rb') as sf:
                            shutil.copyfileobj(sf,f)
                except FileExistsError:
                    pass

def apkYML(file,system,basefile):
    baseLocation = locate+system+basefile+system+"apktool.yml"
    tmplist = [x for x in file if not x.startswith(basefile)]
    with open(baseLocation) as files:
        #First Line Always Error
        error = files.readline()
        data = yaml.full_load(files)
    tmp = data['doNotCompress']
    for i in tmplist:
        with open(locate+system+i+system+"apktool.yml") as files:
            files.readline()
            datatmp = yaml.full_load(files)
            tmp += datatmp['doNotCompress']
    cleanData = list(set(tmp))
    data['doNotCompress'] = cleanData
    with open(baseLocation,'w') as files:
        files.writelines(error)
        yaml.dump(data,files)

def compile(fileLocation):
    s = subprocess.Popen(['apktool','b','--use-aapt2',fileLocation],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
    out,err = s.communicate()

def run(filename,tmpfile):
    os.chdir("decompile")
    base = os.getcwd()
    value = filename.split("/")[-1]
    extract(filename)
    # print("[+] Extract Done")
    cgFolder(value+".out")
    # print("[+] Change Dir")
    for i in os.listdir():
        if "apk" in i:
            extract(i)
        os.remove(i)
    os.chdir("base")
    cleanXML()
    # print("[+] Clean XML")
    os.chdir("..")
    file = os.listdir()
    moveFile(file,"\\","base")
    # print("[+] Move File")
    apkYML(file,"\\","base")
    # print("[+] Apktool YML")
    compile(os.getcwd() + "\\base")
    # print("[+] Compile")
    os.chdir(base)
    with open(tmpfile,"w") as files:
        files.write("1")
    

def realRun(filename,tmpfile):
    t1 = threading.Thread(target=run,args=(filename,tmpfile,))
    t1.start()