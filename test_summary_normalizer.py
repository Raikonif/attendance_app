from src.summary_builder import normalize_summary_keys, build_summary_object


def test_normalize_summary_v1():
    raw_data = {
        'Meeting title': 'Practice Modulo 1 - Grupo 4',
        'Attended participants': '1',
        'Start time': '10/10/22, 5:37:48 PM',
        'End time': '10/10/22, 5:38:21 PM',
        'Meeting duration': '33s',
        'Average attendance time': '26s'
    }

    expected_summary = {
        'Title': 'Practice Modulo 1 - Grupo 4',
        'Id': 'Practice Modulo 1 - Grupo 4',
        'Attended participants': 1,
        'Start Time': '10/10/22, 5:37:48 PM',
        'End Time': '10/10/22, 5:38:21 PM',
        'Duration': {
            'hours': 0,
            'minutes': 0,
            'seconds': 33
        }
    }

    assert normalize_summary(raw_data) == expected_summary
        

def test_normalize_summary_v2():
    raw_data = {
        'Total Number of Participants', '17', 
        'Meeting Title', 'General', 
        'Meeting Start Time', '10/18/22, 5:49:42 PM', 
        'Meeting End Time', '10/18/22, 7:53:52 PM', 
        'Meeting Id', '220492dd-c020-49b9-bb1c-64b665217a8d'
    }

    expected_summary = {
        'Title': 'General',
        'Id': '220492dd-c020-49b9-bb1c-64b665217a8d',
        'Attended participants': 7,
        'Start Time': '10/18/22, 5:49:42 PM',
        'End Time': '10/18/22, 7:53:52 PM',
        'Duration': {
            'hours': 2,
            'minutes': 4,
            'seconds': 10
        }
    }

    assert normalize_summary(raw_data) == expected_summary


def test_build_summary_object():
    raw = {
        'Title': 'General',
        'Id': '220492dd-c020-49b9-bb1c-64b665217a8d',
        'Attended participants': 7,
        'Start Time': '10/18/22, 5:49:42 PM',
        'End Time': '10/18/22, 7:53:52 PM',
        'Duration': {
            'hours': 2,
            'minutes': 4,
            'seconds': 10
        }
    }

    summary = build_summary_object(raw)
    assert summary is not None
    assert type(summary) is Summary
    assert summary.id == summary['Id']
    assert summary.title == summary['Title']
    assert summary.attended_participants == summary['Attended participants']
    assert summary.start_time == summary['Start Time']
    assert summary.end_time == summary['End Time']
    assert type(summary.duration) is Duration
    assert summary.duration.hours == summary['Duration']['hours']
    assert summary.duration.minutes == summary['Duration']['minutes']
    assert summary.duration.seconds == summary['Duration']['seconds']


