#!/usr/bin/env python3
import csv
from collections import defaultdict

def parse_users_csv(filename):

    license_counts = defaultdict(lambda: defaultdict(int))
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip header row
        for row in reader:
            if not row:
                continue
            department = row[-1].strip()
            # Loop through license columns (from index 2 up to but not including last column)
            for lic in row[2:-1]:
                lic = lic.strip()
                if lic:
                    license_counts[lic][department] += 1
    return license_counts

def parse_invoice_csv(filename):
    invoice_costs = {}
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip header row
        for row in reader:
            if not row:
                continue
            lic = row[0].strip()
            try:
                cost = float(row[1])
            except ValueError:
                cost = 0.0
            invoice_costs[lic] = cost
    return invoice_costs

def write_output_csv(department_costs, total_invoice_cost, output_filename):

    with open(output_filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Department', 'Allocated Cost', 'Percentage'])
        for dept, cost in department_costs.items():
            percentage = (cost / total_invoice_cost) * 100 if total_invoice_cost > 0 else 0
            writer.writerow([dept, f"{cost:.2f}", f"{percentage:.2f}%"])

def main():
    # Hard-coded file paths – update these paths as necessary
    users_csv_path = "/abc/xyz/Downloads/users.csv"
    invoice_csv_path = "/abc/xyz/Downloads/invoice.csv"
    output_csv_path = "/abc/xyz/Downloads/dept_cost_allocation.csv"

    license_counts = parse_users_csv(users_csv_path)
    invoice_costs = parse_invoice_csv(invoice_csv_path)

    department_costs = defaultdict(float)
    total_invoice_cost = 0.0

    # Process each license from the invoice
    for lic, cost in invoice_costs.items():
        dept_counts = license_counts.get(lic, {})
        total_count = sum(dept_counts.values())
        total_invoice_cost += cost
        if total_count > 0:
            cost_per_assignment = cost / total_count
            for dept, count in dept_counts.items():
                department_costs[dept] += count * cost_per_assignment
        else:
            print(f"Warning: License '{lic}' in invoice is not assigned to any user.")

    # Optionally print results to the console
    print("Department Cost Allocation:")
    for dept, cost in department_costs.items():
        percentage = (cost / total_invoice_cost) * 100 if total_invoice_cost > 0 else 0
        print(f"{dept}: ${cost:.2f} ({percentage:.2f}%)")

    # Write the allocation to an output CSV file
    write_output_csv(department_costs, total_invoice_cost, output_csv_path)
    print(f"Output written to {output_csv_path}")

if __name__ == "__main__":
    main()