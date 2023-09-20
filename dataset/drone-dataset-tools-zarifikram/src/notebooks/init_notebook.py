import os, sys
currentFolder = os.path.abspath('')
try:
    sys.path.remove(str(currentFolder))
except ValueError: # Already removed
    pass

# projectFolder = 'E:\\AV\\DataSetExploration\\drone-dataset-tools\\src'
projectFolder = 'D:\\Trimester 233\\Fydp-2\\Trajectory_imputation\\dataset\\drone-dataset-tools-zarifikram\\src'
# projectFolder = 'D:/AV/DataSetExploration/drone-dataset-tools/src'
sys.path.append(str(projectFolder))
os.chdir(projectFolder)
print( f"current working dir{os.getcwd()}")
