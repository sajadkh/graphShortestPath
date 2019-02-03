# Emergency Navigation
in the emergency condition we cannot find exit doors of a building such as university.   
we deploy a system for finding emergency exit.

## APIs list
### Find Path 
#### method
```
GET 
```
#### route
```djangourlpath
{{serverUrl}}/path/
```
#### param
```json
{
  "source" : "sourceName"
}
```
#### success output
```json
{
  "path": [
    "3",
    "2",
    "1"
  ],
  "fire": "",
  "status": "success"
}
```

#### error output
```json
{
  "message": "I'm so sorry for you, you were a good guy. God bless you!",
  "error": "PathNotFound",
  "status": "error"
}
```



### set sensor
#### method
```
PUT
```
#### route
```
{{serverUrl}}/sensor/{{sensorId}}/
```
#### body
```json
{
  "alarm": "boolean"
}
```

#### success output
```json
{
  "id": 4,
  "alarm": true
}
```
