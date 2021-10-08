from SingleResponsibility import Order as IOrder, Payment as IPayment


class Order(IOrder):
    items = []
    status = "Not Paid"

    def add_items(self, item_name: str, price: float, quantity: int):
        item = {
            "name": item_name,
            "price": price,
            "quantity": quantity
        }

        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.get('price') * item.get('quantity')

        return total


class Payment(IPayment):
    @staticmethod
    def debit(order: Order, code: int):
        print(f'Payment is processing using debit card.')
        print(f'Validating code {code}.')
        order.status = 'Paid'
        print(f'Payment Successful')

    @staticmethod
    def credit(order: Order, code: int):
        print(f'Payment is processing using credit card.')
        print(f'Validating code {code}.')
        order.status = 'Paid'
        print(f'Payment Successful')


# Testing.
order = Order()
order.add_items("kushal", 100, 2)
order.add_items("Nischal", 500, 2)
order.calculate_total()

payment = Payment()
payment.debit(order, 123)
