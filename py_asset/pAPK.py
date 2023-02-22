# APKS -> APK Backend
import os
import shutil
import subprocess
import threading
import xml.etree.ElementTree as ET

import yaml

locate = ""

"""
    Remove AndroidManifest Configruation
    -   ExtractNativeLibs
    -   IsSplitRequited
    -   localeConfig
    POP -> Remove Line
"""
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

"""
    Extract APK (Decompile)
"""
def extract(location):
    s = subprocess.Popen(['apktool','d','-f',location],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
    out,err = s.communicate()

"""
    Masuk Ke Directory Unkown (Lokasi Semua APK Split)
"""
def cgFolder(location):
    global locate
    os.chdir(location) # Cd .out
    os.chdir("unknown") # cd unkown
    locate = os.getcwd() # global path cd:\\w\base.out\unkown

"""
    Pindahin Semua Resource Dari APK Lain ke Main APK (Base)
"""
def moveFile(file,system,basefile):
    tmplist = [x for x in file if not x.startswith(basefile)] # Nge List Nama APK Lain
    for i in tmplist:
        for root,dirs,files in os.walk(i): 
            for name in dirs:
                try:
                    os.makedirs(locate+system+basefile+system+os.path.join(root, name).replace(i+system,'')) # Bikin Folde Yang GK ADA DI BASE
                except FileExistsError:
                    pass
            for name in files: # Copy File Udah Ada Skip
                try :
                    fd  = os.open(locate+system+basefile+system+os.path.join(root,name).replace(i+system,''),os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                    with os.fdopen(fd, 'wb') as f:
                        with open(os.path.join(root,name),'rb') as sf:
                            shutil.copyfileobj(sf,f)
                except FileExistsError:
                    pass

"""
    APKTool YML -> Masukin Data APKTool.yml APK Lain ke APK Base
"""
def apkYML(file,system,basefile):
    baseLocation = locate+system+basefile+system+"apktool.yml" # Main apktool.yml Location
    tmplist = [x for x in file if not x.startswith(basefile)] 
    with open(baseLocation) as files: # Baca apktool.yml Main APK
        error = files.readline() # Ketika Di Baca Baris Pertama Pasti Selalu Error Di Semua File
        data = yaml.full_load(files) # Convert Ke YAML
    tmp = data['doNotCompress'] #Ngambil Semua  String Bagian doNotCompress
    for i in tmplist: # Baca apktool.yml APK Lain
        with open(locate+system+i+system+"apktool.yml") as files:
            files.readline()
            datatmp = yaml.full_load(files)
            tmp += datatmp['doNotCompress']
    cleanData = list(set(tmp)) # Bandingin Antara Main ama APK Lain (Kalau Udah Ada Gak Di Masukin)
    data['doNotCompress'] = cleanData 
    with open(baseLocation,'w') as files: # Tulis Ulang Bagian doNotCompress Yang Baru Ke APKTOOL.yml
        files.writelines(error)
        yaml.dump(data,files)

"""
    Recompile Process
"""
def compile(fileLocation):
    s = subprocess.Popen(['apktool','b','--use-aapt2',fileLocation],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
    out,err = s.communicate()

def run(filename,tmpfile):
    os.chdir("decompile") # CD Decompile
    base = os.getcwd() # Ambil Path Current
    value = filename.split("/")[-1] # Split dan Ambil FileName
    extract(filename)
    # print("[+] Extract Done")
    cgFolder(value+".out") # Cd Base.out
    # print("[+] Change Dir")
    for i in os.listdir(): # List Of APK
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