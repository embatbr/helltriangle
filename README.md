# Hell Triangle

Implementação do desafio Hell Triangle, descrito no documento HellTriangle-Challenge.pdf.


## Considerações

- A entrada é composta apenas por inteiros, embora uma adaptação com decimais possa rodar se feita corretamente. Contudo, este caso foi deixado de lado por não parecer necessário.


## Chamada

O módulo é chamado através do terminal, no formato `python3.4 helltriangle.py <num_lines> <lim_min> <lim_max>`, onde

- `num_lines` é o número de linhas do triângulo.
- `lim_min` é o menor valor possível em uma posição.
- `lim_max` é o maior valor possível em uma posição.

A regra para uma entrada válida é `num_lines > 0` e `lim_min < lim_max`.


## Solução

A linguagem utilizada é Python 3.4, devido à minha familiaridade e preferência pessoal.

A implementação foi feita de modo simples. Inicialmente pensei em utilizar arrays de NumPy, contudo concluí que seria uma solução "utilizar uma bazuca para matar uma mosca".

Existem 2 funções auxiliares. A primeira, `create_example`, cria um triângulo exemplo dado o número de linhas (altura) e os limites para os valores (tipo `int`). Caso a regra descrita na seção anterior seja desobedecida, uma exception (InvalidNumLinesError ou InvalidLimitsError, dependendo da violação) é lançada. A segunda função é `print_result`, utilizada apenas para exibir o resultado de forma amigável.

A função principal é `maximum_total`, que recebe o maldito triângulo (variável `example`), sua altura (`num_lines`) e o caminho e resultado iniciais. A função executa uma varredura em profundidade (não é possível, do ponto de vista do algoritmo, antecipar os valores futuros). O triângulo é tratado como uma matriz com valores acima da diagonal principal desconsiderados. Embora seja visto como uma matriz, não é modelado (em termo de estrutura de dados) como uma. Apenas é utilizada uma lista de listas de inteiros. Para cada linha `i`, o valor `j` pode ser `j_prev` ou `j_prev + 1` (indica a coluna à direita daquela indicada por `j_prev`). Isso evita que a busca seja "aberta" demais, algo consideravelmente custoso para triângulos muito altos. Em caso de empate, a regra é "descer tem prioridade sobre descer e pegar a direita" (`j_prev` > `j_prev + 1`).


## Testes

TODO amanhã