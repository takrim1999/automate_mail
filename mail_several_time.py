#!/usr/bin/python3
import subprocess
time = int(input("how many time to send mail?\n>"))
for i in range(time):
    some = subprocess.run("./mailit.py", capture_output=True)
    print("sent " + str(i+1))