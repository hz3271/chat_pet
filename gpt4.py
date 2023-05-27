from pyChatGPT import ChatGPT
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

session='eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..5gdQgVDM2tbICGWH.zJNH0Efs7L2owzJzz5W_wlrmu97ZxUpgu4gMl2-momGJDHuUx6RKWHXSHZB_C-TdowiDvsTzOjcVLxQfMYQcV8lZHmiI449wMW0RdDrKGKlUI7qQw5VMBDLa85VD899PNwY9fQH9aAwJI09ry4JruzPpdxx-wv4Oxir49Gi_YiRzU3UGFYaY9oQqMipLEqeZQFcUE2-y20BOPvMscuBVVzT8vFDoi3HnJQVQMKyf4yUsS8mUJ-gVO2P9yhc_LKbJV9DKEWiWSuaGgqc0eZ4Zu5AIqvztvpMP4MEhfY6xfHDXHlvIhkW3tVlgGaU_gmibb8fm0EbLyV5ke-qw1daxu7q-y-4Hb1cb9obRGjyKa7BFmP88uUoMt0ep06FHeu0J--jkffDvCb91EkgyvMTt9sg3ALeDarGceq_8Ix1gJHQWdLYG6FYQ8uRll466avoYGCsxMyWJLyRlHXmXEm_Wi9t6VqR8ipxsAl1WBImFocCIT27_I0PxReTndcX1sJFRkOXrHQBLKgbB5foZBmg5E2mIvK2EVtjx1GwUt1UJiCsEoXhE4sO-5_OB-5oACr7k6ZY2InYky_yi7hlh7cDOv5yj7Cz3vLa12zYOvlKWqTCtcZZg_WSluky--_dRMZ9RNUW_GMP6S4H-iMPZofwr_zmtrn5Wy9Sw5bxBWcBYa56P1n2Ve3SO4PFcQgPrfTB1hiplPZ3Mwpq4qWib38OGGJvnJPbT8Pb6kN_pbbtJzpfN29R0CE6noCE9bbJ11TEZJ6v2FG-BH8QeY8kGclw6aIIwQwQYf8ctvuKr4ggzcu17V_PPR0h321rUJ1dZ4wbg9s5ayUoaf1sjw8NDtW10VRT5RxB0l58tPb10_YwOzTjR6SE3fHGz5Iw_mFiSvuZLMNj1o8OjIQfDyZVBQ42K6BQ20qVjSvVrgTlczsPRoHTv4MHQ5TeDOHKmkaKnkxaqXPdyw2_8W_01jFCQjOO6UhqthEuKVg2gYndZ_gNHqX8v2aswjNNRPXp7OeBOFqGO4qxLrH8mZ3opGIBtOSexXtwARh_42soi7QN13UhNAg10tnsLA-Oopkdkwpv2qcD_Qg0hsffjfUSvE0HJf4mljIBCpvjwHeL3A5_j9U2jN4De8eJXgn6UQ_-0_xJmWsCZs9syGRASsRJfRwfPwwebsw-uRiWKgJZWYHvSAYf75R7XBu3J2G6kbXE4J7FRrLSajDdhqskELt7CrfafUa4k3DKGDkK6qNERQu5jZ1vaqcSbZQbS-m_qDc_TiJpLHYXP5xBX59tgKRtyu8XeuCZkf2AFVzO3_k7pSong8Avkdmp3GZMnenYU9hz48leT_OYzSNW0xxCsT_57XW-P3ujvrJQ1KigNrC54SQKH4JDis1kAUZjpUcCzSboLoeVpYI6tKjf56-gGO5JwhABkkz4auHvW5S5lXJBgumma9-BmgzdWReEK-rziIO2Phzn751TlN2cypSwW2sgt8hjXz4MlWMuwFoIfqiq08N4hpUYpgJ4aFGX6iAe1MNc1HbP9SYGWNh8m38OvI9McY2GS_5rKZTPw07Us4RCjsVKLLvWybys5G4bWtShyL_gLCMXVDQecwk6kwt--Q5-JL9tkn84VSXZJNG00SBZ5gBYEPlDhGgpgOU2jZrd9C-jEUYW0BGkBNMIC8XHSqFsGFvyQrd0T1NcV7uV7u3v3CzBeSS--1mzCIJYYFUST9F5M4Doo3acx67VHEAzlwWLrg8MQ9YI27aXNHGMZACpNmaT9SY_Kl9qOn0_f5KDZrAX6CsaY-DSaYPEeEHYo8EofbFDtvddQOyQTD2RW5s5yAzYs10uzly8vvm56Cd6leSNB1m2DUN1qzEdqrnKme3IQWz1SzKM9w2iolEa8zOB7vERCajawaEAOOs7OkjbooiGMBkMjlZtTOkq6t_62QTI656sHJa_TCbq1d_4kd6p_s15jX2wXDD-RgEHqqEHlyaWEagM70ZOZgzBOQ1u9YUdoHqsou91-nXTmEpaYTczTpgwC3XUwfKJTgatMX7AJfaLOGE_4SUPJ45BfZtq0Ih3NTwVZGCEFROB6h5K49vq9ft2C561riNC_J6pBbKe4qSx9D6sATQegH_FAhv-fMnxmnJCgPUECjY6pZtneDhU_NSqOIYTEUCS-xERhqOxlIKiDHwosZ-S2r8wQtY7-RqLuTIGWdtMdRV7zkMl_uVlNf8o17KRDFFpVwUHTpTQE2vSZg2IWpy6I6tMdYmDfgtiIV72yfNVO909pwm9QMXr7lKXcEl52pbRlB7ouSUkiShOY_QMoKGUN6HmWNUV-aKu2Mct4E1nfjoAtZKAAxF8noWBVm9eBZKi4cDKOP5MPOkQRRCTEG6X4T6B5rkinVSF7tDllQW6EtP-uB67T2pr0ms6301sANur8Y2Z_DpUshq-oaooQLHOz8vHY6WefzPZPwJInniH_MtLqRl7ho5sH_XM0hhy4vjU7eAXBqnZkQKVS4tJJO_YfJVy2vBlzJgd1UeKvpJkubf0ttNBkpgX4PJnhENsmHx7hfJpeBMlK74CNIWQFYGrychCBGnScrqGzApjzNtQ8ZFq7PXsjFg1Rhd7sdxfxsmRFtf8w97TcXKn3RN_MLPKwgOvq8It_Idd19LtxXKH5LCSRQBrtW2TVqiLXuKdPc56gF-ezxP4AoM7mwlMu4QDrVf65n6Fuk7RDXhFPgtHZN5gMdLaGBpgq2tdrWKgL5CzaUSzDqyPyarlrpFNsiJw6dE9h3SxaqTjl0zXYxHrGBO8WEnBaHPFR-nIEis3WYYJopNhX036xCESl0oaXGWAIf-zoKd0BwPN-tg.uvjoL6BTfkf9l2z9YZ-vYA'

class chatbot_conversation():
    def __init__(self):
        id = '645a69ce-fb40-47e7-a4fd-a15c41894f4e'
        conversation_id = id
        session_token = session
        self.chat = ChatGPT(session_token, conversation_id)

        clear_screen()
        print(
            'Conversation started. Type "reset" to reset the conversation. Type "quit" to quit.\n'
        )

    def get_res(self, input):
        response = self.chat.send_message(input)
        return response


#cn=chatbot_conversation()
#answ=cn.get_res(input("你好"))
#print(answ)