n = int(input("Enter the number of jobs --> "))
job = [i for i in range(1, n+1)]
print("Enter the deadline of the jobs")
d = list(map(int, input().split()))
print("Enter the profit of the jobs")
p = list(map(float, input().split()))

c = []
s = []
profit = 0

for i in range(max(d)):
    s.append("0")

for i in range(n):
    for j in range(i+1, n):
        if p[i] < p[j]:

            temp = p[i]
            p[i] = p[j]
            p[j] = temp

            temp = d[i]
            d[i] = d[j]
            d[j] = temp

            temp = job[i]
            job[i] = job[j]
            job[j] = temp
    c.append(0)

for i in range(n):
    for j in range(0, d[i]):
        t = d[i] - j - 1
        if c[t] == 0:
            c[t] = 1
            s[t] = str(job[i])
            profit += p[i]
            break

sequence = " - ".join(s)
print("Job Sequence is:", sequence)
print("Maximum Profit:", profit)