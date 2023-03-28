class Carros:
    def __init__(self, marca='Honda', modelo='Civic',
     ano_fabricacao=2022, cor='Preto', placa='ABC-1234',
     proprietario='Pedro', qtd_tanque=50):
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.cor = cor
        self.placa = placa
        self.proprietario = proprietario
        self.qtd_tanque = qtd_tanque

    def __str__(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nAno Fabricacao: {self.ano_fabricacao}\nCor: {self.cor}\nPlaca: {self.placa}\nProprietario: {self.proprietario}\nQtd Tanque: {self.qtd_tanque}'
       
carro1 = Carros()
print(carro1)
