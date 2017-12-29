
import codecs

def rot13_encode(ins):
    out = codecs.encode(ins, 'rot_13')
    return out
