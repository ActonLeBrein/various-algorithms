# Script text here
from random import randint

class philosopher:
    #limit use for each fork is 5
    def __init__(self):
    #Dinning room
        self.d = {'A':[1,2],'B':[2,3],'C':[3,4],'D':[4,5],'E':[5,1]}
    #Number of forks on table
        self.f = [1,2,3,4,5]
    #Philosophers
        self.p = ['A','B','C','D','E']
    #Semaphore
        self.s = [0,0,0,0,0]
    #Philolophers eating
        self.pe = []
    
    def left_fork(self, phi):
        p = 0
        if phi not in self.p:
            print 'not a valid philosopher'
        elif self.d[phi][0] in self.f:
            del self.f[self.f.index(self.d[phi][0])]
            return True
        else:
            return False
    
    def right_fork(self, phi):
        p = 0
        if phi not in self.p:
            print 'not a valid philosopher'
        elif self.d[phi][1] in self.f and self.d[phi][0] not in self.f:
            del self.f[self.f.index(self.d[phi][1])]
            return True
        else:
            self.f = self.f + [self.d[phi][0]]
            return False
            
    def acquire(self, fork, phi):
        if fork not in self.d[phi]:
            print 'fork %s is not at reach for philosopher %s' % (fork, phi)
        elif self.d[phi].index(fork) == 0:
            if self.left_fork(phi):
                print 'fork %s is free for philosopher %s' % (fork, phi)
                return True
            else:
                if self.p.index(phi) == 0:
                    p = self.p[4]
                else:
                    p = self.p[self.p.index(phi)-1]
                print 'left fork is being used by %s' % p
                self.release(p)
                return False
        else:
            if self.right_fork(phi):
                print 'fork %s is free for philosopher %s' % (fork, phi)
                return True
            else:
                if self.p.index(phi) == 4:
                    p = self.p[0]
                else:
                    p = self.p[self.p.index(phi)+1]
                print 'left fork is being used by %s' % p
                self.release(p)
                return False

    def release(self,phi):
        if self.s[self.p.index(phi)] == 2:
            self.f = self.f + self.d[phi]
            self.f.sort()
            self.s[self.p.index(phi)] = 0
            del self.pe[self.pe.index(phi)]
            print 'philosopher %s finish eating.. NEXT!!!!' % phi
        else:
            self.s[self.p.index(phi)] = self.s[self.p.index(phi)] + 1
            print 'philosopher %s still eating' % phi
    
    def phieating(self,phi):
        if phi in self.pe:
            return True
        else:
            return False
            
if __name__ == '__main__':
    # Establish number of tasks
    tasks = 15
    dinning = philosopher()
    state = ''
    results = {}
    for i in dinning.d.keys():
        results[i] = 0
    while tasks > 0:
        j = randint(0,len(dinning.p)-1)
        if dinning.phieating(dinning.p[j]) == False:
            print 'time to eat'
            f = dinning.d[dinning.p[j]]
            if dinning.acquire(f[0],dinning.p[j]):
                print 'left fork'
                if dinning.acquire(f[1],dinning.p[j]):
                    print 'right fork'
                    tasks -= 1
                    dinning.pe = dinning.pe + [dinning.p[j]]
                    results[dinning.p[j]] = results[dinning.p[j]] + 1
                    print 'philosopher %s is eating' % dinning.p[j]
                else:
                    print 'philosopher %s has to wait... YOU SHALL NOT EAT!!!' % dinning.p[j]
            else:
                print 'philosopher %s has to wait... YOU SHALL NOT EAT!!!' % dinning.p[j]
        else:
            print 'philosopher %s is still eating, let him eat in peace God damn you!!!' % dinning.p[j]
    for k in results.keys():
        print 'philosopher %s ate %s times today' % (k,results[k])