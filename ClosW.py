import subprocess

while True:
    subprocess.call("taskkill /f /im chrome.exe", shell=True)
    subprocess.call("taskkill /f /im msedge.exe", shell=True)
    subprocess.call("taskkill /f /im firefox.exe", shell=True)
