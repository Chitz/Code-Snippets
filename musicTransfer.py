import os
import time
import shutil
#The path of your Music Folder under Linux w/o the backslash at the end e.g '/home'
linuxPathname = "/home/chitesh/Desktop/music"
#The path of your Music Folder under Windows/Other OS w/o the backslash at the end e.g 'media/OS_/User'
winPathname = "/media/OS_/music"
if os.path.exists(linuxPathname+"/log.txt") == False:
    file = open(linuxPathname+"/log.txt",'w')       #LastUpdated Log File
    stat = os.stat(linuxPathname)
    log = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(stat.st_mtime))
    file.write(log)
    file.close()
else:
    file = open(linuxPathname+"/log.txt",'r')
    lastUpdate = file.readline()
    stat = os.stat(linuxPathname)
    presentLog = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(stat.st_mtime))
    if presentLog != lastUpdate:
        linuxFiles = []
        winFiles = []
        for f in os.listdir(linuxPathname):
            linuxFiles.append(f)
        for f in os.listdir(winPathname):
            winFiles.append(f)      
        updateFiles = list(set(linuxFiles)-set(winFiles))
        for f in updateFiles:
            if f != "log.txt":
                filePath = linuxPathname+"/%s"%f
                shutil.copy(filePath, winPathname)
        fileWrite = open(linuxPathname+"/log.txt",'w')
        fileWrite.write(presentLog)
        fileWrite.close()
    file.close()
    
