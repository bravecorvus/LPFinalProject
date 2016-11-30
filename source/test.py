import IPython
import subprocess
IPython.embed()
bashCommand = "gprolog"
output = subprocess.check_output(['bash','-c', bashCommand])
