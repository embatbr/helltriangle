# Hell Triangle

Implementação do desafio Hell Triangle, descrito no documento HellTriangle-Challenge.pdf.


## Considerações

- A entrada é composta apenas por inteiros, embora uma adaptação com decimais possa rodar se feita corretamente. Contudo, este caso foi deixado de lado por não parecer necessário.


## Solução

A solução está implementada no módulo `helltriangle`, dentro do diretório `src`.

### Chamada

O módulo é chamado através do terminal, no formato `python3.4 helltriangle.py <num_lines> <lim_min> <lim_max>` ou `./helltriangle.py <num_lines> <lim_min> <lim_max>`, a partir do diretório `src`, onde

- `num_lines` é o número de linhas do triângulo.
- `lim_min` é o menor valor possível em uma posição.
- `lim_max` é o maior valor possível em uma posição.

A regra para uma entrada válida é `num_lines > 0` e `lim_min < lim_max`. Os limites aceitam números negativos.

### Implementação

A linguagem utilizada é Python 3.4, devido à minha familiaridade e preferência pessoal, além de ser conhecidamente simples de utilizar (sem burocracia).

A implementação foi feita de modo simples. Inicialmente pensei em utilizar arrays de NumPy, contudo concluí que seria desnecessário, por incluir complexidade demais em um projeto tão pequeno. Obviamente, para valores muito altos de `num_lines` (e.g., `num_lines > 20`), o tempo pode ser alto para a preferência do usuário.

Existem 2 funções auxiliares acessáveis. A primeira, `create_example`, cria um triângulo exemplo dado o número de linhas (altura) e os limites para os valores (do tipo `int`) com valores aleatórios. Caso a regra descrita na seção anterior seja desobedecida, uma exception (InvalidNumLinesError ou InvalidLimitsError, dependendo da violação) é lançada. A segunda função é `print_result`, utilizada apenas para exibir o resultado de forma amigável.

A função principal é `maximum_total`, que recebe o triângulo (variável `example`) e o caminho e resultado iniciais (respectivamente (0, 0) e None). A função executa uma varredura em profundidade (não é possível, do ponto de vista do algoritmo, antecipar os valores futuros, logo todo o triângulo deve ser varrido). O triângulo é tratado como uma matriz com valores acima da diagonal principal desconsiderados, embora não seja modelado como uma. Apenas é utilizada uma lista de listas de inteiros. Para cada linha `i`, o valor `j` pode ser `j_prev` ou `j_prev + 1` (indica a coluna abaixo e à direita daquela indicada por `j_prev`). Isso evita que a busca seja "aberta" demais, algo consideravelmente custoso para triângulos muito altos. Em caso de empate, a regra é "descer tem prioridade sobre descer e pegar a direita" (`j_prev` over `j_prev + 1`).

`maximum_total` internamente chama __maximum_total_aux, uma "função privada" (até onde Python allows), que executa toda a recursão (ver código).


## Testes

Os testes foram feitos num módulo separado, chamado `tests`, também no diretório `src`.

### Chamada

A chamada é executada utilizando apenas o comando `python3.4 tests.py` ou `./tests.py`.

### Implementação

Uma subclasse de `unittest.TestCase`, chamada `HellTriangleTests`, contém diversos métodos de testes, cobrindo as possibilidades de erro e os casos de sucesso. O método `setUp` é utilizado para setar o valores default de altura do triângulo, limites e exemplo default (aquele utilizao na explicação) antes de cada teste. Não há necessidade de um método `tearDown`.

Os testes são:

- `test_should_not_create_an_example_with_zero_lines`, que espera uma exception `InvalidNumLinesError` com mensagem 'The triangle must have at least 1 line.'.
- `test_should_not_create_an_example_with_negative_lines`, que espera uma exception `InvalidNumLinesError` com mensagem 'Negative number of lines? Really? Try again.'.
- `test_should_not_create_an_example_with_equal_limit_ends`, que espera uma exception `InvalidLimitsError` com mensagem 'No variability of values.'.
- `test_should_not_create_an_example_with_limit_ends_swapped`, que espera uma exception `InvalidLimitsError` com mensagem 'How can you have an interval starting from a point higher than the end? Try again.'.
- `test_should_create_a_valid_example` que verifica se o triângulo possui o número de linhas corretas, o número de elementos por linha correto (1 na primeira, 2 na segunda e assim por diante) e se, a cada linha, os valores estão dentro do limite proposto.
- `test_should_not_calculate_the_maximum_total_for_an_empty_example`, verifica se a entrada (chamada `example`) é uma lista vazia.
- `test_should_return_a_correct_path_and_maximum_total_for_a_valid_example` que roda a função principal, `maximum_total`, utilizando o exemplo padrão do pdf. São testados se o caminho escolhido é o correto e se o resultado final é o *maximum total*.