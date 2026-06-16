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
        
def imprimirListaEspera():
    global contador

    if contador is None:
        print("A fila de espera está vazia.")
        return

    else:
        atual = contador
    
    while atual is not None:
        print(f"Paciente {atual.numero} - {atual.cor}")
        atual = atual.proximo

def atenderPaciente():
    global contador

    if contador is None :
        print("Não há pacientes para atender.")
        return

    pacienteAtendido = contador

    contador = contador.proximo

    print(f"Paciente {pacienteAtendido.numero} - {pacienteAtendido.cor} dirigir-se para sala de atendimento.")
    
def menu():
    while True:
        print("\n*** SISTEMA DE TRIAGEM HOSPITALAR ***")
        print("1 – Adicionar paciente à fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar paciente")
        print("4 – Fechar programa")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            inserirCor()
        elif opcao == "2":
            imprimirListaEspera()
        elif opcao == "3":
            atenderPaciente()
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()