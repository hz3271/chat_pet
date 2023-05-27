
class Command:
    def __init__(self, dict_data):
        self.id_ = None
        self.text = None
        self.data_list = dict_data['data']
        self.extract_text_id()

    def extract_text_id(self):
        for data_item in self.data_list:
            if data_item['type'] != 'FriendMessage':
                continue

            message_chain = data_item['messageChain']
            if not message_chain:
                continue
            self.text = self._extract_text_from_message_chain(message_chain)
            self.id_ = self._extract_id_from_sender(data_item['sender'])
        return self.id_, self.text

    def _extract_text_from_message_chain(self, message_chain):
        for message_item in message_chain:
            if message_item['type'] == 'Plain':
                self.text = message_item['text']
                #print("Text:", self.text)
        return self.text

    def _extract_id_from_sender(self, sender):
        self.id_ = sender['id']
        #print("ID:", self.id_)
        return self.id_


#text={'code': 0, 'msg': '', 'data': [{'type': 'FriendMessage', 'messageChain': [{'type': 'Source', 'id': 23475, 'time': 1682673099}, {'type': 'Plain', 'text': '/帮助'}], 'sender': {'id': 564243117, 'nickname': '曦城kirei', 'remark': '曦城kirei'}}]}
#command=Command(text)