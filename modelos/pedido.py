import persistent
class Customer(persistent.Persistent):
    def __init__(self, number, name, contact_last_name, contact_first_name, phone, address_line1, address_line2, city, state, postal_code, country, sales_rep_employee_number, credit_limit):
        self.number = number
        self.name = name
        self.contact_last_name = contact_last_name
        self.contact_first_name = contact_first_name
        self.phone = phone
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.sales_rep_employee_number = sales_rep_employee_number
        self.credit_limit = credit_limit
