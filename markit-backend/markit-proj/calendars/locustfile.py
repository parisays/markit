from locust import HttpLocust, TaskSet, task, between, seq_task
import json
import random
import collections
import ast

def read_user_credentials_from_file():
    data = []
    with open("user_info.txt", "r") as inFile:
        data = ast.literal_eval(inFile.read())
    return data

class UserActions(TaskSet):

    token = '6850528cc70dd8af15d9e66c4c9daf343cad5235'
    calendar_id = 0
    calendar_list = []
    user_info = []
    user_credentials = []

    def on_start(self):
        self.user_credentials = read_user_credentials_from_file()
        self.login()
    
    def on_stop(self):
        self.logout()

    def logout(self):
        # with open('user_info.txt', 'w') as outfile:
        #     json.dump(self.user_info, outfile)
        self.client.post("/api/v1.0/auth/rest-auth/logout/", name='logout')

    def login(self):
        # user_info = []
        # for i in range(100):
        #     user_email = 'user{0}@gmail.com'.format(str(i))
        #     first_name = 'user{0}'.format(i)
        #     last_name = 'lastname{0}'.format(i)
        #     data = {'email':user_email, 'password1':"a.123456", 'password2':"a.123456", 'firstName':first_name, 'lastName':last_name}
        #     # print(data)
        #     response = self.client.post('/api/v1.0/auth/rest-auth/registration/',
        #                     data, name='register')
        #     self.user_info.append(json.loads(response.text))

        # randomly choose a use
        user = random.choice(self.user_credentials)
        self.token = user['key']

        # login to the application
        # response = self.client.post('/api/v1.0/auth/rest-auth/login/',
        #                             {'email': 'parisa1378.y@gmail.com', 'password': 'boofoo12345'},
        #                             name='login')
        # self.token = json.loads(response.text)['key']
    

    @seq_task(1)
    def create_calendar_post(self):
        pass
        calendar_response = self.client.post('/api/v1.0/calendar/', # headers={“X-CSRFToken”: csrftoken})
                            {'name': 'My Calendar'}, name='create calendar',
                            headers={'Authorization':'Token {0}'.format(self.token)})

        self.calendar_id = json.loads(calendar_response.text)['id']

        for i in range(4):
            self.client.post('/api/v1.0/post/', # headers={“X-CSRFToken”: csrftoken})
                        {"calendar": "{0}".format(self.calendar_id),
                        "subject": "Post{0}".format(i),
                        "text": "Post{0} Text".format(i)}, name='create post',
                        headers={'Authorization':'Token {0}'.format(self.token)})


    @seq_task(2)
    def list_calendar_post(self):
        pass
        self.calendar_list = self.client.get('/api/v1.0/calendar/', name='list calendar',
                                        headers={'Authorization':'Token {0}'.format(self.token)})

        for calendar in json.loads(self.calendar_list.text):
            self.calendar_id = calendar['id']
            self.client.get('/api/v1.0/post/{0}/'.format(self.calendar_id), name='list post',
                            headers={'Authorization':'Token {0}'.format(self.token)})


    # @task(4)
    # def add_advertiser_api(self):
    #     auth_response = self.client.post('/auth/login/', {'username': 'suser', 'password': 'asdf1234'})
    #     auth_token = json.loads(auth_response.text)['token']
    #     jwt_auth_token = 'jwt '+auth_token
    #     now = datetime.datetime.now()
    #     current_datetime_string = now.strftime("%B %d, %Y")
    #     adv_name = 'locust_adv' 
    #     data = {'name', current_datetime_string}
    #     adv_api_response = requests.post('http://127.0.0.1:8000/api/advertiser/', data, headers={'Authorization': jwt_auth_token})
    
class ApplicationUser(HttpLocust):
    task_set = UserActions
    wait_time = between(2, 9)
    host = 'http://localhost:8000'