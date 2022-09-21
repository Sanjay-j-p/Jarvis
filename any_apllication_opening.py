import os  
  
# Command to execute 
# Using Windows OS command 
cmd = r"G:\wallpaper\alan_wake-wallpaper-1920x1080.jpg"

os.startfile(cmd)
o.system('')
time.sleep(1)


# Python Program - Shutdown Computer
	#shutdown
import os;
check = input("Want to shutdown your computer ? (y/n): ");
if check == 'n':
    exit();
else:
    os.system("shutdown /s /t 1");
    #restart
    import os;
check = input("Want to restart your computer ? (y/n): ");
if check == 'n':
    exit();
else:
    os.system("shutdown /r /t 1");
    #hibernate
    import os
os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

