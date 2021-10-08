from SingleResponsibility import CodeOrder


class Order(CodeOrder):
    items = []
    status = "Not Paid"

    def add_items(self, item_name: str, price: float, quantity: int) -> None:
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

    def payment(self, payment_type: str, code: int):
        if payment_type == 'debit':
            print(f'Payment is processing using {payment_type} card.')
            print(f'Validating code {code}.')
            self.status = 'Paid'
            print(f'Payment Successful')

            return

        if payment_type == 'credit':
            print(f'Payment is processing using {payment_type} card.')
            print(f'Validating code {code}.')
            self.status = 'Paid'
            print(f'Payment Successful')

            return


order = Order()
order.add_items("kushal", 100, 2)
order.add_items("Nischal", 500, 2)

order.calculate_total()
order.payment('credit', 1234)
