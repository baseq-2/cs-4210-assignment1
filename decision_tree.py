#-------------------------------------------------------------------------
# AUTHOR: Gabriel Fok
# FILENAME: decision_tree.py
# SPECIFICATION: create a decision tree based on the given data
# FOR: CS 4210- Assignment #1
# TIME SPENT: 10 hours
#-----------------------------------------------------------*/
#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard dictionaries, lists, and arrays
#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv

db = []
X = []
Y = []
#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            db.append (row)
            print(row)
#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
# X =
for row in db:
    temp = []
    for i in range(4):
        if row[i] == 'Young' or row[i] == 'Myope' or row[i] == 'Yes' or row[i] == 'Normal':
            temp.append(1)
        elif row[i] == 'Prepresbyopic' or row[i] == 'Hypermetrope' or row[i] == 'No' or row[i] == 'Reduced':
            temp.append(2)
        elif row[i] == 'Presbyopic' or row[i] == 'No':
            temp.append(3)
    X.append(temp)
    print(temp)
#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =
for row in db:
    if row[4] == 'Yes':
        Y.append(1)
    elif row[4] == 'No':
        Y.append(2)
    print(Y)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)
#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'],
class_names=['Yes','No'], filled=True, rounded=True)
plt.show()
