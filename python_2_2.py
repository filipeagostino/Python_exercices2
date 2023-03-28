class Carro1:
    def __init__(self):
        self.marca = 'Honda'
        self.modelo = 'Civic'
        self.ano_fabricacao = 2022
        self.cor = 'Preto'
        self.placa = 'ABC-1234'
        self.proprietario = 'Pedro'
        self.qtd_tanque = 50

    def __str__(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nAno Fabricacao: {self.ano_fabricacao}\nCor: {self.cor}\nPlaca: {self.placa}\nProprietario: {self.proprietario}\nQtd Tanque: {self.qtd_tanque}'


class Carro2:
    def __init__(self):
        self.marca = 'Subaru'
        self.modelo = 'Wrx'
        self.ano_fabricacao = 2016
        self.cor = 'Azul'
        self.placa = 'DEF-5678'
        self.proprietario = 'Jonas'
        self.qtd_tanque = 45

    def __str__(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nAno Fabricacao: {self.ano_fabricacao}\nCor: {self.cor}\nPlaca: {self.placa}\nProprietario: {self.proprietario}\nQtd Tanque: {self.qtd_tanque}'

       
carro1 = Carro1()
print(carro1)
print('-=' * 60)
carro2 = Carro2()
print(carro2)