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
            Generates a menu list to be displayed on the user's screen.
        """

        self.line()

        for pos, option in enumerate(items):
            print(f'{pos} - {option}')

        self.line()
    

    def menu(self):

        """
           Invokes the menu to be displayed on the screen and receives the choice of user.
        """ 

        self.listMenu(['Close program.', 'Insert new product.', 'Withdraw a Product.', 'Seach by Product.'])


        command = int(input('Type your choice : '))

        print('\n')

        return command
    

    def insert(self):

        """
            Screen presented for Insertion of information in the database.
        """

        while True:

            try:
                product_name = str(input('Insert the name by product : ')).capitalize()
                product_price = float(input('Inform the price of the product : '))

                database_obj.insert_bd(product_name, product_price)
                
                break

            except ValueError:
                print('\nProduct must be a Name and price a numeric value!\n')

    
    def withdraw(self):

        """
            Screen presented for Product Removal on the screen of user.
        """

        while True:
            database_obj.list_bd()
            
            srch = str(input('\nName of the product to be removed : '))

            database_obj.withdraw_bd(srch)
            print()
            
            break


    def search(self):

        
        """
            Screen presented to the user seeking to find products in the database.
        """

        while True:
            srch = str(input('Search for a product : '))

            database_obj.search_bd(srch)

            break



myFunctions = MyFunctions()