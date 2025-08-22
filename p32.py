#Create a program named “emp.py” and implement the functions DA, HRA, PF and
#TAX. Create another program that uses the function of the employee module and
#calculates gross and net salary of an employee
import p32emp

epmloyee_name = input("enter the name :")
basic_salary = float(input("enter the salary"))

emp_da = p32emp.DA(basic_salary)
emp_hra = p32emp.HRA(basic_salary)
emp_pf = p32emp.PF(basic_salary)
emp_gross_salary = basic_salary + emp_da + emp_hra


print(f"\nEmployee Name: {epmloyee_name}")
print(f"Basic Salary: {basic_salary}")
print(f"Dearness Allowance (DA): {emp_da}")
print(f"House Rent Allowance (HRA): {emp_hra}")
print(f"Provident Fund (PF): {emp_pf}")
print(f"Gross Salary: {emp_gross_salary}")
