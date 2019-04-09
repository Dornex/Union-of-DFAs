input = open("input.txt", "r")
output = open("output.txt", "w")

delta1 = {}
delta2 = {}

numar_stari_1 = int(input.readline().split()[0])
stari_1 = set(input.readline().split())

numar_litere_1 = int(input.readline().split()[0])
litere_1 = set(input.readline().split())

stare_initiala_1 = input.readline().split()[0]

numar_stari_finale_1 = int(input.readline().split()[0])
stari_finale_1 = set(input.readline().split())

numar_tranzitii_1 = int(input.readline().split()[0])

for i in range(numar_tranzitii_1):
    tranzitie_1 = input.readline().split()
    delta1[(tranzitie_1[0], tranzitie_1[1])] = tranzitie_1[2]

numar_cuvinte_1 = int(input.readline().split()[0])

for i in range(numar_cuvinte_1):
    cuvant = input.readline().split()[0]
    output.write("{0}\n".format(cuvant))

#################################################################

numar_stari_2 = int(input.readline().split()[0])
stari_2 = set(input.readline().split())

numar_litere_2 = int(input.readline().split()[0])
litere_2 = set(input.readline().split())

stare_initiala_2 = input.readline().split()[0]

numar_stari_finale_2 = int(input.readline().split()[0])
stari_finale_2 = set(input.readline().split())

numar_tranzitii_2 = int(input.readline().split()[0])

for i in range(numar_tranzitii_2):
    tranzitie_2 = input.readline().split()
    delta2[(tranzitie_2[0], tranzitie_2[1])] = tranzitie_2[2]

numar_cuvinte_2 = int(input.readline().split()[0])

for i in range(numar_cuvinte_2):
    cuvant = input.readline().split()[0]
    output.write("{0}\n".format(cuvant))

###############################################################

delta1redem = {}
delta2redem = {}

cnt = 1

for stare in stari_1:
    delta1redem[stare] = cnt
    cnt+=1


for stare in stari_2:
    delta2redem[stare] = cnt
    cnt+=1

stare_noua = str(cnt)

graf = {}

for (nod, litera) in delta1.keys():
    graf[(delta1redem[nod], litera)] = delta1redem[delta1[(nod, litera)]]

for (nod, litera) in delta2.keys():
    graf[(delta2redem[nod], litera)] = delta2redem[delta2[(nod, litera)]]

############################################################

try:
    graf[(stare_noua, '.')].add(delta1redem[stare_initiala_1])
except:
    graf[(stare_noua, '.')] = set(delta2redem[stare_initiala_2])

print(graf)
