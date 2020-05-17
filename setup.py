"""SysIdentPy: System Identification Library for Python
is open-source software for mathematics,
science, and engineering regarding the use of NARMAX models
built on top of numpy and is distributed under the 3-Clause BSD license.
"""

from __future__ import print_function
import sys
from setuptools import setup, find_packages

if sys.version_info[:2] < (3, 6):
    raise RuntimeError("Python version >= 3.6 required.")

with open('requirements.txt') as f:
    INSTALL_REQUIRES = [l.strip() for l in f.readlines() if l]


try:
    import numpy
except ImportError:
    print('numpy is required during installation')
    sys.exit(1)

try:
    import matplotlib
except ImportError:
    print('matplotlib is required during installation')
    sys.exit(1)

DISTNAME = 'sysidentpy'
DESCRIPTION = 'Open source System Identification library in Python'
LONG_DESCRIPTION = 'Take a look into https://github.com/wilsonrljr/sysidentpy'
MAINTAINER = 'Wilson Rocha Lacerda Junior'
MAINTAINER_EMAIL = 'wilsonrljr@outlook.com'
URL = 'http://sysidentpy.org'
DOWNLOAD_URL = 'https://pypi.org/project/sysidentpy/#files'
LICENSE = 'new BSD'
PROJECT_URLS = {
    'Source Code': 'https://github.com/wilsonrljr/sysidentpy'
}

import sysidentpy

VERSION = sysidentpy.__version__

NUMPY_MIN_VERSION = '1.17.3'
MATPLOTLIB_MIN_VERSION = '3.1.0'


def setup_package():
    metadata = dict(packages=find_packages(),
                    name=DISTNAME,
                    maintainer=MAINTAINER,
                    maintainer_email=MAINTAINER_EMAIL,
                    description=DESCRIPTION,
                    license=LICENSE,
                    url=URL,
                    download_url=DOWNLOAD_URL,
                    project_urls=PROJECT_URLS,
                    version=VERSION,
                    long_description=LONG_DESCRIPTION,
                    classifiers=[
                            'Intended Audience :: Science/Research',
                            'Intended Audience :: Developers',
                            'Programming Language :: Python :: 3.6',
                            'Programming Language :: Python :: 3.7',
                            'Programming Language :: Python :: 3.8',
                            'Development Status :: 0.0.1 - Alpha',
                            'Intended Audience :: Science/Research',
                            'Topic :: Scientific/Engineering',
                            'Topic :: Software Development'
                            'Operating System :: Microsoft :: Windows',
                            'Operating System :: Unix',
                            ],
                    python_requires=">=3.6",
                    install_requires=[
                                        'numpy>={}'.format(NUMPY_MIN_VERSION),
                                        'matplotlib>={}'.format(MATPLOTLIB_MIN_VERSION)
                                    ],
                    )

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
