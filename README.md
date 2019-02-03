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
### param
```json
{
  "source" : "sourceName"
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
### body
```json
{
  "alarm": "boolean"
}
```
