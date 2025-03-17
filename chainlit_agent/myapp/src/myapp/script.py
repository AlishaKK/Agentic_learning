import subprocess

def run():
    subprocess.run(["chainlit", "run" , ".//src//myapp//main.py", "-w"])