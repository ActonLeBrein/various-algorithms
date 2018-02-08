def string_compression(s):
    counter = 0
    string_compress = ''
    character = ''
    for i in s:
        if character == '':
            character = i
            counter += 1
        elif i == character:
            counter += 1
        else:
            if counter == 1:
                string_compress += character
                character = i
            else:
                string_compress += character
                string_compress += str(counter)
                character = i
                counter = 1
    if counter > 1:
        string_compress += character
        string_compress += str(counter)
    else:
        string_compress += character
    return string_compress
    
print string_compression('abcaaabbb')
print string_compression('aaabaaaaccaaaaba')