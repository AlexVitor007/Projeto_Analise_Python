import mysql.connector

def inserir_cliente_mysql():
    # Solicita ao usuário os dados principais para o cliente
    nome = input("Nome da Empresa: ")
    sobrenome = input("Sobrenome do Contato: ")
    primeiro_nome = input("Primeiro Nome do Contato: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    cidade = input("Cidade: ")
    codigo_postal = input("Código Postal: ")
    pais = input("País: ")

    try:
        # Estabelece conexão com o banco MySQL ClassicModels
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database="classicmodels"
        )

        cursor = conexao.cursor()

        # Consulta para obter o maior ID atual dos clientes
        cursor.execute("SELECT MAX(customerNumber) FROM customers")
        max_id = cursor.fetchone()[0]
        novo_id = (max_id or 0) + 1  # Define o novo ID incrementado

        # Query SQL para inserir um novo cliente com todos os campos obrigatórios
        query = """
        INSERT INTO customers (
            customerNumber, customerName, contactLastName,
            contactFirstName, phone, addressLine1,
            city, postalCode, country, salesRepEmployeeNumber, creditLimit
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Valores para a query, incluindo valores padrão para salesRepEmployeeNumber e creditLimit
        valores = (
            novo_id, nome, sobrenome, primeiro_nome, telefone, endereco,
            cidade, codigo_postal, pais, 1002, 50000.00
        )

        # Executa o comando de inserção no banco
        cursor.execute(query, valores)

        # Confirma a transação no banco de dados
        conexao.commit()

        print(f"\n✅ Cliente inserido com sucesso com ID {novo_id}!")

    except mysql.connector.Error as e:
        # Trata possíveis erros na inserção
        print(f"❌ Erro ao inserir cliente: {e}")

    finally:
        # Fecha cursor e conexão se ainda estiverem abertas
        if conexao.is_connected():
            cursor.close()
            conexao.close()
