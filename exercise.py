#https://www.codewars.com/kata/53368a47e38700bd8300030d

names_dictionary =[{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Flanders'} ]

def namelist(names):
    string = ""
    size = len(names)
    i = 0
    while i <= size and size > 2:
        string += str(names[i].get("name")) + ", "
        i += 1
        if i == (size - 2):
            string += str(names[-2].get("name")) + " & " + str(names[-1].get("name"))
            return string
    if size == 2:
        string += str(names[0].get("name")) + " & " + str(names[1].get("name"))
        return string
    elif size == 1:
        string = str(names[0].get("name"))
        return string
    else:
        return ''

print(namelist(names_dictionary))
