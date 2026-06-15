# Class representing a Job
class Job:
    def __init__(self, id, dead, profit):
        self.id = id          # Job ID
        self.dead = dead      # Deadline
        self.profit = profit  # Profit


def JobScheduling(arr, n):

    # sort jobs in decreasing order of profit
    arr.sort(key=lambda job: job.profit, reverse=True)
    # find the maximum deadline
    max_deadline = max(job.dead for job in arr)

    # track occupied time slots (-1 means empty)
    slot = [-1] * (max_deadline + 1)

    count_jobs = 0
    total_profit = 0

    # try scheduling each job
    for i in range(n):

        # Schedule the job as late as possible
        for j in range(arr[i].dead, 0, -1):
            # If the slot is free
            if slot[j] == -1:
                slot[j] = arr[i].id   # Assign the job
                count_jobs += 1
                total_profit += arr[i].profit
                break

    return count_jobs, total_profit


# Driver Code
if __name__ == "__main__":

    arr = [
        Job(1, 4, 20),
        Job(2, 1, 10),
        Job(3, 2, 40),
        Job(4, 2, 30)
    ]

    n = len(arr)

    jobs_done, profit = JobScheduling(arr, n)

    print("Jobs Done:", jobs_done)
    print("Total Profit:", profit)