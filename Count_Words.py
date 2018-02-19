#INPUT#
stream = "ycaarcarzkiucatuifeadogsdoooooggdogfxvcatcatcatdwzqhaaathat"
words = ["car", "dooooog", "cat", "hat"]
#OUTPUT#
result = {'car': 1, 'hat': 1, 'dog': 2, 'cat': 4}

def count_word(s,w):
    d = {}
    for h in w:
        d[h] = 0
    r = ['']*len(w)
    for c in s:
        for l in xrange(len(w)):
            if c in w[l]:
                if c not in r[l]:
                    r[l] += c
                    print c, l, w[l], r
                    if (len(w[l]) == len(r[l])) and (w[l] == r[l]):
                        d[w[l]] += 1
                        r[l] = ''
                        print d
                    elif r[l] == w[l][0:len(r[l])] and len(r[l]) < len(w[l]):
                        pass
                    else:
                        r[l] = ''
                elif l < len(w)-2:
                    print w[l][len(r[l])]
                    if w[l][len(r[l])] == c:
                        r[l] += c
                    else:
                        r[l] = ''
                else:
                    r[l] = ''
            else:
                r[l] = ''
    return d

print count_word(stream,words)

###################################################################################

def count_words( in_string, in_words ):
    n_letters = len(in_string)
    n_words   = len(in_words)
    count = [0] * n_words
    c_letters = 0
    while c_letters < n_letters:
        c_words = 0
        while c_words < n_words:
            if in_string[c_letters:c_letters + len(in_words[c_words])] == in_words[c_words]:
                count[c_words] += 1
            c_words += 1
        c_letters += 1
    
    ### Order Output
    out_count = []
    c_words = 0
    while min(count) != float('inf'):
        min_count = min(count)
        min_index = [i for i, j in enumerate(count) if j == min_count]
        words = sorted( [ in_words[i] for i in min_index] )
        for word in words:
            out_count += [[word,min_count]]
        for index in min_index:
            count[index] = float('inf')
    return out_count

stream = "ycaarcarzkiucatuifeadogsdoooggdogfxvcatcatcatdwzqhaaathat"
words = ["car", "dog", "cat", "hat"]
for word_count in count_words( stream, words ):
    print '\'', word_count[0], '\': ', word_count[1], ' ',

###################################################################################

def count_word_super_efficient(string,words):
    result = {}
    len_words=list(set([len(w) for w in words]))
    result={w:0 for w in words}
    for char_s in xrange(len(string)-min(len_words)):
        for word in len_words:
          try:
            if string[char_s:char_s+word] in words:
              result[string[char_s:char_s+word]]+=1
          except:
            pass
    return result

print count_word_super_efficient(stream,words)