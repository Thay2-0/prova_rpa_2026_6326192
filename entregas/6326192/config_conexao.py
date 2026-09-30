def main():
    ENDPOINT_URL = "https://api.example.com"
    PORTA = 443
    TAXA_AMOSTRAGEM = 5.0
    USA_HTTPS = True

    parametros = {
        "ENDPOINT_URL": ENDPOINT_URL,
        "PORTA": PORTA,
        "TAXA_AMOSTRAGEM": TAXA_AMOSTRAGEM,
        "USA_HTTPS": USA_HTTPS
    }
    
    for chave, valor in parametros.items():
        print(f"{chave}: {valor} (tipo: {type(valor).__name__})")


if __name__ == "__main__":
    main()
