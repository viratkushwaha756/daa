class Job:
    def __init__(self, job_id, profit, deadline):
        self.job_id = job_id  
        self.profit = profit  
        self.deadline = deadline  
def job_scheduling(jobs, n):
   
    jobs.sort(key=lambda x: x.profit, reverse=True)

    result = [False] * n  
    
    job_sequence = [None] * n

    total_profit=0

    for job in jobs:
        for j in range(min(n, job.deadline) - 1, -1, -1):
            
            if not result[j]:
                result[j] = True  
                job_sequence[j] = job.job_id
                total_profit += job.profit  
                break

    return [job for job in job_sequence if job is not None],total_profit

if __name__ == "__main__":  
    num_jobs = int(input("Enter the number of jobs: "))
    jobs = []

    for i in range(num_jobs):
        job_id = input(f"Enter job ID for job {i + 1}: ")
        profit = int(input(f"Enter profit for job {job_id}: "))
        deadline = int(input(f"Enter deadline for job {job_id} (units of time): "))
        jobs.append(Job(job_id, profit, deadline))

    max_slots = max(job.deadline for job in jobs)
    optimal_schedule , total_profit = job_scheduling(jobs, max_slots)
    print("Optimal Job Schedule to Maximize Profit:", optimal_schedule)
    print("Total Profit from Scheduled Jobs:", total_profit)
