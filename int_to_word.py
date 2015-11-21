# Recursive function the converts a number into it's string representation.
# Numbers greatr than 999999999 wll result in errors.
# function name: int_to_word
# params: int
# returns: str
#
# Author: Karlo L. Martinez Martos

def int_to_word(num):

    fnum = '{:,}'.format(int(num)).split(',');
    fsize = len(fnum);
    # Refers to the centecimal values
    pcen = {
        '1': 'hundred',
        '2': 'thousand',
        '3': 'million'
    }
    # Refers to the decimal values
    pdec = {
        '0': '',
        '1': '',
        '2': 'twenty',
        '3': 'thirty',
        '4': 'forty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety'
    }
    # Refers to the unit values
    punit = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen'
    }
    word = '' # Initialize the variable that holds the result.
    # Makes it possible to perform opperations on srings of length 0.
    csize = fsize; # Couter for the different parts of the number.
    # Keeps track of which segment of the number is evaluated so that the proper attribute is stored in the word.
    for part in fnum:
        # Handles both millions and thousands
        if csize >= 2:
            word += int_to_word(int(part));
            word += pcen[str(csize)] + ' ';
            # Handles hundreds, decimals and units
        elif csize == 1:
            # Hundreds
            if len(part) == 3:
                word += punit[part[0]] + ' '
                word += pcen[str(csize)] + ' '
                word += int_to_word(int(part[1:3])) + ' ';
            # Decimals, greater than tenths
            if len(part) == 2:
                if part[0] >= '2':
                    word += pdec[part[0]] + ' '
                    word += int_to_word(part[1])
                else:
                    word += punit[part]
            # Tenths and units
            if len(part) == 1:
                word += punit[part[0]]
        csize -= 1
    return word;
