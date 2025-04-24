from produtos import mostrar_produtos
from carrinho import adicionar_carrinho, mostrar_carrinho
from pagamento import pagar

saldo = 10.0  

while True:
    print("\n1. Ver produtos")
    print("2. Adicionar produto")
    print("3. Ver carrinho")
    print("4. Pagar")
    print("5. Sair")

    op = input("Escolhe uma opção de 1 a 5: ")
    if op == '1':
        mostrar_produtos()
    elif op == '2':
        adicionar_carrinho()
    elif op == '3':
        mostrar_carrinho()
    elif op == '4':
        saldo = pagar(saldo)
    elif op == '5':
        print("Valeu, tchau.")
        break
    else:
        print("Opção errada")