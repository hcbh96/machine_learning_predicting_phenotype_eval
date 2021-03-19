""" ------------------------------------------
    Processing and saving data for furthur use
    __________________________________________
"""
import rpy2.robjects as robjects
robjects.r['load']("data/cross.Rdata")

cross = robjects.r['cross']

print(cross)

