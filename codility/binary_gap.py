def solution2(N):
    N = bin(N)[2:] #cut the "0b"
    return len(max(str(N).rstrip("0").split("1")))

def main():
    N = 16
    print(solution2(N))

if __name__ == "__main__":
    main()
