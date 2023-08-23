print('--------------------------------------')
print('Welcome to the Employee Payroll System')
print('--------------------------------------\n')
print('If you need to Exit, please enter End for the name.\n')
print('The system will calculate the gross and net pay of all employees,')
print('as well as display the taxes deducted with the rate.\n')
print('Payroll dates must be in the format mm/dd/yyyy')
print('--------------------------------------\n')
from datetime import datetime
def create_users():
    print('----------------------------------')
    print('Create users, passwords, and roles')
    print('----------------------------------')
    user_file = open("users.txt", "a+")
    while True:
        username = GetUserName()
        if (username.upper() == "END"):
            break
        user_pwd = GetUserPassword()
        user_role = GetUserRole()
        user_detail = username + "|" + user_pwd + "|" + user_role + "\n"
        user_file.write(user_detail)
    user_file.close()
    printuserinfo()
def GetUserName():
    username = input("Enter user name or 'End' to quit: ")
    return username
def GetUserPassword():
    pwd = input("Enter password: ")
    return pwd
def GetUserRole():
    user_role = input("Enter role (Admin or User): ")
    while True:
        if (user_role.upper() == "ADMIN" or user_role.upper() == "USER"):
            return user_role
        else:
            user_role = input("Enter role (Admin or User): ")
def printuserinfo():
    UserFile = open("users.txt", "r")
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            break
        UserDetail = UserDetail.replace("\n", "")
        UserList = UserDetail.split("|")
        username = UserList[0]
        user_password = UserList[1]
        user_role = UserList[2]
        print("User Name: ", username, " Password: ", user_password, "Role: ", user_role)

def Login():
    user_file = open("users.txt", "r")
    user_list = []
    user_name = input("Enter User Name: ")
    user_role = "None"
    while True:
        user_detail = user_file.readline()
        if not user_detail:
            return user_role, user_name
        user_detail = user_detail.replace("\n", "")
        user_list = user_detail.split("|")
        if user_name == user_list[0]:
            user_role = user_list[2]  # user is valid, return role
            return user_role, user_name
    return user_role, user_name

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
    emp_file = open("Employees.txt", "r")
    while True:
        run_date = input("Enter start date for report (MM/DD/YYYY) or All for all data in file: ")
        if (run_date.upper() == "ALL"):
            break
        try:
            run_date = datetime.strptime(run_date, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Try again.")
            print()
            continue
    while True:
        emp_detail = emp_file.readline()
        if not emp_detail:
            break
        emp_detail = emp_detail.replace("\n", "")
        emp_list = emp_detail.split("|")
        from_date = emp_list[0]
        if (str(run_date).upper() != "ALL"):
            check_date = datetime.strptime(from_date, "%m/%d/%Y")
            if (check_date < run_date):
                continue
        to_date = emp_list[1]
        emp_name = emp_list[2]
        hours = float(emp_list[3])
        hourly_rate = float(emp_list[4])
        tax_rate = float(emp_list[5])
        gross_pay, tax, net_pay = calc_tax_and_netpay(hours, hourly_rate, tax_rate)
        print(from_date, to_date, emp_name, f"{hours:,.2f}", f"{hourly_rate:,.2f}", f"{gross_pay:,.2f}",
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
        details_printed = True
    if (details_printed):
        print_totals(emp_totals)
    else:
        print("No detail information to print")

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

if __name__ == "__main__":
    create_users()
    print()
    print("##### Data Entry #####")
    UserRole, UserName = Login()
    DetailsPrinted = False
    emp_totals = {}
    if (UserRole.upper() == "NONE"):
        print(UserName, " is invalid.")
    else:
        if (UserRole.upper() == "ADMIN"):
            emp_file = open("Employees.txt", "a+")
            while True:
                emp_name = get_name()
                if (emp_name.upper() == "END"):
                    break
                from_date, to_date = get_from_and_to_dates()
                hours = get_total_hours()
                hourly_rate = get_hourly_rate()
                tax_rate = get_tax_rate()
                emp_detail = from_date + "|" + to_date + "|" + emp_name + "|" + str(hours) + \
                             "|" + str(hourly_rate) + "|" + str(tax_rate) + "\n"
                emp_file.write(emp_detail)
            emp_file.close()
        printinfo(DetailsPrinted)