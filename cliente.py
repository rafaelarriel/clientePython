#
#create by Rafael Arriel year2022
#
######################### IMPORTS ########################
import requests
import json
#import http.client


###################### URL's base pra conexão ############
urlbase = "http://192.168.103.27:5000/tarefas" 
#urlbase = "http://localhost:5000/tarefas" 



######################### METODOS ########################

#metodo GET #####################
def GET():
	
	connection = requests.get(urlbase)
	
	json_data = json.loads(connection.text)
	
	print(json.dumps(json_data,indent=2))
	#print(connection.text)
	
#metodo POST ####################
def POST():

	print(" Digite o id: ")
	id = input()
		
	print(" Digite a decrição: ")
	descricao = input()
		
	print(" Digite o prazo: ")
	prazo = input()
		
	print(" Digite se a tarefa está completa ou não")
	print(" Utiliza S pra sim, e N para não: ")
	completa = input()

	if completa == "S" or "s":
		completa = True
	elif completa == "N" or "n":
		completa = False
		
		
	data = { 'id': id, 'descricao':descricao,'prazo':prazo,'completa':completa}
	connection = requests.post(urlbase +"/post/",json=data)
	
	json_data = json.loads(connection.text)
	
	print(json.dumps(json_data,indent=2))
	#print(connection.text)

#metodo GET com ID ##############
def GET_ID():

	print(" Digite o id da tarefa que deseja listar: ")
	id = input()
	
	connection = requests.get(urlbase+"/get/"+id)
	json_data = json.loads(connection.text)
	
	print(json.dumps(json_data,indent=2))
	#print(connection.text)

#metodo DELETE usa ID ###########
def DELETE():

	print(" Digite o id da tarefa que deseja deletar: ")
	id = input() 
	
	connection = requests.delete(urlbase+"/delete/"+id)
		
	print(connection.text)

#metodo PUT usa ID ##############
def PUT():

	print(" Digite o id da tarefa a ser atualizada: ")
	id = input()
		
	print(" Digite a decrição: ")
	descricao = input()
		
	print(" Digite o prazo: ")
	prazo = input()
		
	print(" Digite se a tarefa está completa ou não")
	print(" Utilize S pra sim, e N para não: ")
	completa = input()

	if completa == "S"or "s":
		completa = True
	elif completa == "N" or "n":
		completa = False
		
		
	data = { 'id': id, 'descricao':descricao,'prazo':prazo,'completa':completa}
	connection = requests.put(urlbase+"/put/"+id,json=data)
	
	json_data = json.loads(connection.text)
	
	print(json.dumps(json_data,indent=2))
	#print(connection.text)


######################### "MAIN" ##########################

print(" Olá Bem vindo a API de gerancia de tarefas \n")

print(" Digite algum dos comandos:\n")
print(" 1 para listar as tarefas exitentes")
print(" 2 para cadastrar uma nova tarefa")
print(" 3 para listar alguma tarefa especifica utilizando id")
print(" 4 para deletar alguma tarefa")
print(" 5 para atualizar alguma tarefa")
print(" ex para sair")

op = input()


#rotina principal #####################

while op!= "ex":
	
	
	#GET ##########################
	if op=="1":
		GET()
		print("\n")
		
		
	#POST/ Add ####################
	if op=="2":
		POST()
		print("\n")
	
	
	#GET_ID #######################
	if op=="3":
		GET_ID()
		print("\n")
	
	
	#DELETE #######################
	if op=="4":
		DELETE()
		print("\n")
	
	#PUT/ UPDATE #################
	if op=="5":
		PUT()
		print("\n")
	
		
	#OP INVALIDA##################
	#else:
	
		#print("Opção Invalida")
		
	
	
	#SELECT OP ###################
	
	print(" Digite algum dos comandos:\n")
	print(" 1 para listar as tarefas exitentes")
	print(" 2 para cadastrar uma nova tarefa")
	print(" 3 para listar alguma tarefa especifica utilizando id")
	print(" 4 para deletar alguma tarefa")
	print(" 5 para atualizar alguma tarefa")
	print(" ex para sair")
	
	op = input()
	
print(" !!!Obrigado por usar a API de gerencia de tarefas!!!")
print(" !!!Volte Sempre!!!")
