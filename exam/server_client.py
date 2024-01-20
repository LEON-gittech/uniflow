import sys
import redis
import json
sys.path.append(".")
sys.path.append("..")
sys.path.append("../..")

from uniflow.flow.client import TransformClient, Client
from uniflow.viz import Viz

client = Client("expand_reduce_flow")
input = [{"How are you?": "Fine.", "Who are you?": "I am Bob."}, {"Where are you?": "I am at home.", "What are you doing?": "Coding."}]
output = client.run(input)

redis_pool = redis.ConnectionPool(host='127.0.0.1', port= 6379, db= 0)
redis_conn = redis.Redis(connection_pool= redis_pool)

print(output)
# 遍历output列表中的字典数据，并将其序列化为JSON字符串后，存入Redis中
for dict in output:
    output_tmp = dict['output']
    for dic in output_tmp:
        for key in dic.keys():
            redis_conn.set(key, dic[key])

graph = Viz.to_digraph(output[1]["root"])

print(graph)

