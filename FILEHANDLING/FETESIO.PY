employees = []
yearly_salary = 60000
hourly_salary = 50
hours_worked = 100
tax_brackets = {1000: 0.1, 2000: 0.2, 3000: 0.3}
deductions = {'Healthcare': 250}

class Employee:
    def __init__(self, employee_id, name, address, contact_details, employment_type):
        self.employee_id = employee_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.employee_type = employment_type

        employees.append(self)

    def store(self):
        return f'~~~\n{self.employee_id}\n' \
               f'{self.name}\n' \
               f'{self.address}\n' \
               f'{self.contact_details}\n' \
               f'{self.employee_type}\n'

    def update_record(self, attribute, new_value):
        match attribute:
            case '1':
                self.name = new_value
            case '2':
                self.address = new_value
            case '3':
                self.contact_details = new_value
            case '4':
                self.employee_type = new_value
            case _:
                print('Error')

    def delete_record(self):
        employees.remove(self)



class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, address, contact_details, annual_salary):
        super().__init__(employee_id, name, address, contact_details, employment_type='FULL-TIME')
        self.annual_salary = annual_salary

    def compute_monthly_salary(self):
        pass


class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, address, contact_details, hourly_rate, hours_worked_per_month):
        super().__init__(employee_id, name, address, contact_details, employment_type='PART-TIME')
        self.hourly_rate = hourly_rate
        self.hours_worked_per_month = hours_worked_per_month

    def compute_monthly_salary(self):
        pass


class TaxCalculator:
    def __init__(self, tax_brackets, deductions):
        self.tax_brackets = tax_brackets
        self.deductions = deductions

    def compute_tax(self, employee):
        income = yearly_salary / 12 if employee.employee_type == 'FULL-TIME' else hourly_salary * hours_worked
        tax = 0
        for bracket, rate in self.tax_brackets.items():
            if income > bracket:
                tax += (income - bracket) * rate
                income = bracket
        return self.apply_deductions(tax)

    def apply_deductions(self, taxable_income):
        for deduction in self.deductions.values():
            taxable_income -= deduction
        return taxable_income




def main():


    while True:
        print('===== Payroll and HRIS System =====\n\n'
              '1. Add New Employee\n'
              '2. Update Employee Record\n'
              '3. Delete Employee Record\n'
              '4. Compute Salary\n'
              '5. Compute Taxes\n'
              '6. View Employee Information\n'
              '7. Generate Reports\n'
              '8. Exit\n')
        choice = input('Please select an option (1 - 8): ')

        match choice:
            case '1':
                print('===== Add New Employee =====\n\n'
                      'Enter Employee Details:')
                empl_id = 'E' + str(len(employees) + 1)
                print(f'Employee ID: {empl_id}')
                inp_name = input('Name: ')
                inp_address = input('Address: ')
                inp_contact = input('Contact Details: ')
                inp_type = input('Employment Type (Full-time / Part-time): ')
                if inp_type.upper() == 'FULL-TIME':
                    print(f'Annual Salary: ${yearly_salary}')
                    emp = FullTimeEmployee(empl_id, inp_name, inp_address, inp_contact, yearly_salary)
                    print('\nEmployee Added\n')
                elif inp_type.upper() == 'PART-TIME':
                    print(f'Hourly rate: ${hourly_salary}')
                    emp = PartTimeEmployee(empl_id, inp_name, inp_address, inp_contact, hourly_salary, hours_worked)
                    print('\nEmployee Added\n')
                else: print('Error')

                with open("employee_list.txt", "a") as e:
                    e.write(emp.store())


            case '2':
                print('===== Update Employee Record =====\n')
                inp_id = input('Enter Employee ID: ')
                for employee in employees:
                    if inp_id == employee.employee_id:
                        print('Choose Attribute to update: \n'
                              '1. Name\n'
                              '2. Address\n'
                              '3. Contact Details\n'
                              '4. Employment Type\n')
                        choice = input('Enter Option: ')
                        new_value = input('Enter new value: ')
                        employee.update_record(choice, new_value)

                        with open("employee_list.txt", "r") as e:
                            new = e.read().split("\n")
                            new.insert(new.index(inp_id) + int(choice), new_value)
                            new.pop(new.index(new_value) + 1)
                        with open("employee_list.txt", "w") as f:
                            for line in new:
                                f.write(line)
                                f.write('\n')

            case '3':
                print('===== Delete Employee Record =====\n')
                inp_id = input('Enter Employee ID: ')
                for employee in employees:
                    if inp_id == employee.employee_id:
                        employee.delete_record()
                        print('Employee Record Deleted Succesfully')

                    with open("employee_list.txt", "r") as e:
                        new = e.read().split("\n")
                        new.pop(new.index(inp_id) - 1)
                        new.remove(inp_id)
                        new.remove(employee.name)
                        new.remove(employee.address)
                        new.remove(employee.contact_details)
                        new.remove(employee.employee_type)
                    with open("employee_list.txt", "w") as f:
                        for line in new:
                            f.write(line)
                            f.write('\n')

            case '4':
                print('===== Compute Salary =====\n')
                inp_id = input('Enter Employee ID: ')
                for employee in employees:
                    if inp_id == employee.employee_id:
                        if employee.employee_type == 'FULL-TIME':
                            print(f'Monthly Salary: ${yearly_salary/12}')
                        elif employee.employee_type == 'PART-TIME':
                            print(f'Hourly Salary: ${hourly_salary}')
            case '5':
                print('===== Compute Salary =====\n')
                inp_id = input('Enter Employee ID: ')
                for employee in employees:
                    if inp_id == employee.employee_id:
                        if employee.employee_type == 'FULL-TIME':
                            print(f'Tax Amount per month: ${(yearly_salary/12) / 5}')
                        elif employee.employee_type == 'PART-TIME':
                            print(f'Tax Amount per month: ${((hourly_salary*3)*20) / 25}')
                    else: print('No Employee Found')
            case '6':
                print('===== View Employee Information =====\n')
                inp_id = input('Enter Employee ID: ')
                for employee in employees:
                    if inp_id == employee.employee_id:
                        print(f'ID: {employee.employee_id}\n'
                              f'Name: {employee.name}\n'
                              f'Address: {employee.address}\n'
                              f'Contact Details: {employee.contact_details}\n'
                              f'Employment Type: {employee.employee_type}\n')
                        if employee.employee_type == 'FULL-TIME':
                            print(f'Monthly Salary: ${yearly_salary/12}')
                        else:
                            print(f'Hourly Salary: ${hourly_salary}')
            case '7':
                print('===== Generate Reports =====\n\n'
                      '1. Employee List\n'
                      '2. Tax Report\n')
                choice = input('Enter Option: ')

                if choice == '1':
                    cntr = 1
                    for employee in employees:
                        print(f'{cntr}. {employee.name} ({employee.employee_id}) - {employee.employee_type}')
                        cntr += 1
                    print()
                elif choice == '2':
                    for employee in employees:
                        calculator = TaxCalculator(tax_brackets, deductions)
                        tax = calculator.compute_tax(employee)
                        print(f'{employee.employee_id}: ${tax:.2f}')
                    print()
            case '8':
                print('Exiting the Payroll and the HRIS System. Thank you.')
                break

if __name__ == '__main__':
    main()