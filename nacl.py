from _tweetnacl import *

def _fromhex(h):
    return h.decode("hex")

def _randreplace(orig):
    import random
    offset = random.randrange(0, len(orig))
    whichbit = random.randrange(0, 8)
    corrupted = (orig[:offset]
                 + chr(ord(orig[offset]) ^ (1 << whichbit))
                 + orig[offset+1:])
    return corrupted
