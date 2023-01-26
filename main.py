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
print ("1) Clash Royale Decrypted Files Injector")
print ("2) Clash Royale Modded Files Injector")
print ("3) Exit")
print ("\n")
choice = int(input("Your Choice : "))
if choice not in range (1, 3+1):
    raise IndexError
if choice==1:
    os.system('chmod +x decrypted.sh')
    os.system('./decrypted.sh')
elif choice==2:
    os.system('chmod +x modded.sh')
    os.system('./modded.sh')
elif choice==3:
    os.system('exit')