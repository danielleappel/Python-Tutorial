# Who can install Python
Just about anyone can install and run Python. It can be run on Windows, Macs,
Linux, and even on Android and iOS tablets.  

# How to install Python
First, check if you have Python installed.

You'll need to open a Command Prompt. On Windows, just search for the app `cmd`. Next, type `python`. 

If Python is installed, you'll see the version that is downloaded, some other information, and `>>>` to indicate that you have launched Python.

If Python is *not* installed, Windows may link you to the app store, but you can also download directly from [Python's website.](https://www.python.org/downloads/) Click `Download Python 3.8.5`. Once the files download, double click on the `python-3.8.5` to launch the task manager. Make sure to select `Add Python to PATH` so that you only have to type `python` instead of a tedious global name/file path. Click `Install now`. When it has finished, close the window and head back to the Command Prompt. Check that Python is installed by entering `python`. If you see the Python version number and the entrance symbol (`>>>`), then congrats! You've installed Python.

If it still does not find Python, try restarting your computer and then entering `python` into the Command Prompt one more time.

# Text editor
Python code is run via the Command Line, but it is written in a text editor. There are a seemingly endless number of text editors, and you could use many of them. I'll be using Visual Studio Code (VSC). The first thing that drew me to VSC was the price - it's free. VSC also has *IntelliSense*, which means that while coding, VSC provides smart completion in addition to syntax highlighting and autocomplete. Furthermore, Git commands are built in as well as debugging software that allows the user to create break points, call stacks, and use an interactive console. VSC is also very natural to integrate with GitHub. You can download it [here](https://code.visualstudio.com/download) if you're interested. You can also use many other text editors, including Notepad++ and Atom.
Alternatively, you can use an Integrated Development Environment (IDE) like PyCharm, but IDEs can be confusing for beginners.

If you're using Visual Studio Code, click `Terminal` to switch the screen to a dual view of the Command Line and an editing field. Type `python` again to make sure that it runs without a problem. When Visual Studio Code gives you a message that your Python Interpreter is not installed, click it to enter the path. Enter `/usr/local/bin/python3.8` as the path and click enter. This should prompt Visual Studio Code to ask if you would like to download another file. Download it, and you'll be all set!

# Hello, world!

It is finally time to write you're first Python code. Open up you're text editor and create a new document. Name it `helloworld.py` and make sure to select `Python` as the type of document, and save it somewhere accessible. Preferably, save it in a dedicated Python folder.

Python code is extremely easy to write. You simply start writing code. For this first program, just type
```
print("Hello, world!")
```
Then head to the Command Line or the Integrated Terminal from the `Terminal` button of VSC. Before you can run your code, you first need to navigate to where your Python file is saved. By using `cd folder` (which stands for change directory) to navigate your files. Now you can enter
```
python helloworld.py
```
You should now see `Hello, world!` below the command you just entered.

This is the same way that you'll run all of your files. Use the `cd` command to get to where the file is saved, then run 
`python your_code_name_here.py`.

# Comments
Comments are very important when coding. Readable code is more likely to be correct than unreadable code. In Python, just enter a `#` on a line, and all code on the same line and to the right of it will be ignored by your computer when the code is run. That way you can add notes to remind yourself and other readers what your code does. 

# Sources
* VisualStudio.com https://code.visualstudio.com/ Accessed September 15, 2020.
* Dummies.com https://www.dummies.com/programming/python/what-is-python-and-what-can-you-do-with-it/ Accessed September 15, 2020.
