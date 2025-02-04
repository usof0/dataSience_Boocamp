def read_and_write(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as csv_file:
        with open(output_file, 'w', encoding='utf-8') as tsv_file:
            for line in csv_file:
                tsv_line = []
                in_quotes = False
                field = []

                for char in line:
                    if char == '"':
                        in_quotes = not in_quotes
                        field.append(char)
                    elif char == ',' and not in_quotes:
                        tsv_line.append(''.join(field))
                        tsv_line.append('\t')
                        field = []
                    else:
                        field.append(char)
                
                tsv_line.append(''.join(field))
                tsv_file.write(''.join(tsv_line))

def main():
    input_file = 'ds.csv'
    output_file = 'ds.tsv'
    read_and_write(input_file, output_file)

if __name__ == "__main__":
    main()
