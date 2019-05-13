FIRST_TEN = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
             'eight', 'nine']
SECOND_TEN = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
              'sixteen', 'seventeen', 'eighteen', 'nineteen']
OTHER_TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
              'eighty', 'ninety']

SCALE = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrilion',
         'quintillion', 'sixtillion']

OPERATORS = {'+':'plus', '-':'minus', '*':'multiple', '/':'divide'}

def is_formatted_equality(equality):
    """ Check if received string is a well-formatted math equality.

    input: string 
        Expected string like 'a + b \ c = d', where a, b, c, d are 
        positive or negative non-decimal integers.
        Supports operators: listed in global OPERATORS only.
        Minimun space-separated elements: 5
        Single space separated only.
        Supports '+' or '-' chars before number.
        Underscores in Numeric Literals (PEP 515) - not supported.
        Example input: '1 + -321 - 41 * 3424 = 123' is OK.
        Mathematical thruthness does not checked.
    return: bool

    Comments: Using regex to filter correct equalities of any length only 
    considered as hardly maintalable solution.
    That is why simple sequence of if-s is chosen.
    """

    # Check if space at start or end of the equality
    if len(equality) != len(equality.strip()):
        print ('excessive space at the start or end of the equality')
        return False

    # Check for multiple spaces
    if '  ' in equality:
        return False

    equality = equality.split()

    # Check the equality length is > 5
    if len(equality) < 5:
        return False

    # Check the equality is odd
    if not len(equality) % 2:
        return False

    # Check each even element is a number (positive or negative)
    for elem in equality[::2]:
        if elem[0] in ['+', '-']:
            elem = elem[1:]
        if not elem.isdigit():
            return False

    # Check each odd element is an OPERATOR (except last one) 
    for elem in equality[1:-3:2]:
        if elem not in OPERATORS:
            return False

    # Check equality[-2] is '='
    if equality[-2] != '=':
        return False

    return True


def humanise_small_number(number):
    """ Returns received number (in range 0 ...999) how it's written in words
    
    input: any non-decimal number in range 0 ...999
    return: string """

    n = number // 100
    res = [FIRST_TEN[n-1], 'hundred'] if n > 0 else []

    n = (number // 10) % 10
    res += [OTHER_TENS[n-2]] if n > 1 else []

    n = number % (10 if n > 1 else 20)
    res += [(FIRST_TEN+SECOND_TEN)[n-1]] if n > 0 else []

    return ' '.join(res)


def humamise_number(number):
    """ Returns received any number how it's written in words 
    
    input: any non-decimal number with no underscores within
    call: humanise_small_number() 
    return: string """

    if number == 0:
        return 'zero'
    if number < 0 :
        number *= -1
        prefix = 'negative'
    else:
        prefix = ''
    res = []
    scale_val = 0
    while number:
        if number % 1000:
            res = ([humanise_small_number(number % 1000), SCALE[scale_val]]
                + res)
        number = number // 1000
        scale_val += 1
    res = [prefix] + res
    print(res)
    return ''.join(res)

def humanise_equality(equality):
    """Return inputed math equality as it written in words
    
    input: string 
        Works only with equality like 'a + b = c', where a, b, c are 
        positive or negative non-decimal integers.
        Supports operators: '+', '-', '*', '/' only.
        Single space separated only.
        Supports '+' or '-' chars before number.
        Does not support PEP 515 -- Underscores in Numeric Literals
    call: humamise_number(), is_formatted_equality()
    return: string
    """

    if not is_formatted_equality(equality):
        return 'invalid input'

    equality = equality.split()

    res = []
    for number, operator in zip(equality[:-1:2], equality[1:-2:2]):
        res.append(humamise_number(int(number)))
        res.append(OPERATORS[operator])
    res += [humamise_number(int(equality[-3])), 'equals',
            humamise_number(int(equality[-1]))]
    return " ".join(res)
    