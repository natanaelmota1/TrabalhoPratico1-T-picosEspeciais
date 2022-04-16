def calculaMedia(ap1, ap2):
    #Tratando casos de entradas inválidas
    try:
        ap1 = float(ap1)
        ap2 = float(ap2)
    except ValueError:
        return("Entrada inválida, a entrada não é um número.")

    if(ap1 > 10):
        return("Entrada inválida, a AP1 tem valor maior que 10.")
    elif(ap1 < 0):
        return("Entrada inválida, a AP1 tem valor negativo.")
    elif(ap2 > 10):
        return("Entrada inválida, a AP2 tem valor maior que 10.")
    elif(ap2 < 0):
        return("Entrada inválida, a AP2 tem valor negativo.")
    
    #fazendo cálculo da média
    media = (ap1 + ap2) / 2
    if (media >= 8):
        return("Aluno aprovado.")
    elif (media < 4):
        return("Aluno reprovado.")
    else:
        return("Aluno precisa fazer PF.")
