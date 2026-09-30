leituras = [36.5, 41.2, 38.0, 105.0, 37.4, -999.0, 39.1, 40.0]


def monitorar(lista):
    validas = []
    soma = 0.0

    for leitura in lista:
        if leitura > 80.0:
            print(f"[DESCARTE] {leitura} fora da faixa permitida.")
            continue

        if leitura == -999.0:
            print(f"[FALHA] Sensor corrompido: {leitura}.")
            break

        print(f"[OK] Leitura de {leitura}C registrada.")
        validas.append(leitura)
        soma += leitura

    if validas:
        media = soma / len(validas)
        print(f"Quantidade de leituras validas: {len(validas)}")
        print(f"Media: {media:.2f}C")
    else:
        print("Quantidade de leituras validas: 0")
        print("Media: 0.00C")


if __name__ == "__main__":
    monitorar(leituras)