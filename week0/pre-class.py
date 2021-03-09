#problem 1
THICKNESS = 0.00008
folded_thickness = THICKNESS * pow(2,43)
print("Thickness: {} meters".format(folded_thickness))

#problem 2
print("Thickness: {:.2f} kilometers".format(folded_thickness/1000))

#problem 3
p = 1
for i in range(43):
    p = p * 2

#problem 4
import time
import timeit
start = time.time()
p = 1
for i in range(43):
    p = p * 2
elapsed_time = time.time() - start
print("time : {}[s]".format(elapsed_time))

# %timeit
# p = 1
# for i in range(43):
#     p = p * 2

#problem 5
thicknessList = [THICKNESS]
for i in range(43):
    thicknessList.append(thicknessList[i]*2)
print(len(thicknessList))

#problem 6
import matplotlib.pyplot as plt
#%matplotlib inline
plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.tick_params(labelsize=20) # Make settings related to axis values
plt.plot(thicknessList, color = 'red') # Enter the variable name of the list in "List name"
plt.show()
