This folder is submitted by Srinivasaraghavan Seshadhri R00195470 for Assignment 2 of Meta Heuristic Optimization. The folder contains the following files.

My Workstation Computer where all the code were run Specifications:

Processor: i7 8750H 6 cores 12 Threads base clock: 2.2GHz
Memory: 16GB DDR4
OS: Ubuntu 20.04
Clock Speed: Turboed from 2.4GHz to 2.7GHz based on thermal limitations (Stayed around 85 degree C)

Part 2 Files:
HillClimbing_no_side.py :
It is a file given for assignment which has been modified to remove the side movements. No other change as been made in it.

HillClimbing.py :
It is a file given for assignment where no other change as been made in it.

Queens.py :
It is a file given for assignment where no other change as been made in it.

RTD_Q_launcher.py:
It is a program that is made to run the Hillclimbing with different iterations and restart values with and without side and save the results in output_pooled_1.txt
It was run in linux terminal with the &>, for example python RTD_Q_launcher.py &> output_pooled_1.txt to capture all the outputs with runtime into the specified txt file.

output_pooled_1.txt:
It is the output file of RTD_R_launcher.py which contains all the stored output. However a "\n" was missed in the code and hence some of the outputs were in the same line. So those were manually cleaned, by moving them to the next line.

result_gen.ipynb is the ipythonnotebook which contains the analysis for the RTD - Recommended to run locally in any software that supports ipynb (Jupyter Notebook for example)


Part 1 Files:

inst-7.tsp,inst-19.tsp,inst-20.tsp are the tsp files given for doing the assignment and are not modified.

TSP_A2_R00195470.py:
It contains the code for running the basic2opt and the 2 variants. It has no sysargs and can be run directly.

Folder 'results' contain the outputs generated by the above py file. It basically appends the output to the txt files. 
It stores the output in 2 files where one has the program running outputs and the other file contains the time taken for the operation.
Eg: "inst-7.tsp VAR 0.txt" has the outputs for the run whilst "inst-7.tsp VAR 0 time.txt" contains the time taken for the operation.


Folder 'plots' contains the images of the latest TSP run in TSP_with_graphics.ipynb where it stores the initial and solved images for each of TSPs.

tsp_inst_19_first_variant.mov video is a 10 second file which consists a sample of what the TSP_with_graphics.ipynb runs. It has the video of first variant solving the inst-19.tsp file.

TSP_with_graphics.ipynb shows the live solving of the TSP. HIGHLY recommended to run only in Jupyter Notebook.



RECOMMENDED ORDER TO VIEW THE FILES for best EXPERIENCE:

PART 1:
1) tsp_inst_19_first_variant.mov #See video
2) TSP_with_graphics.ipynb # See VISUAL Solving file
3) Images in the plots folder #See more outputs
4) TSP_A2_R00195470.py #See full code with detailed explanation with parallel running
5) results folder #Outputs

PART 2:
1) HillClimbing_no_side.py #Quick look, nothing much here
2) RTD_Q_launcher.py #Main code for part 2 running
3) output_pooled_1.txt #Output file
4) RT_results_data.xlsx #Extracted data from output file
5) result_gen.ipynb #Analysis and visualizing file