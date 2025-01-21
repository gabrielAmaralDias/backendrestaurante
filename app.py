import os
restaurantes = []
def mostrar_mensagem(texto):
    os.system('cls')
    linha = '*'  * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print('\n')

def ativar_restaurante():
    '''Essa Função Ativa os Restaurantes que estão desativados '''
    mostrar_mensagem('Alterando Restaurante')
    nome_restaurante = input('Digite O Nome do Restaurante: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O Restaurante foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O Restaurante Não Foi encontrado')

    voltar_aomenu()
def voltar_aomenu():
    '''Essa Função Volta ao Menu Principal'''
    input('Digite uma Tecla Para Voltar ao menu')
    main()
def finalizar():
    os.system('cls')
    print('Finalisando o Programa')
def opcao_inval():
    print('Opção Invalida')
    voltar_aomenu()
def cadastrar_restaurante():
    '''Essa Função Cadastra um Restaurante
    inputs: Nome do Restaurante
    Categoria do restaurante
    
    output: Adciona No dicionario dados_restaurante os inputs acima'''
    os.system('cls')
    mostrar_mensagem('Cadastrando Restaurante')
    nome_restaurante = input('Digite O Nome do Restaurante').strip().upper()
    categoria_restaurante = input('Digite A Categoria do restaurante: ').strip().upper()
    dados_resutarante = {'nome': nome_restaurante.ljust(15), 'categoria': categoria_restaurante.ljust(15),  'ativo': False}
    print('Restaurante Cadastrado com Sucesso')
    restaurantes.append(dados_resutarante)
def listar_restaurante():
    '''Essa Função Lista os Restaurantes '''
    os.system('cls')
    mostrar_mensagem('Listando Restaurantes')
    if restaurantes:
         
         for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria_restaurante = restaurante['categoria']
            ativado = 'Ativado' if restaurante['ativo'] else 'Desativado'             
            print(f' { nome_restaurante}|  {categoria_restaurante }| {ativado}')
    else:
        print('Nenhum restaurante cadastrado.')
    voltar_aomenu()
    
    os.system('cls')
    print(f'A Lista de Restaurantes Cadastrados são : {restaurantes}')
def opcoes():
    '''Essa Função é o Menu de Opções'''
    print('Sabor express\n')
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair \n')  
def resultado(op):
    '''Essa Função Determinar O resultado do usuario'''
    match op:
        case 1:
            cadastrar_restaurante()
        case 2:
            listar_restaurante()
        case 3:
            ativar_restaurante()
        case 4:
            finalizar()
        case _:
            opcao_inval()
    

def main():
     while True:
        os.system('cls')
        opcoes()
        try:
            op = int(input('Escolha uma opção: '))
            resultado(op)
            if op == 4:
                break
        except ValueError:
            opcao_inval()
if __name__ == '__main__':
    main()





