## The Advanced Computing Center for Research and Education

The Advanced Computing Center for Research and Education (ACCRE) is a computer cluster serving the high-performance computing needs of research for Vanderbilt University. In this data question, you will be analyzing data on jobs run on ACCRE's hardware.

When a job is submitted to ACCRE, it goes through the [slurm scheduler](https://slurm.schedmd.com/documentation.html), which tracks and manages compute and memory resources. For this project, your main objective is to investigate a potential cause of the scheduler to become unresponsive.

It is hypothesized that the slurm scheduler is processing so many job completions so frequently that it sometimes becomes unresponsive to commands from users trying to schedule new jobs or check job status. This is a particularly bad problem for clients who use automated submission systems, such as members of the Open Science Grid. The goal of this project is to investigate the hypothesis that lots of job completions in a short time period are causing the scheduler to be unresponsive, and determine the rough threshold at which it becomes an issue.

You have been provided three datasets for this task:
* **fullsample.csv**: This file contains output for jobs run through the slurm scheduler.
* **slurm_wrapper_ce5.log** and **slurm_wrapper_ce6.log**: Logs of every slurm command that a pair of servers, ce5 and ce6, executed, how long it took, and if it succeeded. These servers connect ACCRE's local cluster to the Open Science Grid and submit jobs to slurm on behalf of the grid.

Job completions can be identified by looking at the fullsample csv and loking for jobs with exit code 0:0 in the "COMPLETED" state.

To identify periods of unresponsiveness, use the two log files. Look for records that are the "sbatch" command from user 9204 (the test user) that have return code 1 and an execution time of greater than 15 seconds.

At the end of the project, your group will deliver a 10-15 minute presentation showing your findings and conclusions about this question. Do you find evidence to support the hypothesis that the scheduler is more likely to be unresponsive during periods of a high number of job completions? Your presentation can include any exploratory analysis that you did to work towards answering the main question. 