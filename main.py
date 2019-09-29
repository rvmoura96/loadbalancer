from load_balancer import LoadBalancer


with open("input.txt", "r") as file:
    filereader = file.readlines()

tasks = [int(i.rstrip("\n")) for i in filereader]
TTASK = int(tasks[0])
UMAX = int(tasks[1])

load_balancer = LoadBalancer(TTASK, UMAX)
tasks = tasks[2:]

for i in tasks:
    load_balancer.run_tasks()
    load_balancer.assign_task_to_server(i)
    load_balancer.calculate_user()
    print(load_balancer.output())

while len(load_balancer.servers):
    load_balancer.run_tasks()
    load_balancer.calculate_user()
    print(load_balancer.output())

print(load_balancer.total)
