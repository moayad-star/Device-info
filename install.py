import os


print("Enter Your device type : \n kali linux [1] \n Termux [2] ")
num = input("The number:")
name = int(num)
print("Permissions are given now")
os.system("chmod +x install.py && chmod +x my-device.py")
print("Powers have been given")
os.system("clear")
print("The update is now being updated")
os.system("pkg upgrade -y && pkg update -y")
print("Updated successfully")
os.system("clear")
print("The files are finally downloaded")
if name == 1:
    print("Your Device type Kali linux ??? Ok! No problem")
    os.system("apt-get install neofetch -yy")
    print("It was completed")
    os.system("clear")
    print("Device = kali linux \n powers = True \n update = True \n final files = True")
    print("Installing now \n please don't run this file again")
    print("enter ======> python3 my-device.py <===== to start")
elif name == 2:
    print("Your Device type Android (Termux) ??? Ok! No problem")
    os.system("pkg install neofetch -yy")
    print("It was completed")
    os.system("clear")
    print("Device = Android (Termux) \n powers = True \n update = True \n final files = True")
    print("Installing now \n please don't run this file again")
    print("enter ======> python3 my-device.py <===== to start")
else :
    os.system("clear")
    print("Why did not you enter a number?")
    print:("It will be opened again, please choose a number from the list")
    print("Enter python3 install.py to start")

print("Thank you <3")
