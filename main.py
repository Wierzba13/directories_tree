from pathlib import Path
from sys import argv
from os import path, getcwd

startPath = ""
if len(argv) > 1 and path.isdir(argv[1]):
    startPath = argv[1]
else:
    startPath = getcwd()
startPath = Path(startPath)

# prefix components:
space =  '    '
branch = '│   '
# pointers:
tee =    '├── '
last =   '└── '

def tree(dir_path: Path, prefix: str=''):
  
    contents = list(dir_path.iterdir())
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        yield prefix + pointer + path.name
        if path.is_dir(): 
            extension =  branch if pointer == tee else space 
            yield from tree(path, prefix=prefix+extension)


try:
    for line in tree(startPath):
        print(line)
except KeyboardInterrupt:
    exit()
