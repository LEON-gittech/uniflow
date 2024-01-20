'''
Author: 王泽洲 leon.kepler@bytedance.com
Date: 2024-01-19 17:33:43
LastEditors: 王泽洲 leon.kepler@bytedance.com
LastEditTime: 2024-01-19 21:58:18
FilePath: /uniflow/example/server_client/server_client.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import sys

sys.path.append(".")
sys.path.append("..")
sys.path.append("../..")

from uniflow.flow.client import TransformClient
from uniflow.flow.config import TransformExpandConfig, ExpandReduceConfig
from uniflow.flow.flow_factory import FlowFactory
from uniflow.viz import Viz

FlowFactory.list()

client = TransformClient(ExpandReduceConfig(split_func="half_split", merge_func="half_merge"))
# input = [{"a": 1, "b": 2}, {"c": 3, "d": 4}, {"e": 5, "f": 6}, {"g": 7, "h": 8}]
input = [{"1": "2", "3": "4", "5": "6", "7": "8"}]
output = client.run(input)

print(client._config)
print(output)

graph = Viz.to_digraph(output[0]["root"])
# for mac: brew install graphviz
display(graph)

graph = Viz.to_digraph(output[1]["root"])
# for mac: brew install graphviz
display(graph)

