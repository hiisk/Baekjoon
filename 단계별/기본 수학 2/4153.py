while True:
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break
    elif max(x,y,z)**2 *2 == x**2 + y**2 + z**2:
        print("right")
    else:
        print("wrong")