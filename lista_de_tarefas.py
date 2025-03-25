toDo = []

def adicionar():
   
    while True:
        tarefa = input("Adicione a próxima tarefa: ").lower()
        toDo.append({

            'tarefas':tarefa,
            'status':'em andamento'

            })
        print("\n========= >>> Nova tarefa adicionada! <<< =========\n")
        parada = input(">>> Deseja adicionar mais uma tarefa? [S] ou [N] <<<\n").lower()
        if parada == 'n':
            break


    
def listar_tarefas():

    if len(toDo) == 0:
        print(">>>>> Não há tarefas! <<<<<")

    else:
        print("\n================= >>>>> SUAS TAREFAS <<<<< ==================")
        for tarefa in toDo:
           
            print("\nA tarefa: ",tarefa['tarefas']," está: ",tarefa['status'])
        

        
def tarefa_status():

    if len(toDo) == 0:
        print(">>>>> Não há tarefas na lista <<<<<")
    else:
        print("======================== Lista de Tarefas ========================")
        for tarefa in toDo:
            print('Tarefa: ' + tarefa['tarefas'] + ' Status: ' + tarefa['status'])
        print("==================================================================")
        concluida = input("Digite a tarefa concluida com base na lista.\n").lower()
        for tarefa in toDo:
            if concluida in tarefa['tarefas']:
                tarefa['status'] = 'concluida'
        print("\n=========Tarefa concluida!=========")

            
def remover_uma_tarefa():
    if len(toDo) == 0:
        print(">>>>>> Não tarefas para serem exluidas! <<<<<<")
    else:
        print("======================== Lista de Tarefas ========================")
        for tarefa in toDo:
            print('Tarefa: ' + tarefa['tarefas'] + ' | Status: ' + tarefa['status'])
        print("==================================================================")
        removida = input("Qual a tarefa que deseja remover da lista? ").lower()
        for tarefa in toDo:
         if removida in tarefa['tarefas']:
            toDo.remove(tarefa)
        print("\n=========Tarefa excluida!=========")
       
    
def remover_tudo():
    toDo[:] = [tarefa for tarefa in toDo if tarefa['status'] != 'concluida']
    
            
