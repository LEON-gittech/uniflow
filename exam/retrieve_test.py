'''
Author: 王泽洲 leon.kepler@bytedance.com
Date: 2024-01-20 17:15:56
LastEditors: 王泽洲 leon.kepler@bytedance.com
LastEditTime: 2024-01-20 17:27:00
FilePath: /uniflow/exam/retrieve_test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from flask import Flask, request, jsonify
import redis
import json

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/keyvaluepairs', methods=['GET'])
def get_key_value_pairs():
    # Retrieve pagination parameters from the request
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Retrieve all keys from Redis
    keys = r.keys("*")
    keys = [x.decode('utf-8') for x in keys]
    print("keys",keys)
    # Calculate start and end indices of the current page
    start = (page - 1) * per_page
    end = start + per_page
    print("start",start)
    print("end",end)

    # Retrieve values for keys on the current page
    key_value_pairs = []
    print(keys[start:end])
    for key in keys[start:end]:
        value = r.get(key).decode('utf-8')
        print(value)
        key_value_pairs.append({"key": key, "value": value})

    # Return the current page of key-value pairs and pagination information
    return jsonify({
        "page": page,
        "per_page": per_page,
        "total": len(keys),
        "data": key_value_pairs
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=15143)
