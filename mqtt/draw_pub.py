import matplotlib.pyplot as plt
import numpy as np
from numpy.random.mtrand import pareto
import pandas as pd

folder = ['1', '3', '5', '7', '10']
mqtt3_data = {"pub": {"1": {"tps": 8403.317537608717}, "3": {"tps": 8088.510604698731}, "5": {"tps": 7198.671598427553}, "7": {"tps": 6349.543722959952}, "10": {"tps": 4915.119707126024}}, "sub": {"1": {"tps": 290.19004687399166, "qos": 34.480000000000004}, "3": {"tps": 836.2981805669233, "qos": 34.480000000000004}, "5": {"tps": 1241.2708510550278, "qos": 34.4799}, "7": {"tps": 1279.177242887465, "qos": 34.461999999999996}, "10": {"tps": 1529.3354864838761, "qos": 34.414049999999996}}}
mqtt5_data = {"pub": {"1": {"tps": 8312.33855781041}, "3": {"tps": 7878.781927106942}, "5": {"tps": 7164.528969700308}, "7": {"tps": 6407.590392736577}, "10": {"tps": 4985.770309637333}}, "sub": {"1": {"tps": 287.065551869672, "qos": 34.480000000000004}, "3": {"tps": 814.8538515071789, "qos": 34.480000000000004}, "5": {"tps": 1234.0904867105332, "qos": 34.480000000000004}, "7": {"tps": 1275.2198340055977, "qos": 34.45594285714286}, "10": {"tps": 1564.6845885415044, "qos": 34.40867}}}



def extract_tps_to_npmpy(data):
    pass

mqtt3_sub_tps = []
mqtt5_sub_tps = []
for i in folder:
    mqtt3_sub_tps.append(int(mqtt3_data['sub'][i]['qos']))
    mqtt5_sub_tps.append(int(mqtt5_data['sub'][i]['qos']))

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
ax.set_ylabel('QoS(Correct Packets /Amount of packets)')
# ax.set_ylabel('TPS(packets /1 sec)')
ax.set_xlabel('Amount of Publishers')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_yticklabels(['0','10%','15%','20%','25%','30%','35%','40%'])
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()