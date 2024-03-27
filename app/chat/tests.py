from django.test import TestCase,APITestCase
from users.models import User
# Create your tests here.
class ChatAPITestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            email = '1234@naver.com',
            password = '1234'
        )
        self.user2= User.objects.create_user(
            email = '123456@naver.com',
            password = '123456'
        )