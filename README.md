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
<?xml version='1.0' encoding='utf8'?>
<messages>
    <message>
        <title>My first message</title>
        <content>Hello World</content>
        <sender>Hieu Le</sender>
        <url>https://www.google.com/</url>
    </message>
    <message>
        <title>A message from somewhere</title>
        <content>It's a secret</content>
        <sender>Tony Stark</sender>
        <url>https://www.bbc.co.uk/</url>
    </message>
    <message>
        <title>Title</title>
        <content>Content</content>
        <sender>Sender</sender>
        <url>https://www.google.com</url>
    </message>
</messages>
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

