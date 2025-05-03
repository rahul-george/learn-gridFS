from pymongo import MongoClient
import gridfs

CONNECTION_STRING = '<Connection string>'
DB_NAME = '<DB Name>'

client = MongoClient(CONNECTION_STRING)
DB = client[DB_NAME]

fs = gridfs.GridFS(DB)

# Example 1
# create a new file in gridFS
if 0:
    a = fs.put(b"hello world")
    print(a) # a contains the file_id

    # Get the file
    print(fs.get(a).read())


# Example 2
# create file with other details
if 0: 
    a = fs.put(b"new world order", filename="foo", bar='baz')
    out = fs.get(a)
    print(out.read())
    print(out.filename)
    print(out.bar)
    print(out.upload_date)

    # can files be searched using the key value attributes? 
    result = fs.find({"filename": "foo"})       # Result is an iterable! 
    for idx, each_result in enumerate(result, start=1):
        print(f"file#{idx}")
        print(each_result.filename)

# Example 3
# create file with other details as metadata
if 1:
    a = fs.put(b"Experiment 6", filename="foo", bar='baz', metadata={"help_text": "text 1", "version": 1})
    out = fs.get(a)
    print(out.read())
    print(out.filename)
    print(out.bar)
    print(out.upload_date)
    print(out.metadata)
    print(out.metadata["version"])



    # Can files be searched using other nested attributes? 
    result = fs.find({"metadata.help_text": "text 1"})       # Result is an iterable! 
    for idx, each_result in enumerate(result, start=1):
        print(f"file#{idx}")
        print(each_result.filename)
        print(each_result.metadata)
    
    for each_item in fs.get_version(filename="foo", version=-3):
        print("get_version", each_item)


if 0: 
    # Create a new gridfs bucket and put files in that bucket. 
    images_bucket = gridfs.GridFSBucket(DB, bucket_name="images")
    reports_bucket = gridfs.GridFSBucket(DB, bucket_name="reports")

    print(images_bucket)
    print(reports_bucket)

    file_id = images_bucket.upload_from_stream("test_file", b"data I want to store") 

if 0: 
    # What is the difference between a gridFS bucket and the normal gridFS? 
    # GridFS is the mongoDB specification. 
    # GridFSBucket is a driver provided implementation to use gridFS. 
    # GridFSBucket is a better way to use gridFS in an application because of the streaming methods it offers. 
    pass

if 0:
    images_bucket = gridfs.GridFSBucket(DB, bucket_name="fs")
    for item in images_bucket.find():
        images_bucket.delete(item._id)
        




