## Building and Publishing a Python libray on pypi 
- We will use `setuptools` for generating the source and binary distribution for the package. 
- We will use `pyproject.toml` to specify all the build related metadata and define the build system
- We will use `twine` to upload to test pypi repository.

We will follow this guide https://setuptools.pypa.io/en/latest/userguide/quickstart.html 
for this tutorial.

## Creating the test env
```python
conda create -n  setuptool-dev python=3.8
conda activate setuptool-dev
```

**Overview of the project structute**

This is a simpel package which contains all the code under a single 
source directory names `rahulg` which follows the flat-src project structure. 
- the folder `rahulg` is the base package for this project. 
- Under `rahulg` folder, there are other packages like `nested`. It can be named anything. 
- Under `nested` package, we have added another package names `inner`. It can be name anything.


- Name of the package distribution created will be `rahulg_package` used for installation
- name of the package to be used in code for importing is `rahulg`.

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

**Create `pyproject.toml` file**
- create a file 
- define the build system 
- define the project basic details
- define the source code to be included
- define the depedencies to be install with the package
The idea is to not have any `setup.py` or `setup.cfg` file on this tutorial.

**Install the python `build` utility**
```
pip install --upgrade build
```

**Generate the Build Distribution packages**
Once the configuration is completed, it straight forward to generate the artifact,
```python
python -m build
```
```python
(setuptool-dev) ➜  python-setuptools git:(setuptool2) ✗ ls dist 
rahulg_package-1.1-py3-none-any.whl  # wheel file  
rahulg_package-1.1.tar.gz  # source tar file.
```
****
****


## Uploading the package to testpypi repository 

We will use `twine` utility to upload the python distribution. 
https://twine.readthedocs.io/en/stable/index.html
https://packaging.python.org/en/latest/guides/using-testpypi/
- Created a account in the test pypi repository 

**Install twine**
```
pip install twine
```
**Upload to pypi**
```python
twine upload -r testpypi dist/*
```
**Testing the install**

```python
pip install -i https://test.pypi.org/simple/ rahulg-package
```

## Other installs and testing
```python
(setuptool-dev) ➜  python-setuptools git:(setuptool2) ✗ pip list
Package             Version
------------------- --------
build               1.1.1
certifi             2024.2.2
charset-normalizer  3.3.2
docutils            0.20.1
idna                3.6
importlib_metadata  7.0.2
importlib_resources 6.3.2
jaraco.classes      3.3.1
keyring             24.3.1
markdown-it-py      3.0.0
mdurl               0.1.2
more-itertools      10.2.0
nh3                 0.2.15
packaging           24.0
pip                 24.0
pkginfo             1.10.0
Pygments            2.17.2
pyproject_hooks     1.0.0
rahulg_package      1.1
readme_renderer     43.0
requests            2.31.0
requests-toolbelt   1.0.0
rfc3986             2.0.0
rich                13.7.1
setuptools          69.2.0
tomli               2.0.1
twine               5.0.0
typing_extensions   4.10.0
urllib3             2.2.1
wheel               0.42.0
zipp                3.18.1

```
