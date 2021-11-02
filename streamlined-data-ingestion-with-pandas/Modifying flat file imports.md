# Notes

## Limiting Columns

```
col_nums = [0,1,2,3]
col_names = ['Test','nome','testt']
tax_data = pd.read_csv('data.csv', usecols=col_nums)
```
OR
```
tax_data = pd.read_csv('data.csv', usecols=col_names)
```
## Limiting Rows

Limiting Rows
```
tax_data = pd.read_csv('data.csv', nrows=1000)
```
Skipping Rows (Very Useful for chunking)

**Important point pandas make header first line default**
```
tax_data = pd.read_csv('data.csv', nrows=1000, skiprows=1000, header=None)
```
## Assign Column Names

```
cols_names = list(tax_data)
tax_data_next_500 = pd.read_csv('data.csv', nrows=1000, skiprows=500, header=None, names=cols_names)
```

## Handling errors and missing data


* Verify and setting columns data types with `dataframe.dtypes`

  Example: (object is the pandas counterpart to Python string)
  ```
  tax_data = pd.read_csv('us_data.csv', dtype={"zipcode": str})
  ```

* Missing data, using `na_values` param (In this examples it'll change any 0 value in zipcode to NaN and can be checked later with `isna()` function in the column):
  ```
  tax_data = pd.read_csv('us_data.csv', na_values={"zipcode": 0})
  
  print(tax_data[tax_data.zipcode.isna()])
  ```

* Lines with Error

  Set the param `error_bad_lines=False` to skip unparseable records, this will avoid pandas to give errors when find bad data and skip to the next one.
  Also set param `warn_bad_lines=True` to see the messages when records are skipped
