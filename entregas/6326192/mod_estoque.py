def cadastrar_item(nome: str, quantidade: int, preco_unitario: float) -> dict:
    """Retorna os dados de um item do estoque."""
    return {
        "nome": nome,
        "quantidade": quantidade,
        "preco_unitario": preco_unitario,
    }

def calcular_valor_estoque(itens: list) -> float:
    """Retorna o valor total de todos os itens do estoque."""
    return sum(
        item["quantidade"] * item["preco_unitario"]
        for item in itens
    )


def listar_itens_em_falta(itens: list, minimo: int) -> list:
    """Retorna os itens cuja quantidade e menor que o minimo."""
    return [
        item
        for item in itens
        if item["quantidade"] < minimo
    ]

