from setuptools import setup, find_packages

VERSION = '0.0.6' 
DESCRIPTION = 'Backtracking Python package'
LONG_DESCRIPTION = 'Generic implementation of a backtracker algorithm based on Steven Skiena in python.'

# Setting up
setup(
       # the name must match the folder name
        name="backtracker", 
        version=VERSION,
        author="Ryan Najafi",
        author_email="ryan.m.najafi@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'backtracker'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)