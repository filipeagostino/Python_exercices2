class Products:
    def __init__(self, list_names=[], list_prices=[]):
        self.names = list_names
        self.prices = list_prices
        self.dict = {}
        self.dict['names'] = list_names
        self.dict['prices'] = list_prices

    def __str__(self):
        return f'Items:\n{self.dict}'

class Manage(Products):
    def __init__(self, list_names=[], list_prices=[]):
        super().__init__(list_names, list_prices)

    def insert_prods(self, names, prices):
        if names not in self.names:
            self.names.append(names)
            self.prices.append(prices)
            return f'Item(s):\nname: {names!r}, price: {prices} Added!'
        else:
            return f'Item: {names} Already Added!'
    
    def remove_prods(self, names):
        cont = 0
        for n in self.dict['names']:
            if n == names:
                self.dict['names'].pop(cont)
                self.dict['prices'].pop(cont)
                return f'Item(s):\nname: {names!r} Removed!\n (Items: {self.dict})'
            cont += 1
        else:
            return f'Item: {names!r} Not Registered!'
    
    def update_prods(self, names, prices):
        cont = 0
        for n in self.dict['names']:
            if n == names:
                self.dict['prices'][cont] = prices
                return f'Item:\nprice of {names!r} updated to {prices}!\n (Items: {self.dict})'
            cont += 1
        else:
            return f'Item: {names!r} Not Registered!'

class List_products(Products):
    def list_prods(self):
        return f'Items:{self.dict}'

    def __str__(self):
        return f'Items:\n{self.dict}'

    

manage_products = Manage()
resp = 'y'

while resp != 'n':
    name = str(input('Product name: '))
    price = float(input('Product price: '))
    print(manage_products.insert_prods(name, price))
    print('-=' * 30)
    resp = str(input('Continue ? (y/n): ')).lower()

    while resp not in ('y', 'n'):
        resp = str(input('Continue ? (y/n): ')).lower()

resp = 'y'
print('-=' * 30)
print(manage_products)
print('-=' * 30)

while resp != 'n':
    name = str(input('Product name to remove: '))
    print(manage_products.remove_prods(name))
    print('-=' * 30)
    resp = str(input('Continue ? (y/n): ')).lower()

    while resp not in ('y', 'n'):
        resp = str(input('Continue ? (y/n): ')).lower()

print('-=' * 30)
resp = 'y'

while resp != 'n':
    name = str(input('Product name to update price: '))
    price = float(input('Product new price: '))
    print(manage_products.update_prods(name, price))
    print('-=' * 30)
    resp = str(input('Continue ? (y/n): ')).lower()

    while resp not in ('y', 'n'):
        resp = str(input('Continue ? (y/n): ')).lower()

print('-=' * 30)
listing = List_products()
print(listing)

