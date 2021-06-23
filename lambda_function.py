import sys
import json

def lambda_handler(event, context):
  
  print('Hello from Lambda!')
  print(sys.version)
    
    return {
        # Required values when using Lambda Proxy Intergration:
        
        # statusCode
        # headers
        # body
        
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(event)
    }
