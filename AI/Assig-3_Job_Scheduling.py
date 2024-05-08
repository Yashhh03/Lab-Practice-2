def jobScheduling(arr,t):
    n = len(arr)
    arr.sort(key=lambda x:x[2],reverse=True)
    result = [False] * t
    job = []
    for i in range(n):
        for j in range(min(i,arr[i][1]-1),-1,-1):
            if not result[j]:
                result[j] = True
                job.append(arr[i][0])
                break
    print("Job Scheduling: ",job)

if __name__ == '__main__':
    num_jobs = int(input("Enter the number of jobs: "))
    arr = []

    for i in range(num_jobs):
        job_name = input(f"Enter the name of job {i+1}: ")
        deadline = int(input(f"Enter the deadline of job {job_name}: "))
        profit = int(input(f"Enter the profit of job {job_name}: "))
        arr.append([job_name,deadline,profit])

    total_slots = int(input("Enter the total number of slots: "))
    print("Solution of Job Scheduling: ")
    jobScheduling(arr,total_slots)
