from mod_estoque import (
    cadastrar_item,
    calcular_valor_estoque,
    listar_itens_em_falta,
)


def main():
    itens = [
        cadastrar_item("Arroz", 10, 25.90),
        cadastrar_item("Feijao", 3, 8.50),
        cadastrar_item("Macarrao", 1, 6.75),
    ]

    valor_total = calcular_valor_estoque(itens)

    minimo = 5
    itens_em_falta = listar_itens_em_falta(itens, minimo)

    print(f"Valor total do estoque: R$ {valor_total:.2f}")
    print(f"Itens com quantidade menor que {minimo}:")

    for item in itens_em_falta:
        print(f'- {item["nome"]}: {item["quantidade"]} unidade(s)')


if __name__ == "__main__":
    main()
