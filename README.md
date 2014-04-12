# Unix-Like tools in Python

I created these basic Unix tools in Python in order to use it on Windows. **I don't try to emulate them**, just add some functionalities that are useful to me.

Place them in your system path to use them everywhere.

# Usage

## Touch
The touch command is the easiest way to create new, empty files.

*touch.py file_name1 [file_name2 [file_nameN]]*


## Renamer
**Renamer will have more features.**

*renamer.py old_names_list.txt new_names_list.txt*

Example:
* File *old_names_list.txt*:
```
  a.txt
  b.txt
  c.txt
```
* File *new_names_list.txt*:
```
  w.txt
  x.txt
  y.txt
```
It will rename *a.txt* into *w.txt*, *b.txt* into *x.txt*, *c.txt* into *y.txt*

## ls
List files in current directory.


License
====
[MIT License](https://github.com/nrikee/Unix-Like_tools_in_Python/blob/master/LICENSE)

