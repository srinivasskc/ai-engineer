"""
This program is a basic form of steganography—the practice of concealing
a secret message within an ordinary message.

The rule for this specific pin extractor is:

Look at each line of the poem one by one
(tracked by line_index: line 0, line 1, line 2, etc.).

From each line, grab the word that matches that line's index number.

Count how many letters are in that word. That count becomes a digit in your secret PIN.
"""


def pin_extractor(poems):
    secret_codes = []
    for single_poem in poems:
        secret_code = ""
        lines = single_poem.split("\n")
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += "0"
        secret_codes.append(secret_code)

    return secret_codes


poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = "The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow"
poem3 = "There\nonce\nwas\na\ndragon"

print(pin_extractor([poem, poem2, poem3]))
