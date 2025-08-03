import requests

URL = "http://127.0.0.1:8000/componentes"

# ---------- LISTAR ----------
def listar(endpoint):
    print(requests.get(f"{URL}/{endpoint}").text)

# ---------- CADASTRAR ----------
def cadastrar_teclado():
    modelo = input("Modelo: ")
    interface = input("Interface: ")
    tipo = input("Tipo: ")
    sistemas = input("Sistemas compatíveis (vírgula): ").split(",")
    layout = input("Layout: ")
    descanso = input("Descanso de pulso (s/n): ").lower() == "s"

    teclado = {
        "modelo": modelo,
        "interface": interface,
        "tipo": tipo,
        "sistemas_compativeis": [s.strip() for s in sistemas],
        "layout": layout,
        "descanso_de_pulso": descanso
    }
    print(requests.post(f"{URL}/teclados", json=teclado).text)

def cadastrar_mouse():
    modelo = input("Modelo: ")
    tipo = input("Tipo: ")
    interface = input("Interface: ")
    peso = input("Peso (ou vazio): ")
    dpi = int(input("DPI Máx: "))
    sensor = input("Sensor: ")

    mouse = {
        "modelo": modelo,
        "tipo": tipo,
        "interface": interface,
        "peso": float(peso) if peso else None,
        "dpi_max": dpi,
        "sensor": sensor
    }
    print(requests.post(f"{URL}/mouses", json=mouse).text)

def cadastrar_monitor():
    modelo = input("Modelo: ")
    tamanho = input("Tamanho: ")
    resolucao = input("Resolução: ")
    taxa = input("Taxa de atualização: ")
    tempo = input("Tempo de resposta: ")
    painel = input("Tipo de painel: ")
    entradas = input("Entradas (vírgula): ").split(",")
    ajuste = input("Ajuste altura (s/n): ").lower() == "s"

    monitor = {
        "modelo": modelo,
        "tamanho": tamanho,
        "resolucao": resolucao,
        "taxa_atualizacao": taxa,
        "tempo_resposta": tempo,
        "tipo_painel": painel,
        "entradas": [e.strip() for e in entradas],
        "ajuste_altura": ajuste
    }
    print(requests.post(f"{URL}/monitores", json=monitor).text)

def cadastrar_placa_video():
    modelo = input("Modelo: ")
    fabricante = input("Fabricante: ")
    interface = input("Interface: ")
    resolucoes = input("Resoluções suportadas: ")
    saidas = input("Saídas de vídeo (vírgula): ").split(",")
    tecnologias = input("Tecnologias suportadas (vírgula): ").split(",")
    consumo = int(input("Consumo (W): "))
    alimentacao = input("Alimentação extra (ou vazio): ")

    placa = {
        "modelo": modelo,
        "fabricante": fabricante,
        "interface": interface,
        "resolucoes_suportadas": resolucoes,
        "saidas_video": [s.strip() for s in saidas],
        "suporte_tecnologias": [t.strip() for t in tecnologias],
        "consumo": consumo,
        "alimentacao_extra": alimentacao or None
    }
    print(requests.post(f"{URL}/placas_de_video", json=placa).text)

def cadastrar_fonte():
    modelo = input("Modelo: ")
    fabricante = input("Fabricante: ")
    potencia = int(input("Potência (W): "))
    tipo = input("Tipo: ")
    modularidade = input("Modularidade: ")
    conectores = input("Conectores (vírgula): ").split(",")
    voltagem = input("Voltagem: ")
    protecoes = input("Proteções (vírgula): ").split(",")
    eficiencia = input("Eficiência: ")

    fonte = {
        "modelo": modelo,
        "fabricante": fabricante,
        "potencia": potencia,
        "tipo": tipo,
        "modularidade": modularidade,
        "conectores": [c.strip() for c in conectores],
        "voltagem": voltagem,
        "protecoes": [p.strip() for p in protecoes],
        "eficiencia": eficiencia
    }
    print(requests.post(f"{URL}/fontes", json=fonte).text)

def cadastrar_headset():
    modelo = input("Modelo: ")
    fabricante = input("Fabricante: ")
    conexao = input("Tipo de conexão: ")
    compatibilidade = input("Compatibilidade (vírgula): ").split(",")
    microfone = input("Microfone: ")
    tipo = input("Tipo: ")
    controle = input("Controle de volume: ")

    headset = {
        "modelo": modelo,
        "fabricante": fabricante,
        "tipo_conexao": conexao,
        "compatibilidade": [c.strip() for c in compatibilidade],
        "microfone": microfone,
        "tipo": tipo,
        "controle_volume": controle
    }
    print(requests.post(f"{URL}/headsets", json=headset).text)

def cadastrar_placa_mae():
    modelo = input("Modelo: ")
    fabricante = input("Fabricante: ")
    socket = input("Socket: ")
    chipset = input("Chipset: ")
    formato = input("Formato: ")
    suporte_memoria = input("Suporte memória: ")
    armazenamento = input("Armazenamento (vírgula): ").split(",")
    saidas = input("Saídas de vídeo (vírgula): ").split(",")

    placa = {
        "modelo": modelo,
        "fabricante": fabricante,
        "socket": socket,
        "chipset": chipset,
        "formato": formato,
        "suporte_memoria": suporte_memoria,
        "armazenamento": [a.strip() for a in armazenamento],
        "saidas_video": [s.strip() for s in saidas]
    }
    print(requests.post(f"{URL}/placas_maes", json=placa).text)

# ---------- SUBMENU ----------
def submenu(nome, endpoint, cadastrar_func):
    while True:
        print(f"\n--- {nome} ---")
        print("1 - Listar")
        print("2 - Cadastrar")
        print("3 - Voltar")
        opcao = int(input("Digite a opção: "))
        
        if opcao == 1:
            listar(endpoint)
        elif opcao == 2:
            cadastrar_func()
        elif opcao == 3:
            break

# ---------- MENU PRINCIPAL ----------
def menu_principal():
    while True:
        print("\n=== MENU COMPONENTES ===")
        print("1 - Teclados")
        print("2 - Mouses")
        print("3 - Monitores")
        print("4 - Placas de Vídeo")
        print("5 - Fontes")
        print("6 - Headsets")
        print("7 - Placas Mãe")
        print("8 - Sair")
        opcao = int(input("Digite a opção: "))
        
        if opcao == 1:
            submenu("Teclados", "teclados", cadastrar_teclado)
        elif opcao == 2:
            submenu("Mouses", "mouses", cadastrar_mouse)
        elif opcao == 3:
            submenu("Monitores", "monitores", cadastrar_monitor)
        elif opcao == 4:
            submenu("Placas de Vídeo", "placas_de_video", cadastrar_placa_video)
        elif opcao == 5:
            submenu("Fontes", "fontes", cadastrar_fonte)
        elif opcao == 6:
            submenu("Headsets", "headsets", cadastrar_headset)
        elif opcao == 7:
            submenu("Placas Mãe", "placas_maes", cadastrar_placa_mae)
        elif opcao == 8:
            print("Saindo...")
            break

menu_principal()
