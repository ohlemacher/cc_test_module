import codecs

def rot13_encode(ins):
    """ A trivial function to test in a package from concourse """
    out = codecs.encode(ins, 'rot_13')
    return out
