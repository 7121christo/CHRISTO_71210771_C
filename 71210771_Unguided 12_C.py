class Node:
    def __init__(self, data, parent):
        self._data = data
        self._children = []
        self._parent = parent
    
    def addChild(self,data) : 
        self._children.append(data)

    def operator(self):
        return self._data
    
    def parent(self):
        return self._parent
    
    def children(self):
        return self._children
    
    def inRoot(self):
        return self._parent is None
    
    def isExternal(self):
        return len(self._children) == 0
    
class tree:
    def __init__(self, data, parent):
        self._data = data
        self._children = []
        self._parent = parent

    def addChild(self, data):
        self._children.append(data)

    def parent(self):
        return self._parent

    def minus(self,node): 
        for i in node.children():
            self.minus(i) 
        emp.append(node.operator())
        if node.operator() != val300.operator(): 
            pass
        else: 
            print("Hasil penjumlahan semua node dalam tree : ", sum(emp))    

    def sibling(self): 
        while True: 
            total = 0 
            parnt = self._parent() 
            for i in parnt._children(): 
                total += i._operator()
            print("sibling : ", total)
            break
    
emp=[]

if __name__ == '__main__':
    val300 = Node(300, None)
    t = tree(val300, None) #Level 0
    val9 = Node(9,None)
    a = tree(val9, None)
    val1 = Node(1,None)
    x = tree(val1, None)
    val11 = Node(11,None)
    y = tree(val11, None)
    val99 = Node(99,None)
    yt = tree(val99, None)
    val17 = Node(17,None)
    ty = tree(val17, None)


    #Level 1 parent 120
    val9 = t.addChild( 9)
    val1 = t.addChild( 1)
 
    #Level 2 parent 9
    val11 = a.addChild(11) 
    val99 = a.addChild( 99) 
 
    #Level 2 parent 1
    val17 = x.addChild( 17) 
 
    #Level 3 parent 11
    val28 = y.addChild(28) 
    val72 = y.addChild( 72)
 
    #Level 3 parent 99
    val90 = yt.addChild( 90) 
    val33 = yt.addChild( 33)
 
    #Level 3 parent 17
    val17 = ty.addChild( 2)
    val17 = ty.addChild( 4)
    val17 = ty.addChild( 43)
 
    # No 2. #
    print(f'Sisa hasil pengurangan dari node {val300.data} adalah {t.minus(val300)}')
 
    # No 3. #
    print(f'Total nilai dari semua saudara pada node {val90.data} adalah {t.sibling(val90)}')
