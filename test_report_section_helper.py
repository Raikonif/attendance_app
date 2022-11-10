from src.report_section_helper import  extract_section_rows


def test_extract_section_data_summary():
    data = [
        ['1. Summary'], 
        ['Meeting title', 'Practice Modulo 1 - Grupo 4'], 
        ['Start time', '10/10/22, 5:37:48 PM'], 
        ['End time', '10/10/22, 5:38:21 PM'], 
        ['Meeting duration', '33s'], 
        ['Average attendance time', '26s'],
        [],
        ['2. Participants'],
        ['Name', 'First join', 'Last leave', 'In-meeting duration', 'Email', 'Participant ID (UPN)', 'Role'], 
        ['Diego Terrazas Sanchez', '10/10/22, 5:37:54 PM', '10/10/22, 5:38:21 PM', '26s', 'Diego.Terrazas@fundacion-jala.org', 'Diego.Terrazas@fundacion-jala.org', 'Presenter'], 
        [], 
        ['3. In-Meeting activities'], 
        ['Name', 'Join time', 'Leave time', 'Duration', 'Email', 'Role'], 
        ['Diego Terrazas Sanchez', '10/10/22, 5:37:54 PM', '10/10/22, 5:38:21 PM', '26s', 'Diego.Terrazas@fundacion-jala.org', 'Presenter']
    ]
    
    section = extract_section_rows(data, '1. Summary', '2. Participants')
    assert section is not None
    assert type(section) is list
    assert all(row != [] for  _, row in section)
    assert all(row != ['1. Summary'] for _, row in section)
    assert all(row != ['2. Participants'] for _, row in section)
    assert [row for _, row in section] == [
        ['Meeting title', 'Practice Modulo 1 - Grupo 4'], 
        ['Start time', '10/10/22, 5:37:48 PM'], 
        ['End time', '10/10/22, 5:38:21 PM'], 
        ['Meeting duration', '33s'], 
        ['Average attendance time', '26s']
    ]

def test_extract_section_data_participants():
    data = [
        ['1. Summary'], 
        ['Meeting title', 'Practice Modulo 1 - Grupo 4'], 
        ['Start time', '10/10/22, 5:37:48 PM'], 
        ['End time', '10/10/22, 5:38:21 PM'], 
        ['Meeting duration', '33s'], 
        ['Average attendance time', '26s'],
        [],
        ['2. Participants'],
        ['Name', 'First join', 'Last leave', 'In-meeting duration', 'Email', 'Participant ID (UPN)', 'Role'], 
        ['Diego Terrazas Sanchez', '10/10/22, 5:37:54 PM', '10/10/22, 5:38:21 PM', '26s', 'Diego.Terrazas@fundacion-jala.org', 'Diego.Terrazas@fundacion-jala.org', 'Presenter'], 
        [], 
        ['3. In-Meeting activities'], 
        ['Name', 'Join time', 'Leave time', 'Duration', 'Email', 'Role'], 
        ['Diego Terrazas Sanchez', '10/10/22, 5:37:54 PM', '10/10/22, 5:38:21 PM', '26s', 'Diego.Terrazas@fundacion-jala.org', 'Presenter']
    ]    
    section = extract_section_rows(data, '2. Participants', '3. In-Meeting activities')
    assert section is not None
    assert type(section) is list
    assert all(row != [] for _, row in section)
    assert all(row != ['2. Participants'] for _, row in section)
    assert all(row != ['3. In-Meeting activities'] for _, row in section)
    assert [row for _, row in section] == [
        ['Name', 'First join', 'Last leave', 'In-meeting duration', 'Email', 'Participant ID (UPN)', 'Role'], 
        ['Diego Terrazas Sanchez', '10/10/22, 5:37:54 PM', '10/10/22, 5:38:21 PM', '26s', 'Diego.Terrazas@fundacion-jala.org', 'Diego.Terrazas@fundacion-jala.org', 'Presenter']
    ]

def test_extract_section_data_activities():
    data = [
        ['1. Summary'], 
        ['Meeting title', 'Practice Modulo 1 - Grupo 4'], 
        ['Start time', '10/10/22, 5:37:48 PM'], 
        ['End time', '10/10/22, 5:38:21 PM'], 
        ['Meeting duration', '33s'], 
        ['Average attendance time', '26s'],
        [],
        ['2. Participants'],
        ['Name', 'First join', 'Last leave', 'In-meeting duration', 'Email', 'Participant ID (UPN)', 'Role'], 
        ['Diego Terrazas Sanchez', '10/10/22, 5:37:54 PM', '10/10/22, 5:38:21 PM', '26s', 'Diego.Terrazas@fundacion-jala.org', 'Diego.Terrazas@fundacion-jala.org', 'Presenter'], 
        [], 
        ['3. In-Meeting activities'], 
        ['Name', 'Join time', 'Leave time', 'Duration', 'Email', 'Role'], 
        ['Diego Terrazas Sanchez', '10/10/22, 5:37:54 PM', '10/10/22, 5:38:21 PM', '26s', 'Diego.Terrazas@fundacion-jala.org', 'Presenter']
    ]

    section = extract_section_rows(data, '3. In-Meeting activities', '')
    assert section is not None
    assert type(section) is list
    assert all(row != [] for _, row in section)
    assert all(row != ['3. In-Meeting activities'] for _, row in section)
    assert all(row != [] for _, row in section)
    assert [row for _, row in section] == [
        ['Name', 'Join time', 'Leave time', 'Duration', 'Email', 'Role'], 
        ['Diego Terrazas Sanchez', '10/10/22, 5:37:54 PM', '10/10/22, 5:38:21 PM', '26s', 'Diego.Terrazas@fundacion-jala.org', 'Presenter']
    ]
 