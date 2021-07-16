import matplotlib.pyplot as plt
import numpy as np
from numpy.random.mtrand import pareto
import pandas as pd

folder = ['1', '3', '5', '7', '10']
mqtt3_sub_data = {"pub": {"1": {"tps": 8403.317537608717}, "3": {"tps": 8156.231136991885}, "5": {"tps": 8074.845220997508}, "7": {"tps": 8096.835585475652}, "10": {"tps": 8118.081194789408}}, "sub": {"1": {"tps": 290.19004687399166, "qos": 34.480000000000004}, "3": {"tps": 281.64385665383605, "qos": 34.48000000000001}, "5": {"tps": 278.86424664849585, "qos": 34.48000000000001}, "7": {"tps": 279.6864178799534, "qos": 34.48000000000001}, "10": {"tps": 280.31562658104986, "qos": 34.48000000000001}}}
mqtt5_sub_data = {"pub": {"1": {"tps": 8312.33855781041}, "3": {"tps": 8584.202828853975}, "5": {"tps": 8062.809497678443}, "7": {"tps": 8122.5964701370585}, "10": {"tps": 8113.053505396657}}, "sub": {"1": {"tps": 287.065551869672, "qos": 34.480000000000004}, "3": {"tps": 280.4757995445883, "qos": 34.48000000000001}, "5": {"tps": 278.41535314869304, "qos": 34.48000000000001}, "7": {"tps": 280.4764601159261, "qos": 34.48000000000001}, "10": {"tps": 280.1335980848054, "qos": 34.48000000000001}}}

def extract_tps_to_npmpy(data):
    pass

mqtt3_sub_tps = []
mqtt5_sub_tps = []
for i in folder:
    mqtt3_sub_tps.append(int(mqtt3_sub_data['sub'][i]['qos']))
    mqtt5_sub_tps.append(int(mqtt5_sub_data['sub'][i]['qos']))

mqtt3_sub_tps = np.array(mqtt3_sub_tps)
mqtt5_sub_tps = np.array(mqtt5_sub_tps)

labels = folder
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.4  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, mqtt3_sub_tps, width, label='mqtt3')
rects2 = ax.bar(x + width/2, mqtt5_sub_tps, width, label='mqtt5')

# Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_title('Publisher TPS')
ax.set_title('Subscriber QoS')
ax.set_yticklabels(['0','10%','15%','20%','25%','30%','35%','40%'])
# ax.set_ylabel('QoS(Correct Packets /Amount of packets)')
ax.set_ylabel('TPS(packets /1 sec)')
ax.set_xlabel('Amount of subscriber')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()