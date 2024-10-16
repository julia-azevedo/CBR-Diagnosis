import pandas as pd
import subprocess

MYCBR_PATH = "mycbr/mycbr-x.x.x/mycbr.jar"  # Ajuste para o caminho correto do seu MyCBR

def carregar_base_de_dados(caminho):
    """Carrega a base de dados de casos médicos a partir de um arquivo CSV."""
    return pd.read_csv(caminho)

def iniciar_my_cbr(caminho_base_casos):
    """Inicia o MyCBR com a base de casos especificada."""
    try:
        # Chama o MyCBR com a base de dados
        subprocess.run(["java", "-jar", MYCBR_PATH, caminho_base_casos], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao iniciar o MyCBR: {e}")

def recuperar_diagnostico(sintomas, base_de_dados):
    """Recupera o diagnóstico com base nos sintomas informados."""
    # Separar os sintomas informados pelo usuário
    sintomas_usuario = [sintoma.strip().lower() for sintoma in sintomas.split(",")]

    # Filtrar os resultados da base de dados que contenham todos os sintomas informados
    def checar_sintomas(sintomas_base):
        sintomas_base = [sintoma.strip().lower() for sintoma in sintomas_base.split(",")]
        return all(sintoma in sintomas_base for sintoma in sintomas_usuario)

    resultados = base_de_dados[base_de_dados['Sintomas'].apply(checar_sintomas)]

    # Se não encontrar na base de dados local, tenta MyCBR
    if resultados.empty:
        iniciar_my_cbr('data/base_de_casos.csv')  # Ajuste para o caminho correto
        return "Nenhum diagnóstico encontrado na base de dados local. Verifique o MyCBR."
    
    return resultados
