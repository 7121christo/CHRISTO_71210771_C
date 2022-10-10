#71210771 - Christophorus Adyatma Wahyu Setya Nayottama

class PrefixConverter:
    def __init__(self):
        self.stackList = ['?']
    
    def push(self,data):
        self.stackList.append(data)

    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "isi Stack Kosong"

    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
            return data
        else:
            return data
    
    def cekValidExpression(self,expression):
        #code anda
    
    def infixToPrefix(self,expression):
        #code anda
        
#Test Case
if __name__ == '__main__':
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix("1+2+3*3/42-1"))
    print(expresi1.infixToPrefix("A * (B + C) / D"))
    print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
    print(expresi1.infixToPrefix("100 * / 600 - 30 + 100 * 777"))

#dah lah syulit dimengertos    