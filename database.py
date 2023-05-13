import time

class DB:
    def __init__(self):
        self.bd = {'Limão' : 12.4, 'Café' : 8.50}


    def insert_bd(self, product='', price=0):
        self.bd[product] = price

        print(f'\n{product} added to list !\n')


    def withdraw_bd(self, item='', var=False):      
        
        for k in self.bd.keys():
            
            if k == item:
                print(f'\nO item {k} foi ENCONTRADO !\n')
                time.sleep(1.5)
                self.bd.pop(k, None)
                print(f'\nO item {k} foi REMOVIDO !\n')
                
                return None
        
        print(f'\nO produto {item} NÃO foi encontrado no estoque!')


    def search_bd(self, item):
        for k in self.bd.keys():

            if k == item:
                print(f'\nO produto {k} foi ENCONTRADO no estoque!\n')
                time.sleep(1.5)
                
                return None
        
        print(f'\nO produto {item} NÃO foi encontrado no estoque!')


    def list_bd(self):
        for k, v in self.bd.items():
            print(f'Product : {k} | Price : {v}')

        print()

database_obj = DB()
