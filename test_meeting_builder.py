from src.participant_builder import build_participant_object


def test_build_meeting_object():
    raw_meeting = {
        'Title': 'General',
        'Id': '220492dd-c020-49b9-bb1c-64b665217a8d',
        'Attended participants': 7,
        'Start Time': '10/18/22, 5:49:42 PM',
        'End Time': '10/18/22, 7:53:52 PM',
        'Duration': {
            'hours': 2,
            'minutes': 4,
            'seconds': 10
        },
        'Participants': [
            {
                'Full Name': 'Santiago Martinez Saavedra',
                'Join time': '10/18/22, 7:49:42 PM',
                'Leave time': '10/18/22, 7:53:52 PM',	
                'Duration': {
                    'Hours': 0,
                    'Minutes': 6,
                    'Seconds': 26
                },	
                'Email': 'Santiago.Martinez@fundacion-jala.org',
                'Role': 'Presenter',
                'Participant ID (UPN)': 'Santiago.Martinez@fundacion-jala.org'
            },
            {
                'Full Name': 'Random Random Random',
                'Join time': '10/18/22, 5:49:42 PM',
                'Leave time': '10/18/22, 7:50:52 PM',	
                'Duration': {
                    'Hours': 1,
                    'Minutes': 46,
                    'Seconds': 26
                },	
                'Email': 'randomname.randomlastname@fundacion-jala.org',
                'Role': 'Presenter',
                'Participant ID (UPN)': 'randomname.randomlastname@fundacion-jala.org'
            },
        ]
    }

    meeting = build_meeting_object(raw_meeting)
    assert meeting is not None
    assert type(meeting) is Meeting
    assert meeting.id == raw_meeting['Id']

    ## assert summary object
    assert meeting.summary is not None
    assert type(meeting.summary) is Summary
    assert meeting.summary.title == raw_meeting['Title']
    assert meeting.summary.id == raw_meeting['Id']
    assert meeting.summary.attended_participants == raw_meeting['Attended participants']
    assert meeting.summary.start_time == raw_meeting['Start Time']
    assert meeting.summary.end_time == raw_meeting['End Time']
    assert meeting.summary.duration.hours == raw_meeting['Duration']['hours']
    assert meeting.summary.duration.minutes == raw_meeting['Duration']['minutes']
    assert meeting.summary.duration.seconds == raw_meeting['Duration']['seconds']

    ## assert participant object
    assert type(meeting.participants) is not None
    assert type(meeting.participants) is list
    assert len(meeting.participants) == len(raw_meeting['Participants'])
    assert all(type(participant) is Participant for participant in meeting.participants)

    