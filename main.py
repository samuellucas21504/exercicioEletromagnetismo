iVetorA = input("Digite o valor de i no vetor 1: ")
jVetorA = input("Digite o valor de j no vetor 1: ")
kVetorA = input("Digite o valor de k no vetor 1: ")

iVetorB = input("Digite o valor de i no vetor 2: ")
jVetorB = input("Digite o valor de j no vetor 2: ")
kVetorB = input("Digite o valor de k no vetor 2: ")

iVetorAVetorialB = ((int(jVetorA) * int(kVetorB)) - (int(kVetorA) * int(jVetorB)))
jVetorAVetorialB = ((int(kVetorA) * int(iVetorB)) - (int(iVetorA) * int(kVetorB)))
kVetorAVetorialB = ((int(iVetorA) * int(jVetorB)) - (int(jVetorA) * int(iVetorB)))


print('A ▪ B = ' + str(iVetorAVetorialB) + 'i, ' + str(jVetorAVetorialB) + 'j, ' + str(kVetorAVetorialB) + 'k')
