from setuptools import setup, find_packages
setup(
)
# import sys, os
# import subprocess
# from setuptools import setup
# from distutils.command.build import build
# from setuptools.command.build_ext import build_ext
# from distutils.core import Extension
# import shutil

# if sys.version_info < (3, 0):
#     raise ValueError("Do not run the script under Python2")

# # Automate long desc = readme
# src_dir = os.path.dirname(os.path.abspath(__file__))
# long_description = ''
# with open(os.path.join(src_dir, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

# class build_binaries(build):
#     def run(self):
#         # protoc_command = ["python3", os.path.join(src_dir, "genbinding.py")]
#         # if subprocess.call(protoc_command) != 0:
#         #     sys.exit(-1)
#         build_dir = "build/lib/dicetower"
#         shutil.copyfile('c_build/dice.so', f'{build_dir}/c_build/dice.so')
#         shutil.copy('c_includes', f'{build_dir}/c_includes')
#         build.run(self)

# setup(
#     name='DiceTower',
#     version='2.1.0',
#     description='A comprehensive dice notation parser',
#     url='https://github.com/ianfhunter/DiceTower',
#     author='Ian Hunter',
#     author_email='ianfhunter@gmail.com',
#     license='GPL v3',
#     py_modules=['dicetower.parser'],
#     install_requires=[],
#     include_package_data=True,
#     # packages=["dicetower"],

#     classifiers=[
#         'Development Status :: 1 - Planning',
#         'Intended Audience :: Science/Research',
#         'License :: OSI Approved :: BSD License',
#         'Operating System :: POSIX :: Linux',
#         'Programming Language :: Python :: 2',
#         'Programming Language :: Python :: 2.7',
#         'Programming Language :: Python :: 3',
#         'Programming Language :: Python :: 3.4',
#         'Programming Language :: Python :: 3.5',
#         'Programming Language :: Python :: 3.6',
#         'Programming Language :: Python :: 3.7',
#         'Programming Language :: Python :: 3.8',
#         'Programming Language :: Python :: 3.9',
#     ]
#     # ,ext_modules=[
#     #     Extension('dicetower.core', [
#     #             'c_build/y.tab.c',
#     #             'c_build/lex.yy.c',
#     #             'c_includes/vector_functions.c',
#     #         ],
#     #         language='c',
#     #         include_dirs=[
#     #             'c_includes/'
#     #         ],
#     #         define_macros = [
#     #             ("YY_NO_INPUT", 1),
#     #             ("YY_NO_UNPUT", 1)
#     #         ]
#     #     )
#     # ]
#     # ,cmdclass={
#     #     "build": build_binaries,
#     # }
#     # ,package_data = {'':['**/*.so']}
# )
