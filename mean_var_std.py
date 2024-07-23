import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    # Convert to Array and Flatten
    listToArray = np.array(list)
    listToArray = listToArray.reshape((3,3))
    flattenedArray = listToArray.flatten('F')

    # Calculate Mean
    meanFlattend = np.mean(flattenedArray)
    meanAxis0 = np.mean(listToArray, axis=0)
    meanAxis1 = np.mean(listToArray, axis=1)
    meanAxis0ToList = meanAxis0.tolist()
    meanAxis1ToList = meanAxis1.tolist()
    meanflattend = meanFlattend.tolist()

    # Calculate Variance
    varFlattend = np.var(flattenedArray)
    varAxis0 = np.var(listToArray, axis=0)
    varAxis1 = np.var(listToArray, axis=1)
    varAxis0ToList = varAxis0.tolist()
    varAxis1ToList = varAxis1.tolist()
    varflattend = varFlattend.tolist()

    # Calculate Standard Deviation
    stdFlattend = np.std(flattenedArray)
    stdAxis0 = np.std(listToArray, axis=0)
    stdAxis1 = np.std(listToArray, axis=1)
    stdAxis0ToList = stdAxis0.tolist()
    stdAxis1ToList = stdAxis1.tolist()
    stdflattend = stdFlattend.tolist()

    # Calculating Max
    maxFlattend = np.max(flattenedArray)
    maxAxis0 = np.max(listToArray, axis=0)
    maxAxis1 = np.max(listToArray, axis=1)
    maxAxis0ToList = maxAxis0.tolist()
    maxAxis1ToList = maxAxis1.tolist()
    maxflattend = maxFlattend.tolist()

    # Calculating Min
    minFlattend = np.min(flattenedArray)
    minAxis0 = np.min(listToArray, axis=0)
    minAxis1 = np.min(listToArray, axis=1)
    minAxis0ToList = minAxis0.tolist()
    minAxis1ToList = minAxis1.tolist()
    minflattend = minFlattend.tolist()

    # Calculating Sum
    sumFlattend = np.sum(flattenedArray)
    sumAxis0 = np.sum(listToArray, axis=0)
    sumAxis1 = np.sum(listToArray, axis=1)
    sumAxis0ToList = sumAxis0.tolist()
    sumAxis1ToList = sumAxis1.tolist()
    sumflattend = sumFlattend.tolist()

    # Final Result
    calculations = {'mean':[meanAxis0ToList, meanAxis1ToList, meanflattend],
    'variance':[varAxis0ToList, varAxis1ToList, varflattend],
    'standard deviation':[stdAxis0ToList, stdAxis1ToList, stdflattend],
    'max':[maxAxis0ToList, maxAxis1ToList, maxflattend],
    'min':[minAxis0ToList, minAxis1ToList, minflattend],
    'sum':[sumAxis0ToList, sumAxis1ToList, sumflattend]}
    return calculations

# try:
    # hello = calculate([2,6,2,8,4,0,1,3])
    # print(hello)
# except ValueError as e:
    # print(e)