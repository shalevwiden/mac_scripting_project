import os
import platform

print(os.getcwd())
splitdir=os.getcwd().split('/')
print(splitdir)
del splitdir[0]
print()
print(splitdir)

print()


def greet_user_mac():
    splitdir=os.getcwd().split('/')
    # list comprehension to filter out non truthy values 
    splitdir = [word for word in splitdir if word]

    print(f'Hi, {splitdir[1]}!')



def greet_user_windows():
    testwindowspath='C:\\Users\\YourUsername\\'
    username=os.getlogin()
    print(f'Hi, {username}!')

print(greet_user_windows())
# Unicode Emojis?
# \U0001F600
def main():
    if platform.system() == "Darwin":  # macOS
        greet_user_mac()
    elif platform.system() == "Windows":
        # greet_user_windows()
        greet_user_windows()
    else:
        print("Unsupported OS")
main()