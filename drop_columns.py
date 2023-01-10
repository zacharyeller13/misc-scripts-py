import pandas as pd
from pathlib import Path

def drop_columns(in_file: str, value_count: int) -> int:
    "Given a csv file, drop all columns with < 5 values, write to a new csv"

    out_file = f"{Path(in_file).parent}/{Path(in_file).stem}_01.csv"

    try:
        df = pd.read_csv(in_file, encoding="ANSI")

        columns_to_drop = df.columns[df.count() < value_count]
        df = df.drop(columns=columns_to_drop)
    except PermissionError:
        print(f"Could not read in_file {in_file} due to a permission error")
        return 1

    try:
        df.to_csv(out_file, index=False)
    except PermissionError:
        print(f"Could not write to out_file {out_file} due to a permission error")
        return 1
        
    return 0

if __name__ == "__main__":

    in_file = input("Absolute Filepath: ")
    value_count = int(input("Input min number of required values: "))

    drop_columns(in_file, value_count)
