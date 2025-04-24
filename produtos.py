produtos = {
    'banana': 2.00,
    'maçã': 2.00,
    'pão': 1.00,
    'leite': 3.00
}

def mostrar_produtos():
    print("\nProdutos disponíveis:")
    for p in produtos:
        print(p, "R$", produtos[p])
        