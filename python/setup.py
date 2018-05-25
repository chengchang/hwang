from setuptools import setup, Extension
import shutil
import os
from sys import platform

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))

if platform == 'linux' or platform == 'linux2':
    EXT = '.so'
else:
    EXT = '.dylib'

SO_PATH = os.path.abspath('{p:s}/../build/libhwang{e:s}'.format(p=SCRIPT_DIR,
                                                                e=EXT))
DEST_PATH = os.path.abspath('{p:s}/hwang/libhwang.so'.format(p=SCRIPT_DIR))
shutil.copyfile(SO_PATH, DEST_PATH)
if EXT != '.so':
    DEST_PATH = os.path.abspath('{p:s}/hwang/libhwang'.format(p=SCRIPT_DIR) + EXT)
    shutil.copyfile(SO_PATH, DEST_PATH)

module1 = Extension(
    'hwang_python',
    include_dirs = [ROOT_DIR,
                    os.path.join(ROOT_DIR, 'build'),
                    os.path.join(ROOT_DIR, 'thirdparty/install/include')],
    libraries = ['hwang'],
    library_dirs = [os.path.join(ROOT_DIR, 'build'),
                    os.path.join(ROOT_DIR, 'thirdparty/install/lib')],
    sources = [os.path.join(ROOT_DIR, 'hwang/hwang_python.cpp')],
    extra_compile_args=['-std=c++11'])

setup(
    name='hwang',
    version='0.1.0',
    url='https://github.com/scanner-research/hwang',
    author='Alex Poms',
    author_email='apoms@cs.cmu.edu',
    packages=['hwang'],
    license='Apache 2.0',
    ext_modules=[module1],
)
