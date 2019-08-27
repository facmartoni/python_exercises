def run():
    t = int(input())
    while(t != 0):
        for i in range(t):
            n = int(input())
            if(n % 2 == 0):
                print(n * 2 - 2)
            else:
                print(n * 2 - 1)
        t = int(input())


if __name__ == '__main__':
    run()
