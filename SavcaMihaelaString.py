##De la tastatura se citesc 4 cuvinte, fiecare fiind citit intr-o singura variabila, un cuv va fi format din min 3 caract elaborati un program care va forma un cuv nou 
a=input()
b=input()
c= input()
d=input()
if len(a)>=3 and len(b)>=3 and len (c)>=3 and len (d) >=3:
    if len(d)>=3:
        n=round(len (d)/2)
    x=a[:2]+b[0]+c[:3]+d[:n]
    y=a+''+b+''+c+''+d+''+x
    print(y)
elif len(a) <3 or len (b) <3 or len(c) <3 or len(d)< 3:
    print("Eroare")