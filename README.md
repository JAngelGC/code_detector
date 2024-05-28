
# How to run
### Activate virtual environment
```
source venv/bin/activate
```

### Start API
```
python3 run.py
```

----------------------------------
------------------------------------

# API DOCUMENTATION
This API provides endpoints to retrieve and submit submissions and its similarities.

### Get submission similarity
#### Request
- Method: GET
- URL: /api/submission/*<submission_id>*/*<homework_id>*
#### Response
- Status: 201 OK
- Content-Type: application/json
- Body:
```
{
    "id": "<submission_id>",
    "matches": "<matches>",
    "similarity": "<0-100>",
    "submissionA": "Submission object",
    "submissionB": "Submission object",
}
```


#### Response example
``` {
  "id": "KvuiiiD35noKAZKXd6KB",
  "matches": [
    {
      "hash": "6092963f04594b9f6a564aa999e2830c",
      "submissionA": [
        {
          "endCol": 41,
          "endLine": 14,
          "startCol": 2,
          "startLine": 2
        }
      ],
      "submissionB": [
        {
          "endCol": 39,
          "endLine": 12,
          "startCol": 2,
          "startLine": 2
        }
      ]
    },
    {
      "hash": "388d19e4e5c3b47e20c2fe19225675ff",
      "submissionA": [
        {
          "endCol": 5,
          "endLine": 0,
          "startCol": 5,
          "startLine": 5
        }
      ],
      "submissionB": [
        {
          "endCol": 44,
          "endLine": 0,
          "startCol": 5,
          "startLine": 5
        },
        {
          "endCol": 49,
          "endLine": 0,
          "startCol": 12,
          "startLine": 12
        }
      ]
    },
    {
      "hash": "383bcd6f45a91b068125025c037e265f",
      "submissionA": [
        {
          "endCol": 44,
          "endLine": 0,
          "startCol": 6,
          "startLine": 6
        }
      ],
      "submissionB": []
    },
    {
      "hash": "9bdad6f637f3184725e733494b107ada",
      "submissionA": [
        {
          "endCol": 44,
          "endLine": 20,
          "startCol": 6,
          "startLine": 6
        }
      ],
      "submissionB": []
    },
    {
      "hash": "a2155eb76da9799c1325f91f380e687d",
      "submissionA": [
        {
          "endCol": 43,
          "endLine": 0,
          "startCol": 9,
          "startLine": 9
        }
      ],
      "submissionB": [
        {
          "endCol": 43,
          "endLine": 0,
          "startCol": 8,
          "startLine": 8
        }
      ]
    },
    {
      "hash": "190a9936e26fb444206aa015dbb421f1",
      "submissionA": [
        {
          "endCol": 32,
          "endLine": 10,
          "startCol": 10,
          "startLine": 10
        }
      ],
      "submissionB": [
        {
          "endCol": 32,
          "endLine": 10,
          "startCol": 9,
          "startLine": 9
        }
      ]
    },
    {
      "hash": "033793aac02ec446f61c92377e966bc3",
      "submissionA": [
        {
          "endCol": 20,
          "endLine": 0,
          "startCol": 13,
          "startLine": 13
        }
      ],
      "submissionB": []
    },
    {
      "hash": "000713e873b9864be77712dfb731bc3a",
      "submissionA": [
        {
          "endCol": 49,
          "endLine": 15,
          "startCol": 14,
          "startLine": 14
        }
      ],
      "submissionB": []
    },
    {
      "hash": "0d40cd236590ab38d4925e07092e8cc0",
      "submissionA": [
        {
          "endCol": 14,
          "endLine": 4,
          "startCol": 19,
          "startLine": 18
        }
      ],
      "submissionB": [
        {
          "endCol": 18,
          "endLine": 4,
          "startCol": 21,
          "startLine": 18
        },
        {
          "endCol": 14,
          "endLine": 4,
          "startCol": 24,
          "startLine": 23
        }
      ]
    },
    {
      "hash": "4df55dc74e6fa9b1d46ef59a38bf9ede",
      "submissionA": [
        {
          "endCol": 19,
          "endLine": 17,
          "startCol": 19,
          "startLine": 19
        }
      ],
      "submissionB": [
        {
          "endCol": 19,
          "endLine": 17,
          "startCol": 24,
          "startLine": 24
        }
      ]
    },
    {
      "hash": "84ec70d07869a6b1cf7cba6823c179d9",
      "submissionA": [],
      "submissionB": [
        {
          "endCol": 44,
          "endLine": 20,
          "startCol": 5,
          "startLine": 5
        },
        {
          "endCol": 49,
          "endLine": 15,
          "startCol": 12,
          "startLine": 12
        }
      ]
    },
    {
      "hash": "2764545a5ea5028b650012faaae0aefa",
      "submissionA": [],
      "submissionB": [
        {
          "endCol": 13,
          "endLine": 8,
          "startCol": 19,
          "startLine": 19
        }
      ]
    },
    {
      "hash": "1525ab8dfc3b30ee3924d83a85f2eec1",
      "submissionA": [],
      "submissionB": [
        {
          "endCol": 14,
          "endLine": 0,
          "startCol": 21,
          "startLine": 21
        }
      ]
    }
  ],
  "similarity": 60.0,
  "submissionA": {
    "author": "Angel",
    "content": "",
    "filename": "my_file.py",
    "id": "KvuiiiD35noKAZKXd6KB"
  },
  "submissionB": {
    "author": "Angel",
    "content": "",
    "filename": "my_file.py",
    "id": "8tJVZ47elSBQWYZ944u5"
  }
}
```


------------------------------

### Get all homeworks
#### Request
- Method: GET
- URL: /api/homework
#### Response
- Status: 201 OK
- Content-Type: application/json
- Body:
```
{
    "homeworks": "List of homeworks",
    "message": "A message",
}
```


#### Response example
```
{
  "homeworks": [
    {
      "homework_id": "VOoS30fvywYfrezeXjwl",
      "name": "mi tarea de mate"
    }
  ],
  "message": "Homeworks retrieved successfully"
}
```


------------------------------

### Post a submission
#### Request
- Method: POST
- URL: /api/submission
#### Response
- Status: 201 OK
- Content-Type: application/json
- Body:
```
{
    "author": "an author",
    "homework_id": "a homework id",
    "file_name": "a file name",
    "file_url": "url of the code"
}
```


#### Response example
```
{
  "message": "Homework submission saved successfully",
  "submission_id": "<submission_id>"
}
```

------------------------------

### Create a homework
#### Request
- Method: POST
- URL: /api/homework
#### Response
- Status: 201 OK
- Content-Type: application/json
- Body:
```
{
    "name": "a super name"
}
```


#### Response example
```
{
  "homework_id": "e4N5XwlT4c7zv364Zy2w",
  "message": "Homework created successfully"
}
```