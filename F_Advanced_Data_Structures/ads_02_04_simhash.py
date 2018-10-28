"""
Simhash
"""

from A_Classes.simhash import Simhash

def test(str1, str2):
    print()
    hash1 = Simhash(str1.split())
    print("{}\t[simhash = 0x{}]".format(str1, hash1))

    hash2 = Simhash(str2.split())
    print("{}\t[simhash = 0x{}]".format(str2, hash2))

    print("{:f} % similar".format(hash1.similarity(hash2)))
    print(hash1.hamming_distance(hash2), "bits differ out of", hash1.hashbits)

def main():

    test('This is a test string for testing', 'This is a test string for testing')

    test('111010010101010101011011001', '000101010101111101001010001')

    test('This is a test string for testing', 'testing is a test for This string')

    test('This is a test string for testing', 'This is a test string for testing also!')

    test('This is a test string for testing', 'This testing is nice')

    print("Done!!")

if __name__ == "__main__":
    main()
    print("Done!!")
    