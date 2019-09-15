# URL = http://www.pythonchallenge.com/pc/def/oxygen.html
# second list = [105, 110, 116, 101, 103, 114, 105, 116, 121]


def colors_to_text(color_list):
    text = []
    for color in color_list:
        hex_value = color[:2]
        dec_value = int(hex_value, 16)
        text.append(chr(dec_value))
    return ''.join(text)


def run():
    color_list = ['737373', '6d6d6d', '616161', '727272', '747474', '202020', '676767', '757575',
                  '797979', '2c2c2c', '202020', '797979', '6f6f6f', '757575', '202020', '6d6d6d',
                  '616161', '646464', '656565', '202020', '696969', '747474', '2e2e2e', '202020',
                  '747474', '686868', '656565', '202020', '6e6e6e', '656565', '787878', '747474',
                  '202020', '6c6c6c', '656565', '767676', '656565', '6c6c6c', '202020', '696969',
                  '737373', '202020', '5b5b5b', '313131', '303030', '353535', '2c2c2c', '202020',
                  '313131', '313131', '303030', '2c2c2c', '202020', '313131', '313131', '363636',
                  '2c2c2c', '202020', '313131', '303030', '313131', '2c2c2c', '202020', '313131',
                  '303030', '333333', '2c2c2c', '202020', '313131', '313131', '343434', '2c2c2c',
                  '202020', '313131', '303030', '353535', '2c2c2c', '202020', '313131', '313131',
                  '363636', '2c2c2c', '202020', '313131', '323232', '313131', '5d5d5d']
    decoded_text = colors_to_text(color_list)
    print(decoded_text)

    # Next step

    second_list = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    second_decoded_text = [chr(num) for num in second_list]
    second_decoded_text = ''.join(second_decoded_text)
    print(second_decoded_text)


if __name__ == '__main__':
    run()
