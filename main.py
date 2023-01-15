import time
import pandas as pd


class ContactControl():

    def __init__(self):
        self.clients = pd.DataFrame(columns=['name', 'email', 'contact_person'])
        self.users = pd.DataFrame(columns=['id', 'name', 'is_manager'])
        self.tasks = pd.DataFrame(columns=['contact_person', 'task_author',
                                           'task_desc', 'task_start', 'priority_level'])

    def add_client(self, name, email, contact_person):
        client = pd.DataFrame({'name': name, 'email': email, 'contact_person': contact_person}, index=[0])
        self.clients = pd.concat([self.clients, client], ignore_index=True)

    def add_user(self, id, name, is_manager):
        user = pd.DataFrame({'id': id, 'name': name, 'is_manager': is_manager}, index=[0])
        self.users = pd.concat([self.users, user], ignore_index=True)

    def add_task(self, contact_person, task_author, task_desc, task_start, priority_level):
        task = pd.DataFrame({'contact_person': contact_person, 'task_author': task_author, 'task_desc': task_desc,
                             'task_start': task_start, 'priority_level': priority_level}, index=[0])
        self.tasks = pd.concat([self.tasks, task], ignore_index=True)

    def report(self, name):
        return len(self.tasks[self.tasks['task_author'] == name])

    def search(self, name):
        return self.clients['contact_person'][self.clients['name'] == name]
