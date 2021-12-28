from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

# pip install flask flask-restf ul
app = Flask(__name__)  # initialize our flask app
api = Api(app)  # initialize our flask  api

# we are going to have two diff endpoint
# /
users_path = 'users.csv'
locations_path = 'locations.csv'


# /locations
# class Users(Resource):
#     def get(self):
#         data = pd.read_csv(users_path)#to read the CSV
#         data = data.to_dict()#conveert to dict
#         return {'data': data}, 200
#
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('userId', required=True, type=int)
#         parser.add_argument('name', required=True, type=str)
#         parser.add_argument('city', required=True, type=str)
#         args = parser.parse_args()
#         # return {
#         #     'loc': args['locationId'],
#         #     'name': args['name'],
#         #     'city': args['city']
#         # }, 200
#
#         data = pd.read_csv(users_path)
#
#         if args['userId'] in data['userId']:
#             return {
#                        'message': f"{args['userId']} already exists"
#                    }, 409
#         else:
#             data = data.apped({
#                 'userId': args['userId'],
#                 'name': args['name'],
#                 'city': args['city'],
#                 'locations': []
#             }, ignore_index=True)
#             data.to_csv(users_path, index=False)
#             return {'data': data.to_dict()}, 200
class Users(Resource):
    def get(self):
        data = pd.read_csv(users_path)  # to read the CSV
        data = data.to_dict()  # conveert to dict
        return {'data': data}, 200

    def post(self):
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('userId', required=True)  # add args
        parser.add_argument('name', required=True)
        parser.add_argument('city', required=True)

        args = parser.parse_args()  # parse arguments to dictionary


        # create new dataframe containing new values
        new_data = pd.DataFrame({
            'userId': args['userId'],
            'name': args['name'],
            'city': args['city'],
            'locations': [[]]
        })
        # read our CSV
        data = pd.read_csv('users.csv')
        # add the newly provided values
        data = data.append(new_data, ignore_index=True)
        # save back to CSV
        data.to_csv('users.csv', index=False)
        return {'data': data.to_dict()}, 200  # return data with 200 OK

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId', required=True, type=int)
        args = parser.parse_args()

        data = pd.read_csv(users_path)

        if args['userId'] in data['userId']:

            data = data[data['userId'] != str(args['userId'])]

            data.to_csv(users_path, index=False)
            # return "true"
            return {'data': data.to_dict()}, 200
        else:
            return {
                   'message': f"{args['userId']}does not exist"
                   }, 404


class Locations(Resource):
    pass


# to make sure that endpoint is added to api we need to write api add resourse
# and need to specify  the we address of the  where the endpoint will be stored
api.add_resource(Users, '/users')  # the users in web address
# api.com/users
api.add_resource(Locations, '/locations')

if __name__ == '__main__':  # to run our api or test it
    app.run(debug=True)
