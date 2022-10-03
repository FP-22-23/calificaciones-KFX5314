def calcula_nota_cuatrimestre(cuestionarios,proyecto,examen):
    cuestionarios=cuestionarios[0]+cuestionarios[1]+cuestionarios[2]
    nota=(0.1*cuestionarios)+(0.6*examen)+(0.1*proyecto)
    return nota

