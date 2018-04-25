import itchat
from itchat.content import *


class Messages(object):

    @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
    def text_reply(msg):
        '''Process text messages'''
        return msg['Text']

    @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
    def download_files(msg):
        '''Processing media messages'''
        if msg['Type'] == 'PICTURE':
            return "图片已收到"
        # i = msg['Text'](msg['FileName'])
        # i = msg['Text']

    @itchat.msg_register(FRIENDS)
    def add_friend(msg):
        '''Process friend add request'''
        itchat.add_friend(**msg['Text'])
        itchat.send_msg("Nice to meet you, I'm Lcarusd!",
                        msg['RecommendInfo']['UserName'])

    @itchat.msg_register(TEXT, isGroupChat=True)
    def text_reply(msg):
        '''Processing group messages'''
        if msg['isAt']:
            itchat.send(u'@%s\u2005I received: %s' %
                        (msg['ActualNickName'], msg['Content']), msg['FromUserName'])

    def get_friends_info():
        itchat.get_friends()    # 获取全部好友信息
        # itchat.search_friends()  # 获取自己的用户信息


itchat.auto_login(hotReload=False, enableCmdQR=2)
itchat.run()
