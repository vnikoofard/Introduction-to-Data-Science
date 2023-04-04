use banco;
-- Exemplo 1. Selecione todas as linhas e colunas da tabela:
-- a) Pedidos

SELECT * from pedidos;

-- b) Clientes

SELECT * FROM clientes;

-- Exemplo 2. Selecione e altere o nome de colunas específicas de clientes:
 
SELECT Email as E_Mail, Qtd_Filhos as Quantidade_de_Filhos from clientes;
 
-- Exemplo 3. Selecione as 5 primeiras linhas da tabela produtos
 
 select * from produtos limit 5;
 
-- Exemplo 4. Mostre a tabela produtos, ordenando pala coluna Preco_Unit

select * from produtos order by Preco_Unit desc;

 -- Criando Filtros --

 -- Exemplo 5. Mostre produtos com preços iguais ou maiores que R$1800,00
 
 select * from produtos;
 select Nome_Produto, Marca_Produto, Preco_Unit from Produtos where Preco_Unit >= 1800;
 
 -- Exemplo 6. Mostre os produtos com preços iguais a R$3100,00
 
 select * from produtos where Preco_Unit = 3100;
 
 -- Exemplo 7. Mostre produtos da marca DELL
 
select * from produtos where Marca_Produto = 'Dell';

-- Exemplo 8. Mostre apenas pedidos feitos no dia 03/01/2019

select * from pedidos;
select * from pedidos where Data_Venda = '2019-01-03';

-- Exemplo 9. Mostre apenas os clientes solteiros e do sexo masculino.

select * from clientes;
select Nome, Sobrenome, Email, Telefone from clientes where Estado_Civil = 'S' and Sexo = 'M';

-- Exemplo 10.Mostre produtos da marca Dell ou Samsung

select * from produtos;
select Nome_Produto, Marca_Produto, Preco_Unit from produtos where Marca_Produto = 'DELL' or Marca_Produto = 'SAMSUNG';

-- SUM, AVG, MIN, MAX --

-- Exemplo 11. Se você vender uma unidade de cada produto, quanto você ganhará?
select * from produtos;
select sum(Preco_Unit) from produtos;

-- Exemplo 12. Qual o custo médio dos produtos?

select avg(Custo_Unit) from produtos;

-- Exemplo 13. Qual é o seu cliente com a menor e maior renda anual? Mostre quem são

select * from clientes;
select min(Renda_Anual), max(Renda_Anual) from clientes;
select Nome,
 Sobrenome,
 Renda_Anual
 from clientes 
 where Renda_Anual = 10000 or Renda_Anual = 170000;

-- GROUP BY -- 

-- Exemplo 14. Quais são as quantidades de filhos dos clientes?
select * from clientes;
select Qtd_Filhos from clientes group by Qtd_Filhos;


-- Exemplo 15. Total de clientes por sexo?

select * from clientes;
select Sexo, count(*) from clientes group by Sexo;

-- Exemplo 16. Total de produtos por marca?

select * from produtos;
select Marca_Produto, count(*) from produtos group by Marca_Produto;

-- Exemplo 17. Receita total e custo total por ID_Loja da tabela pedidos?

select * from pedidos;
select ID_Loja from pedidos group by ID_Loja;
select ID_Loja, sum(Receita_Venda), sum(Custo_Venda) from pedidos group by ID_Loja;

-- Exemplo 18. Lucro por loja?
select ID_Loja, sum(Receita_Venda)-sum(Custo_Venda) as 'Lucro' from pedidos group by ID_Loja;

-- Exemplo 19. Quantidade de ítens por marca
select * from produtos;
select Marca_Produto, count(*) from produtos group by Marca_Produto;


-- Exemplo 20. Relacione duas tabelas, produtos e lojas, elas têm em comum ID_Loja
select * from pedidos;
select * FROM lojas;

select pedidos.*,lojas.Loja, lojas.Gerente,lojas.Telefone from pedidos inner join Lojas;

select pedidos.*,lojas.Loja, lojas.Gerente,lojas.Telefone from pedidos inner join Lojas on pedidos.ID_Loja = lojas.ID_Loja;
