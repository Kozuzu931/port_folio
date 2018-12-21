select 
t4.月,
t4.日,
t4.時,
t4.気温
from 
Tokyo t4,
(select  
t2.id,
t2.月,
t2.日,
t2.時,
t2.気温,
t2.降水量,
t2.日照時間,
(abs(t2.気温 - t1.気温)) diff_temp_abs
 from Tokyo t1 , (select * from Tokyo limit 24, 1416) t2 
 order by diff_temp_abs desc
 limit 10) t3
 where
 t4.id = t3.id + 2 or t4.id = t3.id - 2 or t4.id = t3.id + 1 or t4.id = t3.id - 1;
 