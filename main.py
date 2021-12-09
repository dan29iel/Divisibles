def main ():
    divisibles8 = list()
    for x in range(1,1001):
        if x % 8 == 0:
            divisibles8.append(x)
    print(divisibles8)

if __name__ == '__main__':
    main()
