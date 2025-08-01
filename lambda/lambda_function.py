import boto3
import datetime
def lambda_handler(event, context):
    print("-------- Lambda triggered with latest changes! --------")
    print("Full event:", event)
    s3 = boto3.client('s3', region_name = 'ap-south-1') 
    try: 
        bucket = event['Records'][0]['s3']['bucket']['name'] 
        key = event['Records'][0]['s3']['object']['key']
        response = s3.get_object(Bucket = bucket, Key = key) 
        content = response['Body'].read().decode('utf-8')
        modified_content = content + "\nProcessed by lambda"
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S") 
        output_key = f"output_files/processed_{now}.txt" 
        s3.put_object(Bucket=bucket, Key=output_key, 
        Body=modified_content.encode('utf-8')) 
        print(f"File saved as: {output_key}") 
        print("-------- Lambda execution completed successfully with Auto deploy! --------") 
    except: print(f"Error: {event}")