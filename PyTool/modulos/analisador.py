import matplotlib.pyplot as plt

def pegar_sequencias(arquivo):
    seq = []
    with open(arquivo,"r") as fasta:
        for linhas in fasta:
            if linhas.startswith(">"):
                pass
            else:
                seq.append(linhas)
    return seq

def contar_cg(lista_de_sequencias):
    lista_de_conteudo_cg = []
    for sequencias in lista_de_sequencias: #Ver sequencias da lista de sequencias
        numero_cg = 0
        conteudo_cg = 0
        comprimento = len(sequencias)
        for nucleotideos in sequencias: #Chegar os nucleotides na sequencia de dna
            if nucleotideos == "C" or nucleotideos == "G":
                numero_cg = numero_cg + 1
                conteudo_cg = (numero_cg / comprimento) * 100    
        lista_de_conteudo_cg.append(conteudo_cg)
    return lista_de_conteudo_cg

def comprimento_das_sequencias(lista_de_sequencias):
    lista_de_comprimentos = []
    for sequencias in lista_de_sequencias:
        comprimento = len(sequencias)
        lista_de_comprimentos.append(comprimento)
    return lista_de_comprimentos

def diagrama_disper(x,y,nome):
    plt.figure(figsize = (10,10))
    plt.scatter(x,y)
    plt.title("Diagrama de dispersão",fontsize = 30)
    plt.ylabel("Comprimento", fontsize = 20)
    plt.yticks(fontsize = 18)
    plt.xlabel("Conteudo CG(%)", fontsize = 20)
    plt.xticks(fontsize = 18)
    plt.show()
    plt.savefig(f"{nome}.png")