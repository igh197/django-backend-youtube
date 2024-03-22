from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User
from subscriptions.models import Subscription
# Create your tests here.
class SubscriptionAPITestCase(APITestCase):
    #테스트 코드 실행시 가장 먼저 실행되는 함수
    def setUp(self):
        self.user1 = User.objects.create_user(
            email = '1234@naver.com',
            password = '1234'
        )
        self.user2= User.objects.create_user(
            email = '123456@naver.com',
            password = '123456'
        )
        self.client.login(email='1234@naver.com',password='1234')
        #내가 구독한 유튜버 리스트
    def test_sub_list_get(self):
        Subscription.objects.create(subscriber=self.user1,subscribed_to = self.user2)
        
        url = reverse('subed-to-list')
        res = self.client.get(url)
        
        self.assertEqual(res.status_code,200)
        self.assertEqual(len(res.data),1)
        self.assertEqual(res.data[0]['subscribed_to'],self.user2.id)
        #구독버튼 테스트
    def test_sub_list_post(self):
        url = reverse('sub-list')
        data={
            'subscriber':self.user1.pk,
            'subscribed_to':self.user2.pk
        }

        res = self.client.post(url,data)

        self.assertEqual(res.status_code,201)
        self.assertEqual(Subscription.objects.get().subscribed_to,self.user2)
        self.assertEqual(Subscription.objects.count(),1)
        #구독자 리스트 테스트
    def test_sub_detail_get(self):
        Subscription.objects.create(subscriber=self.user1,subscribed_to = self.user2)
        url = reverse('sub-detail',kwargs={'pk':self.user2.pk})
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)
        self.assertEqual(len(res.data),1)
        #구독 취소
    def test_sub_detail_delete(self):
        sub = Subscription.objects.create(subscriber=self.user1,subscribed_to = self.user2)
        url = reverse('sub-detail',kwargs = {'pk':sub.id})
        res = self.client.delete(url)

        self.assertEqual(res.status_code,204)
        self.assertEqual(Subscription.objects.count(),0)
