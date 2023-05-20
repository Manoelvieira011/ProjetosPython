class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Tarefa adicionada com sucesso!")

    def edit_task(self, index, new_task):
        if index >= 0 and index < len(self.tasks):
            self.tasks[index] = new_task
            print("Tarefa editada com sucesso!")
        else:
            print("Índice inválido!")

    def delete_task(self, index):
        if index >= 0 and index < len(self.tasks):
            del self.tasks[index]
            print("Tarefa excluída com sucesso!")
        else:
            print("Índice inválido!")

    def display_tasks(self):
        print("Lista de tarefas:")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")


def main():
    todo_list = TodoList()

    while True:
        print("\n===== Aplicativo de Lista de Tarefas =====")
        print("1. Adicionar tarefa")
        print("2. Editar tarefa")
        print("3. Excluir tarefa")
        print("4. Exibir tarefas")
        print("0. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            task = input("Digite a nova tarefa: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Digite o índice da tarefa a ser editada: ")) - 1
            new_task = input("Digite a nova descrição da tarefa: ")
            todo_list.edit_task(index, new_task)
        elif choice == "3":
            index = int(input("Digite o índice da tarefa a ser excluída: ")) - 1
            todo_list.delete_task(index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "0":
            print("Encerrando o aplicativo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()

