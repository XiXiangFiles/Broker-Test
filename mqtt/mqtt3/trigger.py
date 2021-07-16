import os
import json
import time

result = {}
times = 1000000

result['start'] = time.time()
os.system("./scripts/publisher.sh")
result['end'] = time.time()

start = result['start'] * 10000000
end = result['end'] * 10000000
sub = int(end- start)
result['tps'] = (times/sub) * 10000000

print(json.dumps(result))