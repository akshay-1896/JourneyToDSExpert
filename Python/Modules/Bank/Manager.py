manager_name = "dherendra shikhawat"
manager_id = "dheerendra@gmail.com"
manager_password = "ghjk852332"

n_employee = 10 
employe_name = "anshika"
employee_id = "anshika@gmail.com"
employee_pass = "anshika823645"
employee_salary = "400000"

if __name__ == "__main__": # restriction
    def show_manager_credentials():
        print(manager_name)
        print(manager_id)
        print(manager_password)

def show_anshika_details():
    print(employe_name)
    print(employee_id)
    print(employee_pass)
    print(employee_salary) 
    
# print("Manager file executed!")
# print(__name__) # if executed through itself then returns __main__ & if executed through other file than returns the file name (Manager)
