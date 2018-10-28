"""
Divide and Conquer Examples
"""

def my_sum(list_):
    return list_[0] + my_sum(list_[1:]) if list_ else 0

def factorial(n):
    return n * factorial(n-1) if n else 1

def euclids(a, b):
    return euclids(b, a % b) if b != 0 else a

def main():

    result = my_sum([])
    print("Sum:", result)

    result = my_sum([1])
    print("Sum:", result)

    result = my_sum([1, 3, 5, 7, 9])
    print("Sum:", result)

    result = factorial(5)
    print("Faltorial:", result)

    result = euclids(1680, 640)
    print("GCD:", result)

if __name__ == "__main__":
    main()
    print("Done!!")
