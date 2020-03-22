from setuptools import setup, find_packages

print("starting package creation...")
print(find_packages())
setup(name='rahulg',
    version='0.1',
    url='http://github.com/rahul26goyal',
      author='Rahul Goyal', 
      author_email='goyal.1234rahul@gmail.com',
      license='MIT',
      packages=['rahulg'], #use: import rahulg
      zip_safe=False
)