class brackets:
    def check(self):
        a=['*']
        b=input("Enter the string:")
        a.append(b[0])
        ai=1
        for  i in range(1,len(b)):
            if b[i]=='[' or b[i]=='(' or b[i]=='{':
                a.append(b[i])
                ai+=1
            if (b[i]==']'):
                if a[ai]=='[':
                    a.pop()
                    ai-=1
            if (b[i]==')'):
                if a[ai]=='(':
                    a.pop()
                    ai-=1
            if (b[i]=='}'):
                if a[ai]=='{':
                    a.pop()
                    ai-=1
        if a==['*']:
            print(" Valid ")
        else:
            print(" Invalid ")

b1=brackets()
b1.check()
