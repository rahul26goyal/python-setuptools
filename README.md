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
```
 python setup.py bdist_wheel --universal
 ```
 
 This will create a `<package-name>-<>.whl` file inside `dist` which can be uploaded to pypi or installed.
 
 To Install the wheel:
 ```
 (venv) ➜ pip install ./dist/rahulg_test_tool-0.1-py2.py3-none-any.whl 
 
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. A future version of pip will drop support for Python 2.7. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
Processing ./dist/rahulg_test_tool-0.1-py2.py3-none-any.whl
Installing collected packages: rahulg-test-tool
Successfully installed rahulg-test-tool-0.1
```
