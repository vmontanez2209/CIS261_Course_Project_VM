import datetime

print('--------------------------------------')
print('Welcome to the Employee Payroll System')
print('--------------------------------------\n')
print('If you need to Exit and Total, please enter End.\n')
print('The system will calculate the gross and net pay of all employees,')
print('as well as display the taxes deducted with the rate.\n')
print('Payroll dates must be in the format mm/dd/yyyy')
print('--------------------------------------\n')


def get_name():
    name = input("Enter employee full name: ")
    return name

def get_total_hours():
    total_hours = float(input("Enter total hours worked for pay period: "))
    return total_hours

def get_hourly_rate():
    hourly_rate = float(input("Enter employee hourly rate: "))
    return hourly_rate

def get_tax_rate():
    tax_rate = float(input("Enter tax rate (%): "))
    return tax_rate

def get_gross_pay(total_hours, hourly_rate):
    gross_pay = float(total_hours) * float(hourly_rate)
    return gross_pay

def calc_tax_and_netpay(total_hours, hourly_rate, tax_rate):
    tax = float(total_hours) * float(hourly_rate) * (float(tax_rate) / 100)
    net_pay = float(total_hours) * float(hourly_rate) - tax
    return tax, net_pay

def display_employee_info(from_date, to_date, name, total_hours, hourly_rate, tax_rate,
tax, gross_pay, net_pay):
    print("----------------------------------------------------")
    print("-----------------Employee Payroll-------------------")
    print("----------------------------------------------------")
    print("From Date: ", from_date.strftime('%m/%d/%y'))
    print("To Date: ", to_date.strftime('%m/%d/%y'))
    print("Employee name:", name)
    print("Total hours:", total_hours)
    print("Hourly rate:", hourly_rate)
    print("Tax rate:", tax_rate)
    print("Income tax:", round(tax, 2))
    print("Gross pay:", gross_pay)
    print("Net pay:", net_pay)
    print("----------------------------------------------------")
def display_total_info(total_info):
    print("----------------------------------------------------")
    print("-----------Total Employee Payroll Numbers-----------")
    print("----------------------------------------------------")
    print("Total number of employees:", total_info['total_employees'])
    print("Total hours:", total_info['total_hours'])
    print("Total tax:", round(total_info['total_tax'], 2))
    print("Total gross pay:", total_info['total_gross_pay'])
    print("Total net pay:", total_info['total_net_pay'])
    print("----------------------------------------------------")

def get_from_and_to_dates():
    from_date = input("Enter From date:")
    from_date = datetime.datetime.strptime(from_date, '%m/%d/%Y').date()
    to_date = input("Enter To date:")
    to_date = datetime.datetime.strptime(to_date, '%m/%d/%Y').date()
    return from_date, to_date

def calc_emp_taxes(emp_list, total_info):
    for emp in emp_list:
        from_date, to_date, name, hours, hourly_rate, tax_rate = emp
        gross_pay = get_gross_pay(hours, hourly_rate)
        tax, net_pay = calc_tax_and_netpay(hours, hourly_rate, tax_rate)
        display_employee_info(from_date, to_date, name.title(), hours, hourly_rate, tax_rate, tax, gross_pay, net_pay)
    total_info['total_employees'] += 1
    total_info['total_hours'] += hours
    total_info['total_tax'] += tax
    total_info['total_gross_pay'] += gross_pay
    total_info['total_net_pay'] += net_pay

def main():
    emp_list = []
    total_info = {'total_employees': 0, 'total_hours': 0, 'total_tax': 0, 'total_gross_pay': 0, 'total_net_pay': 0}
    while True:
        name = get_name()
        if name.capitalize() == "End":
            break
        from_date, to_date = get_from_and_to_dates()
        hours = get_total_hours()
        hourly_rate = get_hourly_rate()
        tax_rate = get_tax_rate()
        emp_list.append([from_date, to_date, name, hours, hourly_rate, tax_rate])
        calc_emp_taxes(emp_list, total_info)
        display_total_info(total_info)

if __name__ == '__main__':
    main()
