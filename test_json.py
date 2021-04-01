import json

json_text = '''
{
    "test": [
        {
            "customer": "test1",
            "type": [
                "windows"
            ],
            "contact": [{
                "name": "a",
                "email": "avc@gmail.com"
            }]
        },
        {
            "customer": "test2",
            "type": [
                "android"
            ],
            "contact": [{
                "name": "b",
                "email": "@gmail.com"
            }]
        },
        {
            "customer": "test3",
            "type": [
                "android"
            ],
            "contact": [{
                "name": "a",
                "email": "@naver.com"
            }]
        }
    ]
}
'''

content = json.loads(json_text)
#email = [ x for x in content['test'][0]
email = content['test'][0]
print(email)
