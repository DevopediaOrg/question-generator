
import  os
import logging
import sqlite3
import time
import json

from stackapi import StackAPI
from datetime import date, timedelta, datetime
from logger import setup_logger
from so_user_info_cache import SqliteHandler
from stackapi.stackapi import StackAPIError


''' This Module will give the reputation for perticaular user
at perticular time'''

class StackUsers:
    def __init__(self, dbPath, SITE, logger):

        '''
        dbPath : Cache path
        SITE: stack api object
        logger: logging module instance
        '''
        self.sqlhandler = SqliteHandler(dbPath, logger)
        self.SITE = SITE
        self.logger = logger

    def get_data_from_servers(self, users):
        ''' Fetch data using stack_api'''
        result = []
        try:
            users = self.SITE.fetch('users', ids=users)
            if 'items' in users:
                result = users['items']
        except StackAPIError as e:
            self.logger.error("Error while getting data, %s", e)
        return result

    def get_users_info(self, users):
        old_users = []
        user_data = {}
        system_time = int(time.time())
        for userid in users:
            info = self.sqlhandler.get_user(userid)
            if not info == 0:
                old_users.append(userid)
            elif  system_time - (60*60*24*30) > info[1]:
                old_users.append(userid)
            else:
                info = json.loads(info[2])
                user_data[userid] = info

        new_user_data = self.get_data_from_servers(old_users)
        for user in new_user_data:
            user_data['stored_at'] = system_time
            user_id = user["user_id"]
            user_data[user_id] = user
            self.sqlhandler.insert_user(system_time, user_id, user_data)
        return user_data

    def calculate_reputation(self, time, user_id, user_data):
        stored_time  = user_data['stored_at']
        user_data = user_data[user_id]
        reputation = None

        day = 60*60*24
        week = 60*60*24*7
        month = 60*60*24*30
        quarter = 60*60*24*30*4

        if time > stored_time:
            reputation = user_data["reputation"]
        elif time > stored_time - day:
            reputation = user_data["reputation"] - abs(user_data["reputation_change_day"])
        elif time > stored_time - week:
            reputation = user_data["reputation"] - abs(user_data["reputation_change_week"])
        elif time > stored_time - month:
            reputation = user_data["reputation"] - abs(user_data["reputation_change_month"])
        elif time > stored_time - quarter:
            reputation = user_data["reputation"] - abs(user_data["reputation_change_quarter"])
        else:
            reputation = user_data["reputation"] - abs(user_data["reputation_change_year"])
        return reputation

    def get_valid_reputation(self, users, users_data):
        time  = users['time']
        result = {'time': time,
                  'reputations' : []
        }
        for user_id in users['users']:
            if not user_id in users_data:
                continue
            user = users_data[user_id]
            reputations = self.calculate_reputation(time, user_id, users_data)
            result['reputations'].append(reputations)
        return result
        
    def get_user_and_reputation(self, users_info):
        result = []
        all_users_list = []
        [all_users_list.extend(value["users"]) for value in users_info]
        
        users_data = self.get_users_info(all_users_list)

        for users in users_info:
            data = self.get_valid_reputation(users, users_data)
            if data:
                result.append(data)
        return result
