import sys

def extract_names(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        emails = file.read().splitlines()

    tsv_data = []

    for email in emails:
        if not email:
            continue
        local_part, domain = email.split('@')
        name, surname = local_part.split('.')
        name = name.capitalize()
        surname = surname.capitalize()
        tsv_data.append(f'{name}\t{surname}\t{email}')
    
    with open('employees.tsv', 'w', encoding='utf-8') as tsv_file:
        tsv_file.write("Name\tSurname\tE-mail\n")
        tsv_file.write('\n'.join(tsv_data))

def main():
    if len(sys.argv) != 2:
        return
    
    input_file = sys.argv[1]

    extract_names(input_file)

if __name__ == "__main__":
    main()
    