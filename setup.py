import os
import setuptools

import my_osmc

_ROOT = os.path.abspath(os.path.dirname(__file__))

with open('requirements.txt') as f:
    REQUIREMENTS = f.read().splitlines()

with open(os.path.join(_ROOT, 'README.md')) as f:
    README_MD = f.read()

CLASSIFIERS = [
    'Operating System :: POSIX :: Linux',
    'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
    'Operating System :: MacOS',
    'Development Status :: 1 - Planning',
    'Environment :: Console',
    'Intended Audience :: End Users/Desktop',
    'Topic :: Multimedia'
    'Topic :: Utilities'
]

CLASSIFIERS += [('Programming Language :: Python :: %s' % x) for x in '3 3.5 3.6 3.7 3.8'.split()]

setuptools.setup(
    name='My OSMC',
    version=my_osmc.__version__,
    license='GPL-2.0-or-later',
    description='Replace with My OSMC description',
    long_description=README_MD,
    long_description_content_type='text/markdown',
    author='OSMC',
    url='https://github.com/osmc/my.osmc',
    download_url='https://github.com/osmc/my.osmc/archive/master.zip',
    packages=setuptools.find_packages(exclude=['tests*']),
    package_data={
        'myosmc': ['xml_schema/*.xsd']
    },
    install_requires=REQUIREMENTS,
    python_requires='>=3.5',
    setup_requires=['setuptools>=38.6.0'],
    entry_points={
        'console_scripts': [
            'myosmc = my_osmc.my_osmc:main'
        ]
    },
    keywords='osmc myosmc my_osmc',
    classifiers=CLASSIFIERS
)
