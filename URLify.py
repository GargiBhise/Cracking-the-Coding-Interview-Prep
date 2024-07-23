def urlify1(input_string):
    rep = '%20'
    input_string = input_string.strip()  # To remove any leading or trailing spaces
    print(input_string)
    result = ''
    for char in input_string:
        if char == ' ':
            result += rep
        else:
            result += char
    return result

input_string = "Mr John Smith "
print(urlify1(input_string))
