# python-setuptools

Example Project for Learning Building and Distributing Python Packages.

- Name of the distribution craeted by setup.py is `rahulg-test-tool`
- name of the package to be used is `rahulg` as specified in setup.py #packages
### To install this package for local testing:
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

### To install the package directly from git repo:

```
pip install git+https://github.com/rahul26goyal/python-setuptools.git@master
```

This will do the following:
* Download the source code into a temp directory
* Create a wheel distribution.
* install the created wheel using pip command.
* Done.
```
(venv) ➜ pip install git+https://github.com/rahul26goyal/python-setuptools.git@master
 ...
  Cloning https://github.com/rahul26goyal/python-setuptools.git (to revision master) to /pri/tmpd-t0Zi_0
...
Building wheels for collected packages: rahulg-test-tool
Building wheel for rahulg-test-tool (setup.py) ... done
Created wheel for rahulg-test-tool: filename=rahulg_test_tool-0.1-py2-none-any.whl size=5729 sha256=c52cea
Stored in directory: /private/var/folders/d8/xp6v/T/pip-ephem-wheel-cache-KIWzy3/wheels/30/f9/fb/5b41832c7f7bed
Successfully built rahulg-test-tool
Installing collected packages: rahulg-test-tool
Successfully installed rahulg-test-tool-0.1
```


### To Create a Source Distribution Package:
```
python setup.py sdist
```
This produced 2 Outputs:
  * `dist` folder where the tar.gz file is created.
  * `<prodect-name.egg-info>` folder with its files.
  * the tarball does not include the dependencies.
  
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


### To create a standalone package for this repo with all its dependencies

* include package.py file
* include MANIFEST.in file.
* include the install time dependencies into requirements.txt
* uncomment `cmdclass={ "package": Package },` line in setup.py to use the package.py utility.
* To create the package: 
```
(venv)✗ python setup.py package
```

It does the following:
* create a wheelhouse for the dependencies specified in requirements.txt file.
```
running package
Packing requirements.txt into wheelhouse
Running shell command: %s rm -rf wheelhouse
Running shell command: %s mkdir -p wheelhouse
Running shell command: %s pip wheel --wheel-dir=wheelhouse -r requirements.txt
```

* all the wheel files are downloaded for the dependencies into `wheelhouse` directory and then moved to `dist/.tar.` zip file.

To test:
* Disconnect from internet.
* do a `pip list` and make sure that `requests` package is not
 present.
 ```
 (venv)✗ pip list
pip        20.0.2    
setuptools 44.1.0    
urllib3    1.24.3    
wheel      0.34.2 
 
 ```
* untar the created `dixt/*tar.gz` in some folder and `cd <>`
```
tar zxf rahulg-test-tool-0.1.tar.gz
cd rahulg-test-tool-0.1
ls wheelhouse
```
* try installing the dependencies using pip
```
 pip install -r requirements.txt  --no-index --find-links wheelhouse
 ```
* do a `pip list` again to see that `requests` package is present in the virtual env with all its dependencies.
```
(venv)✗ pip list
certifi    2019.11.28
chardet    3.0.4     
idna       2.8       
pip        20.0.2    
requests   2.21.0    
setuptools 44.1.0    
urllib3    1.24.3    
wheel      0.34.2 
```