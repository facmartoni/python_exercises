import turtle


def main():
    window = turtle.Screen()
    dave = turtle.Turtle()

    length = int(input('¿De qué tamaño será el cuadrado? '))
    make_square(dave, length)
    turtle.mainloop()


def make_square(dave, length):

    for i in range(4):
        make_line_and_turn(dave, length)


def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)


if __name__ == '__main__':
    main()
