from settings import *
import requests
import tarfile
import datetime as dt
import os

class Healtheintent(object):

    def __init__(self):

        self.uri = "https://wny.api.us.healtheintent.com/"
        self.headers = BEARER_HEADER
        self.headers_op = BEARER_HEADER_OP_API
        self.channel_id = None
        self.feed_id = None
        self.personnel_id = None
        self.organization_id = None
        self.personnel_group = None
        self.personnel_group_member_id = None
        self.location_id = None
        self.body = None
        #self.params = None

    def __send_request__(self, endpoint,
                         method = None, json = None, headers = None, params = None, data = None):
        if method == 'GET':
            return requests.get('{uri}{endpoint}'.format(uri=self.uri, endpoint=endpoint)
                                , headers=headers
                                , params=params).json()
        elif method == 'DELETE':
            return requests.delete('{uri}{endpoint}'.format(uri=self.uri, endpoint=endpoint)
                                   , headers=headers, params=params).json()
        elif method == 'POST':
            return requests.post('{uri}{endpoint}'.format(uri=self.uri, endpoint=endpoint),
                                   headers=headers, data=data, json=json)
        else:
            return requests.get('{uri}{endpoint}'.format(uri=self.uri, endpoint=endpoint)
                                , headers=headers, params=params)
#Data Syndication Class      
class DataSyndication(Healtheintent):

    def get_feeds(self):
        return self.__send_request__(endpoint='data-syndication/v1/feeds', method='GET', headers=self.headers)

    def get_channels(self):
        return self.__send_request__(endpoint='data-syndication/v1/channels', method='GET', headers=self.headers)

    def get_channel_status(self, channel_id = None):
        return self.__send_request__(endpoint='data-syndication/v1/channels/{channel_id}'.format(channel_id=channel_id), method='GET',
                                     headers=self.headers)

    def get_channel_deliveries(self, channel_id = None):
        return self.__send_request__(endpoint='data-syndication/v1/channels/{channel_id}/deliveries'.format(channel_id=channel_id),
                                     method='GET', headers=self.headers)

    def get_channel_downloads(self, delivery_id = None, destination_path = None):
        response = self.__send_request__(endpoint='data-syndication/v1/downloads/{delivery_id}'.format(delivery_id=delivery_id)
                                         , headers=self.headers)


        wd = os.getcwd()
        path = destination_path + '/' + dt.datetime.strftime(dt.datetime.today(), '%Y-%m-%d') + '.tar.gz'

        if response.status_code == 200:
            with open(path, 'wb') as i:
                i.write(response.content)
        i.close()

        temp = tarfile.open(name=path, mode='r:gz')
        os.chdir(destination_path)
        temp.extractall()
        temp.close()
        os.chdir(wd)

# IDENTITY DOMAIN
# Personnel
class Personnel(Healtheintent):
    def get_personnel(self):
        return self.__send_request__(endpoint='personnel/v1/personnel', method='GET'
                                     , headers=self.headers_op)

    def create_personnel(self): # INCOMPLETE
        return self.__send_request__(endpoint='personnel/v1', method='POST', headers=self.headers_op)

    def get_personnel_status(self, personnel_id = None):
        return self.__send_request__(endpoint='personnel/v1/{personnel_id}'.format(personnel_id=personnel_id)
                                     , method='GET'
                                     , headers=self.headers_op)

    def update_personnel(self): # INCOMPLETE
        return self.__send_request__(endpoint='personnel/v1', method='PUT', headers=self.headers_op)

    def delete_personnel(self, personnel_id = None):
        return self.__send_request__(endpoint='personnel/v1/{personnel_id}'.format(personnel_id=personnel_id)
                                     , method='DELETE'
                                     , headers=self.headers_op)

    
    #PERSONNEL GROUPS
    def get_personnel_groups(self):
        return self.__send_request__(endpoint='personnel/v1/personnel-groups', method='GET'
                                     , headers=self.headers_op)

    def create_personnel_group(self): # INCOMPLETE
        return self.__send_request__(endpoint='personnel/v1', method='POST', headers=self.headers_op)

    def get_personnel_group_status(self, personnel_group_id = None):
        return self.__send_request__(endpoint='personnel/v1/{personnel_group_id}'.format(personnel_group_id=personnel_group_id)
                                     , method='GET'
                                     , headers=self.headers_op)

    def update_personnel_group(self, personnel_group_id = None): #INCOMPLETE
        return self.__send_request__(endpoint='personnel/v1/{personnel_group_id}'.format(personnel_group_id=personnel_group_id)
                                     , method='PUT'
                                     , headers=self.headers_op)

    def delete_personnel_group(self, personnel_group_id = None):
        return self.__send_request__(endpoint='personnel/v1/{personnel_group_id}'.format(personnel_group_id=personnel_group_id)
                                     , method='DELETE'
                                     , headers=self.headers_op)

    def get_personnel_group_members(self, personnel_group_id = None):
        return self.__send_request__(endpoint='personnel/v1/{personnel_group_id}/members'.format(personnel_group_id=personnel_group_id)
                                     , method='GET'
                                     , headers=self.headers)

    def add_personnel_group_members(self, personnel_group_id = None, personnel_group_member_id = None):
        return self.__send_request__(endpoint='personnel/v1/{personnel_group_id}/members/{personnel_group_member_id}'
                                     , method='PUT', headers=self.headers)

    def delete_personnel_group_members(self, personnel_group_id = None, personnel_group_member_id = None):
        return self.__send_request__(endpoint='personnel/v1/{personnel_group_id}/members/{personnel_group_member_id}'
                                     , method='DELETE', headers=self.headers)

class Organization(Healtheintent):
    # ORGANIZATIONS
    def get_organizations(self,params=None):
        return self.__send_request__(endpoint='organization/v1/organizations'.format(params=params)
                                     , method='GET'
                                     , headers=self.headers_op)
    def create_organizations(self,data=None,json=None):
        return self.__send_request__(endpoint='organization/v1/organizations'.format(data=data, json=json)
                                     , method='POST'
                                     , headers=self.headers_op
                                     , data=data
                                     ,json=json)
    
    # Locations
    def get_locations(self):
        return self.__send_request__(endpoint='organization/v1/locations', method='GET'
                                     , headers=self.headers_op)

    def create_location(self):
        return self.__send_request__(endpoint='organization/v1/locations', method='POST'
                                     , headers=self.headers_op)

    def get_location_status(self, location_id = None):
        return self.__send_request__(endpoint='organization/v1/{location_id}'.format(location_id=location_id)
                                     , method='GET', headers=self.headers_op)

    def update_location(self, location_id = None):
        return self.__send_request__(endpoint='organization/v1/{location_id}'.format(location_id=location_id)
                                     , method='PUT', headers=self.headers_op)

    def delete_location(self, location_id = None):
        return self.__send_request__(endpoint='organization/v1/{location_id}'.format(location_id=location_id)
                                     , method='DELETE', headers=self.headers_op)

