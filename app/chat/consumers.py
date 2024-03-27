from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
            self.room_id=self.scope['url_route']['kwargs']['room_id']
            self.room_group_name='chat_'+ str(self.room_id)
            await self.channel_layer.group_add(self.room_group_name,self.channel_name)
            await self.accept()

    async def receive(self,text_data):
          import json
          data_json=json.loads(text_data)
          message=data_json.get('message')

          await self.channel_layer.group_send(self.room_group_name,{
                'type':'chat_message',
                'message':message
          })

    async def chat_message(self,event):
          msg=event['message']
          #email=event['email']

          await self.send(text_data=json.dumps({
                'type':'chat.message',
                'message':msg
                #'email':email
          }))
        
    async def disconnect(self,close_code):
          await self.channel_layer.group_discard(self.room_group_name,self.channel_name)