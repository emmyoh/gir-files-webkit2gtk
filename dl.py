#!/usr/bin/env python3
import os
from distutils.dir_util import copy_tree

src_dir = "/usr/share/gir-1.0/"
dest_dir = os.path.abspath("./gir_files/")
copy_tree(src_dir, dest_dir)