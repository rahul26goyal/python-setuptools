from setuptools import setup

"""
Having this file adds suport for generating the source distributsion using 
`python __setup.py sdist` command which is the legacy way of generating distrobution files. 
rename __setup.py -> setup.py

If you migrate to `pip install --upgrade build`, u can remove this file 
and directly generate the source file from the `python -m build` command.


"""
print("RUnning python __setup.py sdist   ::legacy mode.")
setup()