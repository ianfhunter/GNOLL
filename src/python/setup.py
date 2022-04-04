import sys
import subprocess
from setuptools import setup
from setuptools.command.build_ext import build_ext
from distutils.core import Extension

setup(
    name='DiceTower',
    version='2.1.0',
    description='A comprehensive dice notation parser',
    url='https://github.com/ianfhunter/DiceTower',
    author='Ian Hunter',
    author_email='ianfhunter@gmail.com',
    license='GPL v3',
    py_modules=['dicetower.parser'],
    install_requires=[],
    include_package_date=True,
    # packages=["dicetower"],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
    # ,ext_modules=[
    #     Extension('dicetower.core', [
    #             'c_build/y.tab.c',
    #             'c_build/lex.yy.c',
    #             'c_includes/vector_functions.c',
    #         ],
    #         language='c',
    #         include_dirs=[
    #             'c_includes/'
    #         ]
    #     )
    # ]
    # cmdclass={
    #     "build_ext": Build,
    # }
)
