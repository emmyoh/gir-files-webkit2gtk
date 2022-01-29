#!/usr/bin/env python3
import os
import shutil

GIR_FILES=[
"JavaScriptCore-5.0", "Soup-3.0", "WebKit2-5.0",
"WebKit2WebExtension-5.0", "freetype2-2.0", "GLib-2.0",
]

dest_dir = os.path.abspath("./")

for file in GIR_FILES:
    src = f"/usr/share/gir-1.0/{file}.gir"
    dest = f"{dest_dir}/{file}.gir"
    try:
        shutil.copy(src, dest)
    except FileNotFoundError:
        print(f"gir file not found {file}")