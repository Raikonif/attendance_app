import pytest
from src.participant_builder import normalize_participant, resolve_participant_join_last_time, build_participant_object

def test_resolve_join_last_time():
    raw_participants = [
        {
            'Full Name': 'Katerin Apaza Romero',
            'Join Time': '10/14/22, 5:53:17 PM',
            'Leave Time': '10/14/22, 6:31:17 PM',
            'Duration': '37m 59s',
            'Email': 'Katerin.Apaza@fundacion-jala.org',
            'Role': 'Presenter',
            'Participant ID (UPN)': 'Katerin.Apaza@fundacion-jala.org'
        },
        {
            'Full Name': 'Katerin Apaza Romero',
            'Join Time': '10/14/22, 6:38:21 PM',
            'Leave Time': '10/14/22, 7:37:08 PM',
            'Duration': '58m 46s',
            'Email': 'Katerin.Apaza@fundacion-jala.org',
            'Role': 'Presenter',
            'Participant ID (UPN)': 'Katerin.Apaza@fundacion-jala.org'
        }
    ]

    assert resolve_participant_join_last_time(raw_participants) == {
        'Name': 'Katerin Apaza Romero',
        'First Join Time': '10/14/22, 5:53:17 PM',
        'Last Leave time': '10/14/22, 7:37:08 PM',	
        'In-meeting Duration': '1h 36m 45s',	
        'Email': 'Katerin.Apaza@fundacion-jala.org',
        'Role': 'Presenter',
        'Participant ID (UPN)': 'Katerin.Apaza@fundacion-jala.org'
    }


def test_normalize_participant_v1():
    raw_participant = {
        'Name': 'Santiago Martinez Saavedra',
        'First Join Time': '10/14/22, 5:51:55 PM',
        'Last Leave time': '10/14/22, 7:40:21 PM',	
        'Duration': '1h 48m 26s',	
        'Email': 'Santiago.Martinez@fundacion-jala.org',
        'Role': 'Presenter',
    }

    assert normalize_participant(raw_participant) == {
        'Full Name': 'Santiago Martinez Saavedra',
        'Join time': '10/14/22, 5:51:55 PM',
        'Leave time': '10/14/22, 7:40:21 PM',	
        'In-meeting Duration': {
            'Hours': 1,
            'Minutes': 48,
            'Seconds': 26
        },	
        'Email': 'Santiago.Martinez@fundacion-jala.org',
        'Role': 'Presenter',
        'Participant ID (UPN)': 'Santiago.Martinez@fundacion-jala.org'
    }


def test_normalize_participant_v2():
    raw_participant = {
        'Full Name': 'Emily Cadena Quisbert',
        'Join Time': '10/18/2022, 5:50:03 PM',
        'Leave Time': '10/18/2022, 7:53:52 PM',
        'In-meeting Duration': '2h 3m',
        'Email': 'Salome.Quispe@fundacion-jala.org',
        'Role': 'Presenter',
        'Participant ID (UPN)': 'Salome.Quispe@fundacion-jala.org'
    }
    
    assert normalize_participant(raw_participant) == {
        'Full Name': 'Santiago Martinez Saavedra',
        'Join time': '10/14/22, 5:51:55 PM',
        'Leave time': '10/14/22, 7:40:21 PM',	
        'In-meeting Duration': {
            'Hours': 2,
            'Minutes': 3,
            'Seconds': 0
        },	
        'Email': 'Santiago.Martinez@fundacion-jala.org',
        'Role': 'Presenter',
        'Participant ID (UPN)': 'Santiago.Martinez@fundacion-jala.org'
    }

def test_build_participant_object():
    raw = [
        {
            'Full Name': 'Santiago Martinez Saavedra',
            'Join time': '10/14/22, 5:51:55 PM',
            'Leave time': '10/14/22, 7:40:21 PM',	
            'In-meeting Duration': {
                'Hours': 2,
                'Minutes': 3,
                'Seconds': 0
            },	
            'Email': 'Santiago.Martinez@fundacion-jala.org',
            'Role': 'Presenter',
            'Participant ID (UPN)': 'Santiago.Martinez@fundacion-jala.org'
        },
    ]

    participant = build_participant_object(raw)
    assert participant is not None
    assert type(participant) is participant
    assert participant.full_name == raw['Full Name']
    assert participant.join_time == raw['Join Time']
    assert participant.leave_time == raw['Leave Time']
    assert participant.email == raw['Email']
    assert participant.role == raw['Role']
    assert participant.id == raw['Participant ID (UPN)']
    assert participant.in_meeting_duration.hours == raw['In-meeting Duration']['hours']
    assert participant.in_meeting_duration.minutes == raw['In-meeting Duration']['minutes']
    assert participant.in_meeting_duration.seconds == raw['In-meeting Duration']['seconds']


def test_build_participant_object():
    raw = [
        {
            'Full Name': None,
            'Join time': None,
            'Leave time': None,	
            'In-meeting Duration': {
                'Hours': 2,
                'Minutes': 3,
                'Seconds': 0
            },	
            'Email': 'Santiago.Martinez@fundacion-jala.org',
            'Role': 'Presenter',
            'Participant ID (UPN)': 'Santiago.Martinez@fundacion-jala.org'
        },
    ]

    with pytest.raises(
        expected_exception=ValueError, 
        match="Full Name, Join time, Leave time cannot be None"):
        build_participant_object(raw)