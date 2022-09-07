import sys
sys.path.append("..")
import click
import time
from modulos.analisador import pegar_sequencias, contar_cg, comprimento_das_sequencias, diagrama_disper

@click.group()
def contador():
    pass

@contador.command()
@click.option("--meufasta", help = "Diretório do fasta") #linha de comando
@click.option("--output",help = "Nome do arquivo de saida")

def ler(meufasta,output): #python
    print("Abrindo aquivo")
    time.sleep(1)
    fasta_seqs = pegar_sequencias(meufasta) # -> lista com sequencias do fasta
    
    print("Calculando conteúdo CG")
    time.sleep(1)
    lista_com_cg = contar_cg(fasta_seqs) # -> lista com conteudo cg de cada sequencia
    
    print("Calculando Comprimento das sequências")
    time.sleep(1)
    lista_com_comprimentos = comprimento_das_sequencias(fasta_seqs) # -> lista com comprimento de cada sequencia
    
    diagrama_disper(lista_com_cg,lista_com_comprimentos,str(output)) #-> grafico com o resultado
    # return print(lista_com_cg[500],lista_com_comprimentos[500])

if __name__ == '__main__':
    contador()