
import subprocess
import subprocess

def run_monitor_instance_script(instance_id, max_checks=30):
    subprocess.Popen(["sudo", "python", "./monitor.py", "--id", str(instance_id), "--max_checks", str(max_checks)])


run_monitor_instance_script(instance_id=7093592)