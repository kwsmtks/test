from flask import Flask, jsonify
import json
import urllib.request
import base64

app = Flask(__name__)

@app.route("/")
def index():
    url = 'http://internal-TestALB-580899179.ap-northeast-1.elb.amazonaws.com'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = json.loads(res.read())
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {
                "content-type" : "application/json",
                "Content-Security-Policy": "default-src 'self' *.",
                "X-Content-Type-Options": "nosniff",
                "X-XSS-Protection": "1; mode=block",
                "Strict-Transport-Security": "max-age= 63072000; includeSubdomains; preload"
            },
        "body": body
    }

@app.route("/api/v1/hello")
def hello():
    url = 'http://internal-TestALB-580899179.ap-northeast-1.elb.amazonaws.com'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = json.loads(res.read())
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {
                "content-type" : "application/json",
                "Content-Security-Policy": "default-src 'self' *.",
                "X-Content-Type-Options": "nosniff",
                "X-XSS-Protection": "1; mode=block",
                "Strict-Transport-Security": "max-age= 63072000; includeSubdomains; preload"
            },
        "body": body
    }

if __name__ == "__main__":
    app.run()
