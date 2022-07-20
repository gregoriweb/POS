-- Problema 8
-- 1- Total de reservas realizadas 
-- 2- Quantas reservas possuíam trechos  
-- 3- Quantas tem troca de aeronave 
-- 4- Quantas reservas foram canceladas por falta de bilhetes não emitidos até o prazo 
-- estipulado 
-- 5- Quantas reservas foram prorrogadas 
-- 6- Qual a média de voos feita por dia, mês e ano 

use voebem;

-- 1- Total de reservas realizadas 
select count(*) from reserva;

-- 2- Quantas reservas possuíam trechos  
select count(*) from trecho_voo tv
join reserva r on r.voo_id = tv.voo_id

-- 3- Quantas tem troca de aeronave 
select * from reserva r
join voo v on v.voo_id = r.voo_id
where upper(v.status) = upper('Troca de Aeronave')


-- 4- Quantas reservas foram canceladas por falta de bilhetes não emitidos até o prazo 
-- estipulado 
select count(*) from reserva where dt_cadastro is null


-- 5- Quantas reservas foram prorrogadas 
select count(*) from reserva where 
DATEDIFF(dt_validade, dt_reserva) > 61


-- 6- Qual a média de voos feita por dia, mês e ano
SELECT 
 count(*) / DATEDIFF(max(dt_embarque),min(dt_embarque)) as voos_dia,
(count(*) / DATEDIFF(max(dt_embarque),min(dt_embarque)))/30 as voos_mes
(count(*) / DATEDIFF(max(dt_embarque),min(dt_embarque)))/365 as voos_ano
FROM trecho_voo;



