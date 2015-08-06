import subprocess

shell_dir = subprocess.check_output("find ~ -type d -name 'Shell-Lab'", shell=True).split('\n')
shell_dir.pop()
if len(shell_dir) != 1:
    raise Exception("Ensure there is exactly one instance of the Shell-Lab directory on your computer")
shell_dir = shell_dir[0]
command = "find " + shell_dir + " -type f | wc -l"

subprocess.call(command, shell=True)
