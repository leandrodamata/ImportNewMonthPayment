*Todos os dados deste projeto são fictícios*

Este projeto toma como base a seguinte situação:

Sendo responsável pela análise de uma empresa, o RH envia todo mês uma planilha no Excel com uma relação de salários dos funcionários,
Contendo essas informaçõe todo mês, se formou uma base de dados de alguns meses

Ao receber essa planilha mensalmente, o processo normal, seria ir na planilha nova, copiar a linha com o nome da pessoa,
procurar o nome dessa pessoa na base de dados existente, e inserir a informação do novo mês colando ela logo abaixo do último mês

Portanto, pensando em otimizar o processo de inserir esses dados em todo mês, visto que eventualmente essa base de dados pode
se tornar bem grande, e isso geraria um trabalho gigante com o passar do tempo, criei um projeto em Python, utilizando Pandas, 
onde carrego a planilha de base de dados, e em seguida a planilha nova, verificamos se o nome já existe na planilha de base de dados,
se ele existe, inserimos a informação abaixo da última vez que o nome aparece, se ele não existe, inserimos a informação no final da lista.
No final, salvamos essa junção de informações em uma nova planilha, uma base de dados atualizada, e fazemos um leve tratamento de dados para
a data ficar no formato de data abreviada na nova planilha do Excel, e também ordenamos o DataFrame pela coluna 'Nome Empregado' e 'Data'
para manter a ordem correta, mantendo sempre o mês mais antigo por último.

Este foi meu primeiro projeto utilizando Pandas para tratamento de dados, e eu achei bem divertido e tranquilo de utilizar a biblioteca
Para o futuro pretendo realizar uma análise visual desses dados utilizando o Power BI
