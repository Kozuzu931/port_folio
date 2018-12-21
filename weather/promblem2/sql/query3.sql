select 
tt1.main_id,
(cast(tt2.月 as text) || '/' || cast(tt2.日 as text) || ' '|| cast(tt2.時 as text) || ':00 ' || '~' || cast(tt1.main_month as text) || '/' || cast(tt1.main_day as text) || ' ' || cast(tt1.main_time as text) || ':00') term_rain,
(tt1.main_rain + tt1.even_rain + tt2.降水量) rain_sum_three_hour
from (select 
 t3.id main_id,
 t3.月 main_month,
 t3.日 main_day,
 t3.時 main_time,
 t3.降水量 main_rain,
 t2.id even_id,
 t2.降水量 even_rain
 from
 (select * from Tokyo where (id + 1) % 3 = 0) t3 left outer join Tokyo t2 on t2.id = t3.id - 1) tt1 left outer join Tokyo tt2 on tt2.id = tt1.main_id - 2
 order by rain_sum_three_hour desc
 limit 10;