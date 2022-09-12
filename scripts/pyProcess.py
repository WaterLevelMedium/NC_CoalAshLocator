import subprocess, sys, os

p = subprocess.Popen(['powershell.exe', os.getcwd() + '//try.ps1'], stdout=subprocess.PIPE)
p_out, p_err = p.communicate()

print(p_out)