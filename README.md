# python-setuptools

Example Project for Learning Building and Distributing Python Packages.

- Name of the distribution craeted by setup.py is `rahulg-test-tool`
- name of the package to be used is `rahulg` as specified in setup.py #packages
### To install this packeg for local testing:
* create a virtual env `venv`
* `pip install .`
* open python shell.

```
(venv) ➜  python-setuptools git:(master) ✗ python
Python 2.7.16 (default, Dec  3 2019, 07:02:07) 
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> import rahulg
>>> 
>>> rahulg.start()
Hello guys, this is a method called in lib/init..
>>> 
>>> from rahulg import nested
>>> 
>>> nested.nested()
you have invoked a nested module...
>>> 
>>>
```

### To Create a Source Distribution Package:
```
python setup.py sdist
```
This produced 2 Outputs:
  * `dist` folder where the tar.gz file is created.
  * `<prodect-name.egg-info>` folder with its files.
  
To install a source distribution zip, do the following:
  ```
  (venv)✗ pip install ./dist/rahulg-test-tool-0.1.tar.gz 
  
  (venv)✗ ls ./venv/lib/python2.7/site-packages/rahulg
rahulg/                          rahulg_test_tool-0.1.dist-info/
  ```

### To create a wheel distribution:
