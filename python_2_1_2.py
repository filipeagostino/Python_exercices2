class Carros:
    marca = 'Honda'
    modelo = 'Civic'
    ano_fabricacao = 2022
    cor = 'Preto'
    placa = 'ABC-1234'
    proprietario = 'Cleiton'
    qtd_tanque = 50

    def __str__(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nAno Fabricacao: {self.ano_fabricacao}\nCor: {self.cor}\nPlaca: {self.placa}\nProprietario: {self.proprietario}\nQtd Tanque: {self.qtd_tanque}'
       
carro = Carros()
print(carro)
