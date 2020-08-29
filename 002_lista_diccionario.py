data = {
    'students':[
        {
            'name': 'Jair Valle',
            'Class': '2015',
            'Scores':[10,9,8,10,7.8,8.9]
        },
        {
            'name': 'Edgar Lucio',
            'Class': '2015',
            'Scores':[8,9,7.5,10,9.8,8.9]
        },
        {
            'name': 'Galielo Guzaman',
            'Class': '2015',
            'Scores':[9.9,10,8.5,10,9,8]
        },
        {
            'name': 'Met Velazques',
            'Class': '2015',
            'Scores':[9,9.5,8,8.9,7.5,10]
        }
    ]
}

print(type(data))

# students = data['students']
students = data.get('students') #es mejor usar get porque es más rápido

print(students)