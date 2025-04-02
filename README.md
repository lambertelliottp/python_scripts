# scripts
This repo contains all of my scripts used for various tasks
## Department License Cost Allocator

### Overview
`department_license_cost_allocator.py` is a Python script that calculates the cost allocation of Microsoft licenses across different departments based on user assignments. It takes two CSV files as input:

- **Users CSV** – Contains employee names, usernames, assigned licenses, and their department.
- **Invoice CSV** – Lists license types and their total cost from an invoice.

The script computes the **total cost per department** and outputs a CSV file with cost distribution and percentage breakdown.

---

## License Data Flattener

### Overview
`license_data_flattener` is a Python script that processes a CSV file containing user license data (specifically an O365 admin Active Users export format that has the Licenses column split text-to-columns deliminated by the `+` sign) and expands multiple license entries per user into separate rows in a new CSV file. Each user may have up to 8 licenses (this limit can be modified), and the script ensures that each license is recorded individually while keeping other user details intact.

- **input_file** = "/xyz/abc/Downloads/users.csv"
- **output_file** = "/xyz/abc/Downloads/flattened_user_data.csv"

---

## Export-ADGroupMembers.ps1

This PowerShell script retrieves the user members of multiple Active Directory security groups and exports the results to a neatly formatted text file on the user's Desktop.

### Prerequisites

- Windows PowerShell (recommended: PowerShell 5.1+)
- Active Directory module (`Import-Module ActiveDirectory`)
- Must be run with domain privileges that can query group membership

### How to Use

1. **Prepare a group list file**

   Create a plain text file that contains the names of the security groups you want to check.  
   Example path: `C:\Scripts\GroupsList.txt`

   ```
   Sales-Team
   Finance-Admins
   IT-Operations
   ```

2. **Run the Script**

   You can run the script directly in PowerShell:

   ```powershell
   .\Export-ADGroupMembers.ps1
   ```

   Make sure the script file is in the same directory, or adjust the path accordingly.

3. **Output**

   The script generates a file named `GroupMembers.txt` on your Desktop.

   Example output:
   ```
   Group: Sales-Team
     Alice Johnson (ajohnson)
     Bob Smith (bsmith)

   Group: Finance-Admins
     Charlie Green (cgreen)
   ```

### Configuration

Edit the following line in the script if you use a different path for your group list file:

```powershell
$GroupListPath = 'C:\Scripts\GroupsList.txt'
```

### Features

- Supports up to 25+ security groups
- Resolves nested group members (recursive lookup)
- Filters to include only user accounts
- Output is clean and grouped by security group name

