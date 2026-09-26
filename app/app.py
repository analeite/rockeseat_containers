import os
import sys
import mysql.connector

# Leitura direta de variáveis de ambiente
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "app_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "app_password")
DB_NAME = os.getenv("DB_NAME", "app_db")
DB_PORT = int(os.getenv("DB_PORT", "3306"))

def conectar():
    try:
        return mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT
        )
    except Exception as e:
        print(f"Erro ao conectar no MySQL ({DB_HOST}): {e}")
        sys.exit(1)

def inicializar_banco():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def menu():
    inicializar_banco()
    
    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Criar Tarefa (Create)")
        print("2. Listar Tarefas (Read)")
        print("3. Atualizar Tarefa (Update)")
        print("4. Deletar Tarefa (Delete)")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        conn = conectar()
        cursor = conn.cursor()

        if opcao == "1":
            titulo = input("Título da tarefa: ")
            cursor.execute("INSERT INTO tarefas (titulo) VALUES (%s)", (titulo,))
            conn.commit()
            print("--> Criado com sucesso!")

        elif opcao == "2":
            cursor.execute("SELECT id, titulo FROM tarefas")
            tarefas = cursor.fetchall()
            print("\n--- Lista de Tarefas ---")
            for t in tarefas:
                print(f"[{t[0]}] {t[1]}")

        elif opcao == "3":
            id_t = input("ID da tarefa para atualizar: ")
            novo_titulo = input("Novo título: ")
            cursor.execute("UPDATE tarefas SET titulo = %s WHERE id = %s", (novo_titulo, id_t))
            conn.commit()
            print("--> Atualizado com sucesso!")

        elif opcao == "4":
            id_t = input("ID da tarefa para deletar: ")
            cursor.execute("DELETE FROM tarefas WHERE id = %s", (id_t,))
            conn.commit()
            print("--> Removido com sucesso!")

        elif opcao == "5":
            cursor.close()
            conn.close()
            print("Saindo...")
            break

        cursor.close()
        conn.close()

if __name__ == "__main__":
    menu()