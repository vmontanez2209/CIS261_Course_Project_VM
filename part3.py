print('--------------------------------------')
print('Welcome to the Employee Payroll System')
print('--------------------------------------\n')
print('If you need to Exit, please enter End for the name.\n')
print('The system will calculate the gross and net pay of all employees,')
print('as well as display the taxes deducted with the rate.\n')
print('Payroll dates must be in the format mm/dd/yyyy')
print('--------------------------------------\n')

def get_name():
    name = input("Enter employee full name: ")
    return name.capitalize()

def get_from_and_to_dates():
    from_date = input("Enter From date:")
    to_date = input("Enter To date:")
    return from_date, to_date

def get_total_hours():
    hours = float(input("Enter total hours worked for pay period: "))
    return hours

def get_hourly_rate():
    hourly_rate = float(input("Enter employee hourly rate: "))
    return hourly_rate

def get_tax_rate():
    tax_rate = float(input("Enter tax rate (%): "))
    return tax_rate

def calc_tax_and_netpay(hours, hourly_rate, tax_rate):
    gross_pay = hours * hourly_rate
    tax = gross_pay * (tax_rate / 100)
    net_pay = gross_pay - tax
    return tax, net_pay, gross_pay

def printinfo(emp_detail_list):
    total_emp = 0
    total_hours = 0.00
    total_gross_pay = 0.00
    total_tax = 0.00
    total_net_pay = 0.00
    for emp_list in emp_detail_list:
        from_date = emp_list[0]
        to_date = emp_list[1]
        name = emp_list[2]
        hours = emp_list[3]
        hourly_rate = emp_list[4]
        tax_rate = emp_list[5]
        gross_pay, tax, net_pay = calc_tax_and_netpay(hours, hourly_rate, tax_rate)
        print(from_date, to_date, name, f"{hours:,.2f}", f"{hourly_rate:,.2f}", f"{gross_pay:,.2f}",
              f"{tax_rate:,.1%}", f"{tax:,.2f}", f"{net_pay:,.2f}")
        total_emp += 1
        total_hours += hours
        total_gross_pay += gross_pay
        total_tax += tax
        total_net_pay += net_pay
    emp_totals["total_emp"] = total_emp
    emp_totals["total_hours"] = total_hours
    emp_totals["total_gross_pay"] = total_gross_pay
    emp_totals["total_tax"] = total_tax
    emp_totals["total_net_pay"] = total_net_pay


def print_totals(emp_totals):
    print("----------------------------------------------------")
    print("-----------Total Employee Payroll Numbers-----------")
    print("----------------------------------------------------")
    print(f"Total Number of Employees: {emp_totals['total_emp']}")
    print(f"Total Hours Worked: {emp_totals['total_hours']}")
    print(f"Total Gross Pay: {emp_totals['total_tax']:,.2f}")
    print(f"Total Income Tax: {emp_totals['total_gross_pay']:,.2f}")
    print(f"Total Net Pay: {emp_totals['total_net_pay']:,.2f}")
    print("----------------------------------------------------")


def write_employee_info(employee):
    file = open("employee_payroll.txt", "a")
    file.write(
        '{}|{}|{}|{}|{}|{}\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))


def get_from_date():
    valid = False
    from_date = ""
    while not valid:
        from_date = input("Enter From Date you would like to see payroll from (mm/dd/yyyy) or ALL: ")
        if len(from_date.split('/')) != 3 and from_date.upper() != 'ALL':
            print("Invalid Date Format: ")
        else:
            valid = True
    return from_date


def read_employee_info(from_date):
    emp_detail_list = []
    file = open("employee_payroll.txt", "r")
    data = file.readlines()
    condition = True
    if from_date.upper() == 'ALL':
        condition = False
    for employee in data:
        employee = [x.strip() for x in employee.strip().split("|")]
        if not condition:
            emp_detail_list.append(
                [employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
        else:
            if from_date == employee[0]:
                emp_detail_list.append(
                    [employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
    return emp_detail_list


if __name__ == "__main__":
    emp_detail_list = []
    emp_totals = {}
    while True:
        name = get_name()
        if name.upper() == "END":
            break
        from_date, to_date = get_from_and_to_dates()
        hours = get_total_hours()
        hourly_rate = get_hourly_rate()
        tax_rate = get_tax_rate()
        print()
        emp_detail = [from_date, to_date, name, hours, hourly_rate, tax_rate]
        write_employee_info(emp_detail)
        print()
        from_date = get_from_date()
        emp_detail_list = read_employee_info(from_date)
        print()
        printinfo(emp_detail_list)
        print()
        print_totals(emp_totals)
