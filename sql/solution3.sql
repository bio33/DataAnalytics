
select t4.rnum as RidingNumber, t4.cand_name as CandidateName, vs.ridingname_en as RidingName from (


select t3.ridingnumber as rnum,t3.name1 as party_int, cuv.cand_name  from (
select table1.ridingnumber,table2.name1 from (
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

ON table1.ridingnumber = table2.ridingnumber and table1.winning = table2.winning order by table1.ridingnumber

) as t3 join  (
select candidates2.ridingnumber, con as cand_name, 1 as name1 from candidates2  
union 
select candidates2.ridingnumber, lib as cand_name ,2 as name1 from candidates2 
union 
select candidates2.ridingnumber, ndp as cand_name ,3 as name1 from candidates2 
union 
select candidates2.ridingnumber, grn as cand_name , 4 as name1 from candidates2 
union 
select candidates2.ridingnumber, bq as cand_name  ,5  as name1 from candidates2 
union 
select candidates2.ridingnumber, ppc as cand_name ,6 as name1  from candidates2 
) as cuv on cuv.ridingnumber = t3.ridingnumber and cuv.name1 = t3.name1
where cuv.cand_name like 'John%'

) as t4 join vote_share2 as vs on vs.ridingnumber = t4.rnum


/*
OUTPUT : 

30	"John Williamson"	"New Brunswick Southwest"
114	"John Brassard"	"Barrie-Innisfil"
193	"John Nater"	"Perth-Wellington"
205	"John McKay"	"Scarborough-Guildwood"
281	"John Barlow"	"Foothills"
*/