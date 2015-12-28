from setuptools import setup, find_packages
import sys, os

version = '0.3.9.16'

setup(name='ninfo-plugin-riddler',
    version=version,
    description="riddler.io",
    keywords='',
    author='Daniel Mollberg',
    author_email='d-ninfo@yta52.net',
    url='',
    license='',
    zip_safe=False,
    packages = find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "ninfo",
    ],
    entry_points = {
        'ninfo.plugin': [
            'riddler    =   ninfo_plugin_riddler'
        ]
    }
) 
