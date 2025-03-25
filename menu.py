import lista_de_tarefas as lista



while True:
    
    print()
    print("=======================TO DO LIST =======================")
    print("\nDigite [1] para adicionar uma tarefa")
    print("Digite [2] para lista as taferas")
    print("Digite [3] para concluir uma tarefa")
    print("Digite [4] para remover qualquer tarefa")
    print("Digite [5] para remover todas as tarefas concluidas")
    print("Digite [6] para SAIR")
    print("\n=======================================================")
    opcao = input("\nESCOLHA UMA OPÇÃO: ")
    
    if opcao == '1':
        lista.adicionar()
    elif opcao == '2':
        lista.listar_tarefas()
    elif opcao == '3':
        lista.tarefa_status()
    elif opcao == '4':
        lista.remover_uma_tarefa()
    elif opcao == '5':
        lista.remover_tudo()
    elif opcao == '6':
        print("SAINDO")
        break
    else:
        print("OPÇÃO INVÁLIDA!")