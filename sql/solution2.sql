select t3.ridingnumber as RidingNumber,t3.winning as VoteShare,t3.name1 as Party ,cuv.cand_name as CandidateName from (
select t1.ridingnumber,t1.winning,t2.name1 from (
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


) as unionview group by ridingnumber  order by ridingnumber) as t1 
inner join
(
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
) as t2 on t2.ridingnumber = t1.ridingnumber and t1.winning = t2.partyvotes


) as t3  join  (
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
order by t3.winning desc
limit 1


/*
OUTPUT :
261	0.855	1	"Damien Kurek"

Damien Kurek of LIB has maximum vote share among all candidates

*/
