import pandas as pd


# ============================================
# Pandas Data Cleaning
# Missing Values and Sorting
# ============================================

# Read the Excel file
employee = pd.read_excel("Employee.xlsx")

print("Original Data:")
print(employee)

print("#" * 50)

# ============================================
# Select Columns
# ============================================

# Select one column - returns a Series
print("Name Column:")
print(employee["Name"])

print("#" * 50)

# Select multiple columns - returns a DataFrame
print("Name and Salary Columns:")
print(employee[["Name", "Salary"]])

print("#" * 50)

# ============================================
# Check Missing Values
# ============================================

# Check every cell for missing values
print("Missing Values:")
print(employee.isnull())

print("#" * 50)

# Count missing values in each column
print("Missing Values Count:")
print(employee.isnull().sum())

print("#" * 50)

# ============================================
# Remove Missing Data
# ============================================

# Remove rows where all values are missing
df = employee.dropna(how="all")

print("After Removing Completely Empty Rows:")
print(df)

print("#" * 50)

# Remove rows where the Name value is missing
df = employee.dropna(subset=["Name"])

print("After Removing Rows With Missing Names:")
print(df)

print("#" * 50)

# ============================================
# Fill Missing Values
# ============================================

# Fill missing values with one value
df = employee.fillna(value="Not found")

print("Fill Missing Values With 'Not found':")
print(df)

print("#" * 50)

# Fill missing values with different values for specific columns
df = employee.fillna(
    {
        "Salary": 0,
        "Name": "User"
    }
)

print("Fill Missing Values By Column:")
print(df)

print("#" * 50)

# ============================================
# Sort Data
# ============================================

# Sort the DataFrame by Name in descending order
df = df.sort_values(
    by="Name",
    ascending=False
)

print("Sorted Data:")
print(df)