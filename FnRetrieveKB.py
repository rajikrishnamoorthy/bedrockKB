import json
import boto3
#create client object with bedrock agent
client_bedrock_knowledgebase = boto3.client('bedrock-agent-runtime')
def lambda_handler(event, context):
        user_prompt=event['prompt']
        # Use retrieve and generate method of bedrock agent object. Upfront check the unique ID of the Bedrock knowledge base from the AWS management console.
        client_knowledgebase = client_bedrock_knowledgebase.retrieve_and_generate(
        input={
            'text': user_prompt
        },
        retrieveAndGenerateConfiguration={
            'type': 'KNOWLEDGE_BASE',
            'knowledgeBaseConfiguration': {
                'knowledgeBaseId': 'NEHDLX3RJL', 
                'modelArn': 'arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-instant-v1'
                    }
                })
      
        responseKB=client_knowledgebase['output']['text']
        return {
            'statusCode': 200,
            'body': responseKB
        }
    
