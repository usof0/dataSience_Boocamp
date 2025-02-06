import sys

def call_center(clients, recipients):
    clients_set = set(clients)
    recipients_set = set(recipients)

    return list(clients_set - recipients_set)

def potential_clients(clients, participants):
    clients_set = set(clients)
    participants_set = set(participants)

    return list(participants_set - clients_set)

def loyalty_program(clients, participants):
    clients_set = set(clients)
    participants_set = set(participants)

    return (clients_set - participants_set)

def main():
    clients = [
        'andrew@gmail.com',
        'jessica@gmail.com',
        'ted@mosby.com',
        'john@snow.is',
        'bill_gates@live.com',
        'mark@facebook.com',
        'elon@paypal.com',
        'jessica@gmail.com'
    ]
    participants = [
        'walter@heisenberg.com',
        'vasily@mail.ru',
        'pinkman@yo.org',
        'jessica@gmail.com',
        'elon@paypal.com',
        'pinkman@yo.org',
        'mr@robot.gov',
        'eleven@yahoo.com'
    ]
    recipients = [
        'andrew@gmail.com',
        'jessica@gmail.com',
        'john@snow.is'
    ]
    try:
        if len(sys.argv) != 2:
            raise ValueError('Invalid number of arguments')
        
        task_name = sys.argv[1]

        if task_name == 'call_center':
            result = call_center(clients, recipients)
        elif task_name == 'potential_clients':
            result = potential_clients(clients, participants)
        elif task_name == 'loyalty_program':
            result = loyalty_program(clients, participants)
        else:
            raise ValueError('Invalid task name. Valid options: call_center, potential_clients, loyalty_program')
        
        for email in result:
            print(email)
    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == "__main__":
    main()
