
import random

def fromhex(h):
    return h.decode("hex")

def flip_bit(orig):
    offset = random.randrange(0, len(orig))
    whichbit = random.randrange(0, 8)
    corrupted = (orig[:offset]
                 + chr(ord(orig[offset]) ^ (1 << whichbit))
                 + orig[offset+1:])
    return corrupted
