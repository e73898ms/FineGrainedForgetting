import sys
import os
import subprocess
import shutil

java = "Java-12 Path"
jar = "Path to jar file"
repository = "Path to input ontologies"
outRep = "Output directory"
experimentScript = "Path to the single experiment script"
coverage=100

for i in range(1, 91):
    name = "experiment" + str(i)
    outDir = outRep + name
    os.makedirs(outDir)
    try:
        os.makedirs(outDir)
    except FileExistsError:
        print ("Output directory exists. Directory will be emptied and recycled")

    for file in os.listdir(outDir):
        file_path = os.path.join(outDir, file)
        try:
            if os.path.isfile(file_path):
                if file != "output.log":
                    os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

    print(name + " started")
    with open(outDir + '/output.log', 'w') as out:
        executorCmd = "python {script} -n {name} -c {coverage}}".format(script=experimentScript, name=name,coverage=coverage)
        subprocess.call(executorCmd, stdout=out, stderr=out)
    print(name + " complete")

summaryPath = outRep + "summary.csv"
if os.path.isfile(summaryPath):
    os.unlink(summaryPath)
    # print("Summary file exists. Statistics will be appended to file.")

summaryFile = open(summaryPath, "w+")
summaryFile.write("Experiment,O Size,Sig Size,Different Result?,Semantic View Time,Reduction Time,Excluded Clauses,Lethe Time")
summaryFile.close()



summaryCmd = '{java} -cp {jar} {prog} -repo {repo} -outFile {outFile}'.format(java=java,
                                                                              jar=jar,
                                                                              prog="uk.ac.man.OfflineSummaryGenerator",
                                                                              repo=outRep,
                                                                              outFile=summaryPath)

print(summaryCmd, flush=True)
returned_value = subprocess.call(summaryCmd,shell=True)
