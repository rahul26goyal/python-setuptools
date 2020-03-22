from setuptools import setup, find_packages

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
      zip_safe=False
)