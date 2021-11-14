import csv
import pandas as pd 
import plotly.graph_objects as go 
import plotly.figure_factory as ff
import random
import statistics 

df = pd.read_csv('school1.csv')
data = df['Math_score'].tolist()

mean = statistics.mean(data)
std = statistics.stdev(data)

print(mean)
print(std)

def random_setofmean(counter):
    dataset = []
    for i in range(1,counter):      
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    setofmean = random_setofmean(100)
    mean_list.append(setofmean)

mean = statistics.mean(mean_list)
std = statistics.stdev(mean_list)

print('mean of sampling distribution-->',mean)
print('standard deviation-->',std)


##fig = ff.create_distplot([mean_list],['Math_score'], show_hist = False)
## fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.20],mode = 'lines', name = 'MEAN'))
## fig.show()

first_std_deviation_start, first_std_deviation_end = mean-std, mean+std
second_std_deviation_start, second_std_deviation_end = mean-(2*std), mean+(2*std)
third_std_deviation_start, third_std_deviation_end = mean-(3*std), mean+(3*std)

print("std1",first_std_deviation_start, first_std_deviation_end)
print("std2",second_std_deviation_start, second_std_deviation_end)
print("std3",third_std_deviation_start, third_std_deviation_end)

fig = ff.create_distplot([mean_list],['Math_score'],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = 'lines', name = 'MEAN'))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.show()

## print("mean of the data is {}".format(mean))
## print("mode of the data is {}".format(mode))
## print("median of the data is {}".format(median))
## print("standard deviation is {}".format(std))
## print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)))
## print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice_result)))
## print("{}% of data lies within 3 standard deviation".form
