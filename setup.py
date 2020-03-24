from setuptools import setup, find_packages
from package import Package

print("starting package creation...")
print(find_packages())
setup(name='rahulg-test-tool',
    version='0.1',
    url='http://github.com/rahul26goyal',
    author='Rahul Goyal', 
    author_email='goyal.1234rahul@gmail.com',
      license='MIT',
      #packages=['rahulg', 'rahulg.*'], #use: import rahulg
      packages=find_packages(include=['rahulg', 'rahulg.*']),
      #cmdclass={ "package": Package }, #to create a standalone package for this repo with all its dependencies
      zip_safe=False
)