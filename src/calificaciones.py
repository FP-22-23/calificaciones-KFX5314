def nota(aciertos,errores,totalRespuestas):
    if ((aciertos*10)/totalRespuestas)-((errores*10)/(50-totalRespuestas))<0:
        print("ERROR, VUELVE A INTRODUCIR LOS DATOS")
    else:
        return (((aciertos*10)/totalRespuestas)-((errores*10)/(50-totalRespuestas)))

def datos():
    aciertos=int(input("Aciertos:"))
    errores=int(input("Errores:"))
    totalRespuestas=int(input("Total de respuestas:"))
    print("\n",aciertos,"\n",errores,"\n",totalRespuestas)
    return aciertos, errores, totalRespuestas