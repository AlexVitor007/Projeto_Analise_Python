def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Mostrar primeiros clientes")
        print("2. Mostrar pedidos")
        print("3. Gráfico de vendas")
        print("4. Análises Temporais de Preço e Estoque")
        print("5. Sair")

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
            print("Saindo...")
            break
