import sys
import subprocess
from setuptools import setup
from setuptools.command.build_ext import build_ext


class Build(build_ext):
    def run(self):
        protoc_command = ["make" "all"]
        if subprocess.call(protoc_command) != 0:
            sys.exit(-1)
            build_ext.run(self)

setup(
    name='DiceTower',
    version='2.1.0',
    description='A comprehensive dice notation parser',
    url='https://github.com/ianfhunter/DiceTower',
    author='Ian Hunter',
    author_email='ianfhunter@gmail.com',
    license='GPL v3',
    py_modules=['parser'],
    install_requires=[],
    packages=["dicetower"],

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
    ],
    ext_modules=[
        # Extension('dicetower.core', [
        #         '../../build/y.tab.c',
        #         '../../build/lex.yy.c',
        #         '../../src/grammar/vector_functions.c',
        #     ]
            # include_dirs=[
            #     '../../src/grammar/'
            # ]
        # )
    ]
    # cmdclass={
    #     "build_ext": Build,
    # }
)
