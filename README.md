# Flask practice: Message board

REST APIs for adding and listing messages

## Requirements
- Python 3
- pip

## Instructions
- Go to the root folder
- Execute `run_app.sh`

## Endpoints
- GET `/message`: List messages
- POST `/message` with JSON body: Add a message

## Examples
- GET `localhost:5000/message?version=2&format=json` results in the response below with status 200 (OK)
```
[
    {
        "content": "Hello World",
        "sender": "Hieu Le",
        "title": "My first message"
    },
    {
        "content": "It's a secret",
        "sender": "Tony Stark",
        "title": "A message from somewhere"
    }
]
```
- POST `localhost:5000/message` with body below results in an empty response with status 201 (CREATED)
```
{
	"title": "Title",
	"content": "Content",
	"sender": "Sender",
	"url": "https://www.google.com"
}
```

