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
        name = self.name
        return name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sale(self):
        pass

    def get_sales(self):
        pass

    def met_quota(self,quota):
        pass

    def compare_to(self, other):
        pass

    def _str_(self):
        pass