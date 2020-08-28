"""
compile.py: Used to compile the core file
For details, you can view detailed documentation: docs/COMPILE_TO_C.md
How to run this script:
python compile.py build_ext --inplace
"""
from __future__ import print_function
import os
import shutil
from Cython.Distutils import build_ext
from setuptools import find_packages, setup
from setuptools.extension import Extension


def build_extension(root_dir, root_package):
    extensions = {}
    for (dirpath, dirnames, filenames) in os.walk(root_dir):
        current_dir = os.path.basename(dirpath)
        if current_dir == '__pycache__':
            continue
        for f in filenames:
            ext = os.path.splitext(f)[-1]
            if f == '__init__.py' or ext != '.py':
                continue
            abs_path = os.path.join(dirpath, f)
            if "SSDTensorflow" in abs_path:
                continue
            if 'inception' in f:
                continue

            if os.name == 'nt':
              path_list = abs_path.split('\\')
            else:
              path_list = abs_path.split('/')

            index = [index for index, val in enumerate(path_list) if val == root_package]
            path_list = path_list[index[-1]+1:]
            if len(path_list) == 1:
                continue

            key = '.'.join(path_list)[:-3]
            path_list.insert(0, os.path.join(os.path.dirname(root_dir), root_package))
            val = '/'.join(path_list)

            extensions[key] = val

    return extensions

# find plumber root
dist_dir = os.path.abspath(os.path.dirname(__name__))
base_dir = os.path.abspath(os.path.join(dist_dir, '..',))
src_dir = dist_dir
build_so_dir = os.path.join(base_dir, 'build_so')

# The build_so directory is used to store
# the compiled source code .so directory

if os.path.exists(build_so_dir):
    print("exist")
    shutil.rmtree(build_so_dir)
#os.mkdir(build_so_dir)

shutil.copytree(dist_dir, build_so_dir)

# Construct a file that needs to be compiled Extensions
extensions = {}
extension_modules = []

extension_sg = build_extension(src_dir, 'compile')
extensions.update(extension_sg)


for k, v in extensions.items():
    print(k, v)
    extension_modules.append(Extension(k, [v]))

# import pdb; pdb.set_trace()
# Execute the compiled entry
setup(name='rbcompiler',
      packages=find_packages('../build_so'),
      package_dir={'':'../build_so'},
      ext_modules=extension_modules
      )


for (dirpath, dirnames, filenames) in os.walk(build_so_dir):
    for f in filenames:
        ext = os.path.splitext(f)[-1]
        if ext == ".c" or ext == '.py' or f == "__pycache__":
            del_path = os.path.join(dirpath, f)
            print("RM ", del_path)
            os.remove(del_path)

demo_files = os.listdir(dist_dir)
for f in demo_files:
    if ".py" in f and f != "compile.py":
        shutil.copy(os.path.join(dist_dir, f), build_so_dir)
