import os # It helps your Python program talk to and control the computer it's running on, like reading files, creating folders, and more.
from pathlib import Path #It's a tool for making it easier to work with file and folder locations (like telling your program where to find things).
import logging #It helps you keep track of what your program is doing, especially when you need to find and fix issues or errors later.

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')#[2023-09-06 12:34:56]: Your log message here

project_name="textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/config/configuration.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"    
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created directory {filedir}")

    if (not os.path.exists(filename)) or (os.pth.getsize(filepath)==0):
        with open(filepath,"w"):
            pass
        logging.info(f"Created file {filepath}")