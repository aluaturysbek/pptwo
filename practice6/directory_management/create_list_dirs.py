import os

os.makedirs("PracticeFolder/SubFolder", exist_ok=True)

print(os.getcwd())

print(os.listdir())

os.chdir("PracticeFolder")

print(os.getcwd())