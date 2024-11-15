# Arquivo principal em Python
from models import Ponto
from utils import salvar_dados, carregar_dados

def registrar_entrada():
    nome = input("Digite seu nome: ")
    ponto = Ponto(nome)
    ponto.registrar_entrada()
    salvar_dados(ponto)
    print(f"Entrada registrada para {nome}")

def registrar_saida():
    nome = input("Digite seu nome: ")
    ponto = carregar_dados(nome)
    ponto.registrar_saida()
    salvar_dados(ponto)
    print(f"Saída registrada para {nome}")

def main():
    print("Bem-vindo ao Sistema de Ponto!")
    while True:
        print("\nEscolha uma opção:")
        print("1. Registrar Entrada")
        print("2. Registrar Saída")
        print("3. Sair")
        opcao = input("Escolha a opção (1/2/3): ")
        if opcao == "1":
            registrar_entrada()
        elif opcao == "2":
            registrar_saida()
        elif opcao == "3":
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
