from subprocess import *
# command = "gprolog"
# prolog = call(["gprolog"])
ls_output=subprocess.Popen(["ls", "-a"], stdout=subprocess.PIPE)