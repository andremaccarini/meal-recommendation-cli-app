class Receita: 
    """Principal classe do programa"""

    def __init__(self, nome, ingredientes, preparo):
        self.nome = nome
        self.ingredientes = ingredientes 
        self.preparo = preparo 
    
    def exibir_ingredientes(self): 
        print("Ingredientes:")
        for ingrediente, quantidade in self.ingredientes.items(): 
            print(f"{ingrediente}: {quantidade}")
    
    def exibir_preparo(self):
        print("Modo de preparo:")
        print(self.preparo)

class LivroDeReceitas:
    """"Classe das Receitas"""

    def __init__(seld):
        self.receitas = {'café': [], 'almoço': [], 'lanche': [], 'janta': []}

    def adicionar_receita(self, momento, receita):
        self.receitas[momento].append(receita)
    
    def listar_receitas(self, momento):
        if momento in self.receitas:
            print(f"Receitas para {momento}:")
            for i, receita in enumerate(self.receitas[momento], 1):
                print(f"{i}. {receita.nome}")
            return True
        else:
            print("Momento do dia Inválido:")
            return False 
        
#ADICIONA LÓGICA PARA INTERAÇÃO COM USUÁRIO

def main(): 
    livro = LivroDeReceitas() #Instancia o livro de receitas 
    #Aqui seria adicionado as receitas ao livro usando livro.adicionar_receita()

    print("Bem-vindo ao Selecionador de Receita!")
    momento = input("Para qual momento do dia você deseja uma receita? (café, almoço, lanche, janta)")

    if livro.listar_receitas(momento):
        escolha = int(input("Escolha a receita pelo número: ")) - 1 
        if 0 <= escolha < len(livro.receitas[momento]):
            receita = livro.receitas[momento][escolha] 
            receita.exibir_ingredientes()
            receita.exibir_preparo()
        else: 
            print("Número de receita inválido.")
    else:
        print("Opção inválida, por favor reinicie o programa.")

if __name__ == "__main__": 
    main()

#ADICIONA LÓFICA PARA AJUSTAR OS INGREDIENTES

class ReceitaAlmocoJanta(Receita): 
    def ajustar_ingredientes(self, ingrediente_principal, nova_quantidade):
        if ingrediente_principal in self.ingredientes:
            fator = nova_quantidade / self.ingredientes[ingrediente_principal]
            for ing, qtd in self.ingredientes.item():
                self.ingredientes[ing] = qtd * fator
        else:
            print("Ingrediente principal não encontrado.")