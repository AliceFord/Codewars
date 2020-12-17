def ips_between(start, end):
    start = start.split(".")
    end = end.split(".")
    ips = [int(end[i]) - int(start[i]) for i in range(len(start))]
    return ips[0] * 16777216 + ips[1] * 65536 + ips[2] * 256 + ips[3]

print(ips_between("10.0.0.0", "10.0.0.50"))