# Function to parse interface monitor output and create a trace
def parse_interface_monitor_output(interface_output):
    trace = []
    lines = interface_output.strip().split('\n')
    for line in lines:
        timestamp, txn_type, data = line.split()
        txn_info = {"Timestamp": int(timestamp)}
        txn_info["TxnType"] = txn_type
        if txn_type == "Rd":
            txn_info["Data"] = "-"
        else:
            txn_info["Data"] = data.strip("'")
        trace.append(txn_info)
    return trace


# Example interface monitor output
interface_output = """
0 Rd -
2 Wr 'hxxxxxxxx
4 Wr 'hyyyyyyyy
10 Rd 'hzzzzzzzz
15 Rd -
20 Wr 'haaaaaaaa
25 Rd 'hbbbbbbbb
30 Wr 'hcccccccc
35 Rd 'hdddddddd
40 Rd -
45 Wr 'heeeeeeee
50 Wr 'hffffffff
55 Rd 'hgggggggg
60 Wr 'hhhhhhhh
65 Rd 'x12345678
70 Wr 'x9abcdef0
75 Rd 'xdeadbeef
80 Wr 'xfeedface
85 Rd 'xabcdef09
90 Wr 'x87654321
95 Rd 'xfedcba98
100 Rd -
105 Wr 'x10203040
110 Wr 'x50607080
115 Rd 'x90a0b0c0
120 Wr 'xd0e0f000
125 Rd 'xfedcba98
130 Wr 'x76543210
135 Rd 'xabcdeff0
140 Wr 'x12345678
145 Rd 'xdeadbeef
150 Wr 'xfeedface
"""

# Assuming 32 bits data width
data_width = 32


# Function to calculate average latency
def calculate_average_latency(trace):
    total_latency = 0
    num_transactions = 0
    last_request_time = None

    for entry in trace:
        if entry['TxnType'] == 'Rd':
            request_time = entry["Timestamp"]
            if last_request_time is not None:
                latency = request_time - last_request_time
                total_latency += latency
                num_transactions += 1
            last_request_time = request_time

    if num_transactions == 0:
        return 0

    average_latency = total_latency / num_transactions
    return average_latency

# Function to calculate bandwidth


def calculate_bandwidth(trace, data_width):
    total_bytes_transferred = 0

    for entry in trace:
        if entry['TxnType'] == 'Wr':
            data = entry["Data"]
            if data != '-':
                # Convert bits to bytes
                total_bytes_transferred += len(data) // (data_width // 8)

    total_cycles = len(trace)
    if total_cycles == 0:
        return 0

    bandwidth = total_bytes_transferred / total_cycles
    return bandwidth

# Main function to process simulator output


def process_simulator_output(trace, data_width):
    average_latency = calculate_average_latency(trace)
    bandwidth = calculate_bandwidth(trace, data_width)

    # Print or store the results as needed
    print("Average Latency:", average_latency, "cycles")
    print("Bandwidth:", bandwidth, "bytes/cycle")


# Parse interface monitor output and create trace
trace = parse_interface_monitor_output(interface_output)

# Process simulator output
process_simulator_output(trace, data_width)
