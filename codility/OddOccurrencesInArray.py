import collections
def main():
    A = [9, 3, 9, 3, 9, 7, 9]
    count = collections.Counter(A)
    for k, v in count.items():
        if v % 2 != 0: #finding the odd number
            print(k)


if __name__ == "__main__":
    main()