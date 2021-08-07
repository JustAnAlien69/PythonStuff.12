#unsure why it isnt working
import pandas as pd
import statistics
import random

df = pd.read_csv("medium_data.csv")
data = df["responses"].tolist()


def getSampleAverage(number):
    samples=[]
    for i in range(1,number):
        a=random.randint(0,len(data)-1)
        b=data[a]
        samples.append(b)
    c=statistics.mean(samples)
    return(c)

def averageOfSampleAverages():
    allAverages=[]
    k=[]
    for i in range(1,100):
         x = getSampleAverage(100)
         allAverages.append(x)
    return(allAverages)

z = averageOfSampleAverages()

mean=statistics.mean(z)
standardDeviation=statistics.stdev(z)
print(mean,standardDeviation)

range1Start,range1End = mean-standardDeviation,mean+standardDeviation
range2Start,range2End = mean-2*standardDeviation,mean+2*standardDeviation
range3Start,range3End = mean-3*standardDeviation,mean+3*standardDeviation
range4Start,range4End = mean-4*standardDeviation,mean+4*standardDeviation

range1Array = [i for i in data if i > range1Start and i < range1End]
range2Array = [i for i in data if i > range2Start and i < range2End]
range3Array = [i for i in data if i > range3Start and i < range3End]
range4Array = [i for i in data if i > range4Start and i < range4End]

Range1Count = len(range1Array)
Range2Count = len(range2Array)
Range3Count = len(range3Array)
Range4Count = len(range4Array)
totalCount = len(data)

percentage_Range1 = Range1Count*100/totalCount
percentage_Range2 = Range2Count*100/totalCount
percentage_Range3 = Range3Count*100/totalCount
percentage_Range4 = Range4Count*100/totalCount

print(percentage_Range1,percentage_Range2,percentage_Range3,percentage_Range4)