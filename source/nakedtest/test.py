import sys
from Naked.toolshed.shell import meterun_rb

response = muterun_rb('testscript.rb')

if response.exitcode == 0:
    #the command was successful (returned 0 exit code)
    print(response.stdout)
else:
    # the command wa snot successful (returned non-0) exit code)
    sys.stderr.write(response.stderr)