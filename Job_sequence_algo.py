from dataclasses import dataclass

@dataclass
class Job:
    job_name:str
    profit:int
    deadline:int


# Inputs
job_names = ['J1','J2','J3','J4','j5']
profits = [50, 15, 10, 25,55]
deadlines = [2,1,2,1,3]


jobs = [] 
# adding jobs
for i in range(len(job_names)):
    jobs.append(Job(job_names[i],profits[i],deadlines[i]))

# sorting jobs based on profit
jobs = sorted(jobs,key = lambda x:x.profit,reverse=True) 


max_deadline = max(deadlines) 


job_sequence = [None] * max_deadline

# for counting jobs added to sequence
count = 0 


for job in jobs:
    if count >= max_deadline:
        break
    
    for i in range(job.deadline-1,-1,-1):
        if job_sequence[i] is None:
            job_sequence[i] = job.job_name,job.profit  
            count+=1
            break
            
print(job_sequence)