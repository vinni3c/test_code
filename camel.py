def to_camel_case(text):
    new_string = ""
    i = []
    x = 0
    for char in text:
        if char == "_" or char == "-":
            new_string += ""
            i.append(x)
        else:
            new_string += char
            x += 1

    final_string = list(new_string)
    for item in i:
        final_string[item] = final_string[item].upper()
    final_string = "".join(final_string)

    print(final_string)
    return final_string






# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python


to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value"
