class Receita:
    def __init__(self, nome, ingredientes, preparo):
        self.nome = nome
        self.ingredientes = ingredientes
        self.preparo = preparo

    def exibir_receita(self):
        print(f"Receita de {self.nome}")
        print("Ingredientes:")
        for ingrediente, quantidade in self.ingredientes.items():
            print(f"{ingrediente}: {quantidade}g")
        print("Modo de preparo:")
        print(self.preparo)

class Cafe(Receita):
    pass  # Pode adicionar métodos específicos para café se necessário

class Almoco(Receita):
    def ajustar_ingredientes(self, ingrediente, nova_quantidade):
        if ingrediente in self.ingredientes:
            self.ingredientes[ingrediente] = nova_quantidade
        else:
            print(f"{ingrediente} não encontrado na receita.")

class Lanche(Receita):
    pass  # Métodos específicos para lanche

class Janta(Receita):
    pass  # Métodos específicos para janta

class LivroDeReceitas:
    def __init__(self):
        self.receitas = {'café': [], 'almoço': [], 'lanche': [], 'janta': []}

    def adicionar_receita(self, momento, receita):
        if momento in self.receitas:
            self.receitas[momento].append(receita)
        else:
            print("Momento da refeição inválido.")

    def listar_receitas(self, momento):
        for receita in self.receitas.get(momento, []):
            receita.exibir_receita()
