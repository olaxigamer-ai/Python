import pandas as pd

#part one: panda series
score=[98500,87200,76400,65100,54800]
players=pd.Series(score,index=['NightWolf','StarBlaze','PixelKing','CyberFox','IronStorm'])
print(players)

#part 2: creating data frame
data={
    'player':['NightWolf','StarBlaze','PixelKing','CyberFox','IronStorm'],
    'level':[42,38,35,30,27],
    'score':[98500,87200,76400,65100,54800],
    'wins':[210,185,162,140,118]
}
df=pd.DataFrame(data)

print(df)
#part 3: access rows using .LOC

print("First Row :",df.loc[0])
print("Second And third row :",df.loc[1:2])

#part 4: loding csv file and viewing data

load_file=pd.read_csv('leaderboard.csv')

print(load_file.head(2))

print(load_file.tail(3))

print(load_file.info())

#part 5: clean the data

print("Row with missing values removed by using dropna:")

cleandf=load_file.dropna()
print(cleandf.to_string())
print("Missing Values filled with 0 by using fillna:")

filldf=load_file.fillna(0)
print(filldf.to_string())