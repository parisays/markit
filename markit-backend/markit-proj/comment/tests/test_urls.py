from rest_framework.authtoken.models import Token                                  
from django.test import Client 
# from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from users.models import User
from calendars.models import Calendar
from posts.models import Post
from collaboration.models import Collaborator, Role
from comment.models import Comment
from comment.serializers import CommentSerializer, CommentDetailSerializer
import json

# Create your tests here.

class CommentURLTests(APITestCase):
    """
     Test comment urls.
    """

    def setUp(self):
        """
         Initialization.
        """
        # Create first user
        self.first_name = "john"
        self.last_name = "snow"
        self.email = "john@snow.com"
        self.password = "youknownothing"
        
        self.first_user = User.objects.create_user(
            firstName=self.first_name, lastName=self.last_name,
            email=self.email, password=self.password
            )
        # Create calendar
        self.calendar_name = "germany"
        
        self.calendar = Calendar.objects.create(
            owner=self.first_user, name=self.calendar_name
        )
        # Create post
        self.post_subject = "berlin"
        self.post_text = "Berlin is the capital and largest city of Germany"

        self.post = Post.objects.create(
            subject=self.post_subject, text=self.post_text, calendar=self.calendar
        )
        # Create role
        self.role_name = 'Owner'
        self.role_access = ['post_comment']
        self.first_user_role = Role.objects.create(
            name=self.role_name, access=self.role_access
        )
        # Create collaborator
        self.first_user_collaborator = Collaborator.objects.create(
            user=self.first_user, calendar=self.calendar, role=self.first_user_role, isConfirmed=True
        )

        # urls
        self.create_comment_url = reverse('create-comment')
        self.list_comment_url = reverse("list-comment", kwargs={"post_id": self.post.pk})
        # self.detail_comment_url = reverse("detail-comment", kwargs={"post_id": self.post.pk})

        # Authorization
        self.token, self.created = Token.objects.get_or_create(user=self.first_user) 
        self.client = APIClient()               
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


    def test_create_comment_success(self):
        """
            Success test for create comment.
        """
        self.client.login(email=self.email, password=self.password)
        data = {'post': self.post.pk, 'text': 'testing comment create url'}
        response = self.client.post(self.create_comment_url, data, format='json')
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0}:{1} instead.'
                         .format(response.status_code, response.content))
        
        comment_one = Comment.objects.create(
            post=self.post, collaborator=self.first_user_collaborator,
            text='testing comment create url'
        )

        comment_serializer_data = json.dumps(CommentSerializer(instance=comment_one).data)
        comment_serializer_data = json.loads(comment_serializer_data)
        response_data = json.loads(response.content)

        self.assertEqual(comment_serializer_data['id'], response_data['id'] + 1)
        self.assertEqual(comment_serializer_data['post'], response_data['post'])
        self.assertEqual(comment_serializer_data['text'], response_data['text'])
        self.assertEqual(comment_serializer_data['reply'], response_data['reply'])

    def test_create_comment_permision_denied(self):
        """
            Permission test for create comment.
        """
        self.first_user_role.access = []
        self.first_user_role.save()
        self.client.login(email=self.email, password=self.password)
        data = {'post': self.post.pk, 'text': 'testing comment create url'}
        response = self.client.post(self.create_comment_url, data, format='json')
        self.assertNotEqual(response.status_code, 201,
                            'Expected Response Code 403, received {0}:{1} instead.'
                            .format(response.status_code, response.content))


    def test_list_comment_success(self):
        """
            Success test for list comment.
        """
        comment_one = Comment.objects.create(
            post=self.post, collaborator=self.first_user_collaborator,
            text='testing comment create url number 1'
        )

        comment_two = Comment.objects.create(
            post=self.post, collaborator=self.first_user_collaborator,
            text='testing comment create url number 2'
        )

        self.client.login(email=self.email, password=self.password)
        response = self.client.get(self.list_comment_url, format='json')
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0}:{1} instead.'
                         .format(response.status_code, response.content))

        response_data = json.loads(response.content)
        self.assertEqual(len(response_data), 2)

        comment_serializer_data_one = json.dumps(CommentSerializer(instance=comment_one).data)
        comment_serializer_data_one = json.loads(comment_serializer_data_one)

        self.assertEqual(comment_serializer_data_one['id'], response_data[0]['id'])
        self.assertEqual(comment_serializer_data_one['post'], response_data[0]['post'])
        self.assertEqual(comment_serializer_data_one['text'], response_data[0]['text'])
        self.assertEqual(comment_serializer_data_one['reply'], response_data[0]['reply'])

        comment_serializer_data_two = json.dumps(CommentSerializer(instance=comment_two).data)
        comment_serializer_data_two = json.loads(comment_serializer_data_two)
        
        self.assertEqual(comment_serializer_data_two['id'], response_data[1]['id'])
        self.assertEqual(comment_serializer_data_two['post'], response_data[1]['post'])
        self.assertEqual(comment_serializer_data_two['text'], response_data[1]['text'])
        self.assertEqual(comment_serializer_data_two['reply'], response_data[1]['reply'])



        
