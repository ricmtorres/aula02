from menu import menu
from cadastro import cadastrar_aluno
from exibicao import exibir_alunos
from calculos import calcular_media

def main():
    alunos = []
    while True:
        opcao = menu()

        if opcao == 1:
            cadastrar_aluno(alunos)
        elif opcao == 2:
            exibir_alunos(alunos)
        elif opcao == 3:
            calcular_media(alunos)
        elif opcao == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida. tente novamente.")

if __name__ == "__main__":
    main()
