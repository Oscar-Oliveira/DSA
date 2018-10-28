"""
Symmetric-key algorithm
"""

class SymmetricKey():
    """
    Simple symmetric-key algorithm
    Example:
        Txt: ABCDEF
        Key: 123
        Enc: BDFEGI [A+1, B+2, C+3, D+1, E+2, F+3]
        Dec: ABCDEF [B-1, D-2, F-3, E-1, G-2, I-3]
    """

    @staticmethod
    def encrypt(txt, key):
        txt_encripted = ""
        key = [int(i) for i in str(key)]
        for i, v in enumerate(txt):
            txt_encripted += chr(ord(v) + (i % len(key)))
        return txt_encripted

    @staticmethod
    def decrypt(txt, key):
        txt_decripted = ""
        key = [int(i) for i in str(key)]
        for i, v in enumerate(txt):
            txt_decripted += chr(ord(v) - (i % len(key)))
        return txt_decripted
