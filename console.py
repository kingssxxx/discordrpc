import os 
import sys 
import psutil
import logo
import time
import requests
import colors
import settings
import webbrowser

class appsettings():
    usingwrite = settings.app.usingwrite 

def write(phrase, speed):
    if appsettings.usingwrite == False: 
        phraseBackspace = phrase.replace("\n", "")
        print(phraseBackspace)
    else: 
        for char in phrase:
            time.sleep(speed)
            sys.stdout.write(char)
            sys.stdout.flush()  

BYELLOW = '\033[93m'
GREEN  = '\33[92m'
RED    = '\33[31m'
github = "https://github.com/Kingssxd/discordrpc"
CBLUE   = '\33[94m'
bs = 0.00000001
updatelink = "https://raw.githubusercontent.com/Kingssxd/discordrpc/main/update.txt"
version = 1.1

nodefile = "node.exe"
currentdirectory = os.getcwd()

if appsettings.usingwrite == False:
    os.system("title DiscordRPC")
else: 
    os.system("title D")
    time.sleep(bs)
    os.system("title Di")
    time.sleep(bs)
    os.system("title Dis")
    time.sleep(bs)
    os.system("title Disc")
    time.sleep(bs)
    os.system("title Disco")
    time.sleep(bs)
    os.system("title Discor")
    time.sleep(bs)
    os.system("title Discord")
    time.sleep(bs)
    os.system("title DiscordR")
    time.sleep(bs)
    os.system("title DiscordRP")
    time.sleep(bs)
    os.system("title DiscordRPC")

class commands(): 
    launch = "launch"
    configure = "configure"
    help = "help"
    invisiblelaunch = "invislaunch"
    stop = "stop"
    library = "libinstall"
    github = "github"
    update = "update"

def update():
    os.system("cls")
    print(CBLUE + logo.logos.update)
    write("at the moment not available")
    input("press enter to continue")

def githubi(): 
    os.system("cls")
    print(CBLUE + logo.logos.github)
    write(BYELLOW + f"GitHub: {github}", bs)
    write(BYELLOW + "\nPress 1 to open link, press enter to cotinue.", bs)
    choice = input("\n > ")
    if int(choice) == 1:
        os.system(f"start \"\" {github}")
        main()
    else: 
        time.sleep(0.1)
        main()
    
def libinstall(): 
    print(" ")
    os.system("title DiscordRPC ^| Installing PSUTIL")
    os.system("pip install psutil")
    time.sleep(5)
    main()

def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def stopinvis(): 
    for proc in psutil.process_iter():
        if proc.name() == nodefile:
            proc.kill()
    time.sleep(2)
    main()

def invislaunch(): 
    invisiblepath = currentdirectory + "\invisible.vbs"
    invisrunbatch = currentdirectory + "\invisrun.bat"
    os.system("cls")
    os.system("title Discord RPC ^| Background Launch")
    print(CBLUE + logo.logos.invislaunch)
    write(BYELLOW + "Launching....", bs)
    os.system("wscript.exe " + invisiblepath +  " " + invisrunbatch)
    time.sleep(3)
    main()

def configure(): 
    os.system("cls")
    print(CBLUE + logo.logos.configure)
    write(BYELLOW + "Ready for some configuration?", bs)
    time.sleep(2)
    os.system("notepad discordrpc.js")
    input(BYELLOW + "Press enter to continue")
    main()

def helpfnc():
    os.system("cls")
    print(CBLUE + logo.logos.help)
    write(BYELLOW + "Here's a command list for you! ^^", bs)
    print(" ")
    write(CBLUE + "\n- launch: Launches the DiscordRPC, giving it to life!", bs)
    write(CBLUE + "\n- configure: Configures the DiscordRPC, give it a personality!", bs)
    write(CBLUE + "\n- invislaunch: launch the program with no cmd", bs)
    write(CBLUE + "\n- stop: stop the running invislaunch cmd", bs)
    write(CBLUE + "\n- libinstall: install required py libraries (psutil)", bs)
    write(CBLUE + "\n- github: open github repository", bs)
    print(" ")
    input(BYELLOW + "\nPress enter to continue:D")
    main()

def launch():
    os.system("cls")
    print(CBLUE + logo.logos.launch)
    write(BYELLOW + "Launching...", bs)
    time.sleep(1)
    try: 
        os.system("node discordrpc.js")
        write(CBLUE + "\nFailed to launch.", bs)
        input(CBLUE + "Press enter to continue")
        time.sleep(0.5)
        main()
    except:
        write(RED + "Something went wrong... Make sure to have done file configuration!", bs) 
        input()

def main():
    os.system("cls")
    os.system("title DiscordRPC")
    global commandline
    print(CBLUE + logo.logos.discordrpclogo)
    write(BYELLOW + "Welcome to DiscordRPC! Here you can customize your discord profile with whatever you want! ^^", bs)
    if checkIfProcessRunning("node.exe"):
        write(BYELLOW + "\nDiscordRPC Status: " + GREEN + " Running", bs)
    else:
        write(BYELLOW + "\nDiscordRPC Status: " + RED + " Offline", bs) 
    write(BYELLOW + "\nCurrent version: " + CBLUE + str(version), bs)
    write(BYELLOW + "\nDon't know what to do? Run" + GREEN + " 'help'", bs)
    write(BYELLOW + "\nMade with <3 by Kingss", bs)
    print(" ")
    print(" ")
    commandline = input("DiscordRPC > ")
    if commandline == commands.help:
        helpfnc()
    if commandline == commands.launch: 
        launch()
    if commandline == commands.configure:
        configure()
    if commandline == commands.invisiblelaunch:
        invislaunch()
    if commandline == commands.stop: 
        stopinvis()
    if commandline == commands.library: 
        libinstall()     
    if commandline == commands.github: 
        githubi()   
    else:
        print(" ")
        write(RED + "This command doesn't exist!", bs)
        time.sleep(1)
        main()        

main()
