# python-templates
Minimal templates with exlanations for beginners to create Python scripts.  
I always recommend the simple type hints and annotations in Python. They may hurt you now. But in future you will be happy to let them help you find runtime errors early.

## Common header

### Shebang
Start your files with a _shebang_ for use in Unix based environments if they are **entry points from shell**.  
`#!/usr/bin/env python3`  
Your libraries and helper files do not need them.

They allow direct executing your script with the correct Python interpreter defined inside the script:  
`./yourscript.py`  
Script must have execution rights.

Without _shebang_ or without execution rights, your script is only callable in this way:  
`python yourscript.py`  

python may still refer to python2.x on some OSes so make sure to use python3 here explicit:  
`python3 yourscript.py`

Or have a look into your system configuraten which Python executable is used on your Unix bases OS.  
Symbolic links are used to mimic aliases:
```bash
ls -al /usr/bin/python*
lrwxrwxrwx 1 root root     7 21. Dez 21:57 /usr/bin/python -> python3
lrwxrwxrwx 1 root root     9 22. Okt 11:14 /usr/bin/python2 -> python2.7
-rwxr-xr-x 1 root root 14088 22. Okt 11:14 /usr/bin/python2.7
-rwxr-xr-x 1 root root  1681 22. Okt 11:14 /usr/bin/python2.7-config
lrwxrwxrwx 1 root root    16 22. Okt 11:14 /usr/bin/python2-config -> python2.7-config
lrwxrwxrwx 1 root root     9 21. Dez 21:57 /usr/bin/python3 -> python3.8
-rwxr-xr-x 1 root root 14088 21. Dez 21:57 /usr/bin/python3.8
-rwxr-xr-x 1 root root  3120 21. Dez 21:57 /usr/bin/python3.8-config
lrwxrwxrwx 1 root root    16 21. Dez 21:57 /usr/bin/python3-config -> python3.8-config
lrwxrwxrwx 1 root root    14 21. Dez 21:57 /usr/bin/python-config -> python3-config
```
`python` points to `python3` so your system is quite safe of accidently run python2.x.

### Encoding
Better define utf8 for your files. Your Editor or IDE should support and use utf8 then too of course.  
utf8 is quite common and allows all kind of Unicode characters like chinese in strings and comments:  
`# -*- coding: utf-8 -*-`  
You should use it anyway even if your code is restricted to english. You still may use Unicode smileys etc.

See PEP 263: https://www.python.org/dev/peps/pep-0263

## Template files

### main_as_function.py
Simple basic Python template allowing being run safely from command line and imported from other scripts.  
Heavy on comments. If you know the meanings of the file structure you may reduce or remove and replace with your useful script specific comments.

### main_as_class.py
Advanced Python template allowing your program being run safely from command line and imported from other scripts as objects.  
Heavy on comments. If you know the meanings of the file structure you may reduce or remove and replace with your useful script specific comments.

### pyqt5-template.py
**TODO**
