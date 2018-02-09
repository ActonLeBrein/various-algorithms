# Script text here
'''
0: free space
X: player 1
O: player 2
'''
t = ['X',0,'O','X','O',0,'X','O','X']

def checkgame(t):
    for i in range(0,9,3):
        if int(t[i]) & int(t[i+1]) & int(t[i+2]) == 1:
            return True
    for j in range(3):
        if int(t[j]) & int(t[j+3]) & int(t[j+6]) == 1:
            return True
    for k in range(0,3,2):
        if k == 0:
            if int(t[k]) & int(t[k+4]) & int(t[k+8]) == 1:
                return True
        else:
            if int(t[k]) & int(t[k+2]) & int(t[k+4]) == 1:
                return True
    return False


def tictactoe(g,p):
    if p == 'X' or p == 'O':
        #p1: 'X'
        p1 = [0,0,0,0,0,0,0,0,0]
        pr1 = False
        #p2: 'O'
        p2 = [0,0,0,0,0,0,0,0,0]
        pr2 = False
        i = 0
        while i < len(g):
            if t[i] == 'X':
                p1[i] = 1
                i += 1
            elif t[i] == 'O':
                p2[i] = 1
                i += 1
            else:
                i += 1
        print "player1 did %s and player2 %s" % (p1,p2)
        print "you are player %s" % p
        pr1 = checkgame(p1)
        pr2 = checkgame(p2)
        if pr1 == True & pr2 == True or pr1 == False & pr2 == False:
            print "its a draw between p1 and p2"
        elif pr1:
            if p == 'X':
                print "YOU WON!!!! n_n"
            else:
                print "YOU LOST!!! T_T"
        elif pr2:
            if p == 'O':
                print "YOU WON!!!! n_n"
            else:
                print "YOU LOST!!! T_T"
    else:
        print "player %s is invalid" % p

tictactoe(t,'X')

##################################### TICTACTOE GAME ####################################

# Script text here

'''
0: free space
X: player 1
O: player 2
'''

# Script text here

import random
from random import randint

class tictactoe:
    def __init__(self):
        self.game = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.player1 = ''
        self.player2 = ''
        self.position = 0
        self.level = ''
        
    def assignplayer(self,p):
        if p == 'X':
            self.player1 = 'X'
            self.player2 = 'O'
            print 'YOUR ARE PLAYER %s VS PLAYER %s' % (self.player1,self.player2)
        elif p == 'O':
            self.player1 = 'O'
            self.player2 = 'X'
            print 'YOUR ARE PLAYER %s VS PLAYER %s' % (self.player1,self.player2)
        else:
            print 'NOT A VALID PLAYER'
    
    def assignlevel(self,l):
        if 0 < l < 4:
            self.level = l
        else:
            print 'LEVEL OUT OF RANGE!!!!'
    
    def showgame(self):
        self.position = 0
        while self.position < len(self.game):
            print ' '+str(self.game[self.position])+' | '+str(self.game[self.position+1])+' | '+str(self.game[self.position+2])
            self.position += 3
            if self.position < len(self.game):
                print '-----------'
        self.position = 0
    
    def play(self,i):
        if i < len(self.game):
            if self.game[i] == ' ':
                self.game[i] = self.player1
                print 'YOUR MOVE WAS: '
                self.showgame()
                if self.winner() == "PLAY":
                    if self.level == 1:
                        self.IA_EASAY()
                    elif self.level == 2:
                        self.IA_MEDIUM()
                    else:
                        self.IA_HARD()
                elif self.winner() == "DRAW":
                    print "ITS A DRAW"
                    self.showgame()
                elif self.winner():
                    print "YOU WON!!! n_n"
                    self.showgame()
                else:
                    print "YOU LOST... T_T"
                    self.showgame()
            else:
                print "Position is not free"
        else:
            print "Position is greater then lenght of game"
    
    def IA_EASAY(self):
        self.position = 0
        if randint(0,1) == 0:
            while self.position < len(self.game):
                if self.game[self.position] == ' ':
                    self.game[self.position] = self.player2
                    break
                elif self.game[self.position] == self.player2:
                    self.position += 1
                else:
                    self.position += 1
        else:
            while self.position < len(self.game):
                if self.game[self.position] == ' ':
                    self.game[self.position] = self.player2
                    break
                elif self.game[self.position] == self.player2:
                    self.position += 3
                else:
                    self.position += 1
        print 'ENEMY MOVE WAS: '
        self.showgame()
        if self.winner() == "PLAY":
            print 'KEEP PLAYING!!!'
        elif self.winner() == "DRAW":
            print "ITS A DRAW"
            self.showgame()
        elif self.winner():
            print "YOU WON!!! n_n"
            self.showgame()
        else:
            print "YOU LOST... T_T"
            self.showgame()
    
    def IA_MEDIUM(self):
        self.position = 0
        while self.game[self.position] != ' ':
            self.position = randint(0,8)
        self.game[self.position] = self.player2        
        print 'ENEMY MOVE WAS: '
        self.showgame()
        if self.winner() == "PLAY":
            print 'KEEP PLAYING!!!'
        elif self.winner() == "DRAW":
            print "ITS A DRAW"
            self.showgame()
        elif self.winner():
            print "YOU WON!!! n_n"
            self.showgame()
        else:
            print "YOU LOST... T_T"
            self.showgame()
    
    def IA_HARD(self):
        chances = [[0,1],[0,2],[1,2],[0,3],[0,6],[3,6],
                   [0,4],[0,8],[4,8],[2,4],[2,6],[4,6],
                   [3,4],[3,5],[4,5],[6,7],[6,8],[7,8],
                   [1,4],[1,7],[4,7],[2,5],[2,8],[5,8]]
        win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],
               [1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        x = self.state('X')
        o = self.state('O')
        e = self.state(' ')
        cx = []
        co = []
        d = []
        for i in chances:
            if len(list(set(i).intersection(set(x)))) > 1:
                cx = cx + [list(set(i).intersection(set(x)))]
            if len(list(set(i).intersection(set(o)))) > 1:
                co = co + [list(set(i).intersection(set(o)))]
        for i in cx:
            for j in win:
                if set(i).issubset(set(j)):
                    if self.game[list(set(j).difference(set(i)))[0]] == 'O':
                        d = d + [i]
        for k in d:
            del cx[cx.index(k)]
        d = []
        for i in co:
            for j in win:
                if set(i).issubset(set(j)):
                    if self.game[list(set(j).difference(set(i)))[0]] == 'X':
                        d = d + [i]
        for l in d:
            del co[co.index(l)]
        print 'X is %s, O is %s, Empty is %s'%(cx,co,e)
        px = 11.111 * len(cx)
        po = 11.111 * len(co)
        if self.player2 == 'O':
            if (po == 0) & (px == 0) & (len(e) > 1):
                if self.mod2(e):
                    for i in e:
                        if i%2 == 0:
                            self.game[i] = 'O'
                            break
                else:
                    self.game[e[0]] = 'O'
            elif po > px:
                for i in co:
                    for j in win:
                        if set(i).issubset(set(j)):
                            self.game[list(set(j).difference(set(i)))[0]] = 'O'
                            break
                    break
            elif po < px:
                for i in cx:
                    for j in win:
                        if set(i).issubset(set(j)):
                            self.game[list(set(j).difference(set(i)))[0]] = 'O'
                            break
                    break
            elif po == px:
                for i in co:
                    for j in win:
                        if set(i).issubset(set(j)):
                            self.game[list(set(j).difference(set(i)))[0]] = 'O'
                            break
                    break
            else:
                self.game[e[0]] == 'O'
        else:
            if (po == 0) & (px == 0) & (len(e) > 1):
                if self.mod2(e):
                    for i in e:
                        if i%2 == 0:
                            self.game[i] = 'X'
                            break
                else:
                    self.game[e[0]] = 'X'
            elif px > po:
                for i in cx:
                    for j in win:
                        if set(i).issubset(set(j)):
                            self.game[list(set(j).difference(set(i)))[0]] = 'X'
                            break
                    break
            elif px < po:
                for i in co:
                    for j in win:
                        if set(i).issubset(set(j)):
                            self.game[list(set(j).difference(set(i)))[0]] = 'X'
                            break
                    break
            elif px == po:
                for i in cx:
                    for j in win:
                        if set(i).issubset(set(j)):
                            self.game[list(set(j).difference(set(i)))[0]] = 'X'
                            break
                    break
            else:
                self.game[e[0]] == 'X'
        print 'ENEMY MOVE WAS: '
        self.showgame()
        if self.winner() == "PLAY":
            print 'KEEP PLAYING!!!'
        elif self.winner() == "DRAW":
            print "ITS A DRAW"
            self.showgame()
        elif self.winner():
            print "YOU WON!!! n_n"
            self.showgame()
        else:
            print "YOU LOST... T_T"
            self.showgame()
    
    def mod2(self,l):
        for j in l:
            if j%2 == 0:
                return True
        return False
    
    def state(self,e):
        self.position = 0
        r = []
        while self.position < len(self.game):
            if self.game[self.position] == e:
                r = r + [self.position]
                self.position += 1
            else:
                self.position += 1
        return r
    
    def checkgame(self,g):
        for self.position in range(0,9,3):
            if int(g[self.position]) & int(g[self.position+1]) & int(g[self.position+2]) == 1:
                self.position = 0
                return True
        for self.position in range(3):
            if int(g[self.position]) & int(g[self.position+3]) & int(g[self.position+6]) == 1:
                self.position = 0
                return True
        for self.position in range(0,3,2):
            if self.position == 0:
                if int(g[self.position]) & int(g[self.position+4]) & int(g[self.position+8]) == 1:
                    self.position = 0
                    return True
            else:
                if int(g[self.position]) & int(g[self.position+2]) & int(g[self.position+4]) == 1:
                    self.position = 0
                    return True
        self.position = 0
        return False

    def winner(self):
        #p1: 'X'
        p1 = [0,0,0,0,0,0,0,0,0]
        pr1 = False
        #p2: 'O'
        p2 = [0,0,0,0,0,0,0,0,0]
        pr2 = False
        i = 0
        while i < len(self.game):
            if self.game[i] == 'X':
                p1[i] = 1
                i += 1
            elif self.game[i] == 'O':
                p2[i] = 1
                i += 1
            else:
                i += 1
        pr1 = self.checkgame(p1)
        pr2 = self.checkgame(p2)
        #print 'pr1 is %s pr2 is %s' % (pr1,pr2)
        if ((pr1 == False) & (pr2 == False)) & (' ' not in self.game):
            return "DRAW"
        elif ((pr1 == False) & (pr2 == False)) & (' ' in self.game):
            return "PLAY"
        elif pr2 & (self.player1 == 'O'):
                return True
        elif pr1 & (self.player1 == 'X'):
                return True
        else:
            return False
            
t = tictactoe()
t.showgame()
t.assignlevel(3)
t.assignplayer('X')
t.play(0)
t.play(6)
t.play(1)
t.play(8)?