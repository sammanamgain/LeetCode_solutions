-- Write your PostgreSQL query statement below
select tweet_id 
from Tweets
where Length(content)>15