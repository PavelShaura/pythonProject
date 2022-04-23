alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def shift_encode(string):
    string_encoded = ""

    for letter in string:
        position = alphabet.index(letter)
        position_next = (position + 1) % len(alphabet)
        next_letter = alphabet[position_next]
        string_encoded += next_letter

    return string_encoded


print(shift_encode("змея"))


def shift_decode(string):
    string_decode = ""

    for letter in string:
        pos = alphabet.index(letter)
        position_next = (pos - 1 + 33) % len(alphabet)
        next_letter = alphabet[position_next]
        string_decode += next_letter

    return string_decode


print(shift_decode("инёа"))
