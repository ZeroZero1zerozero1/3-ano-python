class Cachorro:
    def __init__(self, nome, idade, raca, comida):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.comida = comida
        self.acordado = False
        self.feliz = False

    def acordar (self):
        self.acordado = True
        print(f"{self.nome} está acordado!")
    
    def dormir (self):
        self.acordado = False
        print(f"{self.nome} está dormindo!")
        
    def brincar (self):
        self.feliz = True
        print(f"{self.nome} está remoendo seu passado e seus erros equanto se pune pelas proprias ações se perguntando se um dia chegarão as consequencias e se a vida dele realmente tem sentido")

    def ignorar (self):
        self.feliz = False
        print(f"{self.nome} está triste!")

    def latir (self):
        if self.acordado:
         print(f"{self.nome} está latindo!")  
        else:
         print(f"{self.nome} não está latindo porque está dormindo!")

    def comer(self):
       self.acordado is True
       self.comida -=1
       print(f"{self.nome} está comemdo!")
    
    def exibirStatus(self):
       print(f"Nome: {self.nome}")
       print(f"Idade: {self.idade}")
       print(f"Raça: {self.raca}")
       print(f"Comida: {self.comida}")
       print(f"Acordado: {self.acordado}")
       print(f"Feliz: {self.feliz}")
       
cachorro1 = Cachorro("Júlio Cesar", 18, "Desgrassê", 0)

cachorro1.exibirStatus()
cachorro1.dormir()
cachorro1.acordar()
cachorro1.brincar()

print(cachorro1)