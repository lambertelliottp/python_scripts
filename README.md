# python_scripts
This repo contains all of my Python scripts used for various tasks
## Department License Cost Allocator

### Overview
`department_license_cost_allocator.py` is a Python script that calculates the cost allocation of Microsoft licenses across different departments based on user assignments. It takes two CSV files as input:

- **Users CSV** – Contains employee names, usernames, assigned licenses, and their department.
- **Invoice CSV** – Lists license types and their total cost from an invoice.

The script computes the **total cost per department** and outputs a CSV file with cost distribution and percentage breakdown.

## License Data Flattener

### Overview
`license_data_flattener` is a Python script that processes a CSV file containing user license data (specifically an O365 admin Active Users export format that has the Licenses column split text-to-columns deliminated by the `+` sign) and expands multiple license entries per user into separate rows in a new CSV file. Each user may have up to 8 licenses (this limit can be modified), and the script ensures that each license is recorded individually while keeping other user details intact.

- **input_file** = "/xyz/abc/Downloads/users.csv"
- **output_file** = "/xyz/abc/Downloads/flattened_user_data.csv"
