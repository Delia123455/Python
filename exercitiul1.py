class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        """Displays the number of employees"""
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        """Displays employee details"""
        print("Name: ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        Employee.empCount -= 1

    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)


class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, department):
        NUME_ECHIPA = "F01-"  # Prefixul echipei
        super().__init__(name, salary)
        self.department = NUME_ECHIPA + department
        Manager.mgr_count += 1

    def display_employee(self):
        """Modify display_employee based on the value of X % 3"""
        X = Manager.mgr_count  # X este determinat de numărul de Manageri creați

        if X % 3 == 0:
            print("Name: ", self.name)
        elif X % 3 == 1:
            print("Salary: ", self.salary)
        elif X % 3 == 2:
            print("Department: ", self.department)

    def __del__(self):
        Manager.mgr_count -= 1


if __name__ == "__main__":
    # Crearea obiectelor Manager (Y=12)
    manager1 = Manager("Delia", 3600, "Debugging")
    manager2 = Manager("Andreea", 2500, "Tech")
    manager3 = Manager("Alexandra", 2200, "Tester")
    manager4 = Manager("Gabriela", 3300, "Marketing")
    manager5 = Manager("Denisa", 2700, "QA")
    manager6 = Manager("Ionela", 4000, "HR")
    manager7 = Manager("Vali", 3500, "Operations")
    manager8 = Manager("Bebe", 2900, "Finance")
    manager9 = Manager("Andrei", 3800, "Sales")
    manager10 = Manager("Viorel", 3200, "IT")
    manager11 = Manager("Capet", 3300, "R&D")
    manager12 = Manager("Ioana", 3100, "Logistics")

    # Afișarea informațiilor pentru Manageri
    manager1.display_employee()
    manager2.display_employee()
    manager3.display_employee()
    manager4.display_employee()
    manager5.display_employee()
    manager6.display_employee()
    manager7.display_employee()
    manager8.display_employee()
    manager9.display_employee()
    manager10.display_employee()
    manager11.display_employee()
    manager12.display_employee()

    # Crearea obiectelor Employee
    employee1 = Employee("Preda", 2300)
    employee2 = Employee("Elena", 4300)
    employee3 = Employee("Emilia", 1300)
    employee4 = Employee("Niculae", 2300)
    employee5 = Employee("Gheorghe", 2567)

    # Afișarea informațiilor pentru Employee
    employee1.display_employee()
    employee2.display_employee()
    employee3.display_employee()
    employee4.display_employee()
    employee5.display_employee()

    # Afișarea numărului de manageri și angajați
    print(f"Numărul de manageri este: {Manager.mgr_count}")
    print(f"Numărul total de angajați este: {Employee.empCount}")
