# data_cleaning.py

import numpy as np
import pandas as pd

class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def object_cleaning(self):
        for col in self.df.select_dtypes(include="object").columns:
            print(f"\nColumn: {col}")
            choice2 = input("Do you want to choose this column for cleaning? (yes/no): ")

            if choice2.lower() == "yes":
                choice = "yes"
                while choice.lower() == "yes":
                    find = input("What value do you want to change?: ")
                    replace_value = input("What should it be replaced with?: ")

                    self.df[col] = self.df[col].apply(
                        lambda x: replace_value if x == find else x
                    )

                    choice = input("Do you want to do more find-and-replace in this column? (yes/no): ")

        return self.df

    def float_cleaning(self):
        while True:
            print("\nFloat columns in the DataFrame:")
            obj_cols = self.df.select_dtypes(include="float64").columns
            print(obj_cols)

            choise = input("Do you want to replace a value in one of these columns? (yes/no): ")
            if choise.lower() != "yes":
                break

            col = input("Which column do you want to modify?: ")
            if col not in obj_cols:
                print("Invalid column. Try again.")
                continue

            find = eval(input("What value do you want to replace?: "))
            replace_value = eval(input("What should it be replaced with?: "))

            self.df[col] = self.df[col].replace(find, replace_value)
            print(f"Replaced '{find}' with '{replace_value}' in column '{col}'.")

        print("Final DataFrame:")
        print(self.df.head())
        return self.df

    def int_cleaning(self):
        while True:
            print("\nInteger columns in the DataFrame:")
            obj_cols = self.df.select_dtypes(include="int32").columns
            print(obj_cols)

            choise = input("Do you want to replace a value in one of these columns? (yes/no): ")
            if choise.lower() != "yes":
                break

            col = input("Which column do you want to modify?: ")
            if col not in obj_cols:
                print("Invalid column. Try again.")
                continue

            find = eval(input("What value do you want to replace?: "))
            replace_value = eval(input("What should it be replaced with?: "))

            self.df[col] = self.df[col].replace(find, replace_value)
            print(f"Replaced '{find}' with '{replace_value}' in column '{col}'.")

        print("Final DataFrame:")
        print(self.df.head())
        return self.df

    def replace_null_value(self):
        for col in self.df.columns:
            print(f"\nColumn: {col}")
            choice = input("Do you want to replace NULL values in this column? (yes/no): ")
            if choice.lower() == "yes":
                replace_value = eval(input("Enter replacement value: "))
                self.df[col] = self.df[col].replace(to_replace={np.NaN: replace_value})

        return self.df
