file1 = open("CSC495Data.txt", "r")
data_file = file1.read()
traffic = data_file.split('\n')

throughput = []

count = 0
total = 0

for data in traffic:
    if len(data) > 1:
        y, x = data.split(',')
        throughput.append(float(y))

for traffic in throughput:
    total += traffic
    count += 1

print "Max: %d" % max(throughput)
print "Min: %d" % min(throughput)
print "Avg: %d" % (total/count)