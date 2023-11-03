import heapq
from prettytable import PrettyTable


def schedule_events(arrivals, service_time, num_servers):
    clock_time = 0
    waiting_customers = []
    num_servicing = 0
    busy_time = 0
    schedule = []
    future_events = []

    pq = [(arrival_time, 'Arrival', i)
          for i, arrival_time in enumerate(arrivals)]
    heapq.heapify(pq)

    while pq:
        event_time, event_type, i = heapq.heappop(pq)
        busy_time += num_servicing * (event_time - clock_time)
        clock_time = event_time

        if event_type == 'Arrival':
            if num_servicing < num_servers:
                num_servicing += 1
                end_time = clock_time + service_time[i]
                heapq.heappush(pq, (end_time, 'Departure', i))
            else:
                waiting_customers.append(i)
                future_events.append(('Arrival', arrivals[i]))
                schedule.append(('Arrival', event_time, '-'))
        else:
            num_servicing -= 1
            schedule.append(('Departure', event_time, '-'))
            if len(waiting_customers) > 0:
                next_customer = waiting_customers.pop(0)
                num_servicing += 1
                end_time = clock_time + service_time[next_customer]
                heapq.heappush(pq, (end_time, 'Departure', next_customer))
                future_events.append(('Departure', end_time))
            else:
                future_events.append('-')

    x = PrettyTable()
    x.field_names = ["Event Type", "Event Time", "Future Events"]
    for i in range(len(schedule)):
        x.add_row([schedule[i][0], schedule[i][1], future_events[i]])

    print(x)


arrivals = [8, 6, 1, 8, 2, 8]
service_time = [4, 1, 4, 3, 2, 4]
num_servers = 1

schedule_events(arrivals, service_time, num_servers)
