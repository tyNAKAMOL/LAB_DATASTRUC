class translator:
    def deciToRoman(self,x,i):
        Roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        Values = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        ROMAN =''
        if x==0:
            return ROMAN
        if x>0:
            if x >= Values[i]:
                ROMAN += Roman[i]
                return ROMAN + self.deciToRoman(x - Values[i],i)
            else:
                return ROMAN + self.deciToRoman(x,i-1)

    def romanToDeci(self,r,i):
        roman_dict ={'I': 1, 'V': 5,'X': 10, 'L': 50,'C': 100, 'D': 500,'M': 1000}
        dec = 0
        if len(r)>i:
            if i > 0 and roman_dict[r[i]] > roman_dict[r[i-1]]:
                dec += roman_dict[r[i]] - 2*roman_dict[r[i-1]]
            else:
                dec += roman_dict[r[i]]
            return dec + self.romanToDeci(r,i+1)
        else:
            return dec

n = int(input("Enter number to translate : "))
print(translator().deciToRoman(n,12))
print(translator().romanToDeci(translator().deciToRoman(n,12),0))

