# Event-Scheduling-Algorithm
This Python script simulates a simple queueing system using event-driven simulation. The system comprises customers arriving at a service facility and being served by a given number of servers. The code uses the heapq library to manage events, such as customer arrivals and departures, and PrettyTable for displaying the simulation results.

## Working
The code simulates the behavior of customers arriving and departing from the service facility. It keeps track of events, such as arrivals and departures, and calculates key metrics like the busy time of the service facility.

The simulation follows these steps:

1. Initialize variables and data structures.
2. Create an event queue using heapq.
3. Push arrival events onto the event queue.
4. Process events in chronological order.
5. Update the state of the system accordingly (e.g., when a customer arrives, they are either served immediately or added to a waiting queue).
6. Record events and future events as the simulation progresses.
7. Display the simulation results in a table format using PrettyTable.

## Usage
- Clone or download the repository to your local machine.
  ```sh
  git clone https://github.com/mayankpujara/Event-Scheduling-Algorithm.git
- Install the required libraries if you haven't already.
  ```sh
  pip install prettytable
- Modify the arrivals, service_time, and num_servers variables to match your specific queueing system parameters. You can provide your own list of arrival times, service times, and the number of servers.
- Run the script by executing it with Python
  ```sh
  python scheduling_algorithm.py

## Example
The provided example uses the following input parameters:

- Arrival times: [8, 6, 1, 8, 2,]
- Service times: [4, 1, 4, 3, 2, 4]
- Number of servers: 1<br>
After running the simulation, the code will output the results in a tabular format, showing events and future events.

## Author
Mayank Pujara
