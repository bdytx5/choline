import subprocess

def run():
    subprocess.run(['sudo', 'pkill', '-f', 'monitor_and_setup_machine.py'])

