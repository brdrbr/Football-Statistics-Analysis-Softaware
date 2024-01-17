#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:01:04 2023

@author: derinberktay
"""

#Student ID: 1006031820
#Student name: Berke Derin Berktay
#Instructor: Maher Elshakankiri
#Course code:INF1340
#Course name: Programming for Data Science
#Program: MI
#Faculty of Information
#University of Toronto

# Midterm Project

# PLEASE READ THE README FILE FOR THE DETAILED EXPLANATION OF THE PROGRAM.

# Date Created: Oct 19, 2023



import math
import pandas as pd #Importing the required libraries

def takeinput():#function for taking an input filename
    filename = input("Please enter the file name that you want to provide for input in the format of '.....csv': ")
    return filename

def takeoutput():#function for taking an output filename
    filename = input("Please enter the file name that you want to provide for outputin the format of '.....txt': ")
    return filename

def max_function(content, leagueentry, metricentry):
    
    maxval = -100
    teamname = ""
    #case when not all top 5 leagues, but the specific league
    if leagueentry == "ENG" or leagueentry == "ESP" or leagueentry == "GER" or leagueentry == "ITA" or leagueentry == "FRA":    
        for index, row in content.iterrows():#iterating through the rows
            if row['Country'] == leagueentry:#if country matches with our league we compare the row values
                if int(row[metricentry]) >= maxval:# if current case bigger we make it the new max
                    maxval = int(row[metricentry])
                    teamname = row['Squad']# change the current max team
    #case when all leagues
    else:
        for index, row in content.iterrows():
            if int(row[metricentry]) >= maxval:
                maxval = int(row[metricentry])
                teamname = row['Squad']#same procedures as the above case
    return teamname, maxval
                    
                    


def min_function(content, leagueentry, metricentry):
    
    minval = 200000
    teamname = ""
    #case when not all top 5 leagues, but the specific league
    if leagueentry == "ENG" or leagueentry == "ESP" or leagueentry == "GER" or leagueentry == "ITA" or leagueentry == "FRA":    
        for index, row in content.iterrows():#iterating through the rows
            if row['Country'] == leagueentry:#if country matches with our league we compare the row values
                if int(row[metricentry]) <= minval:# if current case smaller we make it the new min
                    minval = int(row[metricentry])
                    teamname = row['Squad']# change the current min team
    #case when all leagues
    else:
        for index, row in content.iterrows():
            if int(row[metricentry]) <= minval:
                minval = int(row[metricentry])
                teamname = row['Squad']#same procedure as the above case
    return teamname, minval

def avg_function(content, leagueentry, metricentry):
    
    avgsum = 0
    avgval = 0
    counter = 0
    #case when not all top 5 leagues, but the specific league
    if leagueentry == "ENG" or leagueentry == "ESP" or leagueentry == "GER" or leagueentry == "ITA" or leagueentry == "FRA":    
        for index, row in content.iterrows():#iterating through the rows
            if row['Country'] == leagueentry:#if country matches with our league we compare the row value
                counter += 1 #increment value counter
                avgsum += row[metricentry]# sum up the new value to the average summer
        avgval = avgsum / counter#compute division to get the average value
        return leagueentry, avgval
    #case when all leagues
    else:
        for index, row in content.iterrows():
            counter += 1
            avgsum += row[metricentry]
        avgval = avgsum / counter#same procedure as the above case
                
    return "All Top 5 leagues", avgval
    

def popstddev_function(content, leagueentry, metricentry):
    
    ouravg = avg_function(content, leagueentry, metricentry)[1]#we call the average function to obtain the corresponding average value since we need it for calculations
    stddevsum = 0
    counter = 0
    #case when not all top 5 leagues, but the specific league
    if leagueentry == "ENG" or leagueentry == "ESP" or leagueentry == "GER" or leagueentry == "ITA" or leagueentry == "FRA":    
        for index, row in content.iterrows():#iterating through the rows
            if row['Country'] == leagueentry:#if country matches with our league we compare the row value
                counter += 1 #increment value counter
                stddevsum += ((row[metricentry] - ouravg)**2)# sum up the new stddev compenent to the sum (applying the formula)
        stddev = math.sqrt(stddevsum/ counter)#applying the formula
        return leagueentry, stddev
    #case when all leagues
    else:
        for index, row in content.iterrows():
            counter += 1
            stddevsum += ((row[metricentry] - ouravg)**2)
        stddev = math.sqrt(stddevsum/ counter)#same procedure as the above case
    return "All Top 5 leagues", stddev


    
def freq_of_occurence_function(content, leagueentry, metricentry):
    freqno = int(input("Please input the number that you want the frequency of occurence of: ")) #taking the occurence target number
    counter = 0
    teamlist = []
    #case when not all top 5 leagues, but the specific league
    if leagueentry == "ENG" or leagueentry == "ESP" or leagueentry == "GER" or leagueentry == "ITA" or leagueentry == "FRA":    
        for index, row in content.iterrows():
            if row['Country'] == leagueentry:
                if int(row[metricentry]) == freqno: #if our specific row's value matches:
                    teamlist.append(row['Squad']) # we append the team name to the list
                    counter += 1 #and increment the counter by one
    #case when all leagues
    else:
        for index, row in content.iterrows():
            if int(row[metricentry]) == freqno:
                counter += 1
                teamlist.append(row['Squad']) #same procedure as the above case
                
    return freqno, counter, teamlist
    
def compare_leagues(content, metricentry):
    avgs = {
        'England ' : avg_function(content, "ENG", metricentry)[1],
        'Germany ' : avg_function(content, "GER", metricentry)[1],
        'France ' : avg_function(content, "FRA", metricentry)[1],
        'Italy ' : avg_function(content, "ITA", metricentry)[1],
        'Spain ' : avg_function(content, "ESP", metricentry)[1],
        } #here we have a readymade dictionary with all league averages with the corresponding metric by calling in our previous average function
    sorted_avgs = sorted(avgs.items(), key=lambda item: item[1], reverse = True) # we sort the dictionary by descending order
    sorted_dict = dict(sorted_avgs)#conversion to a dictionary
    return sorted_dict

def get_team_rank(content, metricentry):
    team = input("Please type a team name: ") #we get our team as an input
    rankincountry = 1 # we start the process assuming our team is the first in rank, but we iterate it based on the comparisons later on
    ranktotal = 1
    country = ""
    value = 0
    
    for index, row in content.iterrows():#we get the current metric value of the team inputted that we are looking to find the rank of
        if row['Squad'] == team:
            country = row['Country']
            value = row[metricentry]
            break
    for index, row in content.iterrows():# iterating through for comparisons
        if row['Squad'] != team:
            if value <= row[metricentry]:# case when there is a higher rank, we increment the rank
                ranktotal += 1 
            if row['Country'] == country: #same procedure, but leagues also have to match here
                if value <= row[metricentry]:
                    rankincountry += 1
    return team, rankincountry, ranktotal
 
def correlation_on_metric(content, metricentry):
    secondmetric = input("Please enter the second metric for correlation analysis: ")
    
    firstmetricvals = content[metricentry].tolist()
    secondmetricvals = content[secondmetric].tolist()#conversion to list the metric values of all rows
    
    firstmetricmean = sum(firstmetricvals) / len(firstmetricvals)
    secondmetricmean = sum(secondmetricvals) / len(secondmetricvals) #computing the mean with built in functions
    
    firstsquarediffs = 0
    secondsquarediffs = 0
    for i in range(len(firstmetricvals)):
        firstsquarediffs += (firstmetricvals[i] - firstmetricmean) ** 2
        secondsquarediffs += (secondmetricvals[i] - secondmetricmean) ** 2 #computing the squared differences from the mean for each row

    firstmetricstddev = math.sqrt((firstsquarediffs / len(firstmetricvals)))
    secondmetricstddev = math.sqrt((secondsquarediffs / len(secondmetricvals))) #computing the std devs
    
    covariance = 0
    for i in range(len(firstmetricvals)):
        covariance += ((firstmetricvals[i] - firstmetricmean) * (secondmetricvals[i] - secondmetricmean))#applying the covariance formula for all the row cases with both of the metrics
        

    correlation = covariance / (firstmetricstddev * secondmetricstddev) / len(firstmetricvals) # applying the correlation formula
    
    return metricentry, secondmetric, correlation
        
        
def printandsave(distinguisher, output, leagueentry, metricentry, outputfile):
    #This function takes the output of the functions above, the metrientry provided, the leagueentry provided, the outputfilename provided and a distinguisher to distinguish between which functions (labeleld 1-8) have been used
    #then prints the output results and saves it to the output file provided as an input
    with open(outputfile, 'a') as file:
        if distinguisher == 1:
            if leagueentry != "All":
                message = "The maximum value of the " + metricentry + " performance metric in the league " + leagueentry + " was obtained by the team " + output[0] + " with the value of: " + str(output[1])
            else:
                message = "The maximum value of the " + metricentry + " performance metric in the pool of all top 5 leagues was obtained by the team " + output[0] + " with the value of: " + str(output[1])
        elif distinguisher == 2:
            if leagueentry != "All":
                message = "The minimum value of the " + metricentry + " performance metric in the league " + leagueentry + " was obtained by the team " + output[0] + " with the value of: " + str(output[1])
            else:
                message = "The minimum value of the " + metricentry + " performance metric in the pool of all top 5 leagues was obtained by the team " + output[0] + " with the value of: " + str(output[1])
        elif distinguisher == 3:
            if leagueentry != "All":
                message = "The average value of the " + metricentry + " performance metric in the league " + leagueentry + " is: " + str(output[1])
            else:
                message = "The average value of the " + metricentry + " performance metric in the pool of all top 5 leagues is: " + str(output[1])
        elif distinguisher == 4:
            if leagueentry != "All":
                message = "The standard deviation value of the " + metricentry + " performance metric in the league " + leagueentry + " is: " + str(output[1])
            else:
                message = "The standard deviation value of the " + metricentry + " performance metric in the pool of all top 5 leagues is: " + str(output[1])
        elif distinguisher == 5:
            if leagueentry != "All":
                message = "There are a total of " + str(output[1]) + " teams with the " + metricentry + " of " + str(output[0]) + " in the league: " + leagueentry + " and they are: "
            else:
                message = "There are a total of " + str(output[1]) + " teams with the " + metricentry + " of " + str(output[0]) + " in all the leagues and they are: "
            for i in range(len(output[2])):
                message += str(output[2][i])
                message += "\n"
        elif distinguisher == 6:
            message = "Based on the performance metric " + metricentry + " the top 5 leagues are ordered as follows in terms of their averages: "
            for key, value in output.items():
                message += str(key) +":" + str(value)
                message += "\n"
        elif distinguisher == 7:
            message = " The rank of the team " + str(output[0]) + " in terms of the performance metric " + metricentry + " is " + str(output[1]) + " in its domestic league and " + str(output[2]) + " overall in the top 5 leagues."
        elif distinguisher == 8:
            message = "The correlation between " + str(metricentry) + " and " + str(output[1]) + " is: " + str(output[2]) #giving closer insights regarding the correlation based on its value
            if output[2] > 0.7:
                message += "Therefore, there is a strong positive correlation."
            elif output[2] > 0.3:
                message += "Therefore, there is a moderate positive correlation."
            elif output[2] > -0.3:
                message += "Therefore, there is a weak correlation."
            elif output[2] > -0.7:
                message += "Therefore, there is a moderate negative correlation."
            else:
                message += "Therefore, there is a strong negative correlation."
        file.write(message + "\n") #save the message to the output file
        print(message) #print the message
    
filename = takeinput()
output_filename = takeoutput()
dummy = ""

with open(filename, 'r') as file:#open the file
    content = pd.read_csv(filename, encoding='ISO-8859-1', delimiter=';')#reading the corresponding csv file and assigning it to a variable called content
    print("Welcome to Derin's football season stats analysis software, here are the definitions of each function: \n"+#provided explanations for each task
          "1. This function outputs and saves the maximum of a performance metric (along with the team that obtained the value) either in a league or all top 5 leagues.\n" +
          "2. This function outputs and saves the minimum of a performance metric (along with the team that obtained the value) either in a league or all top 5 leagues.\n" +
          "3. This function outputs and saves the average of a performance metric either in a league or all top 5 leagues.\n" +
          "4. This function outputs and saves the standard deviation of a performance metric either in a league or all top 5 leagues. \n" +
          "5. This function outputs and saves the frequency of occurence of a specific value (and the teams that have this specific value)inside either a specified league or all top 5 leagues\n" +
          "6. This function outputs and saves the sorted order of the top 5 leagues based on their averages in the specificed performance rating\n" +
          "7. This function outputs and saves the rank of a team in terms of a performance metric amongst its own league and amongst the top 5 leagues\n" +
          "8. This function outputs and saves the correlation value between two performance ratings and gives insights on how strong the value is. \n" ) 
    while True:
        cur_input = input("Please type a number between 1 and 8 to display and save the output of the corresponding function, if you want to quit type 9: ")
        if cur_input == "9":
            break #if typed 9 end the program
        if cur_input != "1" and cur_input != "2" and cur_input != "3" and cur_input != "4" and cur_input != "5" and cur_input != "6" and cur_input != "7" and cur_input != "8":
            print("You have provided an invalid input, please retype a number between 1 and 9 and press enter!") #invalid output case
        else:
            metricentry = input("Enter corresponding metric: \n"+
                  "LgRk \n" +
                  "MP \n" +
                  "W \n" +
                  "D \n" +
                  "L \n" +
                  "GF \n" +
                  "GA \n" +
                  "GD \n" +
                  "Pts \n" +
                  "xG \n" +
                  "Attendance \n" ) #performance metric input
            
            if cur_input == "7" or cur_input == "8" or cur_input == "6": #call corresponding functions
                if cur_input == "6":
                    results = compare_leagues(content, metricentry) #league sort avgs based on a factor like xg
                    printandsave(6, results, dummy, metricentry, output_filename)
                elif cur_input == "7":
                    rank = get_team_rank(content, metricentry) #returns the rank of the team in their league and in top 5 league based on performance metric
                    printandsave(7, rank, dummy, metricentry, output_filename)
                elif cur_input == "8":
                    correlation = correlation_on_metric(content, metricentry) #how much a factor like attendance effects the points
                    printandsave(8, correlation, dummy, dummy, output_filename)
                    
            else: #cases when functions need the leagueentry
                
                leagueentry = input("Enter league pool: \n"+
                      "ENG \n" +
                      "ESP \n" +
                      "GER \n" +
                      "ITA \n" +
                      "FRA \n" +
                      "All\n" ) #league entry input
                
                if cur_input == "1": #call corresponding functions
                    ourmax = max_function(content, leagueentry, metricentry)
                    printandsave(1, ourmax,leagueentry, metricentry, output_filename)
                elif cur_input == "2":
                    ourmin = min_function(content, leagueentry, metricentry)
                    printandsave(2, ourmin, leagueentry, metricentry, output_filename)
                elif cur_input == "3":
                    ouravg = avg_function(content, leagueentry, metricentry)
                    printandsave(3, ouravg, leagueentry, metricentry, output_filename)
                elif cur_input == "4":
                    ourstddev = popstddev_function(content, leagueentry, metricentry)
                    printandsave(4, ourstddev, leagueentry, metricentry, output_filename)
                elif cur_input == "5":
                    ourfreqpair = freq_of_occurence_function(content, leagueentry, metricentry)
                    printandsave(5, ourfreqpair, leagueentry, metricentry, output_filename)
        