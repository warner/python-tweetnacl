
import os
from ._tweetnacl import *

def randombytes(count):
    return os.urandom(count)
