class fraction:
    def __init__(self,a,b):
        self.numerator=a
        self.denominator=b

    def disp(self):
        print(self.numerator,"/",self.denominator)

    def add(self,b):
        if self.denominator != b.denominator:
            n=self.numerator*b.denominator+self.denominator*b.numerator
            d=self.denominator*b.denominator
            
        else:
            n=self.numerator+b.numerator
            d=self.denominator
        return fraction(n,d)
