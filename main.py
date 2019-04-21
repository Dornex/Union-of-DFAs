import queue

def lnfa_to_dfa(start_state, graf):
    coada = queue.Queue()
    viz = set()
    dfa_tranz = {}
    coada.put(start_state)
    stari_finale = set()
    while not coada.empty():
        X = coada.get()
        auxx = frozenset(X)
        viz.add(auxx)
        for litera in litere:
            T = set()
            for stare in X:
                if stare in stari_finale_init:
                    stari_finale.add(auxx)
                if (stare, litera) in graf:
                    T.add(graf[(stare, litera)])
            if len(T) != 0:
                dfa_tranz[(auxx, litera)] = T
            if T not in viz:
                aux = frozenset(T)
                viz.add(aux)
                coada.put(T)
    cnt = 1
    graf_redem = {}
    for (stare, litera) in dfa_tranz.keys():
        if stare not in graf_redem.keys():
            graf_redem[stare] = cnt
            cnt+=1
    for stare in dfa_tranz.values():
        stare_aux = frozenset(stare)
        if stare_aux not in graf_redem.keys():
            graf_redem[stare_aux] = cnt
            cnt+=1
    graf_nou = {}

    for (nod, litera) in dfa_tranz.keys():
        nod_aux = frozenset(nod)
        graf_nou[(graf_redem[nod_aux], litera)] = graf_redem[frozenset(dfa_tranz[(nod_aux, litera)])]

    output.write(str(len(viz)-1))
    output.write("\n")
    for i in viz:
        if len(i) != 0:
            output.write("{0} ".format(graf_redem[i]))
    output.write("\n")
    output.write(str(len(litere)))
    output.write("\n")
    for litera in litere:
        output.write("{0} ".format(litera))
    output.write("\n")
    output.write("1")
    output.write("\n")
    output.write(str(len(stari_finale)))
    output.write("\n")
    for i in stari_finale:
        output.write("{0} ".format(graf_redem[i]))
    output.write("\n")
    output.write(str(len(graf_nou)))
    output.write("\n")
    for (stare, litera) in graf_nou.keys():
        output.write("{0} {1} {2}\n".format(stare, litera, graf_nou[(stare, litera)]))

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

########################################################################

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

########################################################################

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

##########################################################################

for (nod, litera) in delta1.keys():
    if stare_initiala_1 == nod:
        stare_init_1 = delta1redem[nod]

for (nod, litera) in delta2.keys():
    if stare_initiala_2 == nod:
        stare_init_2 = delta2redem[nod]

stare_noua = cnt

graf[(stare_noua, '.')] = set(str(delta1redem[stare_initiala_1]))
graf[(stare_noua, '.')].add(str(delta2redem[stare_initiala_2]))

#########################################################################

start_state = set()
start_state.add(stare_noua)
start_state.add(delta1redem[stare_initiala_1])
start_state.add(delta2redem[stare_initiala_2])

stari_finale_init = set()
litere = litere_1 | litere_2
for stare in stari_finale_1:
    stari_finale_init.add(delta1redem[stare])
for stare in stari_finale_2:
    stari_finale_init.add(delta2redem[stare])

lnfa_to_dfa(start_state, graf)
