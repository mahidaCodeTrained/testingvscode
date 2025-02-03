class TicketMixin():
    def calculate_ticket_prices(self, age):
        if age < 12:
            price = 0
        elif age < 18:
            price = 15
        elif age < 60:
            price = 20
        else:
            price = 10
        return price


class Customer(TicketMixin):

    """
    creates an instance of Customer
    """

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} age {self.age} ticket price will be {self.calculate_ticket_prices(self.age)}"


customer = Customer('Abhi', 17)
print(customer.describe())
