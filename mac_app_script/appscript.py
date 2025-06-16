import os
import time

import platform
import sys
# this tells python, look here to find modules as well
sys.path.append('getuser_project')

# can see all of them by doing print(sys.path)
# refer to another python script created
from getuser_project import get_user_script
# import a specfic function
from getuser_project.get_user_script import greet_user_mac

# see all functions available in get_user_script
print(dir(get_user_script))

'''
June 15, 2025
Mac App Opening and Closing Script
Sample Usage of some of the defined functions in main()
'''

def detect_os():
    if platform.system() == "Darwin":
        print('Using MacOS')
        greet_user_mac()
    elif platform.system() == "Windows":
        print('Using Windows')
        get_user_script.greet_user_windows()
    else:
        print("Unsupported OS")

# a single app
def open_app(app):
    os.system(f'open -a "{app}"')
def close_app(app):
    os.system(f'osascript -e \'quit app "{app}"\'')
    # heres the command
    # osascript -e 'quit app "app"'


# List of apps to open
apps_to_open = [
    "Messages",
    "Google Chrome",
    "Safari",
    "FaceTime",
    "Notes"
]
# or use this to get appl;ist from a file

def get_downloaded_apps():
    splitpath=os.getcwd().split('/')
    beginning_of_path=f'/{splitpath[0]}/{splitpath[1]}'
    appsdir=os.path.join(beginning_of_path,'/Applications')
    # print(firsthalf)
    #  get a list of all apps in the users folder
    downloadedapps=os.listdir(appsdir)
    # now format to remove .app    
    downloadedapps_formatted=[]

    for app in downloadedapps:
        # doesnt include the extension (.app)
        formatted_app=os.path.splitext(app)[0]
        downloadedapps_formatted.append(formatted_app)
    return downloadedapps_formatted

print(f'Downloaded apps function:\n{get_downloaded_apps()}')

def get_app_list(filename):
    applist=[]
    with open(filename, 'r') as appfile:
        for line in appfile:
            applist.append(line.strip().title())
    return applist

# print(get_app_list('applist.txt'))

# Loop through and open apps
def openapps(apps,delay=1.5):
    for app in apps:
        # this command is run in terminal
        os.system(f'open -a "{app}"')
        time.sleep(delay)
# os.system runs things in the terminal




garageband='GarageBand'
open_app(garageband)
print('Opened')
# sleep 3 seconds
time.sleep(3)
close_app(garageband)
print('Closed')


# add more stuff later
def main():
    # open a fourth of all the apps, then close them
    downloaded_apps=get_downloaded_apps()
    for app_index in range(len(downloaded_apps)):
        if (app_index+1)%4==0:
            print(f'Opening {downloaded_apps[app_index]}')
            open_app(downloaded_apps[app_index])
            time.sleep(3)
            print(f'Closing {downloaded_apps[app_index]}')

            close_app(downloaded_apps[app_index])
        
