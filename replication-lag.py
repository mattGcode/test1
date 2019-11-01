import pandas as pd
import re

#csv file generation

fh2 = open('/Users/mathewgeorge/Documents/Cases/Manoj-Logs/pub-logs/PolicyManagerLogs/tips-db/lag_csv.csv', 'w')


with open('/Users/mathewgeorge/Documents/Cases/Manoj-Logs/pub-logs/PolicyManagerLogs/tips-db/tipsdb.log', 'r') as fh:
    for line in fh:
        line = line.strip()
        a = re.split(' |=',line)
        #        print(len(a),  a)
        if "relative lag" in line:
            #print(a[19]+ " "+a[15])
            fh2.write(a[19]+','+a[15]+'\n')

    fh2.close()



pd.options.display.max_rows = 1200
pd.options.display.max_colwidth = 1000

# to-do: load from pandas

columns = ['Node ID','Relative Lag']

pandas_load = pd.read_csv('/Users/mathewgeorge/Documents/Cases/Manoj-Logs/pub-logs/PolicyManagerLogs/tips-db/lag_csv.csv', names= columns, header= None)

#print(pandas_load)

#print(pandas_load['Node ID'].dtype)

b = pandas_load.sort_values(by=['Node ID'], ascending=True)

series = b['Relative Lag']

c = series.value_counts(sort=True)
#print(c[:30])

print(b)

