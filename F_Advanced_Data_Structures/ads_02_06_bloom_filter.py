"""
Bloom filter
See: https://en.wikipedia.org/wiki/Bloom_filter#Probability_of_false_positives
See: http://www.maxburstein.com/blog/creating-a-simple-bloom-filter/
"""

from B_Data_Structures.bloomfilter import BloomFilter

def main():

    bloomfilter = BloomFilter(10)

    print(bloomfilter)

    bloomfilter.add("hello")
    bloomfilter.add("hi")

    print(bloomfilter)

    print("Probably in set" if bloomfilter.exists("hello") \
                            else "Definitely not in set")

    # Probably in set, change the size of the bit array to decrease (ex. 50) false positives
    # also, the hash function should distribute better
    print("Probably in set" if bloomfilter.exists("jack") \
                            else "Definitely not in set")

    print("Probably in set" if bloomfilter.exists("popo") \
                            else "Definitely not in set")

if __name__ == "__main__":
    main()
    print("Done!!")
