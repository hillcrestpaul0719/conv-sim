show1 = {
    'conversation': [
        {
            'speaker': 0,
            'text': '''This is a test of the Conversation Simulation Bot. If you are reading this message. This bot is working correctly as configured, and no action is necessary. Thanks!
            '''
        }
    ],
    'showtime': [2020, 1, 1, 0, 0]
}

show2 = {
    'conversation': [
        {
            'speaker': 0,
            'text': '''Type here what you want this bot to say!
            And say it the bot will'''
        },
        {
            'speaker': 1,
            'text': '''Yes. You are right.
            It's yoda'''
        },
    ],
    'showtime': [2050, 7, 20, 6, 23]
}

speakers = [
    {
        'id': 0,
        'name': "Yoda",
        'profile_picture': "https://upload.wikimedia.org/wikipedia/en/9/9b/Yoda_Empire_Strikes_Back.png",
        'interruption_responses': ['What is here, I will say when I am interrupted', 'Shush!']
    },
    {
        'id': 1,
        'name': "Other yoda",
        'profile_picture': "https://upload.wikimedia.org/wikipedia/en/6/6f/Yoda_Attack_of_the_Clones.png",
        'interruption_responses': ['These are called interruption responses!', 'Stop!']
    },
]

shows = [speakers, [show1, show2]]
