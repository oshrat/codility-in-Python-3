def solution(N):
    num = bin(N)[2:]#cut the "0b"
    max_gap = 0
    size = len(str(num))
    while size > 2:
        gap = 0
        start = num.find("10")
        if start > -1:
            end = num[start + 2:].find("1") + 2
            if end > -1:
                gap = end - start - 1
        if gap > max_gap:
            max_gap = gap
            num = num[end:]
            size = len(str(num))
        else:
            size -= 1
    return max_gap

def solution1(N):
    n = bin(N)[2:]
    counter = 0
    max_gap = 0
    for digit in n:
        if digit == 0:
            counter +=1
        else:
            counter = 0
        if counter > max_gap:
            max_gap = counter
    return  max_gap

def solution2(N):
    N = bin(N)[2:]
    return len(max(str(N).rstrip("0").split("1")))

def main():
    N = 16
    print(solution2(N))

if __name__ == "__main__":
    main()