
class Motocicletas():
    motocicletas = []
    def __init__(self,modelo,ano,valor,cilidrada,quantidade):
        self.modelo= modelo
        self.ano = ano
        self.valor = valor 
        self.cilidrada = cilidrada
        self.quantidades = quantidade
        self.__class__.motocicletas.append(self)
    def __str__(self):
        return f'Modelo: {self.modelo} - Ano: {self.ano} - Valor:{self.ano} - Cilindrada: {self.cilidrada} - Quantidade: {self.quantidades} '
    def listar_motocicletas():
        for i,moto in enumerate(Motocicletas.motocicletas):
            print(f'{i} - {moto}')
moto = Motocicletas('CB Fan', 2020,21.987,160,10)
moto2 = Motocicletas('Fazer ', 2025,19.875,250,5)
moto3 = Motocicletas('African Twin ', 2025,57.900,1000,2)
moto4 = Motocicletas('PCX ', 2021,24.567,160,25)


