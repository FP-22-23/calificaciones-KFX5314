from calificaciones_cuatrimestre import *
def main():
    c1=float(input("Dame la nota del C1 "))
    c2=float(input("Dame la nota del C2 "))
    c3=float(input("Dame la nota del C3 "))
    pr1=float(input("Dame la nota del PROYECTO1 "))
    ex1=float(input("Dame la nota del EX1 "))

    """c4=float(input("Dame la nota del C4 "))
    c5=float(input("Dame la nota del C5 "))
    c6=float(input("Dame la nota del C6 "))
    pr2=float(input("Dame la nota del PROYECTO2 "))
    ex2=float(input("Dame la nota del EX2 "))"""

    print("Tu nota del primer cuatrimestre es:",calcula_nota_cuatrimestre((c1,c2,c3),pr1,ex1))
    #print("Tu nota del segundo cuatrimestre es:",calcula_nota_cuatrimestre((c4,c5,c6),pr2,ex2))



if __name__=="__main__":
    main () 