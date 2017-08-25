import pandas

food_info = pandas.read_csv("DD.csv")
columns = ["START_DATE", "END_DATE"]
zinc_copper = food_info[columns]
print(zinc_copper)
