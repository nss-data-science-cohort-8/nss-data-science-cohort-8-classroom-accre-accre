column | description
-------|---------
JOBID | The identification number of the job or job step. Array jobs are in the form ArrayJobID_ArrayTaskID
STATE | Job state or status (COMPLETED, CANCELLED, FAILED, TIMEOUT, PREEMPTED, etc.)
BEGIN | Beginning time for the job.
END | Ending time for the job.
REQMEM | Requested memory in megabytes. May be per-core (Mc) or per-node (Mn)
USEDMEM | Used memory in megabytes per-node
REQTIME | Requested time in d-hh:mm:ss or hh:mm:ss
USEDTIME | Used time in d-hh:mm:ss or hh:mm:ss
NODES | Number of servers used for this job
CPUS | Total number of CPU-cores allocated to the job
PARTITION | Identifies the partition on which the job ran.
EXITCODE | The exit code returned by the job script or salloc, typically as set by the exit() function. Following the colon is the signal that caused the process to terminate if it was terminated by a signal.