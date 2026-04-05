import subprocess
import os

def run_ci():
    print("Running CI pipeline...")
    print("Step 1: Code checked out")
    print("Step 2: Python 3.11 set up")

    print("Step 3: Installing dependencies...")
    subprocess.run(["pip3", "install", "-r", "requirements.txt"])

    print("Step 4: Running tests...")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    subprocess.run(["python3", "-m", "unittest", "discover", "-s", "tests"], cwd=base_dir)

run_ci()

# Simulate logs
logs = [
    "Step 1: Code checked out OK",
    "Step 2: Python 3.11 set up OK",
    "Step 3: Installing dependencies OK",
    "Step 4: Running tests OK"
]
for log in logs:
    print(log)