from interface.menu import menu
from scripts import analise_temporal

def menu_analise_temporal():
    print("\n=== Análises Temporais ===")
    print("1 - Histórico de Preços por Produto")
    print("2 - Estoque Médio ao Longo do Tempo")
    print("3 - Média Móvel de Vendas (30 dias)")
    print("4 - Sazonalidade Trimestral")
    print("5 - Comparativo Anual de Preços e Quantidade")
    escolha = input("Escolha uma opção (1-5): ")

    if escolha == "1":
        analise_temporal.historico_precos()
    elif escolha == "2":
        analise_temporal.estoque_medio_temporal()
    elif escolha == "3":
        analise_temporal.media_movel_vendas()
    elif escolha == "4":
        analise_temporal.sazonalidade_trimestral()
    elif escolha == "5":
        analise_temporal.comparativo_anual()
    else:
        print("Opção inválida.")
if __name__ == "__main__":
    print("=== Sistema Análise ClassicModels ===")
    menu()

