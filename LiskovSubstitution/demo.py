from LSInterface import Order as IOrder, DemoPayment


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


class DebitPayment(DemoPayment):
    @staticmethod
    def pay(order: Order, code: int):
        print(f'Payment is processing using debit card.')
        print(f'Validating code {code}.')
        order.status = 'Paid'
        print(f'Payment Successful')


class CreditPayment(DemoPayment):
    @staticmethod
    def pay(order: Order, code: int):
        print(f'Payment is processing using credit card.')
        print(f'Validating code {code}.')
        order.status = 'Paid'
        print(f'Payment Successful')
