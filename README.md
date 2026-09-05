# Pandas Data Cleaning

Beginner Python practice using **Pandas** to learn basic data-cleaning techniques, including detecting missing values, removing missing data, filling missing values, selecting columns, and sorting DataFrames.

## 📌 Topics Covered

* Reading Excel files
* Pandas DataFrame
* Selecting columns
* Series vs DataFrame
* `isnull()`
* Counting missing values
* `dropna()`
* `fillna()`
* `sort_values()`
* Sorting in ascending and descending order
* Basic data cleaning

## 🛠️ Technologies

* Python
* Pandas
* Excel
* OpenPyXL

## 📂 Project Structure

```text
pandas-data-cleaning/
│
├── pandas_data_cleaning.py
├── Employee.xlsx
├── requirements.txt
└── README.md
```

## 🚀 Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

```bash
python pandas_data_cleaning.py
```

Make sure that `Employee.xlsx` is available in the project directory.

## 📖 What I Learned

### 1. Selecting Columns

Selecting one column:

```python
employee["Name"]
```

This returns a Pandas Series.

Selecting multiple columns:

```python
employee[["Name", "Salary"]]
```

This returns a DataFrame.

## 🔍 Checking Missing Values

### `isnull()`

The `isnull()` method checks every cell for missing values.

```python
employee.isnull()
```

It returns:

* `True` when a value is missing.
* `False` when a value exists.

### Counting Missing Values

```python
employee.isnull().sum()
```

This counts the number of missing values in each column.

## 🗑️ Removing Missing Data

### `dropna(how="all")`

```python
employee.dropna(how="all")
```

Removes rows where all values are missing.

### `dropna(subset=["Name"])`

```python
employee.dropna(subset=["Name"])
```

Removes rows where the `Name` value is missing.

## 🔄 Filling Missing Values

### Fill With One Value

```python
employee.fillna(value="Not found")
```

This replaces missing values with `"Not found"`.

### Fill Different Columns With Different Values

```python
employee.fillna(
    {
        "Salary": 0,
        "Name": "User"
    }
)
```

This allows each column to have its own replacement value.

For example:

* Missing `Salary` → `0`
* Missing `Name` → `"User"`

## 📊 Sorting Data

The `sort_values()` method sorts the DataFrame according to a selected column.

```python
df.sort_values(
    by="Name",
    ascending=False
)
```

### Ascending Order

```python
ascending=True
```

Sorts from smaller to larger or A → Z.

### Descending Order

```python
ascending=False
```

Sorts from larger to smaller or Z → A.

## 🧠 What I Learned

Through this project, I practiced:

* Detecting missing values
* Counting missing values
* Removing incomplete rows
* Filling missing values
* Selecting specific columns
* Sorting DataFrames
* Understanding basic data-cleaning operations

## 🎯 Project Goal

The goal of this project is to understand the basic techniques used to clean and prepare data before performing data analysis.

## 📚 Future Improvements

Possible next steps:

* Use `dropna()` with different options
* Replace missing values using mean or median
* Detect duplicated rows
* Remove duplicated data
* Rename columns
* Change data types
* Filter data after cleaning
* Combine multiple cleaning techniques
* Work with larger real-world datasets

## 👨‍💻 Author

Nader

## ⭐ Note

This repository is part of my Python and Data Science learning journey.
