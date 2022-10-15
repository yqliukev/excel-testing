import sys
import os
import stat
import subprocess

# define basic shell command executions
def execute_shell_command(cmd, my_env=None):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, env=my_env)
    stdout, stderr, = process.communicate()
    return stdout.decode("utf-8", "ignore"), stderr.decode("utf-8", "ignore"), process.poll
