import os

os.system('clear')

print ("\n")
print ("\n")
print ("\033[1;36m __        __    _    _         _   ___   ")
print (" \ \      / /__ | | _(_) __   _/ | / _ \  ")
print ("  \ \ /\ / / _ \| |/ / | \ \ / / || | | | ")
print ("   \ V  V / (_) |   <| |  \ V /| || |_| | ")
print ("    \_/\_/ \___/|_|\_\_|   \_/ |_(_)___/  ")
print ("\n")
print ("\n")
print ("\n")
print ("Menu Option :\n")
print ("1) Clash Royale Inject File Test")
print ("2) About")
print ("3) Exit")
print ("\n")
choice = int(input("Your Choice : "))
if choice not in range (1, 3+1):
    raise IndexError
if choice==1:
    os.system('chmod +x exploit.sh')
    os.system('./exploit.sh')
elif choice==2:
    print ("Script Made By Slayy2357")
elif choice==3:
    os.system('exit')