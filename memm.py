import psutil
import sys

def getProcessByName(name):
    for proc in psutil.process_iter():
        if (proc.name() == name + ".exe"):
            return proc


def printSummary(maxMemory):
    print("Max memory used: %fMB (%dBytes)" % (maxMemory / 1024 / 1024, maxMemory) )

def main():
    name = sys.argv[1]
    process = getProcessByName(name)
    maxMemory = 0
    if(process == None):
        print("Can't find process: " + name)
        return
    print("%s is using:" % name)
    try:
        while (psutil.pid_exists(process.pid)):
            mBytes = process.memory_info().vms
            if(mBytes > maxMemory):
                maxMemory = mBytes
            
            mMBytes = mBytes / (1024*1024)

            

            print("\t%fMB (%dBytes)" % (mMBytes, mBytes), end="\r")
    except psutil.NoSuchProcess:
        printSummary(maxMemory)
        return
    
    
    printSummary(maxMemory)
    




main()