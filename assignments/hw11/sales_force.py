class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        open_file = open(file_name, "r")
        for line in open_file:
            self.sales_people.append([line.strip()])

    def quota_report(self, quota):
        for list in self.sales_people:
            split_line = list.split(',')
            nums_list = split_line[2].split(' ')
            nums = 0
            for i in nums_list:
                nums = nums + i
                if nums >= quota:
                    list.append(True)

    def top_seller(self):  # .sort to sort numbers from lowest to highest
        total_list = []
        for list in self.sales_people:
            split_line = list.split(',')
            nums_list = split_line[2].split(' ')
            nums = 0
            for i in nums_list:
                nums = nums + i
                total_list.append(nums)
        total_list.sort()
        high_total = total_list[-1]
        return high_total

    def individual_sales(self, employee_id):
        if employee_id in self.sales_people:
            return self.sales_people[2]
        else:
            return None


    def get_sale_frequencies(self):
        pass
