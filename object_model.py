class Computer:

    __IMAGES = [
        r'''
                          .----.
      .---------. | == |
      |.-"""""-.| |----|
      ||       || | == |
      ||       || |----|
      |'-.....-'| |::::|
      `"")---(""` |___.|
     /:::::::::::\" _  "
    /:::=======:::\`\`\
    `"""""""""""""`  '-'
        ''',
        r'''
                          .----.
      .---------. | == |
      |.-"""""-.| |----|
      || *   * || | == |
      || \---/ || |----|
      |'-.....-'| |::::|
      `"")---(""` |___.|
     /:::::::::::\" _  "
    /:::=======:::\`\`\
    `"""""""""""""`  '-'
        ''',
    ]

    def __init__(
        self,
        is_turned_on=True,
        keyboard='Redragon Karura',
        mouse='Common Genius',
        monitor='Samsung S19C300',
        speakers='Common Genius',
        case='Sentey 199',
        cpu='Amd Bulldozer FX 6300'

    ):
        self.__is_turned_on = is_turned_on
        self.__keyboard = keyboard
        self.__mouse = mouse
        self.__monitor = monitor
        self.__speakers = speakers
        self.__case = case
        self.__cpu = cpu

    def on(self):
        self.__is_turned_on = True

    def off(self):
        self.__is_turned_on = False

    def show(self):
        if self.__is_turned_on:
            print(self.__IMAGES[1])
        else:
            print(self.__IMAGES[0])

    # Getters and Setters

    def get_keyboard(self):
        return self.__keyboard

    def get_mouse(self):
        return self.__mouse

    def get_monitor(self):
        return self.__monitor

    def get_speakers(self):
        return self.__speakers

    def get_case(self):
        return self.__case

    def get_cpu(self):
        return self.__keyboard

    def set_keyboard(self, keyboard):
        self.__keyboard = keyboard

    def set_mouse(self, mouse):
        self.__mouse = mouse

    def set_monitor(self, monitor):
        self.__monitor = monitor

    def set_speakers(self, speakers):
        self.__speakers = speakers

    def set_case(self, case):
        self.__case = case

    def set_cpu(self, cpu):
        self.__cpu = cpu


def run():
    pc_nasa = Computer()


if __name__ == '__main__':
    run()
