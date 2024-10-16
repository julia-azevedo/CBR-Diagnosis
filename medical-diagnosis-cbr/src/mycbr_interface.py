# mycbr_interface.py
import subprocess
import os

MYCBR_PATH = "mycbr/mycbr-x.x.x/mycbr.jar"  # Ajuste para o caminho correto do seu MyCBR

def iniciar_my_cbr(caminho_base_casos):
    """Inicia o MyCBR com a base de casos especificada."""
    try:
        subprocess.run(["java", "-jar", MYCBR_PATH, caminho_base_casos], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao iniciar o MyCBR: {e}")
