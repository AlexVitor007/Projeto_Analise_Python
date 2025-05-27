from src.mongo_manager import MongoManager
mongo = MongoManager()

def menu():
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
            from scripts.importar_mysql import carregar_clientes
            print(carregar_clientes().head(25))

        elif opcao == "2":
            from scripts.importar_mysql import carregar_pedidos
            print(carregar_pedidos().head(25))

        elif opcao == "3":
            from visualizacoes.tendencias import gerar_grafico
            gerar_grafico()
            
        elif opcao == "4":
            from main import menu_analise_temporal
            menu_analise_temporal()
            
        elif opcao == "5":
            # Importa a função de inserção
            from scripts.inserir_clientes import inserir_cliente_mysql

            # Chama a função para inserir um cliente via teclado
            inserir_cliente_mysql()
            
        elif opcao == "6":
            numero = int(input("Número do cliente: "))
            texto = input("Comentário: ")
            imagem = input("Caminho da imagem (ou Enter para ignorar): ").strip()
            imagem = imagem if imagem else None
            mongo.adicionar_comentario(numero, texto, imagem)
            print("Comentário adicionado com sucesso!")

        elif opcao == "7":
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
            print("Saindo...")
            break
