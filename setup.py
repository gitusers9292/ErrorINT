# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='toutatis',
    version="1.31",
    packages=find_packages(),
    author="megadose",
    install_requires=["argparse","requests","phonenumbers","pycountry"],
    description="It is a tool written to retrieve private information such as Phone Number, Mail Address, ID on Instagram accounts via API.",
    long_description="It is a tool written to retrieve private information such as Phone Number, Mail Address, ID on Instagram accounts via API.",
    include_package_data=True,
    url='http://github.com/gitusers9292/ErrorINT',
    entry_points = {'console_scripts': ['ErrorINT = ErrorINT.core:main']},
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
