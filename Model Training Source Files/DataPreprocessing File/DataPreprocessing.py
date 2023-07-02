import pandas as pd
import numpy as np

# Set median to null values in dataset
def mean(df,columns):
    for col in columns:
        median_value = df[col].median()
        df[col].fillna(median_value,inplace=True)

# Calculate a value for rankings
def calculating_overall_points(Player_points_overall_innings, Player_points_overall_runs, Player_points_overall_average, Player_points_strike_rate, Player_points_thirties, Player_points_fifties, Player_points_centuries):
    if(Player_points_overall_innings <= 0):
        return 0.0
    else:
        try:
            x = Player_points_overall_innings/Player_points_overall_runs
            y = (20 * Player_points_centuries) + (10 * Player_points_fifties) + (5 * Player_points_thirties)
            z = (0.3 * y) + (0.7 * Player_points_overall_average)
        except:
            x=0
            z=0
        return (x * z) * 10

# Reprocess dataset for train the model
def dataProcessing():
    df = pd.read_csv(r"D:\Disk_4\Projects\Cricket auction\ML Model Training\unique_player_records.csv")

    columns = ['away_strike_rate','away_runs','away_not_out_count','away_average',
               'total_away_ball_faced','away_zeros','away_30s','away_50s','away_100s',
               'home_runs','home_not_out_count','home_average','total_home_ball_faced',
               'home_strike_rate','home_zeros','home_30s','home_50s','home_100s']
    
    mean(df,columns)
 
    newCols = ['overall_Percentage','recent_Percentage','home_Percentage','away_Percentage']

    colNames = [['overall_innings','overall_runs','overall_average','strike_rate','thirties','fifties','centuries'],
                ['form_innings','form_runs','form_average','form_strike_rate','recent_30s','recent_50s','recent_100s'],
                ['home_innings','home_runs','home_average','home_strike_rate','home_30s','home_50s','home_100s'],
                ['away_innings','away_runs','away_average','away_strike_rate','away_30s','away_50s','away_100s']]
    
    for i in range(len(newCols)):
        arr = np.array([])
        for index, row in df.iterrows():
            value = calculating_overall_points(row[colNames[i][0]], row[colNames[i][1]], row[colNames[i][2]], row[colNames[i][3]], row[colNames[i][4]], row[colNames[i][5]], row[colNames[i][6]])
            arr = np.append(arr, value)

        # Calculate percentage from calculated values
        mx = max(arr)
        for j in range(len(df. index)):
            arr[j] = round((arr[j] + (arr[j]/50))*100/mx, 1)
        df[newCols[i]] = arr.astype(float)

    # Save new dataset to a .csv file
    df.to_csv('Player_Points_Stored.csv', index=False)
    
if __name__ == '__main__':
    dataProcessing()