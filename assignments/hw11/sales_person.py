class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sale(self):
        total_sum = 0
        for sale in self.sales:
            total_sum = total_sum + sale
        return total_sum

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sale() >= quota:
            return True
        else:
            return False

    def compare_to(self, other):

        if other.total_sale() == self.total_sale():
            return 0
        elif other.total_sale() >= self.total_sale():
            return -1
        elif self.total_sale() > other.total_sale():
            return 1

    def __str__(self):
        return str(self.get_id()) + '-' + self.get_name() + ' : ' + str(self.total_sale())
