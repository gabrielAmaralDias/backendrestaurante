from catalogo.motocicletas import Motocicletas
class Vendedor:
    cadastros = []
    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
        self.vendas = []
        self.produtos_vendidos = []
        self.__class__.cadastros.append(self)
    def __str__(self):
         return f'Nome:{self.nome}| Matricula:{self.matricula} | Produtos Vendidos {self.produtos_vendidos}'
        
   
    def listar_vendedor():
        for i , item in enumerate(Vendedor.cadastros):
            print(f'{i} - {item}')
    @classmethod
    def encontar_vendedor(self,matricula):
        for vendedor in self.cadastros:
            if vendedor.matricula == matricula:
                return vendedor
            
        return None

    def adc_vendas(self):
        Motocicletas.listar_motocicletas()
        try:
            num = int(input('Digite O Numero de Vendas:'))
            for x in range(num):
                moto = int(input('Digite O Numero da Moto desejada:'))
                if 0 <= moto <= len(Motocicletas.motocicletas):
                    moto_vendida = Motocicletas.motocicletas[moto]
                    self.produtos_vendidos.append(moto_vendida)
                else:
                    print('Indice Não Encontrado')
        except ValueError:
            print('Entrada invalida, digite Um numero Inteiro')
        


usur = Vendedor('Gabriel Amaral','GA26734')
user1 = Vendedor('Amanda Dias', 'Amand2025')
user3 = Vendedor('Marlon Garcia' , 'Mar2020')
op = ''
while op != 0:
    op = int(input('''Digite a Opção
                  [1] - Adcionar venda
                   2 - Listar Vendedores
                   [3] - Listar Vendas Do Vendedor
                   [0] - Sair '''))
    match op:
        case 0 :
            print('Programa Finalizado')
            break
        case 1:
            matricula = input('Digite A matricula do Funcionario')
            vendedor_selecionado = Vendedor.encontar_vendedor(matricula)
            vendedor_selecionado.adc_vendas()
        case 2:
            Vendedor.listar_vendedor()
        case 3:
            v = int(input('Digite O Vendedor que Você deseja Selecionar'))
            vendedor = Vendedor.cadastros[v]
            print((f'Vendedor : {vendedor.nome}\nVendas:'))
            for moto in vendedor.produtos_vendidos:
                print(moto)
            




    
  



    





    