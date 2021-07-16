import matplotlib.pyplot as plt
import numpy as np
from numpy.random.mtrand import pareto
import pandas as pd

folder = ['1k', '1w', '4w', '7w', '10w']
mqtt3_pkg_data = {"pub": {"1k": {"tps": 9319286.376373636}, "1w": {"tps": 427538.78719276376}, "4w": {"tps": 28651.984554000435}, "7w": {"tps": 78818.9454374459}, "10w": {"tps": 8403.317537608717}}, "sub": {"1k": {"tps": 8188.931138075275, "qos": 100.0}, "1w": {"tps": 4374.079188480659, "qos": 100.0}, "4w": {"tps": 1149.547651252307, "qos": 100.0}, "7w": {"tps": 357.16411440536245, "qos": 6.4}, "10w": {"tps": 290.19004687399166, "qos": 34.480000000000004}}}
mqtt5_pkg_data = {"pub": {"1k": {"tps": 9285560.241250606}, "1w": {"tps": 427090.6387309301}, "4w": {"tps": 28810.47241178762}, "7w": {"tps": 79269.28704798436}, "10w": {"tps": 8312.33855781041}}, "sub": {"1k": {"tps": 7744.124749278133, "qos": 100.0}, "1w": {"tps": 4371.1330644753525, "qos": 100.0}, "4w": {"tps": 1156.2948047726923, "qos": 100.0}, "7w": {"tps": 359.12354231271803, "qos": 6.400000000000001}, "10w": {"tps": 287.065551869672, "qos": 34.480000000000004}}}


def extract_tps_to_npmpy(data):
    pass

mqtt3_pkg_tps = []
mqtt5_pkg_tps = []
for i in folder:
    mqtt3_pkg_tps.append(int(mqtt3_pkg_data['sub'][i]['qos']))
    mqtt5_pkg_tps.append(int(mqtt5_pkg_data['sub'][i]['qos']))

mqtt3_pkg_tps = np.array(mqtt3_pkg_tps)
mqtt5_pkg_tps = np.array(mqtt5_pkg_tps)

labels = folder
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.4  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, mqtt3_pkg_tps, width, label='mqtt3')
rects2 = ax.bar(x + width/2, mqtt5_pkg_tps, width, label='mqtt5')

# Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_title('Publisher TPS')
ax.set_title('Subscriber QoS')
ax.set_ylabel('QoS(Correct Packets /Amount of packets)')
# ax.set_ylabel('TPS(packets/1 sec)')
# ax.set_yticklabels(['k','2000k','4000k','6000k','8000k'])
ax.set_yticklabels(['0','20%','40%','60%','80%','100%'])
ax.set_xlabel('Amount of Packets in one time')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()