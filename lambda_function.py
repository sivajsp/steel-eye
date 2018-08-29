import json
import pandas as pd
import boto3

print('Loading function')

def exceltojson(bucketname):
    s3 = boto3.client('s3')
    given_excel = pd.read_excel('ISO10383_MIC.xls', sheet_name = 'MICs List by CC')
    #converting the data into list of dict using the pandas
    json_output = json.loads(given_excel.to_json(orient='records'))
    #writing the content into json_file as per the requirements the xls needs to transferred into list of dict and write into json_file
    response = s3.put_object(Bucket='xlsbucket1',Body=str(json_output) ,Key='/out.json',ServerSideEncryption='AES256')
    
    #below line of code is enough if the you want to skip the step 4 and we will get the same result and don't need json package
    #return s3.put_object(Bucket='xlsbucket1',Body = pd.read_excel('ISO10383_MIC.xls', sheet_name = 'MICs List by CC').to_json(orient='records'),Key = '/out.json',ServerSideEncryption = 'AES256')
    return response
def lambda_handler(event, context):
    print(type(event))
    print("Received event: " + json.dumps(event, indent=2))
    bucketname = event['key1']
    print(exceltojson(bucketname))
    return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')
