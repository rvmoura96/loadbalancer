from load_balancer import LoadBalancer
from server import Server
from user import User


with open("input.txt", "r") as file:
    filereader = file.readlines()


tasks = [int(i.rstrip("\n")) for i in filereader]
print(tasks)
TTASK = int(tasks[0])
UMAX = int(tasks[1])

load_balancer = LoadBalancer(TTASK, UMAX)

for i in tasks[2:]:
    load_balancer.assign_task_to_server(i)
    load_balancer.execute_users()
    load_balancer.calculate_total()
    # load_balancer.disconnect_users()
    print(f"{i} - {len(load_balancer.servers)} - {load_balancer.total_users}")

print(load_balancer.totalm)