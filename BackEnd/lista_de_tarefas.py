toDo = []

def adicionar():
    tarefa = input("Adicione a próxima tarefa: ")
    toDo.append({'tarefas':tarefa,'status':'em andamento'})
    return toDo
    
def listar():
    if len(toDo) == 0:
        print("Não há tarefas!")
    else:
        print("\n============== SUAS TAREFAS ==============")
        for tarefa in toDo:
           
            print("\nA tarefa: ",tarefa['tarefas']," está: ",tarefa['status'])
        print("\n==========================================")
        
def andamento():
    concluida = input("Qual tarefa foi concluida? ")
    for tarefa in toDo:
        if concluida in tarefa['tarefas']:
            tarefa['status'] = 'concluida'
            
def remover():
    removida = input("Qual a tarefa que deseja remover da lista? ")
    for tarefa in toDo:
        if removida in tarefa['tarefas']:
            toDo.remove(tarefa)
    print("\n=========Tarefa excluida!=========")
       
    
def limpar():
    toDo[:] = [tarefa for tarefa in toDo if tarefa['status'] != 'concluida']
    
            


print("=======================TO DO LIST =======================")
print("\nDigite [1] para adicionar uma tarefa")
print("Digite [2] para lista as taferas")
print("Digite [3] para concluir uma tarefa")
print("Digite [4] para remover qualquer tarefa")
print("Digite [5] para remover todas as tarefas concluidas")
print("Digite [6] para SAIR")
print("\n======================= TO DO LIST =======================")
    
while True:
    
    opcao = input("\nESCOLHA UMA OPÇÃO: ")
    
    if opcao == '1':
        adicionar()
    elif opcao == '2':
        listar()
    elif opcao == '3':
        andamento()
    elif opcao == '4':
        remover()
    elif opcao == '5':
        limpar()
    elif opcao == '6':
        print("SAINDO")
        break
    else:
        print("OPÇÃO INVÁLIDA!")