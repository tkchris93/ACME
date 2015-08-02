import os

shell_dir = os.popen("find ~ -type d -name 'Shell-Lab'").read().strip().split('\n')
if len(shell_dir) != 1:
    raise Exception("Ensure there is exactly one instance of the Shell-Lab directory on your computer")

shell_dir = shell_dir[0]
command = "find " + " -type f | wc -l"

print os.popen(command).read().strip()

