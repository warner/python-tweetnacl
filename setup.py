#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Build and install the TweetNaCl wrapper.
"""

from distutils.core import setup, Extension

nacl_module = Extension('_tweetnacl',
                        ["tweetnaclmodule.c", "tweetnacl.c", "randombytes.c"],
                        #include_dirs=["."],
                        extra_compile_args=["-O2",
                                            "-funroll-loops",
                                            "-fomit-frame-pointer"])

setup (name = 'tweetnacl',
       version = '0.1',
       author      = "Brian Warner, Jan Mojžíš",
       description = """Python wrapper for TweetNaCl""",
       ext_modules = [nacl_module],
       py_modules  = ["tweetnacl"])
