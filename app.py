from flask import Flask, request
import json
import cvfuncs
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "error"


# !!! returnları json yap ?
@app.route('/compress', methods=['POST'])
def compress():
    if request.method == 'POST':
        if isinstance(request.json, str):
            json_request = json.loads(request.json)
            compress_rate = json_request['compress_rate']
            base64_string = json_request['base64_string']
            print("string geldi")
            print("compress_rate: ", compress_rate)

            encoded_ret = cvfuncs.compress(base64_string, compress_rate)
            return {"base64_ret": encoded_ret, "raw_len": len(base64_string), "encoded_len": len(base64_string)}

        compress_rate = request.json['compress_rate']
        base64_string = request.json['base64_string']
        print("compress_rate: ", compress_rate)

        encoded_ret = cvfuncs.compress(base64_string, compress_rate)
        print("encoded_len: ", len(encoded_ret))
        print("raw_len", len(base64_string))
        return {"base64_ret": encoded_ret, "raw_len": len(base64_string), "encoded_len": len(base64_string)}

    else:
        return "error"


@app.route('/segmentation', methods=['POST'])
def segmentation():
    if request.method == 'POST':
        if isinstance(request.json, str):
            json_request = json.loads(request.json)
            base64_string = json_request['base64_string']
            print("string geldi")
            print("raw_len", len(base64_string))
            encoded_ret = cvfuncs.segmentation(base64_string)

            return {"base64_ret": encoded_ret}

        base64_string = request.json['base64_string']
        encoded_ret = cvfuncs.segmentation(base64_string)
        print("encoded_len: ", len(encoded_ret))

        return {"base64_ret": encoded_ret}

    else:
        return "error"
