# from os import *
import subprocess
bashCommand = "gprolog"
output = subprocess.check_output(['bash','-c', bashCommand])

# userinput = raw_input()
# userinput = userinput[0:len(userinput)-1]
# print(userinput)
# os.system(gprolog)