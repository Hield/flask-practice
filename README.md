# Flask practice: Message board

REST + SOAP APIs for adding and listing messages

## Requirements
- Python 3
- pip

## Instructions
- Go to the root folder
- Execute `run_app.sh`

## Endpoints
- GET `/message`: List messages
- POST `/message` with JSON body: Add a message
- POST `/soap`: SOAP request

## REST Examples
- GET `localhost:5000/message?version=2&format=xml` results in the response below with status 200 (OK)
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

## SOAP Examples
- POST request to `localhost:5000/soap`
```
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
     <CreateMessage xmlns="http://example.com/sample.wsdl">
     	<title>A new title, baby</title>
     	<content>A new content, dear</content>
     	<sender>Anonymous</sender>
     	<url>http://www.yahoo.com</url>
    </CreateMessage>
   </soap:Body>
</soap:Envelope>
```
- Response
```
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <soap:Body>
        <CreateMessageResponse xmlns="">
            <result>Success</result>
        </CreateMessageResponse>
    </soap:Body>
</soap:Envelope>
```
