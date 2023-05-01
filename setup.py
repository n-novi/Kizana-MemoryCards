try:
    from setuptools import setup, find_packages
except ImportError:
    raise ImportError(
        "setuptools module required, please go to "
        "https://pypi.python.org/pypi/setuptools and follow the instructions "
        "for installing setuptools"
    )
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    install_requires = f.read()

setup(
    name='KizanaMC',
    package_dir={'': 'app'},
    packages=find_packages('app', include=[
        'src*'
    ]),
    entry_points={
        'console_scripts': [
            'KizanaMC = main:main'
        ]
    },
    version='0.0.1',
    author="adenadenna, Kutushevva, nnovi",
    download_url='',
    description='Desktop application for memorizing words.',
    platforms='any',
    python_requires='>=3.5',
    install_requires=install_requires.split('\n'),
    long_description=long_description,
    long_description_content_type='text/markdown',
)
