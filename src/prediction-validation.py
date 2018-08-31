import pandas as pd
actual = data = pd.read_csv('./input/actual.txt', sep="|", header = None)
predicted = pd.read_csv('./input/predicted.txt', sep="|", header = None)
windowFile = open("./input/window.txt")
window = int(windowFile.read())
windowFile.close()

stockDict = {}
for i, row in actual_df.iterrows():
    if row[0] in stockDict:
        stockDict[row[0]][row[1]] = row[2]
    else:
        stockDict[row[0]] = {}
        stockDict[row[0]][row[1]] = row[2]

predicted['error'] = predicted.apply(lambda x : abs(stockDict[x[0]][x[1]]- x[2]), axis = 1)

finalHour = predicted.iloc[- 1, 0]
file = open("./output/comparison.txt","w")
for i in range(1, finalHour - (window-2)):
    error = round(predicted[(predicted[0] >= i) & (predicted[0] <= i + window - 1)]['error'].mean(), 2)
    file.write("" + str(i) + "|" + str(i+window-1) + "|" + str(error) + "\n")
    
file.close()
