import math

class Tree :
    

    def __init__(self, n, depth = 0, value = 0, q = 0) :
        self.depth = depth
        self.value = value
        self.n = n
        if self.depth == 0 :
            self.q = int(math.log(self.n)/math.log(2))
        else :
            self.q = q
        self.childLeft = None
        self.childMiddle = None
        self.childRight = None

        self.parent = None
        self.index = 0
        

    def construct(self) :

        temp = self.value + 2*(2**(self.q-self.depth+1)-1)

        if self.depth <= self.q and self.value <= self.n and temp >= self.n:

            if self.value + 2**(self.q-self.depth+1) <= self.n :
                val = self.value + 2**(self.q-self.depth+1)

                if self.index == 2 :
                    if self.parent.childRight != None :
                        if self.parent.childRight.childLeft != None :
                            if self.parent.childRight.childLeft.value == val :
                                self.childRight = self.parent.childRight.childLeft
                
                elif self.index == 1 :
                    if self.parent.childMiddle != None :
                        if self.parent.childMiddle.childLeft != None :
                            if self.parent.childMiddle.childLeft.value == val :
                                self.childRight = self.parent.childMiddle.childLeft
                else :
                    self.childRight = Tree(self.n,depth= self.depth +1, value = val, q = self.q)
                    self.childRight.construct()
                self.childRight.parent = self
                self.childRight.index = 3
            if temp - 2**(self.q-self.depth) >= self.n :
                val  = self.value + 2**(self.q-self.depth)
                if val <= self.n :
                    self.childMiddle = Tree(self.n,depth= self.depth +1, value = self.value + 2**(self.q-self.depth),q = self.q)
                    self.childMiddle.construct()
                    self.childMiddle.parent = self
                    self.childMiddle.index = 2
            if temp - 2*2**(self.q-self.depth) >= self.n :
                self.childLeft = Tree(self.n,depth= self.depth +1, value = self.value, q = self.q)
                self.childLeft.construct()
                self.childLeft.parent = self
                self.childLeft.index = 1
        return
    

    
    def isLeaf(self) :
        if self.childLeft == None and self.childRight == None and self.childMiddle == None :
            return True
        return False
    
    def counting(self):
        if self.isLeaf():
            return 1*(self.value == self.n)
        else :
            count = 0
            if self.childLeft != None : 
                count += self.childLeft.counting()
            if self.childRight != None : 
                count += self.childRight.counting()
            if self.childMiddle != None : 
                count += self.childMiddle.counting()
            return count
        

    def countingleafs(self) :
        if self.isLeaf() :
            return 1
        else :
            count = 0
            if self.childLeft != None :
                count += self.childLeft.countingleafs()
            if self.childRight != None :
                count += self.childRight.countingleafs()
            if self.childMiddle != None :
                count += self.childMiddle.countingleafs()
            return count
        



solve = []
for i in range(100) :
    TreeElem = Tree(i+1)
    TreeElem.construct()
    solve.append(TreeElem.counting())

print(solve)

TreeElem = Tree(int(100))
TreeElem.construct()
print(TreeElem.counting())