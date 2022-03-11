import random



class TABLE:
    def __init__(self, grandeur):

        self.grandeur = grandeur

        self.placeMine1 = random.randrange(0, self.grandeur*self.grandeur-1)
        self.placeMine2 = random.randrange(0, self.grandeur*self.grandeur-1)
        self.placeMine3 = random.randrange(0, self.grandeur*self.grandeur-1)
        self.placeMine4 = random.randrange(0, self.grandeur*self.grandeur-1)
        self.graph = []
        self.t = 0
        self.a = ""
        self.b = ""
        self.c = ""
        self.vide = "•"
        self.mine = "✹"
        self.flag = "⚐"

        for i in range(self.grandeur*self.grandeur):
                self.graph.append(self.vide)
                

        self.res = self.graph[:]

        self.res[self.placeMine1] = self.mine
        self.res[self.placeMine2] = self.mine
        self.res[self.placeMine3] = self.mine
        self.res[self.placeMine4] = self.mine


        
        for l in self.res:
            mine = 0
            if self.res[self.t-(self.grandeur-1)] == self.mine and (self.t-self.grandeur+1)%self.grandeur != 0 and self.t > self.grandeur-2:
                mine += 1

            if self.res[self.t-self.grandeur] == self.mine and self.t > self.grandeur-1:
                mine += 1

            if self.res[self.t-(self.grandeur+1)] == self.mine and self.t%self.grandeur != 0 and self.t > self.grandeur:
                mine += 1

            if self.res[self.t-1] == self.mine and self.t%self.grandeur != 0:
                mine += 1
            
            if self.t+1 < self.grandeur*self.grandeur and (self.t-self.grandeur+1)%self.grandeur != 0:
                if self.res[self.t+1] == self.mine:
                    mine += 1

            if self.t+(self.grandeur-1) < self.grandeur*self.grandeur and self.t%self.grandeur != 0:
                if self.res[self.t+(self.grandeur-1)] == self.mine:
                    mine += 1

            if self.t+self.grandeur < self.grandeur*self.grandeur:
                if self.res[self.t+self.grandeur] == self.mine:
                    mine += 1

            if self.t+(self.grandeur+1) < self.grandeur*self.grandeur and (self.t-self.grandeur+1)%self.grandeur != 0:
                if self.res[self.t+(grandeur+1)] == self.mine:
                    mine += 1

            if l == self.vide:
                self.res[self.t] = str(mine)
            self.t += 1


    def grille(self):
        return self.graph

    def solution(self):
        return self.res

    def tabletostr(self):
        
        self.a = ""
        self.b = ""
        self.c = ""


        for m in range(self.grandeur+1):
            self.c += str(m) + " "

        self.a += "\033[92m" + self.c + "\033[0m" + "\n"
        for j in range(self.grandeur):
            
            self.a += "\033[92m" + str(j+1) + "\033[0m" + " "

            for k in range(self.grandeur):
                self.a += self.graph[k+self.grandeur*j] + " "
                self.b += self.res[k+self.grandeur*j] + " "
            
            self.a += "\n"
            self.b += "\n"

        


        print(self.a)
        print(self.b)
        


    def load(self, case):

        self.case = case
        self.co = int(self.case.split()[1])-1 + self.grandeur*(int(self.case.split()[2])-1)
        self.cd = self.case.split()[0]
       
        if self.cd == "c":

            self.graph[self.co] = self.res[self.co]

        elif self.cd == "d":

            self.graph[self.co] = self.flag
            
        self.tabletostr()


