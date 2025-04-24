from produtos import produtos
from erros import ProdutoInexistenteError

carrinho = {}

def adicionar_carrinho():
    try:
        prod = input("Qual produto? ")
        if prod not in produtos:
            raise ProdutoInexistenteError(prod)

        qtd = int(input("Quantidade: "))
        if qtd <= 0:
            raise ValueError("Quantidade deve ser maior que zero.")

        if prod in carrinho:
            carrinho[prod] += qtd
        else:
            carrinho[prod] = qtd

    except ProdutoInexistenteError:
        print(f"Erro")
    except ValueError:
        print(f"Erro")
    except Exception:
        print(f"Erro inesperado:")
    else:
        print("Produto adicionado com sucesso.")
    finally:
        print(" Fim da tentativa de adicionar produto.")

def mostrar_carrinho():
    from produtos import produtos
    print("\n Carrinho:")
    total = 0
    for p in carrinho:
        preco = produtos[p] * carrinho[p]
        print(f"{p} -> {carrinho[p]} x R${produtos[p]:.2f} = R${preco:.2f}")
        total += preco
    print(f"Total: R${total:.2f}")
    return total
