class MyFunctions:
    def __init__(self):
        ...

    def line(self, tam=30):
        print('-'*tam)

    def bd(self):
        bank = {'hello': ''}

        return bank
    
    def listMenu(self, items=''):
        
        for pos, option in enumerate(items):
            print(f'{pos} - {option}')
    
    def menu(self):
        
        self.line()

        self.listMenu(['Close program.', 'Insert new product.', 'Withdraw a Product.', 'Seach by Product.'])

        self.line()


        command = int(input('Type your choice : '))

        print('\n')

        return command
    

    def insert(self):
        while True:

            self.line()
            self.listMenu(['First', 'Second', 'Three'])
            self.line()

            product = input('Insert the name by product : ')

            print(f'\n{product} foi adicionado a lista !\n')

            break


myFunctions = MyFunctions()