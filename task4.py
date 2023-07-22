# Function to read data from file and extract the tables
def read_file(file_path):
    with open(file_path, 'r') as file:
        file_lines = file.readlines()
    table4 = []
    table5 = []
    table_lines = []
    is_table = False
    count = 0
    for line in file_lines:
        if 'TABLE 1' in line:
            is_table = True
        elif 'TABLE 4' in line:
            is_table = True
        elif 'TABLE (5)' in line:
            is_table = True
        if is_table:
            table_lines.append(line)
        if 'X---' in line:
            count += 1 # if count == 3, table1 is over; if count == 6, table4 is over; if count == 9, table5 is over
        elif count == 3:
            table_lines = [] # table1 isnt required. So, we can clear the table_lines.
        elif count == 6 and table4 == []:
            is_table = False
            if table_lines:
                table4.append(extract_data_from_table(table_lines))
            table_lines = []
        elif count == 9 and table5 == []:
            is_table = False
            if table_lines:
                table5.append(extract_data_from_table(table_lines))
            table_lines = []
    table4 = table4[0]
    table5 = table5[0]
    return table4, table5

# Function to extract data from the table
def extract_data_from_table(table_lines):
    line_length = 21
    header = ['Num','Nome da Usina', 'Ssis', 'Pos Vaz', 'Usi Jus Ope', 'Usi Des Ope', 'Usi Jus Ene', 'Volume Maximo hm3', 'Volume Minimo hm3',
              'Vutil Inic %', 'Previs Oper', 'Pinst MW', 'Perdas Hid % - M', 'Qtur Maxima m3/s', 'Qdef Minima m3/s', 'Vert Maximo m3/s',
               'Produt Eqv MJ/m3', 'Somprd Eqv MJ/m3', 'Produt 65% VU MJ/m3', 'Somprd 65% VU MJ/m3', 'T I P']
    data = []
    count = 0
    for line in table_lines:
        if 'X---' in line:
            count+=1
            continue
        elif count == 2:
            values = extract_values_from_line(line, line_length)
            row_data = {}
            for i in range(line_length):
                row_data[header[i]] = values[i]
            data.append(row_data)
    return data

# Function to extract values from a table_line
def extract_values_from_line(table_line, line_length):
    values = table_line.strip().split()
    for i in range(line_length):
        if values[i] == 'm':
            values[i-1] += ' m'
            values.remove(values[i])
    return values

# Perform the tasks
def main():
    file_path = 'Task4.txt'
    table4, table5 = read_file(file_path)

    # Extract data for the specified plant names
    plant_names = ['SALTO GRANDE', 'BAGUARI', 'PARAIBUNA', 'A.A. LAYDNER', 'G.B. MUNHOZ', 'ITAPARICA', 'P.AFONSO 123', '14 DE JULHO', 'ITIQUIRA II']
    filtered_data = []
    for row_dict in table4+table5:
        if row_dict['Nome da Usina'] in plant_names:
            filtered_data.append(row_dict)
    print(filtered_data)

    # Select the required columns and multiply the columns
    required_columns = ['Num', 'Nome da Usina', 'Ssis', 'Pinst MW', 'Perdas Hid % - M', 'Produt Eqv MJ/m3']
    new_table = [{col: row[col] for col in required_columns} for row in filtered_data]
    print(new_table)

    # Multiply 'Pinst MW' and 'Produt Eqv MJ/m3' and add the result to a new column 'RESULT'
    for row in new_table:
        row['RESULT'] = str(round(float(row['Pinst MW']) * float(row['Produt Eqv MJ/m3']),2))

    # Display the final table
    for row in new_table:
        print(row)

if __name__ == "__main__":
    main()
