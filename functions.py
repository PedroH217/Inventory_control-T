from database import database_obj

class MyFunctions:
    def __init__(self):
        ...

    def line(self, tam=30):

        """
            This method causes a line to be genereted, size
            can be passed by parameter.
        """

        print('-'*tam)

    
    def listMenu(self, items=''):
        
        """
            Gera uma lista menu para ser apresentada na tela do usuário.
        """

        self.line()

        for pos, option in enumerate(items):
            print(f'{pos} - {option}')

        self.line()
    
    def menu(self):

        """
            Invoca o menu para ser apresentado na tela e recebe a escolha do 
            usuário.
        """ 

        self.listMenu(['Close program.', 'Insert new product.', 'Withdraw a Product.', 'Seach by Product.'])


        command = int(input('Type your choice : '))

        print('\n')

        return command
    

    def insert(self):

        """
            Tela apresentada para Inserção de informações no 
            banco de dados.
        """

        while True:

            try:
                product_name = str(input('Insert the name by product : ')).capitalize()
                product_price = float(input('Inform the price of the product : '))

                database_obj.insert_bd(product_name, product_price)
                
                break

            except ValueError:
                print('\nProduto deve ser um Nome e preço um Valor numérico\n')

    
    def withdraw(self):

        """
            Tela apresentada para Remoção de produto na tela do
            uauário.
        """

        while True:
            database_obj.list_bd()
            
            srch = str(input('\nName of the product to be removed : '))

            database_obj.withdraw_bd(srch)
            print()
            
            break

    def search(self):

        
        """
            Tela apresentada para o usuário buscando encontrar produtos
            no banco de dados.
        """

        while True:
            srch = str(input('Search for a product : '))

            database_obj.search_bd(srch)

            break


myFunctions = MyFunctions()