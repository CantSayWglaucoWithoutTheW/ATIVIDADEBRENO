class ProdutoInexistenteError(Exception):
    def __init__(self, produto):
        super().__init__(f"Produto '{produto}' não encontrado.")

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, total):
        super().__init__(f"Saldo insuficiente: R${saldo:.2f} disponível para um total de R${total:.2f}.")

class PagamentoV(Exception):
    def __init__(self):
        super().__init__("Não da pra fazer o pagamento: o carrinho está vazio.")  