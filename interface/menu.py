def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Mostrar primeiros clientes")
        print("2. Mostrar pedidos")
        print("3. Gráfico de vendas")
        print("4. Análises Temporais de Preço e Estoque")
        print("5. Inserir novo cliente")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            from scripts.importar_mysql import carregar_clientes
            print(carregar_clientes().head(15))

        elif opcao == "2":
            from scripts.importar_mysql import carregar_pedidos
            print(carregar_pedidos().head(15))

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
            print("Saindo...")
            break
