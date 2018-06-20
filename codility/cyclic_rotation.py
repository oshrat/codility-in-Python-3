def one_rotation(iter):
    return iter[-1:] + iter[:-1]

def rotate(iter, key):
    for i in range(key):
        iter = one_rotation(iter)
    return iter

def main():
    A = [3, 8, 9, 7, 6]
    k = 3
    print(rotate(A, k))

if __name__ == "__main__":
    main()