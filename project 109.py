import statistics 
import plotly.express as px 
import plotly.figure_factory as ff 
import pandas as pd
import csv


df=pd.read_csv("Students.csv")
# fig=ff.create_distplot([df["reading(Pounds)"].tolist()],["reading"],show_hist=False)
# fig.show()
mathList=df["math"].to_list()
readingList=df["reading"].to_list()

mathMean=statistics.mean(mathList)
readingMean=statistics.mean(readingList)

mathMedian=statistics.median(mathList)
readingMedian=statistics.median(readingList)

mathMode=statistics.mode(mathList)
readingMode=statistics.mode(readingList)

math_stdev=statistics.stdev(mathList)
reading_stdev=statistics.stdev(readingList)

print("Mean,Median,Mode,standardDeviation of math is:- {},{},{} and {} respectively".format(mathMean,mathMode,mathMode,math_stdev))
print("Mean,Median,Mode,standardDeviation of reading is:- {},{},{} and {} respectively".format(readingMean,readingMode,readingMode,reading_stdev))

mathFirstStdevStart,mathFirstStdevEnd=mathMean-math_stdev,mathMean+math_stdev 
mathSecondStdevStart,mathSecondStdevEnd=mathMean-(2*math_stdev),mathMean+(2*math_stdev)
mathThirdStdevStart,mathThirdStdevEnd=mathMean-(3*math_stdev),mathMean+(3*math_stdev)

readingFirstStdevStart,readingFirstStdevEnd=readingMean-reading_stdev,readingMean+reading_stdev 
readingSecondStdevStart,readingSecondStdevEnd=readingMean-(2*reading_stdev),readingMean+(2*reading_stdev)
readingThirdStdevStart,readingThirdStdevEnd=readingMean-(3*reading_stdev),readingMean+(3*reading_stdev)

mathListOfDataWithin1stdev=[result for result in mathList if result>mathFirstStdevStart and result<mathFirstStdevEnd]
mathListOfDataWithin2stdev=[result for result in mathList if result>mathSecondStdevStart and result<mathSecondStdevEnd]
mathListOfDataWithin3stdev=[result for result in mathList if result>mathThirdStdevStart and result<mathThirdStdevEnd]

readingListOfDataWithin1stdev=[result for result in readingList if result>readingFirstStdevStart and result<readingFirstStdevEnd]
readingListOfDataWithin2stdev=[result for result in readingList if result>readingSecondStdevStart and result<readingSecondStdevEnd]
readingListOfDataWithin3stdev=[result for result in readingList if result>readingThirdStdevStart and result<readingThirdStdevEnd]

print("{} percentage(%) of data for math lies within 1standard deviation".format(len(mathListOfDataWithin1stdev)*100.0/len(mathList)))
print("{} percentage(%) of data for math lies within 2standard deviation".format(len(mathListOfDataWithin2stdev)*100.0/len(mathList)))
print("{} percentage(%) of data for math lies within 3standard deviation".format(len(mathListOfDataWithin3stdev)*100.0/len(mathList)))

print("{} percentage(%) of data for reading lies within 1standard deviation".format(len(readingListOfDataWithin1stdev)*100.0/len(readingList)))
print("{} percentage(%) of data for reading lies within 1standard deviation".format(len(readingListOfDataWithin2stdev)*100.0/len(readingList)))
print("{} percentage(%) of data for reading lies within 1standard deviation".format(len(readingListOfDataWithin3stdev)*100.0/len(readingList)))