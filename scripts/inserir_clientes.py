import mysql.connector

def inserir_cliente_mysql():
    # Coleta os dados principais
    nome = input("Nome da Empresa: ")
    sobrenome = input("Sobrenome do Contato: ")
    primeiro_nome = input("Primeiro Nome do Contato: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    cidade = input("Cidade: ")
    codigo_postal = input("Código Postal: ")
    pais = input("País: ")

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database="classicmodels"
        )

        cursor = conexao.cursor()

        # Obter o próximo ID
        cursor.execute("SELECT MAX(customerNumber) FROM customers")
        max_id = cursor.fetchone()[0]
        novo_id = (max_id or 0) + 1

        # Inserção completa com campos obrigatórios
        query = """
        INSERT INTO customers (
            customerNumber, customerName, contactLastName,
            contactFirstName, phone, addressLine1,
            city, postalCode, country, salesRepEmployeeNumber, creditLimit
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            novo_id, nome, sobrenome, primeiro_nome, telefone, endereco,
            cidade, codigo_postal, pais, 1002, 50000.00  # valores padrão
        )

        cursor.execute(query, valores)
        conexao.commit()

        print(f"\n✅ Cliente inserido com sucesso com ID {novo_id}!")

    except mysql.connector.Error as e:
        print(f"❌ Erro ao inserir cliente: {e}")

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
