import tkinter as tk
from tkinter import ttk, scrolledtext

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

    def __init__(self):
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

class RecipeApp:
    def __init__(self, master, livro):
        self.master = master
        self.livro = livro  # Instância do Livro de Receitas
        master.title("Selecionador de Receitas")

        # Configurações da janela
        master.configure(bg='lightblue')

        # Labels
        self.label = ttk.Label(master, text="Escolha o momento da refeição:")
        self.label.pack(pady=10)

        # Botões para escolher o tipo de refeição
        self.cafe_button = ttk.Button(master, text="Café", command=lambda: self.select_meal('café'))
        self.cafe_button.pack()

        self.almoco_button = ttk.Button(master, text="Almoço", command=lambda: self.select_meal('almoço'))
        self.almoco_button.pack()

        self.lanche_button = ttk.Button(master, text="Lanche", command=lambda: self.select_meal('lanche'))
        self.lanche_button.pack()

        self.janta_button = ttk.Button(master, text="Janta", command=lambda: self.select_meal('janta'))
        self.janta_button.pack()

        # Área de texto para exibir as receitas
        self.text_area = scrolledtext.ScrolledText(master, width=400, height=100)
        self.text_area.pack(pady=10)

    def select_meal(self, meal):
        if meal in self.livro.receitas:
            self.text_area.delete('1.0', tk.END)  # Limpa a área de texto antes de adicionar novo conteúdo
            for receita in self.livro.receitas[meal]:
                self.text_area.insert(tk.END, f"{receita.nome}\nIngredientes:\n")
                for ingrediente, quantidade in receita.ingredientes.items():
                    self.text_area.insert(tk.END, f" - {ingrediente}: {quantidade}g\n")
                self.text_area.insert(tk.END, f"\nModo de preparo:\n{receita.preparo}\n\n")
        else:
            self.text_area.insert(tk.END, "Momento do dia inválido.\n")

def popular_livro(livro):
    # Receitas de café
    livro.adicionar_receita('café', Receita(
        nome='Panqueca',
        ingredientes={'farinha': 100, 'leite': 200, 'ovo': 50},
        preparo='Misture todos os ingredientes e frite as panquecas em uma frigideira até dourar dos dois lados.'
    ))
    livro.adicionar_receita('café', Receita(
        nome='Mingau de Aveia',
        ingredientes={'aveia': 50, 'leite': 250, 'açúcar': 20},
        preparo='Cozinhe a aveia no leite até engrossar, adicione açúcar a gosto.'
    ))
    livro.adicionar_receita('café', Receita(
        nome='Avocado Toast',
        ingredientes={'pão': 50, 'abacate': 100, 'sal': 5, 'pimenta': 2},
        preparo='Amasse o abacate com sal e pimenta, espalhe sobre o pão torrado.'
    ))

    # Receitas de almoço
    livro.adicionar_receita('almoço', Receita(
        nome='Arroz e Feijão com Frango',
        ingredientes={'arroz': 100, 'feijão': 100, 'frango': 200},
        preparo='Cozinhe o arroz e o feijão. Grelhe o frango e sirva tudo junto.'
    ))
    livro.adicionar_receita('almoço', Receita(
        nome='Carne Assada',
        ingredientes={'carne': 300, 'sal': 5, 'pimenta': 5},
        preparo='Tempere a carne com sal e pimenta e asse no forno até o ponto desejado.'
    ))

    # Receitas de lanche
    livro.adicionar_receita('lanche', Receita(
        nome='Shake de Whey',
        ingredientes={'whey protein': 30, 'água': 200, 'banana': 100},
        preparo='Bata todos os ingredientes no liquidificador até ficar homogêneo.'
    ))

    # Receitas de janta
    livro.adicionar_receita('janta', Receita(
        nome='Risoto de Carne em Iscas com Queijo Gorgonzola',
        ingredientes={'arroz arbóreo': 100, 'carne em iscas': 200, 'queijo gorgonzola': 50},
        preparo='Cozinhe o arroz e a carne separadamente, ao final misture o queijo e sirva quente.'
    ))
    livro.adicionar_receita('janta', Receita(
        nome='Massa ao Alho e Óleo',
        ingredientes={'massa': 100, 'alho': 10, 'óleo de oliva': 20},
        preparo='Cozinhe a massa, refogue o alho no óleo e misture com a massa cozida.'
    ))
    livro.adicionar_receita('janta', Receita(
        nome='Massa ao Pesto',
        ingredientes={'massa': 100, 'molho pesto': 50},
        preparo='Cozinhe a massa e misture com o molho pesto pronto.'
    ))
    livro.adicionar_receita('janta', Receita(
        nome='Massa Carbonara',
        ingredientes={'massa': 100, 'bacon': 50, 'ovos': 50, 'queijo parmesão': 20},
        preparo='Cozinhe a massa, frite o bacon, misture os ovos batidos e o queijo com a massa quente.'
    ))
    livro.adicionar_receita('janta', Receita(
        nome='Alfredo’s Pasta',
        ingredientes={'massa': 100, 'creme de leite': 50, 'manteiga': 20, 'queijo parmesão': 20},
        preparo='Cozinhe a massa, misture com creme de leite, manteiga e queijo até formar um molho cremoso.'
    ))

    return livro

def main(): 
    #livro = LivroDeReceitas() #Instancia o livro de receitas 
    livro = popular_livro(LivroDeReceitas())
    #Aqui seria adicionado as receitas ao livro usando livro.adicionar_receita()
    root = tk.Tk()
    app = RecipeApp(root, livro)
    root.mainloop()

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
            for ing, qtd in self.ingredientes.items():
                self.ingredientes[ing] = qtd * fator
        else:
            print("Ingrediente principal não encontrado.")