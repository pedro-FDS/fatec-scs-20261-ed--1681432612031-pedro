'''*---------------------------------------------------------*
* Fatec São Caetano do Sul                                   *
* Atividade B1-1                                             *
* Autor: 1681432612031 - Pedro Henrique Ferreira da Silva    *
* Objetivo: código sobre o catálogo de filmes em python      *
* data: 24/02/2026                                           *
*------------------------------------------------------------*
'''

catalogo = {}

def adicionar_filme ( id_filme , titulo , diretor ) :
 if id_filme in catalogo:
    print ("Esse ID já está cadastrado")

 else: catalogo[id_filme] = {
            "titulo": titulo,
            "diretor": diretor
 }
 print("Filme adicionado com sucesso!!")


def buscar_filme ( id_filme ) :
   filme = catalogo.get(id_filme)

   if id_filme not in catalogo:
    print ("Esse ID não está cadastrado")   

   else:
    print("Titulo:", filme["titulo"])
    print("Diretor:", filme["diretor"])

def remover_filme ( id_filme ) : 
  if id_filme in catalogo:
        catalogo.pop(id_filme)
        print("Filme removido com sucesso!")
  else:
        print("Esse ID não está cadastrado")

def listar_todos () :
   if not catalogo:
      print ("\nO catalogo está vazio .")
   else :
      print ("\n- - - Listagem de Filmes ---")
      
   for id_f , dados in catalogo . items () :
      print (f"ID: { id_f } | Titulo : { dados ['titulo']} | Diretor : { dados [ 'diretor' ]}")

 # Parte para teste

adicionar_filme(1, "Interestelar", "Christopher Nolan")
adicionar_filme(2, "Matrix", "Lana Wachowski")

print("\nBuscando filme ID 1:")
buscar_filme(1)

print("\nListando todos os filmes:")
listar_todos()

print("\nRemovendo filme ID 2:")
remover_filme(2)

print("\nListando novamente:")
listar_todos()