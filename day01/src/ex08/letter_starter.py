import sys

def load_employees():
    employees = {}
    with open('employees.tsv', 'r', encoding='utf-8') as file:
        for line in file:
            name, surname, email = line.strip().split('\t')
            employees[email] = (name, surname)
        return employees

def generate_welcome_letter(email, employees):
    if email in employees:
        name, _ = employees[email]
        return (f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")

def main():
    if len(sys.argv) != 2:
        return
    
    email = sys.argv[1]
    employees = load_employees()

    letter = generate_welcome_letter(email, employees)
    print(letter)

if __name__ == "__main__":
    main()
