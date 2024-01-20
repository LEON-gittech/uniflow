# Backend Interview README
For implementing "Synchronous RESTful Endpoint to Retrieve All key-value Pairs", I used Flask, so there is a slightly difference in pyproject.toml.

To store the key-value pairs, I used Redis.

# Docker
docker pull leonwang24/uniflow:latest
## Run
docker run uniflow

tips: Docker will run exam/server_client.py as default.
# Kubernetes
kubectl apply -f pod.yaml
kubectl apply -f service.yaml
# Synchronous RESTful Endpoint to Retrieve All key-value Pairs

run: python exam/retrieve_test.py 

## Request format: 
http://localhost:port(15143 as default)/keyvaluepairs?page={}&per_page={}
## Response format:
{
    "page": page,
    "per_page": per_page,
    "total": len(keys),
    "data": key_value_pairs
}
## Example:
input: 

[{"How are you?": "Fine.", "Who are you?": "I am Bob."}, {"Where are you?": "I am at home.", "What are you doing?": "Coding."}]

data in redis: 

{'How are you? Who are you?':'Fine. I am Bob.', 'Where are you? What are you doing?':'I am at home. Coding.'}

request: 

http://localhost:15143/keyvaluepairs?page=1&per_page=20

response: 

{"data":[{"key":"How are you? Who are you?","value":"Fine. I am Bob."},{"key":"Where are you? What are you doing?","value":"I am at home. Coding."}],"page":1,"per_page":20,"total":2}
# Conclusion
This is an interesting project, through which I find that asynchronized programming is my weak point and needs to be improved. Thanks for giving me this opportunity!