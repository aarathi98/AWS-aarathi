def lambda_handler(event, context):
    name = event['name']
    greeting = f"Hello, {name}!"
    return {
        'statusCode': 200,
        'body': greeting
    }
