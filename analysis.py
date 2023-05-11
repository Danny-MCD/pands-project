# Programming and Scripting Project
# Research of the Iris Fischers data set
# Author:   Daniel Mc Donagh



import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

irisdata = pd.read_csv('iris_data.csv')                                     # read in of the data set using pandas
pd.set_option("display.precision",2)                                        # rounds all table values to two decimal places



iris_summary = open("summary.txt","w")                                      # Created text file summary.txt for writing in data
print("These are the summary statistics for the Iris dataset.", file = iris_summary)
print ("\n", file = iris_summary)                                           # adds a line break

print("Presentation of the Fisher's Iris dataset", file = iris_summary)
print(irisdata, file = iris_summary)
print ("\n", file = iris_summary)                                           # adds a line break

print("Summary statistics using the describe function", file = iris_summary)
print(irisdata.describe(), file = iris_summary)                             # The describe() function shows count, mean, standard deviation, minimum, median, interquartile ranges
print ("\n", file = iris_summary)                                           # adds a line break

print("The statistical summary of the flower classes ", file = iris_summary)
print(irisdata.describe(include=['object', 'bool']), file = iris_summary)   # Describe function used to show statistics for the class of flower
print ("\n", file = iris_summary)                                           # adds a line break

print("The total number of records for each class", file = iris_summary)
print(irisdata['class'].value_counts(), file = iris_summary)                # Counts the number of records for each class 
print ("\n", file = iris_summary)                                           # adds a line break

print("Summary of each variable grouped by the flower class:", file = iris_summary)
print(irisdata.groupby(['class']).describe(), file = iris_summary)          # Summary of variables grouped by class




font1 = {'family':'oswald','color':'darkred','size':16}                     # creation of font1 to be used in plots
font2 = {'family':'oswald','color':'black','size':14}                       # creation of font2 to be used in plots


iris_virginica = irisdata[irisdata["class"] == "Iris-virginica"]            # data grouped by flower class for plotting
iris_versicolor = irisdata[irisdata["class"] == "Iris-versicolor"] 
iris_setosa = irisdata[irisdata["class"] == "Iris-setosa"]  


sns.set(style="darkgrid")                                                   # this sets the background colour of the grid


def histogram_plot(p1, p2, p3):                                             # creation of the histogram plot function with parameters p1, p2 and p3 to be passed in on execution
    sns.histplot(data = iris_virginica[p1], kde = False, label = 'Iris virginica', color = 'darkblue')      #Sets data to be used for each histogram to be taken from P1
    sns.histplot(data = iris_versicolor[p1], kde = False, label = 'Iris versicolor', color = 'yellow')      # Sets labels and colours of each iris species to distinguish them
    sns.histplot(data = iris_setosa[p1],  kde = False, label = 'Iris setosa', color = 'green')
    plt.xlabel(p2, fontdict = font2)                                                # Adds X label using font2 settings
    plt.ylabel("Frequency", fontdict = font2)                                       # Adds Y label using font2 settings
    plt.title("Histogram Plot of " + p2 + " by Flower Species", fontdict = font1)   # Adds title to plot using p2 parameter and using previously set font1 settings
    plt.grid(color = 'darkgrey', ls = '--', lw = 0.5)                               # Adds settings for grid (colour, style and spacing)
    plt.legend(loc='upper right')                                                   # plots legend in upper right location
    plt.savefig(p3)
    plt.show()


def histograms():                                                           # Passing in of values p1, p2 and p3 for execution of histograms  
    histogram_plot('sepallength', "Sepal Length", "sepal_length_histogram") 
    histogram_plot('sepalwidth', "Sepal Width", "sepal_width_histogram")
    histogram_plot('petallength', "Petal Length", "petal_length_histogram")
    histogram_plot('petalwidth', "Petal Width", "petal_width_histogram")



def scatterplot(p1, p2, p3, p4, p5):                    # Creation of scatterplot function with 5 parameters p1-p5 to be passed in on execution
    sns.scatterplot(data = irisdata, x = p1, y = p2, hue = "class", palette = "deep")           # Settings for scatterplots
    plt.xlabel(p3, fontdict = font2)                                                            # Sets X label and font settings used
    plt.ylabel(p4, fontdict = font2)                                                            # Sets Y label and font settings used
    plt.title("Scatterplot of " + p3 +" and " + p4 + " by Flower Species", fontdict = font1)    # Adds title using parameters P3 and P4 and font settings
    plt.grid(color = 'darkgrey', ls = '--', lw = 0.5)                                           # Settings for Grid (colour, style and spacing)
    plt.legend(loc='upper left')                                                                # sets legend location
    plt.savefig(p5)
    plt.show()


def scatterplots():                                     # Passing in of values p1-p5 for execution of scatterplots
    scatterplot("petallength", "petalwidth", "Petal Length", "Petal Width", "scatterplot_petal")
    scatterplot("sepallength", "sepalwidth", "Sepal Length", "Sepal Width", "scatterplot_sepal")
    scatterplot("petallength", "sepallength", "Petal Length", "Sepal Length", "scatterplot_petallength_sepallength")
    scatterplot("petalwidth", "sepalwidth", "Petal Width", "Sepal Width", "scatterplot_petalwidth_sepalwidth")



histograms()                                            # execution of histogrms
scatterplots()                                          # execution of scatterplots
