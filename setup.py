from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()



setup(
    name='oxforddictionaries',
    version='0.1.11',
    description='A python wrapper for the Oxford Dictionaries API.',
    long_description=long_description, 
    long_description_content_type='text/markdown', 
    url='https://github.com/RafaelBroseghini/OxfordAPI', 
    author='Rafael Broseghini', 
    author_email='rafaellopesbroseghini@gmail.com', 
    classifiers=[ 
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='words synonyms antonyms definitions', 
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests'], 
    project_urls={ 
        'API Source': 'https://developer.oxforddictionaries.com/',
        'Source': 'https://github.com/RafaelBroseghini/OxfordAPI'
    },
)