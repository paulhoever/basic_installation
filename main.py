import os

print("###################################################\n")
print("Starte das Basic Installation Script!\n")
print("###################################################")

os.system("sudo apt update")
os.system("sudo apt upgrade -y")
os.system("sudo apt install neofetch -y")

print("###################################################\n")

os.system("neofetch")

if os.geteuid() == 0:
	print("Du bist root, du Spast!")
else:
	print("Du bist ein low-Bob, du Spast!")

with open("test.txt", "a") as f:
     f.write("nippel\n")

with open("test.config", "a") as f:
     f.write("Anus\n")

print("done!")
