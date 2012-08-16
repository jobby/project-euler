num_map = dict({
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
})

def translate_to_words(n):
    if n < 21:
        return num_map.get(n)
    elif n < 100:
        return num_map.get(n / 10 * 10) + "-" + num_map.get(n % 10)
    elif n < 1000:
        if n % 100 == 0:
            return num_map.get(n / 100 ) + " hundred"
        else:
            return num_map.get(n / 100) + " hundred and " + translate_to_words(n % 100)
    elif n == 1000:
        return "one thousand"
    else:
        return ""

def characters(number):
    return len(translate_to_words(number).translate(None, " -"))

print sum(map(characters, range(1, 1001)))
