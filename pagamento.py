from carrinho import carrinho, mostrar_carrinho
from erros import SaldoInsuficienteError, PagamentoV

saldo = 10.0

def pagar(saldo_atual):
    try:
        total = mostrar_carrinho()
        if total == 0:
            raise PagamentoV()

        if total > saldo_atual:
            raise SaldoInsuficienteError(saldo_atual, total)

        saldo_atual = saldo_atual - total
        print("Compra feita! Saldo agora é:", saldo_atual)
        carrinho.clear()

    except SaldoInsuficienteError:
        print("Sem saldo:")
    except PagamentoV:
        print("Carrinho vazio, assim não da pra pagar.")
    finally:
        print("fim do pagamento")

    return saldo_atual