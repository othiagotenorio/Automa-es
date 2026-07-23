import os
from PIL import Image

# Configuração dos diretórios
PASTA_ENTRADA = './imagens_originais'
PASTA_SAIDA = './imagens_convertidas'
QUALIDADE_WEBP = 80  # Qualidade da imagem WebP (0 a 100). 80 é o equilíbrio ideal.

# Extensões de imagem suportadas
EXTENSOES_SUPORTADAS = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')

def converter_imagens():
    # Cria as pastas caso não existam
    if not os.path.exists(PASTA_ENTRADA):
        os.makedirs(PASTA_ENTRADA)
        print(f"Pasta '{PASTA_ENTRADA}' criada. Coloque suas imagens nela e rode o script novamente.")
        return

    if not os.path.exists(PASTA_SAIDA):
        os.makedirs(PASTA_SAIDA)

    # Lista todos os arquivos da pasta de entrada
    arquivos = os.listdir(PASTA_ENTRADA)
    imagens = [f for f in arquivos if f.lower().endswith(EXTENSOES_SUPORTADAS)]

    if not imagens:
        print(f"Nenhuma imagem encontrada na pasta '{PASTA_ENTRADA}'.")
        print("Cole suas imagens (.jpg, .png, etc.) nessa pasta e execute o script novamente.")
        return

    print(f"Encontradas {len(imagens)} imagens para converter...\n")

    convertidas = 0
    erros = 0

    for i, nome_arquivo in enumerate(imagens, 1):
        caminho_origem = os.path.join(PASTA_ENTRADA, nome_arquivo)
        nome_base = os.path.splitext(nome_arquivo)[0]
        caminho_destino = os.path.join(PASTA_SAIDA, f"{nome_base}.webp")

        try:
            with Image.open(caminho_origem) as img:
                # Converte imagens RGBA/P para RGB se necessário para garantir compatibilidade
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGBA")
                else:
                    img = img.convert("RGB")

                # Salva no formato WebP
                img.save(caminho_destino, 'WEBP', quality=QUALIDADE_WEBP, optimize=True)
                print(f"[{i}/{len(imagens)}] Convertida com sucesso: {nome_arquivo} -> {nome_base}.webp")
                convertidas += 1
        except Exception as e:
            print(f"[{i}/{len(imagens)}] ERRO ao converter {nome_arquivo}: {e}")
            erros += 1

    print("\n" + "="*40)
    print(f"CONVERSÃO CONCLUÍDA!")
    print(f"Sucesso: {convertidas} imagem(ns)")
    if erros > 0:
        print(f"Falhas: {erros} imagem(ns)")
    print(f"As imagens convertidas estão na pasta: {PASTA_SAIDA}")
    print("="*40)

if __name__ == '__main__':
    converter_imagens()
