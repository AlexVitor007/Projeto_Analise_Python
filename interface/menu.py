from src.mongo_manager import MongoManager

# Instancia o gerenciador de conexão e operações com MongoDB
mongo = MongoManager()

def menu():
    """
    
    Exibe o menu principal de interação com o usuário e executa funções
    de acordo com a opção selecionada.

    Funcionalidades disponíveis:
    1. Visualizar clientes da base MySQL.
    2. Visualizar pedidos da base MySQL.
    3. Gerar gráfico de vendas.
    4. Acessar análises temporais (preço e estoque).
    5. Inserir novo cliente na base MySQL.
    6. Adicionar comentário e imagem de cliente no MongoDB.
    7. Listar comentários de cliente armazenados no MongoDB.
    8. Encerrar o programa.
    
    """
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Mostrar clientes")
        print("2. Mostrar pedidos")
        print("3. Gráfico de vendas")
        print("4. Análises Temporais de Preço e Estoque")
        print("5. Inserir novo cliente")
        print("6. Adicionar comentário de cliente (MongoDB)")
        print("7. Listar comentários de cliente (MongoDB)")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Importa e exibe os primeiros 25 clientes da base MySQL
            from scripts.importar_mysql import carregar_clientes
            print(carregar_clientes().head(25))

        elif opcao == "2":
            # Importa e exibe os primeiros 25 pedidos da base MySQL
            from scripts.importar_mysql import carregar_pedidos
            print(carregar_pedidos().head(25))

        elif opcao == "3":
            # Gera e exibe gráfico de vendas com base nos dados históricos
            from visualizacoes.tendencias import gerar_grafico
            gerar_grafico()

        elif opcao == "4":
            # Acessa o submenu de análises temporais de vendas, preços e estoque
            from main import menu_analise_temporal
            menu_analise_temporal()

        elif opcao == "5":
            # Importa e executa a função para inserir novo cliente via terminal
            from scripts.inserir_clientes import inserir_cliente_mysql
            inserir_cliente_mysql()

        elif opcao == "6":
            # Coleta dados do cliente e insere comentário e imagem no MongoDB
            numero = int(input("Número do cliente: "))
            texto = input("Comentário: ")
            imagem = input("Caminho da imagem (ou Enter para ignorar): ").strip()
            imagem = imagem if imagem else None
            mongo.adicionar_comentario(numero, texto, imagem)
            print("Comentário adicionado com sucesso!")

        elif opcao == "7":
            # Busca e exibe comentários de um cliente no MongoDB
            numero = int(input("Número do cliente: "))
            comentarios = mongo.listar_comentarios(numero)
            if comentarios:
                for c in comentarios:
                    print(f"\nData: {c['data']}\nTexto: {c['texto']}")
                    if 'imagem_base64' in c:
                        print("Imagem: [base64 codificada]")
            else:
                print("Nenhum comentário encontrado.")

        elif opcao == "8":
            # Encerra o loop e o programa
            print("Saindo...")
            break
