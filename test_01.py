from toon_format import encode, decode

print('=' * 40)
print('Original JSON data:')
data = {
    "company": "TechCorp",
    "employees": [
        {
            "id": 1,
            "name": "Alice",
            "position": "Software Engineer",
            "skills": [
                "Python",
                "Django",
                "Machine Learning"
            ],
            "projects": [
                {
                    "project_name": "AI Chatbot",
                    "status": "Completed",
                    "duration": "6 months"
                },
                {
                    "project_name": "Data Analytics Platform",
                    "status": "In Progress",
                    "duration": "3 months"
                }
            ]
        },
        {
            "id": 2,
            "name": "Bob",
            "position": "Product Manager",
            "skills": [
                "Product Strategy",
                "Market Research"
            ],
            "projects": [
                {
                    "project_name": "New Mobile App",
                    "status": "Completed",
                    "duration": "8 months"
                }
            ]
        }
    ],
    "office_locations": [
        {
            "city": "San Francisco",
            "address": "123 Main St",
            "employees_count": 150
        },
        {
            "city": "New York",
            "address": "456 Park Ave",
            "employees_count": 100
        }
    ],
    "revenue": 5000000,
    "year_founded": 2010,
    "is_public": False
}
print(data)

print('\n' + '-' * 40 + '\n')

print('Converted to Toon format:')
encode_data = encode(data)
print(encode_data)

print('\n' + '-' * 40 + '\n')
print('Converted to json format:')
decode_data = decode(encode_data)
print(decode_data)

print('=' * 40)