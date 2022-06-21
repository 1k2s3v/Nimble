import os
import werkzeug
from dotenv import load_dotenv
import boto3
from werkzeug.local import LocalProxy
from flask import request, Flask
from botocore.exceptions import ClientError

access_key = os.getenv('ACCESS_KEY_ID')
secret_access_key = os.getenv('SECRET_ACCESS_KEY')
load_dotenv()
client = boto3.client('s3', aws_access_key_id=access_key,
                      aws_secret_access_key=secret_access_key)

app = Flask(__name__)
session = boto3.Session(
        aws_access_key_id=os.getenv('ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('SECRET_ACCESS_KEY'),)


def get_files_from_request(request: werkzeug.local.LocalProxy, index) -> dict[str, werkzeug.datastructures.FileStorage]:
    list_of_sent_files = list(request.files.lists())
    sent_file = list_of_sent_files[index]
    key = sent_file[0]
    file_for_put = sent_file[1][0]
    key_file_value: dict = {key: file_for_put}
    return key_file_value


def put_to_s3(key_file_value: dict) -> True:
    filename = [item for item in key_file_value][0]
    file = key_file_value[filename]

    s3 = session.resource('s3')
    object = s3.Object('nimble-test-task', filename)
    result = object.put(Body=file)
    return True


def get_file_by_pk(file_name: str) -> bytes:
    s3 = boto3.client('s3')
    try:
        response = s3.get_object(Bucket='nimble-test-task', Key=file_name)
        requested_file = response['Body'].read()
        return requested_file
    except ClientError as ex:
        if ex.response['Error']['Code'] == 'NoSuchKey':
            return None



@app.route('/get-create-update/<pk>', methods=['GET', 'PUT'])
def upload_file(pk):
    if request.method == 'PUT':
        if request.files:
            index = 0
            response_for_client = {}
            while index < len(list(request.files.lists())):
                key_file_value = get_files_from_request(request, index)
                result_of_sending = put_to_s3(key_file_value)
                index += 1
                if result_of_sending:
                    response_for_client[[item for item in key_file_value][0]] = "Was update/create successfully"
            return response_for_client, 200
        else:
            return 'Attached file did not found', 400

    if request.method == 'GET':
        file_name = str(pk)
        requested_file = get_file_by_pk(file_name)
        if requested_file is None:
            return 'That file does not exist', 400
    return requested_file, 200


if __name__ == '__main__':
    app.run(debug=True)
