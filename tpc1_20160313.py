#SAD TPC1 João Soares 20160313 Informática de Gestão (PL)

esquerda = {'{','(','['}             #mapeamento das chavetas/parenteses/parenteses retos
direita = {'}',')',']'}              #mapeamento das chavetas/parenteses/parenteses retos



S = input("Introduza a string: ")    #solicita a string ao utilizador

def solution(S):                     #função
	counter = 0                      #ajudar a contar o numero de caracteres mapeados.
	
	for char in esquerda:
		counter += S.count(char)
	for char in direita:
		counter -= S.count(char)
		
	if counter == 0 or counter % 1:
		return 1                    #retorna 1 se a String estiver correta
	else:
		return 0                    #retorna 1 se a String estiver correta    

print(str(solution(S)))             #imprime o resultado