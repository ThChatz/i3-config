import sys
import subprocess
import time


def focus(win_class):
    i3msg = ["i3-msg", "[class=\"{0}\"] focus".format(win_class)]
    t = subprocess.Popen(i3msg, stdout=subprocess.PIPE)
    response = t.stdout.read()
    return response


def execute (command):
    i3msg = ["i3-msg", "exec","--no-startup-id" ,"{0}".format(command)]
    t = subprocess.Popen(i3msg, stdout=subprocess.PIPE)    


SUCC_MSG = b'[{"success":true}]\n'
if len(sys.argv) < 3:
    print("Usage: <window class> <command>")
    exit(1)
response = focus(sys.argv[1])
print(sys.argv[1])


print(response)
print(SUCC_MSG)
if not (response == SUCC_MSG):
    execute(sys.argv[2])
    time.sleep(1)
    focus(sys.argv[1])

exit(0)
