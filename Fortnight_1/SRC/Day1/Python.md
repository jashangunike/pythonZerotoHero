# Day01 - Get to know Python

### Python Introduction
#### The history of Python
1. 1989 Christmas: Guido von Rossum begins writing Python language compilers.
2. February 1991: The first Python compiler (also an interpreter) was born. It was 3. implemented in C language (there are Java and C# implementations of Jython and IronPython, and other implementations such as PyPy, Brython, and Pyston). ), you can call the C language library functions. In the earliest version, Python has provided support for building blocks such as "classes", "functions", and "exception handling". It also provides core data types such as "lists" and "dictionaries". It also supports module-based support. Expansion system.
3. January 1994: Python 1.0 officially released.
4. October 16, 2000: Python 2.0 released, adds full garbage collection , and supports Unicode . At the same time, the entire development process of Python was more transparent, the community's influence on the development progress gradually expanded, and the ecosystem began to form slowly.
4. December 3rd, 2008: Python 3.0 released. This version is not fully compatible with the previous Python code, but many new features were later ported to the old Python 2.6/2.7 version, because there are still companies used in the project and operation and maintenance. Python 2.x code.
The version of Python 3.6.x we are currently using was released on December 23, 2016. The version number of Python is divided into three sections, shaped like ABC. Where A represents the major version number, generally when the overall rewrite, or there is no backward compatible changes, increase A; B said that the function update, the emergence of new features increase B; C represents a small change (such as repairing a bug ), increase C as long as there are changes. If you are interested in the history of Python, you can check out a blog post called "A Brief History of Python ."

#### The advantages and disadvantages of Python
The advantages of Python are many, and the simple ones can be summarized as the following points.

1. Simple and clear, there is only one way to do one thing.
2  The low learning curve makes it easier to learn than many other languages.
3. Open source, with a strong community and ecosystem.
4. Explicit language, perfect platform portability.
5. Supports two major programming paradigms, object-oriented and functional programming.
Extensibility and embeddability, you can call C / C + + code can also be called in C / C + +.
5. The code is highly readable and readable, and it is suitable for people who have code obstruction and obsessive-compulsive disorder.
#### The disadvantages of Python are mainly focused on the following points.

1. Implementation is inefficient, so compute-intensive tasks can be written in C/C++.
2. The code cannot be encrypted, but many companies are not selling software but selling services. This problem will gradually fade.
3. There are too many frameworks to choose from at the time of development, and there are mistakes where there are choices.
#### Python application area
Currently, Python is widely used in cloud infrastructure, DevOps, web crawler development, data analysis and mining, machine learning, and other fields. Therefore, it has also produced server development, data interface development, automated operation and maintenance, scientific computing and data visualization, and chat robots. Development, image recognition and processing a series of positions.

#### Build a programming environment
###### Windows environment
You can download the Python Windows installation program (exe file) from Python's official website . It should be noted that if you install in Windows 7 environment, you need to install the Service Pack 1 patch package first (you can use some software tools to automatically install the system patch function Install), the installation process is recommended to check "Add Python 3.6 to PATH" (Add Python 3.6 to the PATH environment variable) and select the custom installation, the "Optional Features" interface is best to "pip", "tcl/tk" All items such as "Python test suite" are checked. It is highly recommended to use a custom installation path and ensure that there is no Chinese in the path. The installation will see the "Setup was successful" prompt, but when starting the Python environment, the Python interpreter may fail to run due to missing dynamic link library files. The common problem is mainly api-ms-win-crt*. Missing dll and updating of DirectX cause some dynamic link library files to be missing. The former can refer to the method explained in "Api-ms-win-crt*.dll Missing Reason Analysis and Resolution" to process or download Visual C++ directly from Microsoft's official website. The Redistributable for Visual Studio 2015 file is repaired, and the latter can be downloaded with a DirectX repair tool for repair.

#### Linux environment
The Linux environment comes with Python 2.x, but if you want to update to version 3.x, you can download the Python source code from Python's official website and install it through source code installation. The specific steps are as follows .

Install Dependent Libraries (because not having these dependent libraries may fail when the source code artifacts are installed due to missing underlying dependencies).
``` Shell
Yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
```
Download Python source code and extract it to the specified directory.

``` Shell

Wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz
Xz -d Python-3.6.1.tar.xz
Tar -xvf Python-3.6.1.tar
```
Switch to the Python source code directory and execute the following command to configure and install.
``` Shell

Cd Python-3.6.1
./configure --prefix=/usr/local/python3.6 --enable-optimizations
Make && make install
```
Create a soft link so that you can directly start the Python interpreter via python3.

Ln -s /usr/local/python3.6/bin/python3 /usr/bin/python3
#### MacOS environment
MacOS also comes with Python 2.x. You can install the 3.x version through the installation file (pkg file) provided by Python's official website . After the default installation is complete, you can start the 2.x version of the Python interpreter by executing the python command on the terminal. You can start the 3.x version of the Python interpreter by executing the python3 command, but you can also modify the startup by resetting the soft links. Python interpreter commands.

### Run Python programs from the terminal
Confirm Python version
Type the following command at the terminal or command line prompt.

``` Shell

Python --version
```
Of course, you can also enter python into the interactive environment, and then execute the following code to check the Python version.
```

Import sys

Print (sys.version_info)
 print (sys.version)
 ```
#### Writing Python source code
You can use a text editing tool (recommended to use advanced text editing tools such as Sublime, Atom, TextMate, VSCode, etc.) to write Python source code and save it as hello.py. The code content is as follows.
``` Shell
Print ( ' hello, world! ' )
```
#### Run the program
Switch to the directory where the source code resides and execute the following command to see if "hello, world!" is printed on the screen.
``` Shell

Python hello.py
```
### Notes in the code
Annotations are an important part of a programming language. They are used to explain the role of code in source code to enhance the readability and maintainability of the program. Of course, code segments that do not need to participate in the source code can also be removed through comments. This is often used when debugging a program. Comments are removed when they come into the preprocessor or compiled with the source code. They are not retained in the object code and do not affect the execution of the program.

1. Single-line comments - sections beginning with # and spaces
2. Multi-line comments - beginning with three quotes and ending with three quotes
```Python 
"""

The first Python program - hello, world! 
salutes the great Mr. Dennis M. Ritchie

Version: 0.1 
Author: Jashan
Date: 2018-02-26

"""

Print ( ' hello, world! ' )
#print("Hello, world!") 
print ( ' Hello ' , ' world ' )
print ( ' hello ' , ' world ' , sep = ' , ' , end = ' ! ' )
print ( ' goodbye, world ' , end = ' ! \n ' )
```

### Other tools introduced
IDLE - Integrated Development Tools
IDLE is an integrated development tool that comes with the Python environment, as shown below. However, because the user experience of IDLE is not so good, it is rarely used in actual development.



### IPython - Better Interactive Programming Tools
IPython is a Python-based interactive interpreter. Compared to the native Python Shell, IPython provides more powerful editing and interaction features. IPython and Jupyter can be installed via Python's package management tool pip, as shown below.
``` Shell

Pip install ipython jupyter
or

Python -m pip install ipython jupyter
```


``` Shell

Exercise
In the Python interactive environment, the following code looks at the result and translates the content into Chinese.

Import this

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex .
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren ' t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless transparent silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one --  and only only one -- obvious way to do it.
Although that way may not be obvious at first unless you ' re Dutch.
Now is better than never.
Never although but IS Often field of Better Within last * right * now.
If the implementation is hard to explain, it ' sa bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let ' s do more of those!
Learn to use the turtle to draw graphics on the screen.

Import turtle

Turtle.pensize( 4 )
Turtle.pencolor( ' red ' )
Turtle.forward( 100 )
Turtle.right( 90 )
Turtle.forward( 100 )
Turtle.right( 90 )
Turtle.forward( 100 )
Turtle.right( 90 )
Turtle.forward( 100 )
Turtle.mainloop()
```
