class Estado: 
    def __init__(self, sigla, nomeEstado): 
        self.sigla = sigla.upper()
        self.nomeEstado = nomeEstado
        self.proximo = None

tabelaHash = [None] * 10

def funcaoHash(sigla):
    
    sigla = sigla.upper()
    
    if sigla == "DF":
        return 7
    
    char1Ascii = ord(sigla[0])
    char2Ascii = ord(sigla[1])
    
    posicao = (char1Ascii + char2Ascii) % 10
    return posicao

def inserir(sigla, nomeEstado):
    posicao = funcaoHash(sigla)
    
    novoEstado = Estado(sigla, nomeEstado)
    
    novoEstado.proximo = tabelaHash[posicao]
    
    tabelaHash[posicao] = novoEstado
    
def imprimirTabelaHash():
    print("_" * 37)
    print("*** VISUALIZAÇÃO TABELA HASH ***")
    
    for i in range(10):
        print(f"\nPosição [{i}]: ", end="")
        atual = tabelaHash[i]
        
        if atual is None:
            print("None")
        else: 
            elementos = []
            while atual is not None:
                elementos.append(atual.sigla)
                atual = atual.proximo
                
            print(" → ".join(elementos) + " → None")
            
estadosBrasil = [
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins"),
]

for sigla, nomeEstado in estadosBrasil:
    inserir(sigla, nomeEstado)
    
estadoFicticio = "Amanda Mayumi Kado"
siglaFicticia = "AK"

inserir(siglaFicticia, estadoFicticio)

imprimirTabelaHash()