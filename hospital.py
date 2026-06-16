class Paciente: 
    def __init__(self, numero, cor): 
        self.numero = numero
        self.cor = cor
        self.proximo = None

primeiroFila = None
contadorVerde = 1
contadorAmarelo = 201

def inserirSemPrioridade(paciente):
    global primeiroFila
    atual = primeiroFila
    
    while atual.proximo is not None: 
        atual = atual.proximo
    atual.proximo = paciente
    
def inserirComPrioridade(paciente):
    global primeiroFila

    if primeiroFila.cor == "V":
        paciente.proximo = primeiroFila
        primeiroFila = paciente
        return
    
    atual = primeiroFila
    while atual.proximo is not None and atual.proximo.cor == "A":   
        atual = atual.proximo
        
    paciente.proximo = atual.proximo
    atual.proximo = paciente
        
def inserir():
    global contadorVerde, contadorAmarelo, primeiroFila

    while True:
        cor = (
            input("\nDigite a cor (V para verde [sem prioridade], A para amarelo [com prioridade]): ")
            .strip()
            .upper()
        )

        if cor == "V" or cor == "A":
            break

        print("\n[ERRO] Cor inválida. Digite apenas 'V' ou 'A'!")

    if cor == "V":
        numero = contadorVerde
        contadorVerde += 1
    else:
        numero = contadorAmarelo
        contadorAmarelo += 1

    novoPaciente = Paciente(numero, cor)

    if primeiroFila is None:
        primeiroFila = novoPaciente
    else:
        if cor == "V":
            inserirSemPrioridade(novoPaciente)
        else:
            inserirComPrioridade(novoPaciente)
            
    print(f"\nPaciente {novoPaciente.numero}-{novoPaciente.cor} inserido na fila.")
        
def imprimirListaEspera():
    global primeiroFila

    if primeiroFila is None:
        print("\nA fila de espera está vazia.")
        return

    atual = primeiroFila
    
    print("_" * 37)
    print("\nPacientes na fila de espera:")
    
    while atual is not None:
        print(f"\nPaciente {atual.numero} - {atual.cor}")
        atual = atual.proximo

def atenderPaciente():
    global primeiroFila

    if primeiroFila is None :
        print("\nNão há pacientes para atender.")
        return

    pacienteAtendido = primeiroFila

    primeiroFila = primeiroFila.proximo

    print(f"\n[Paciente {pacienteAtendido.numero} - {pacienteAtendido.cor}] Por favor dirigir-se para sala de atendimento.")

def menu():
    while True:
        print("_"*37)
        print("\n*** SISTEMA DE TRIAGEM HOSPITALAR ***")
        print("\n1 – Adicionar paciente à fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar paciente")
        print("4 – Fechar programa")
        print("_"*37)
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            inserir()
        elif opcao == "2":
            imprimirListaEspera()
        elif opcao == "3":
            atenderPaciente()
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()