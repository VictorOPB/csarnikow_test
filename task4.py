# Function to extract data from the table
def extract_data_from_table(table_lines):
    header = table_lines[0].strip().split()
    data = []
    for line in table_lines[1:]:
        values = line.strip().split()
        row_data = {}
        for i, value in enumerate(values):
            row_data[header[i]] = value
        data.append(row_data)
    return data

# Read the file and perform the tasks
def main():
    file_path = 'Task4.txt'

    with open(file_path, 'r') as file:
        file_lines = file.readlines()

    tables = []
    table_lines = []
    is_table = False
    for line in file_lines:
        if line.strip() == 'Tabela':
            is_table = True
        elif line.strip() == 'FimTabela':
            is_table = False
            if table_lines:
                tables.append(extract_data_from_table(table_lines))
                table_lines = []
        elif is_table:
            table_lines.append(line)
    print(tables)

    # Extract data for the specified plant names
    plant_names = ['SALTO GRANDE', 'BAGUARI', 'PARAIBUNA', 'A.A. LAYDNER', 'G.B. MUNHOZ', 'ITAPARICA', 'P.AFONSO 123', '14 DE JULHO', 'ITIQUIRA II']
    filtered_data = []
    for table in tables:
        for row in table:
            if row['Nome da Usina'] in plant_names:
                filtered_data.append(row)

    # Select the required columns and multiply the columns
    required_columns = ['Num', 'Nome da Usina', 'Ssis', 'Pinst MW', 'Perdas Hid % - M', 'Produt Eqv MJ/m3']
    new_table = [{col: row[col] for col in required_columns} for row in filtered_data]

    # Multiply 'Pinst MW' and 'Produt Eqv MJ/m3' and add the result to a new column 'RESULT'
    for row in new_table:
        row['RESULT'] = float(row['Pinst MW']) * float(row['Produt Eqv MJ/m3'])

    # Display the final table
    for row in new_table:
        print(row)

if __name__ == "__main__":
    main()
