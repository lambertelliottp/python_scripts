import csv

def expand_licenses(input_csv, output_csv):

    with open(input_csv, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        
        fieldnames = [
            'Display name',
            'User principal name',
            'First name',
            'Last name',
            'Title',
            'License',
            'LicenseCost',
            'Total Cost/Month',
            'Department1',
            'Department2'
        ]
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            for i in range(1, 9):
                license_col = f'Licenses{i}'
                cost_col = f'Licenses{i}Cost'
                
                license_val = row.get(license_col, '').strip()
                cost_val = row.get(cost_col, '').strip()
                if license_val:
                    writer.writerow({
                        'Display name': row.get('Display name', ''),
                        'User principal name': row.get('User principal name', ''),
                        'First name': row.get('First name', ''),
                        'Last name': row.get('Last name', ''),
                        'Title': row.get('Title', ''),
                        'License': license_val,
                        'LicenseCost': cost_val,
                        'Total Cost/Month': row.get('Total Cost/Month', ''),
                        'Department1': row.get('Department1', ''),
                        'Department2': row.get('Department2', '')
                    })

if __name__ == "__main__":
    input_file = "/xyz/abc/Downloads/users.csv"
    output_file = "/xyz/abc/Downloads/flattned_user_data.csv"
    expand_licenses(input_file, output_file)
    print(f"Done! Expanded data written to {output_file}")
