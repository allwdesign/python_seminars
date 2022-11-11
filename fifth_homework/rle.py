"""
Implement RLE algorithm: Implement data compression and recovery module.
Input and output data are stored in separate text files.
"""
import re


def decode(input_data):
    """
    Decode an input data encoded with the Run Length Encoding Algorithm

    :param input_data:  str. Data to be decoded.
    :return: str. Decoded string.
    """
    decoded_string = ''
    # res: [('9', 'W'), ('3', 'B'), ('24', 'W'), ('1', 'B'), ('14', 'W')]
    res = re.findall(r"(?P<digit>\d+)(?P<char>\w)", input_data)

    if res is None:
        raise Exception("It doesn't match. Wrong input!")

    for item in res:
        digit = item[0]
        char = item[1]
        decoded_string += char * int(digit)

    print(f'Input data: {input_data} => Decode data: {decoded_string}')
    return decoded_string


def encode(input_data: str) -> str:
    """
    Encoding an input data using the Run Length Encoding Algorithm

    :param input_data: str. Data to be encoded.
    :return: str. Encoded string.
    """
    chars_dict = dict()
    last_idx = len(input_data) - 1
    encoded_string = ''
    for i, char in enumerate(input_data):
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
        if i != last_idx:
            next_char = input_data[i + 1]
            if char != next_char:
                encoded_string += f'{chars_dict.pop(char)}{char}'
        else:
            encoded_string += f'{chars_dict[char]}{char}'
    print(f'Input data: {input_data} => Encode data: {encoded_string}')
    return encoded_string


def prepare_data(input_file: str, output_file: str, func) -> None:
    """
    Read data from input_file, encode or decode data and write them
    to the output_file.

    :param input_file: str. Filename with input data.
    :param output_file: str. Filename for output data.
    :param func: function object. Encode or decode functinon.
    :return:
    """
    data = read_input_data(input_file)

    for string in data:
        print(f'Data from {input_file} file')
        output_data = func(string)
        print(f'Write data to {output_file} file')
        write_output_data(output_file, output_data)


def read_input_data(filename: str) -> list:
    """
    Read data from file with the specified filename in current directory.

    :param filename: str.
    :return: None.
    """
    with open(filename, "r") as data:
        input_data = data.readlines()

    input_data = list(map(lambda s: s.strip("\n"), input_data))

    return input_data


def write_output_data(filename: str, line: str) -> None:
    """
    Writes a string with data to a file with the specified filename
    in current directory.

    :param filename: str.
    :param line: str.
    :return: None.
    """
    with open(filename, "a") as data:
        data.write(line + "\n")


if __name__ == "__main__":
    try:
        # 1st Case: read row data from row.txt, encode them
        # and write to encode.txt file
        row_data_file = 'row.txt'
        # Encode data filename
        encode_file = '../seminars/encode.txt'
        # Decode data filename
        decode_file = '../seminars/decode.txt'

        prepare_data(row_data_file, encode_file, encode)

        # 2nd Case: read encode data from encode.txt, decode them
        # and write to decode.txt file
        prepare_data(encode_file, decode_file, decode)
    except Exception as error:
        print(error.args[0])
