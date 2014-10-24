#! /usr/bin/env python
#Data CenterRecover
import sys
class Data_Center:
    #data center has a center_id and a collection of data sets in teh data_sets object
    def __init__(self, key):
        self.center_id=key
        self.data_sets=[]
    #This method takes a dictionary containing keys (of all the data sets) and entries of the first
    #data center that was observed with that data set and uses the dictinary to add necessary
    #values to the data_set (mising values) and returns a list of copy strategies used for each data set
    def add_data_set(self, data_set_dic):
        curr_strategy=[]
        for sets in data_set_dic:
            if sets not in self.data_sets:
                self.data_sets.append(sets)
                x=[sets, data_set_dic[sets], str(self.center_id)]
                curr_strategy.append(x)
        return curr_strategy
    
        
def Data_Center_Protocal():
    #strategy list is returned at the end of the function. It captures the strategies returned by add_data_set method calls
    #lines list will have the lines from the .txt file input in the command line in each entry
    #data_loc is a dictionary that will be used to maintain all the data_sets available.Keys are data sets and entries is the 1st center observed to have the givne entry.
    strategy=[]
    lines=[]
    data_loc={}
    
    for line in sys.stdin:
        lines.append(line.split())
    data_centers=lines[1:]
    #data center lines are maintained in the data_center list
             
    Set_of_Centers=[]
    #data center objects are maintained in the Set_of_Centers list
    num_centers=int(lines[0][0])
    #fills the Set_of_Centers list witht data_center objects and sets their center ids
    #also fills data_loc dictionary 
    for i in range(num_centers):
    
        Set_of_Centers.append(Data_Center(i+1))
        Set_of_Centers[i].data_sets=data_centers[i]
        for j in Set_of_Centers[i].data_sets:
            if j not in data_loc:
                data_loc[j]=str(Set_of_Centers[i].center_id)
    #checks for missing each data_center for missing data, adds the missing data, and gives the strategy list the necessary
    #strategies for filling the missing data sets
    for i in range(num_centers):
        dec=Set_of_Centers[i].add_data_set(data_loc)
        strategy=dec+strategy

    strategy.append("done")
    for i in range(len(strategy)):
        output=sys.stdout.write
        if i<len(strategy)-1:
            output( " ".join(strategy[i]))
            output('\n')
        else:
            output(strategy[i])
            output('\n')
    
   

    
Data_Center_Protocal()

                


    
