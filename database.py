import time



class DB:

    """
        Class responsible for interacting with the database in dictionary format.
    """

    def __init__(self):
        self.bd = {'Lemon' : 12.4, 'Coffe' : 8.50}


    def insert_bd(self, product='', price=0):

        """
            Insert a product into the database.
        """

        self.bd[product] = price

        print(f'\n{product} added to list !\n')


    def withdraw_bd(self, item='', var=False):  

        """
            Remove a product from the database.
        """    
        
        for k in self.bd.keys():
            
            if k == item:
                print(f'\nThe item {k} WAS found !\n')
                time.sleep(1.5)
                self.bd.pop(k, None)
                print(f'\nThe item {k} has been successfully removed!\n')
                
                return None
        
        print(f'\nThe product {item} NOT found in stock')


    def search_bd(self, item):

        """
            Search for a product in the database.
        """

        for k in self.bd.keys():

            if k == item:
                print(f'\nThe product {k} WAS found in the stock\n')
                time.sleep(1.5)
                
                return None
        
        print(f'\nThe product {item} NOT found in the stock !')


    def list_bd(self):

        """
            Makes the "print" of the database on the screen showing
            all its products and corresponding values.
        """

        for k, v in self.bd.items():
            print(f'Product : {k} | Price : {v}')

        print()




database_obj = DB()
