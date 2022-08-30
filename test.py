# from pymongo import MongoClient
# import gridfs
#
# def mongo_conn():
#     try:
#         conn = MongoClient("mongodb://127.0.0.1:27017/new")
#         print("Connected", conn)
#     except Exception as e:
#         print("Error", e)
#
# conn = MongoClient("mongodb+srv://quickwork:quickwork@users.46fhmfp.mongodb.net/?retryWrites=true&w=majority")
# db = conn.testt
# name = 'user.jpg'
# file_loc = "D:\A.I\A.I\Triple EEE\Perfect Learn Free Website Template - Free-CSS.com\perfect-learn/" + name
# file_date = open(file_loc, 'rb')
# data = file_date.read()
#
# fs = gridfs.GridFS(db)
# fs.put(data, filename=name)
# print("upload complete")
#
# data = db.fs.files.find_one({"filename":name})
# my_id = data['_id']
# outputdata = fs.get(my_id).read()
# # download_loc = "C:\Users\Administrator\Desktop" + name
# output = open("C:/Users/Administrator/Desktop/user.jpg" , "wb")
# output.write(outputdata)
# output.close()
# print("download completed")\\\

import cloudinary.uploader
# from flask import Flask, render_template, request
# from flask_cors import CORS, cross_origin



# app = Flask(__name__)
# After creating the Flask app, you can make all APIs allow cross-origin access.
# # CORS(app)
cloudinary.config(
  cloud_name = "dhr6igdst",
  api_key = "578356959545128",
  api_secret = "GFvGFOvSVr0VfdeOMzos9BvU_Xc"
)

# or a specific API
# @app.route("/upload", methods=['POST'])
# @cross_origin()

# print(dir(cloudinary))
if cloudinary.uploader.upload("test.py", use_filename=True, folder='/triple_e', resource_type='auto'):
    print("DOne")

print(cloudinary.utils.cloudinary_url("triple_e/user.jpg")[0])

# https://res.cloudinary.com/dhr6igdst/image/upload/v1661770494/triple_e.jpg
# print(app.logger.info(im))
# cloudinary.uploader.upload(request.FILES['file'])

# if __name__ == '__main__':
    # app.run(debug = True)
  
import os
print(os.path.splitext('user.jpg')[0])