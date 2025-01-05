from setuptools import setup

setup(
    name='Bob',
    version='0.1',
    scripts=['bob.py'],  
    install_requires=[
        'argparse',
        'colorama',
        'requests',
        'beautifulsoup4',
    ],
    description='Checks the availability of domain names with a unique touch by jcastroo.',
    author='João Castro',
    author_email='jcastroo@icloud.com',
    url='https://github.com/jcastroo/bob',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts': [
            'bob=bob:main', 
        ],
    },
)
