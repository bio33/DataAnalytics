
select count(table1.ridingnumber) as RidingWon,name1 as Party  from (
select ridingnumber, max(partyvotes) as winning from (
select vote_share2.ridingnumber, con as partyvotes, 1 as name1 from vote_share2  
union 
select vote_share2.ridingnumber, lib as partyvotes ,2 as name1 from vote_share2 
union 
select vote_share2.ridingnumber, ndp as partyvotes ,3 as name1 from vote_share2 
union 
select vote_share2.ridingnumber, grn as partyvotes , 4 as name1 from vote_share2 
union 
select vote_share2.ridingnumber, bq as partyvotes  ,5  as name1 from vote_share2 
union 
select vote_share2.ridingnumber, ppc as partyvotes ,6 as name1  from vote_share2 


) as unionview group by ridingnumber  order by ridingnumber) as table1 
Inner join 

(select ridingnumber, partyvotes as winning, name1 from (
select vote_share2.ridingnumber, con as partyvotes, 1 as name1 from vote_share2  
union 
select vote_share2.ridingnumber, lib as partyvotes ,2 as name1 from vote_share2 
union 
select vote_share2.ridingnumber, ndp as partyvotes ,3 as name1 from vote_share2 
union 
select vote_share2.ridingnumber, grn as partyvotes , 4 as name1 from vote_share2 
union 
select vote_share2.ridingnumber, bq as partyvotes  ,5  as name1 from vote_share2 
union 
select vote_share2.ridingnumber, ppc as partyvotes ,6 as name1  from vote_share2 


) as unionview ) as table2 

ON table1.ridingnumber = table2.ridingnumber and table1.winning = table2.winning group by name1 
order by RidingWon desc
limit 1

/*
OUTPUT :
158	2

LIB won the elections by winning maximum amout of 158 ridings

*/


