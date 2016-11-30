from subprocess import Popen, PIPE, STDOUT
# command = "gprolog"
# prolog = call(["gprolog"])
print("Launching gprolog process")
prologengine=Popen(["gprolog", "dictionary.pl"], stdin=PIPE, stdout=PIPE, stderr=STDOUT)

while True:
    line = raw_input(">")
    prologengine.stdin.write(line+'\n')
    result = []
    while True:
        if prologengine.poll() is not None:
            print('prologengine has terminated.')
            exit()
        line = prologengine.stdout.readline().rstrip()
        if line == '[end]':
            break
        result.append(line)
    print('result')
    print('\n'.join(result))