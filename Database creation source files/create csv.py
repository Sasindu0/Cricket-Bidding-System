import pandas as pd

input_file = r"D:\Disk_4\Projects\Cricket auction\db creation\Player_Points_Stored.csv"
output_file = r"D:\Disk_4\Projects\Cricket auction\db creation\Updated.csv"

df = pd.read_csv(input_file)

filtered_df = df[(df['overall_innings'] >= 5)]

filtered_df.to_csv(output_file, index=False)
