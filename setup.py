#!/usr/bin/env python3

import os
from setuptools import setup

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements


PACKAGE_NAME = 'networkgen'
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

about = {}  # type: ignore
with open(os.path.join(PROJECT_DIR, PACKAGE_NAME, '__version__.py')) as f:
    exec(f.read(), about)


with open(os.path.join(PROJECT_DIR, 'README.md'), 'r') as f:
    readme = f.read()
    

install_reqs = parse_requirements(os.path.join(PROJECT_DIR, "requirements.txt"), session=False)
install_requires = [str(ir.req) for ir in install_reqs]
    
setup(
    name=about['__title__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=[PACKAGE_NAME],
    include_package_data=True,
    python_requires=">=3.7.*",
    install_requires=install_requires,
    license=about['__license__'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'networkgen = networkgen.cmd:networkgen_command'
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='network'
)
