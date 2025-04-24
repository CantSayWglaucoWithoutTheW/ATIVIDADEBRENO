
README.txt – Sistema de Loja Virtual com Tratamento de Erros em Python


O sistema de loja virtual tem um menu com 5 opções sendo elas:


1. Ver produtos
2. Adicionar produto
3. Ver carrinho
4. Pagar
5. Sair

O código foi divido em 6 módulos sendo eles:

carrinho.py
erros.py
main.py
pagamento.py
produtos.py 
readme.txt
  
Para que essas opções não tenham erros à medida que o utilizador usa elas foi feito o módulo “erros.py”.


Dentro dele temos o seguinte:

class ProdutoInexistenteError(Exception):
    def __init__(self, produto):
        super().__init__(f"Produto '{produto}' não encontrado.")

Este aqui é usado na opção 2 “Adicionar produto” feito para avisar o utilizador de que ele não escreveu o nome do produto corretamente e/ou o produto não existe.



class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, total):
        super().__init__(f"Saldo insuficiente: R${saldo:.2f} disponível para um total de R${total:.2f}.")

Este aqui é usado na opção 4 “pagamento” feito para avisar o utilizador de que ele não tem o saldo necessário para realizar a compra. O utilizador tem um saldo de 10 toda vez que ele inicia o sistema no terminal.



class PagamentoV(Exception):
    def __init__(self):
        super().__init__("Não da pra fazer o pagamento: o carrinho está vazio.") 

Este aqui é usado na opção 4 “pagamento” feito para avisar o utilizador de que ele não tem itens no carrinho para realizar a compra. 

