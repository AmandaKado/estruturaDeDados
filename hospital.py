class Paciente: 
    def __init__(self, numero, cor): 
        self.numero = numero
        self.cor = cor
        self.proximo = None

contador = None
contadorVerde = 1
contadorAmarelo = 201

def inserirVerde(paciente):
    global contador
    atual = contador
    
    while atual.proximo is not None: 
        atual = atual.proximo
    atual.proximo = paciente
    
def inserirAmarelo(paciente):
    global contador

    if contador.cor == "V":
        paciente.proximo = contador
        contador = paciente
        return
    
    atual = contador
    
    while atual.proximo is not None and atual.proximo.cor == "A":   
        atual = atual.proximo
        
    paciente.proximo = atual.proximo
    atual.proximo = paciente
    
    def inserirCor():
        global contadorVerde, contadorAmarelo, contador
        
        cor = input("Digite a cor (V para verde, A para amarelo): ").strip().upper()
        
        if cor != "V" and cor != "A":
            print("Cor inválida. Digite apenas 'V' ou 'A'!")
            return
        elif cor == "V":
            numero = contadorVerde
            contadorVerde += 1
        else:
            numero = contadorAmarelo
            contadorAmarelo += 1
            
        novoPaciente = Paciente(numero, cor)

        if contador is None: 
            contador = novoPaciente
            print(f"Paciente {novoPaciente.numero} com cor {novoPaciente.cor} inserido na fila.") 
        else:
            if cor == "V":
                inserirVerde(novoPaciente)
            else:
                inserirAmarelo(novoPaciente)
            print(f"Paciente {novoPaciente.numero}-{novoPaciente.cor} inserido na fila.")