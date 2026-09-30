import logging
import pandas as pd

logging.basicConfig(level=logging.INFO)

def importar_notas(caminho: str) -> float:
    try:
        df = pd.read_csv(caminho)
        for _, row in df.iterrows():
            logging.info(f"Nota lida: {row['nota']}")
        total = df['valor'].sum()
        logging.info(f"Total faturado: {total}")
        return total
    except FileNotFoundError:
        logging.error("Arquivo não encontrado.")
        return 0.0
    except pd.errors.EmptyDataError:
        logging.error("Arquivo CSV está vazio.")
        return 0.0
    finally:
        logging.info("Tentativa de importação concluída.")

if __name__ == "__main__":
    importar_notas("notas.csv")
