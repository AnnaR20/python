-- hw8
use vk;
-- #3
select gender, count(*) as total
  from profiles as p
  join likes as l
  on p.user_id = l.user_id
  group by p.gender
  order by p.user_id desc
  limit 1;
 

-- #4
 select count(l.target_type_id) as likes_to_10_youngest_users
    from profiles as p
      left join likes as l
        on p.user_id = l.target_id 
    where l.target_type_id = 2 and p.user_id IN (SELECT * FROM (SELECT user_id FROM profiles ORDER BY birthday DESC LIMIT 10) as youngest_10)
    ; 
  
-- #5
select CONCAT(u.first_name, ' ', u.last_name) AS user_names, count(distinct(l.id)) + count(distinct(m.id)) + count(distinct(m2.id)) as activity
  from users u
  left join likes l
     on u.id = l.user_id
  left join media m
     on u.id = m.user_id
  left join messages m2 
     on u.id = m2.from_user_id
    group by u.id
   order by activity
  limit 10;
 