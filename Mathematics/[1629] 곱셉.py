def power(a, b):
    if b == 1:
        return a % C
    else:
        tmp = power(a, b // 2)
        if b % 2 == 0:
            return tmp * tmp % C
        else:
            return tmp * tmp * a % C


if __name__ == "__main__":
    A, B, C = map(int, input().split())

    result = power(A, B)
    print(result)