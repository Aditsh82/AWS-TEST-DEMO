import boto3
import json

def get_data():
    # S3 bucket we'll be interacting with
    s3_bucket = "random-users-data-406568989225"
    # Because we need to combine data from multiple S3 objects, initialize a list to hold this data before returning it.
    data = []
    # Initialize an boto3 S3 client, and list the objects in our bucket. The data about the contents of our bucket will be stored in a list called s3_keys.
    s3 = boto3.client('s3')
    objects = s3.list_objects_v2( Bucket = s3_bucket )['Contents']
        
    print(objects)

    # ########################################################################
    # ########################################################################
    # s3_keys = []
    # for object in objects:
    #     if object['Key'].startswith('users_'):
    #         s3_keys.append(object['Key'])
    # print("GETTING ALL THE KEYS THAT GOT APPENDED #############    ",s3_keys)
    
    # s3_files_list = []
    # # After collecting the appropriate keys that begin with "users_" gather each object, and combine the returned data with the existing "data" list.
    

    # ########################################################################
    
    # for key in s3_keys:
    #     print("THIS IS THE KEY IN LOOP === ",key)
    #     object = s3.get_object( Bucket = s3_bucket, Key = key )
        
    #     object_data = json.loads(object['Body'].read())
    #     print("#"*100)
    #     # print("THIS IS OBJECT DATA for {} ---- {}".format(key, object_data))
    #     # print("THIS IS OBJECT DATA for {} ---- {}".format(key, object_data))

    #     # if "dfsdfs" in json.dumps(object_data):
    #     if "12403" in json.dumps(object_data):
    #         print("TRUEEEEEEEEE")
    #         s3_files_list.append(key)
    #     else:
    #         print("FALSEEEEEEEE")
    #     ########################################################################
    #     # for iteration in object_data:
    #     #     if "registered" in json.dumps(iteration):
    #     #         print("YESSSSSSSSSSSSSSSSSS")
    #     #     else:
    #     #         print("NOOOOOOOOOOOOOOOOOOOOO")
    #     ########################################################################
    #     print("#"*100)
        
        
    #     data += object_data
    # print("This is the final list ---------------",s3_files_list)

    
    # ########################### WORKING CODE ###############################
    # import io
    # fo = io.BytesIO(bytes(",".join(str(i) for i in s3_files_list), "utf-8"))
    # # fo = b'my data stored as file object in RAM'
    # s3.upload_fileobj(fo, s3_bucket, 's3_files.txt')
    # ########################################################################
    # ########################################################################
    # ########################################################################


    s3_files_list = []
    
    for object_dict in objects:
        print(object_dict["Key"])
        # if not object_dict["Key"].lower().endswith((".py", ".txt", ".csv")):
        if object_dict["Key"].startswith('aws') and ".py" not in object_dict["Key"]:
            file_object = s3.get_object( Bucket = s3_bucket, Key = object_dict["Key"])
            
            object_data = json.loads(file_object['Body'].read())
            # data += object_data
            
            if "12403" in json.dumps(object_data):
                print("TRUEEEEEEEEE")
                s3_files_list.append(object_dict["Key"])
            else:
                print("FALSEEEEEEEE")
        
    print("This is the final list ---------------",s3_files_list)
    # Return our combined data from all "users_" objects.
    # return data
    return {"1":"10"}

def handler(event, context):
    # Call the "get_data" function and return appropriately formatted results.
    return {'isBase64Encoded': False,'statusCode': 200,'body': json.dumps(get_data()), 'headers': {"Access-Control-Allow-Origin": "*"}}