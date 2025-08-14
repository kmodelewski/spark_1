# Working with excel

To work with excel we need the following libraries:
1. Pandas
2. openpyxl

### Many file union patter

1. Define empty dataframe

```python
import pandas as pd
union_kpd_files: pd.DataFrame = pd.DataFrame()
```
And then in try catch block concat (union dataframe)

```python
union_kpd_files = pd.concat(union_kpd_files, df)
```

)