import shutil
from pathlib import Path

Path("MovedFiles").mkdir(exist_ok=True)

with open("example.txt", "w") as file:
    file.write("Example text.")

shutil.copy("example.txt", "MovedFiles/example_copy.txt")

shutil.move("example.txt", "MovedFiles/example.txt")

for file in Path("MovedFiles").glob("*.txt"):
    print(file)