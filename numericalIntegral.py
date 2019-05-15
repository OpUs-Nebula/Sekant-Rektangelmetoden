# funktionen som ska integreras
def func(x):
    return -0.25*x**2 + x + 4

def sekant_method(low, high):
	return (func(low) + func(high))/ 2.

def rektangel_method(low,high):
	return func((low + high) / 2) 


"""
Vilken numerisk metod som bör användas

Argument:

opt  -- identifierare för utvald metod
low  -- början på delintervallet
high -- slutet på delintervallet
step -- bredd på varje delinterval vars area bör räknas ut 
"""
def numerical_method(opt, low, high, step):
	return {1:(step*sekant_method(low,high)), 2:(step*rektangel_method(low,high))}[opt] 
# variabler definieras
a = 1.          # vänstra gränsen för arean
b = 5.          # högra gränsen för arean
dx = 0.1          # bredd på parallelltrapetserna(eller rektanglarna)
 
# uträkning av antal parallelltrapetser
n = int((b - a) / dx)
 
# variabeln där arean ska sparas definieras
Area = 0
 
# loop som räknar ut arean för varje parallelltrapets och summerar ihop dessa

method = int(input("Vilken numerisk metod bör användas för beräkning? (skriv 1 för sekantmetoden, 2 för rektangelmetoden) -> "))
for i in range(1, n+1):
    # x-värdet längst till vänster och längst till höger för varje trapets
    x0 = a+(i-1)*dx
    x1 = a+i*dx
 
    # uträkning av arean för varje parallelltrapets
    Ai_old = dx * (func(x0) + func(x1))/ 2.
    Ai = numerical_method(method, x0, x1, dx)
    print("old: {}, new: {}".format(Ai_old,Ai))
    # kumulativ summering av arean för parallelltrapetserna tillsammans
    Area = Area + Ai
 
# Resultatet skrivs ut på skärmen
print ("Area = {}".format(Area))