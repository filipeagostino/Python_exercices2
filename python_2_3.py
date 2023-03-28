class Carros:
    def __init__(self, marca, modelo, ano_fabricacao, cor, placa, proprietario, qtd_tanque):
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.cor = cor
        self.placa = placa
        self.proprietario = proprietario
        self.qtd_tanque = qtd_tanque

    def __str__(self):
        return f'''Marca: {self.marca}\nModelo: {self.modelo}\nAno Fabricacao: {self.ano_fabricacao}\nCor: {self.cor}\nPlaca: {self.placa}\nProprietario: {self.proprietario}\nQtd Tanque: {self.qtd_tanque}'''
       
carro = Carros('Honda', 'Civic', 2022, 'Preto', 'ABC-1234', 'Claudiosvaldo', 50)
print(carro)