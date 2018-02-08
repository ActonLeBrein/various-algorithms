from random import randint

def matrix(n):
    m = []
    l = []
    while len(m) < n:
        while len(l) < n:
            v = randint(0,1)
            l = l + [v]
        m = m + [l]
        l = []
    return m

def live_or_die(cell,alive):
    if cell == 1:
        if alive < 2:
            return False
        elif alive == 2 or alive <=3:
            return True
        else:
            return False
    else:
        if alive == 3:
            return True
        else:
            return False


def game_of_life(n):
    i = 0
    j = 0
    k = i
    l = j
    alive = 0
    cell = 0
    w = matrix(n)
    print 'First state of life'
    for n in w:
        print n
    print 'Final state of life'
    while i < len(w)-1:
        while j < len(w[i])-1:
            cell = w[i][j]
            if k-1 < 0:
                if l-1 < 0:
                    alive = w[k][l+1] + w[k+1][l] + w[k+1][l+1]
                    if live_or_die(cell,alive):
                        w[i][j] = 1
                        j += 1
                        k = i
                        l = j
                    else:
                        w[i][j] = 0
                        j += 1
                        k = i
                        l = j
                elif l+1 > len(w[i])-1:
                    alive = w[k][l-1] + w[k+1][l-1] + w[k+1][l]
                    if live_or_die(cell,alive):
                        w[i][j] = 1
                        j += 1
                        k = i
                        l = j
                    else:
                        w[i][j] = 0
                        j += 1
                        k = i
                        l = j
                else:
                    alive = w[k][l+1] + w[k+1][l] + w[k+1][l+1] + w[k][l-1] + w[k+1][l-1]
                    if live_or_die(cell,alive):
                        w[i][j] = 1
                        j += 1
                        k = i
                        l = j
                    else:
                        w[i][j] = 0
                        j += 1
                        k = i
                        l = j
            elif k+1 > len(w[i])-1:
                if l - 1 < 0:
                    alive = w[k][l+1] + w[k-1][l] + w[k-1][l+1]
                    if live_or_die(cell,alive):
                        w[i][j] = 1
                        j += 1
                        k = i
                        l = j
                    else:
                        w[i][j] = 0
                        j += 1
                        k = i
                        l = j
                elif l+1 > len(w[i])-1:
                    alive = w[k][l-1] + w[k-1][l-1] + w[k-1][l]
                    if live_or_die(cell,alive):
                        w[i][j] = 1
                        j += 1
                        k = i
                        l = j
                    else:
                        w[i][j] = 0
                        j += 1
                        k = i
                        l = j
                else:
                    alive = w[k][l+1] + w[k-1][l] + w[k-1][l+1] + w[k][l-1] + w[k-1][l-1]
                    if live_or_die(cell,alive):
                        w[i][j] = 1
                        j += 1
                        k = i
                        l = j
                    else:
                        w[i][j] = 0
                        j += 1
                        k = i
                        l = j
            else:
                if l-1 < 0:
                    alive = w[k][l+1] + w[k-1][l] + w[k-1][l+1] + w[k+1][l] + w[k+1][l+1]
                    if live_or_die(cell,alive):
                        w[i][j] = 1
                        j += 1
                        k = i
                        l = j
                    else:
                        w[i][j] = 0
                        j += 1
                        k = i
                        l = j
                elif l+1 > len(w[i])-1:
                    alive = w[k][l-1] + w[k-1][l-1] + w[k-1][l] + w[k+1][l] + w[k+1][l-1]
                    if live_or_die(cell,alive):
                        w[i][j] = 1
                        j += 1
                        k = i
                        l = j
                    else:
                        w[i][j] = 0
                        j += 1
                        k = i
                        l = j
                else:
                    alive = w[k][l+1] + w[k][l-1] + w[k-1][l] + w[k-1][l+1] + w[k-1][l-1] + w[k+1][l] + w[k+1][l+1] + w[k+1][l-1]
                    if live_or_die(cell,alive):
                        w[i][j] = 1
                        j += 1
                        k = i
                        l = j
                    else:
                        w[i][j] = 0
                        j += 1
                        k = i
                        l = j
        i += 1
        j = 0
        k = i
        l = j
    return w

for m in game_of_life(20):
    print m