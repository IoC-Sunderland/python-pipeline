import sys
import json

def my_func():
  print('Hello from Lambda!')
  print(sys.version)

def lambda_handler(event, context):
  
  my_func()
    
  return {
        # Required values when using Lambda Proxy Intergration:
        
        # statusCode
        # headers
        # body
        
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(event)
    }
