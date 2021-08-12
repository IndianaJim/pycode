import pandas as pd

#d = {'col1': [1, 2], 'col2': [3, 4]}
#df = pd.DataFrame(data=d)

df = pd.DataFrame([[2,4,6], [20,30,40]],columns=["Price","Count","Value"])
#df = pd.DataFrame([["Jim","Johnson"], ["James","Smith"]],columns=["First","Last"])
#df = pd.DataFrame({'FirstName': ["Bob", "John"], 'LastName': ["Johnson", "Jackson"]})
print(df)


print(df.mean())