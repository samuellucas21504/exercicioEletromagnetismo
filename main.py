import math

def calculoVetorial(nomeVetorA, nomeVetorB):
    iVetorTotA = input("Digite o valor das componentes do "+ nomeVetorA +": [Separe por espaços]\n")
    iVetorTotB = input("Digite o valor das componentes do "+ nomeVetorB +": [Separe por espaços]\n")

    iVetorTotASplitted = iVetorTotA.split();
    iVetorTotBSplitted = iVetorTotB.split();

    iVetorA = int(iVetorTotASplitted[0])
    jVetorA = int(iVetorTotASplitted[1])
    kVetorA = int(iVetorTotASplitted[2])

    iVetorB = int(iVetorTotBSplitted[0])
    jVetorB = int(iVetorTotBSplitted[1])
    kVetorB = int(iVetorTotBSplitted[2])

    iVetorAVetorialB = ((int(jVetorA) * int(kVetorB)) - (int(kVetorA) * int(jVetorB)))
    jVetorAVetorialB = ((int(kVetorA) * int(iVetorB)) - (int(iVetorA) * int(kVetorB)))
    kVetorAVetorialB = ((int(iVetorA) * int(jVetorB)) - (int(jVetorA) * int(iVetorB)))

    vetorVetorialTotArray = [iVetorAVetorialB, jVetorAVetorialB, kVetorAVetorialB]
    return vetorVetorialTotArray

def calculoForcaMagneticaSobreCarga():
    vetor = calculoVetorial(" vetor Velocidade, em m/s", "vetor Campo Magnético, em Tesla")
    vetorString = ''
    verificacao = input("A sua partícula é um eletron ou um proton? Digite 's' ou 'n':\n")
    if(verificacao.upper() == 'S'):
        cargaEletrica = -1.6
        expoente = '*10^-19'
        verificacao = input("Digite 1 para elétron ou 2 para próton:\n")
        if(verificacao == '2'):
            cargaEletrica = cargaEletrica * -1;
    else:
        cargaEletrica = input("Digite o valor da carga elétrica da partícula em Coulomb: [Caso esteja elevado"
                              " a 10, separe o valor por espaços. Por exemplo: 1,6 * 10^-19 = 1,6 10 -19\n")
        cargaEletricaSplitted = cargaEletrica.split()

        if len(cargaEletricaSplitted) > 1:
            cargaEletrica = cargaEletricaSplitted[0]
            expoente = ' *' + cargaEletricaSplitted[1] + '^' + cargaEletricaSplitted[2]


    for index, value in enumerate(vetor):
        newVetor = float(cargaEletrica) * float(value)
        if newVetor == 0:
            vetorString = vetorString + ' 0; '
        else:
            vetorString = vetorString + str(newVetor) + expoente + '; '

    return vetorString

def main():
    print("Digite o número da função que você quer executar:\n")
    print("1 - Calcular o vetorial de dois vetores\n")
    print("2 - Calcular o valor da força magnética sobre uma carga\n")
    selecaoMenu = input("Digite abaixo: ")
    if(selecaoMenu == '1'):
        vetor = calculoVetorial("vetor A", "vetor B")
        print("A X B : (" + str(vetor[0]) + "; " + str(vetor[1]) + "; " + str(vetor[2]) + ") ")

    elif(selecaoMenu == '2'):
        forcaMagnetica = calculoForcaMagneticaSobreCarga()
        print("A força magnética sobre essa carga elétrica é de (" + str(forcaMagnetica) + ")")



main()