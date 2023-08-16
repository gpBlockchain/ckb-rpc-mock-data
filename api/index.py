import json

from flask import Flask, jsonify, render_template, request
import os

app = Flask(__name__, template_folder='templates')

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
file_storage_root = os.path.join(parent_dir, 'mock')

POST_REQUEST_NOT_EQ_ERROR = 501
READ_FILE_NOT_EXIST_ERROR = 502
DIR_NOT_EXIST_ERROR = 503


@app.route('/')
def index():
    # 返回文件列表页面
    root_files = []
    for file_name in os.listdir(file_storage_root):
        file_path = os.path.join(file_storage_root, file_name)
        if os.path.isdir(file_path):
            sub_files = [sub_file for sub_file in os.listdir(file_path) if
                         not os.path.isfile(os.path.join(file_path, sub_file))]
            root_files.append({"directory": file_name, "files": sub_files})
    return render_template('index.html', files=root_files)


@app.route('/test/<directory>/<filename>', methods=['GET', 'POST'])
def test_get(directory, filename):
    # 下载文件内容作为JSON数据返回
    file_path = os.path.join(file_storage_root, directory, filename)
    print(filename)
    if os.path.exists(file_path):
        try:
            with open(f"{file_path}/request.json", "r") as file:
                request_data = file.read()
            with open(f"{file_path}/response.json", "r") as file:
                response_data = file.read()
            request_data = json.loads(request_data)
            response_data = json.loads(response_data)
            if request.method == 'GET':
                return jsonify({"filename": filename, "request": request_data, "response": response_data})
            if request.method == 'POST':
                # 比较POST请求数据和request.json是否一致
                post_data = request.json
                if "params" not in post_data:
                    post_data["params"] = []  # 将 "params" 字段设为一个空列表，即empty场景
                if post_data['params'] is None:
                    post_data['params'] = request_data['params']  # 将 params 为 None 的情况转换为[]/null

                if post_data['method'] == request_data['method'] and post_data['params'] == request_data['params']:
                    response_data['id'] = post_data['id']
                    return jsonify(response_data)
                else:
                    app.logger.error(
                        f"Request data does not match with the data:\n 'expected request':{request_data}\n sdk post':{post_data}")
                    return jsonify({'id': post_data['id'], 'jsonrpc': '2.0',
                                    "error": f"Request data does not match with the expected data:'request':{request_data},'post':{post_data}", }), POST_REQUEST_NOT_EQ_ERROR
        except Exception as e:
            return jsonify({"error": f"Error while reading the file: {str(e)}"}), READ_FILE_NOT_EXIST_ERROR
    else:
        return jsonify({"error": "File not found"}), DIR_NOT_EXIST_ERROR


if __name__ == '__main__':
    app.config['JSON_AS_TEXT'] = False
    app.run(debug=True)
