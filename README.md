This file gives information on the content of this repository and on the usage of the scripts and executables.

Contents
--------
The repository is structured as follows:

-
 - lib: Library folder
   - lethe-dep-2.11.jar: A jar file that contains a build of lethe with all dependencies.
   - fine-grained-forgetting.jar: A jar file that contains a build of our system with all dependencies.
 - ontologies: A folder of experiment ontologies. All ontologies are in OWL format.
   - conceptcoverage: A folder that contains coverage information about the concepts that appear in the ontologies.
 - scripts:
   - batchOfflineExperiment.py: A python script that runs a set of experiments. Each experiment runes offlineExperiment.py.
   - offlineExperiment.py: A python script that runs a single experiment.


Experiment Data
---------------
All experiment data is contained in the folder ontologies. The folder contains ninety ontology files in the OWL format. These are the ontologies that we created in prepare for the experiments.
Each ontology has a corresponding csv file in the conceptcoverage folder.
The file contains information about the concept names that appear in the ontology.
This file is used to determine the forgetting signature in each experiment


Running the Scripts
-------------------
The main script is batchOfflineExperiment.py.
This script runs a batch of experiments and then collects the results in a summary csv file.
To run this script, please modify the variables at the top of the script to the correct values.
You can change the coverage variable to influence the selection of the forgetting signature. The current value of this variable is 100, this means that the forgetting signature must appear in 100% of the ontology, which maps to the Moderate setting in our experiment. The Low and High settings are obtained at coverage values 50 and 150 respectively.
The main loop in the script is used to determine the ontologies that will be used in the experiment.
For example, to run the Low experiment setting on the first thirty ontologies, please change the loop to run from 1 to 31(, and change the coverage variable to 50).

Each experiment invokes offlineExperiment.py. The script computes the deductive forgetting view using our prototype and Lethe, and compares the forgetting views.
Variables at the top of the script should be modified to the correct values.
The variables "coverage" and "experimentName" are passed from batchOfflineExperiment.py.
If you want to run this script directly, the "coverage" and "experimentName" values must be passed directly to the script. For example:
    python offlineExperiment.py -n 20 -c 50
This will run the experiment on ontology20 in the Low setting.
