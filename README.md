# biomass


Para calcular a biomassa, primeiro precisamos do diâmetro da planta. Contudo uma planta pode ter mais de um diâmetro, ou seja, vários perfilhos. 
Poderiamos somar o perímetro de cada perfilho, mas estaríamos somando também os espaços vazios e portanto superestimando a biomassa. Dessa forma, o 
procedimento padrão é primeiro calcular a área de casa perímetro, somar as áreas e calcular o diâmetro da área total. veja:

# calcular a área apartir do perímetro:
# A = (C/π)² * π/4 
# A = área; C = perímetro

# calcular o diâmetro apartir da área total:
# d = √(4*At)/π
# d = diâmetro, At = área total (a1 + a2 + an)

Aqui oferecemos duas funções: Uma para calcular o diâmetro apartir de cada perfilho e uma para calcular a biomassa usando altura e diâmetro. 
Usamos a equação proposta por Sampaio e Silva (2015). 

# Função 1: calc_perfilhos_diam
# parâmetros: table= objeto, tabela de campo, circ: string, nome da coluna que contém as circunferências.
# retorno: retorna a mesma tabela, com os dados de circunferências transformados em diâmetro.
# obs: quando a planta tiver mais de um perfilho, anotar ambos separados por sinal de + (ex: 16+10)

# Função 2: compute_biomass
# parâmetros: table= objeto, tabela de campo, d= string, nome da coluna que contém o diâmetro, h= string, nome da coluna que contém a altura
# col_name= string, nome da coluna a ser criada para salvar a biomassa 
# retorno: retorna a mesma tabela com uma coluna a mais com a biomassa calculada usando as equações de Sampaio e Silva (2015)



