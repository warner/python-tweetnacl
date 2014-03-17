#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Build and install the TweetNaCl wrapper.
"""

import sys, os
from distutils.core import setup, Extension, Command
from distutils.util import get_platform

nacl_module = Extension('_tweetnacl',
                        ["tweetnaclmodule.c", "tweetnacl.c", "randombytes.c"],
                        #include_dirs=["."],
                        extra_compile_args=["-O2",
                                            "-funroll-loops",
                                            "-fomit-frame-pointer"])

class Test(Command):
    description = "run tests"
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass

    def setup_path(self):
        # copied from distutils/command/build.py
        self.plat_name = get_platform()
        plat_specifier = ".%s-%s" % (self.plat_name, sys.version[0:3])
        self.build_lib = os.path.join("build", "lib"+plat_specifier)
        sys.path.insert(0, self.build_lib)

    def run(self):
        self.setup_path()
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), "test"))
        import test_box; test_box.run()
        import test_box_curve25519xsalsa20poly1305; test_box_curve25519xsalsa20poly1305.run()
        import test_hash; test_hash.run()
        import test_hash_sha512; test_hash_sha512.run()
        import test_onetimeauth; test_onetimeauth.run()
        import test_onetimeauth_poly1305; test_onetimeauth_poly1305.run()
        import test_scalarmult; test_scalarmult.run()
        import test_scalarmult_curve25519; test_scalarmult_curve25519.run()
        import test_secretbox; test_secretbox.run()
        import test_secretbox_xsalsa20poly1305; test_secretbox_xsalsa20poly1305.run()
        import test_sign; test_sign.run()
        import test_sign_ed25519; test_sign_ed25519.run()
        import test_stream; test_stream.run()
        import test_stream_salsa20; test_stream_salsa20.run()
        import test_stream_xsalsa20; test_stream_xsalsa20.run()
        import test_verify_16; test_verify_16.run()
        import test_verify_32; test_verify_32.run()

setup (name = 'tweetnacl',
       version = '0.1',
       author      = "Brian Warner, Jan Mojžíš",
       description = """Python wrapper for TweetNaCl""",
       ext_modules = [nacl_module],
       py_modules  = ["nacl"],
       cmdclass = { "test": Test },
       )
