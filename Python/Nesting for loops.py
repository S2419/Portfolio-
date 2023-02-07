#Create a nested for loop with the outer loop having 3 items/elements and the inner loop having 5 items/elements
#Print to the screen in groups so the outer loop is grouped with the 5 inner loop items
#-So item 1 from outer loop should print with the 5 inner/nested loop, then repeat

leads = ['Mark','Bob','Sara']
departments=['IT','Public Relations','Human Resources', 'Sales','Administration']

for x in leads:
         print(x)
         for y in departments:
             print(y)
         print("\n")
