import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel("Deutch_verbs v2.1.xlsx", sheet_name = 0);



print("Column headings:");
print(df.columns);
print("--------------------------");
print(df.head());
