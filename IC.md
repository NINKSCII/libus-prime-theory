# A Evidência do IC — A Página 57 e a Hipótese de Transposição

## Análise do Índice de Coincidência aplicada à Página 57 do *Liber Primus*

**Projeto:** Libus Prime Theory
**Autor:** Nink
**Motor:** Libus Prime Analysis Engine
**Página analisada:** Página 57 do *Liber Primus*

---

# 1. Objetivo

Este documento apresenta uma nova etapa da investigação da **Libus Prime Theory** utilizando o **Índice de Coincidência (IC)**.

O objetivo é determinar se a estrutura matemática observada anteriormente na Página 57 atua principalmente sobre:

* os **valores das runas**;
* ou a **posição das runas**.

Essa distinção é fundamental.

Uma cifra de **substituição** altera os símbolos.

Uma cifra de **transposição** mantém os símbolos, mas altera sua ordem.

Portanto, o IC fornece uma ferramenta importante para investigar se a estrutura encontrada anteriormente está modificando os valores das runas ou preservando-os enquanto altera sua organização.

---

# 2. Relação com a Libus Prime Theory

A análise anterior identificou relações envolvendo:

* Gematria Primus;
* módulo 29;
* Fibonacci;
* período de Pisano;
* organização em matrizes;
* MDC entre posições vizinhas;
* e possíveis invariantes geométricos.

A nova pergunta é:

> Essas estruturas matemáticas estão sendo utilizadas para transformar os valores das runas ou para determinar como elas devem ser posicionadas?

O experimento de IC foi desenvolvido para investigar exatamente essa questão.

---

# 3. Índice de Coincidência

O Índice de Coincidência mede a concentração estatística de símbolos dentro de uma sequência.

Como referência aproximada:

```text
Inglês natural:              IC ≈ 0,066
Cifras polialfabéticas:      IC ≈ 0,040–0,050
```

Esses valores são referências estatísticas e não constituem, isoladamente, uma prova do método de cifragem.

O ponto fundamental para este experimento é outro:

> **Uma transposição altera a ordem dos símbolos, mas preserva a quantidade de cada símbolo. Portanto, o IC global deve permanecer essencialmente inalterado.**

Já uma transformação que modifica os valores das runas pode alterar a distribuição de frequências e, consequentemente, o IC.

---

# 4. O Experimento

O motor recebeu um trecho real da Página 57 e calculou inicialmente o IC da sequência original.

Em seguida, foram aplicadas cinco transformações baseadas nas estruturas investigadas pela Libus Prime Theory.

Foram testados:

1. Deslocamento linear baseado em Fibonacci módulo 29;
2. Deslocamento por linha em uma matriz 14×14;
3. Deslocamento por coluna em uma matriz 14×14;
4. Deslocamento baseado em linha + coluna;
5. Deslocamento não-linear baseado em MDC entre posição e valor.

O objetivo não era simplesmente encontrar o maior IC.

A pergunta principal era:

> **Quais transformações preservam a estrutura estatística original e quais a destroem?**

---

# 5. Resultado do Motor

O terminal produziu:

```text
============================================================
 MOTOR DE TRANSFORMAÇÃO LIBUS PRIME - TESTE DE IC
============================================================

IC Original (Cifrado): 0.0670

------------------------------------------------------------

TESTE 1: Deslocamento Linear (Fibonacci mod 29)

IC Obtido: 0.0374


TESTE 2: Deslocamento por Linha da Matriz 14x14

IC Obtido: 0.0358


TESTE 3: Deslocamento por Coluna da Matriz 14x14

IC Obtido: 0.0367


TESTE 4: Deslocamento por (Linha + Coluna) Matriz 14x14

IC Obtido: 0.0344


TESTE 5: Deslocamento Não-Linear (MDC Posição x Valor)

IC Obtido: 0.0614


============================================================
```

---

# 6. Resultado 1 — O IC Original

O trecho original apresentou:

```text
IC = 0.0670
```

Esse valor está muito próximo da faixa esperada para texto em inglês natural.

Isso é importante porque mostra que a sequência original possui uma concentração estatística muito diferente daquela produzida pelos quatro primeiros modelos testados.

Entretanto, o ponto mais importante é que:

**o IC original não foi destruído antes de qualquer transformação.**

Isso é compatível com a possibilidade de que os valores das runas estejam preservados e que a criptografia esteja atuando principalmente sobre sua organização.

---

# 7. Resultado 2 — Os Testes 1 a 4

Os quatro primeiros modelos produziram:

| Teste    | Transformação          |         IC |
| -------- | ---------------------- | ---------: |
| 1        | Fibonacci mod 29       | **0,0374** |
| 2        | Linha da matriz 14×14  | **0,0358** |
| 3        | Coluna da matriz 14×14 | **0,0367** |
| 4        | Linha + coluna         | **0,0344** |
| Original | Sequência original     | **0,0670** |

A diferença é significativa dentro desta experiência:

```text
Original:  0.0670
Teste 1:   0.0374
Teste 2:   0.0358
Teste 3:   0.0367
Teste 4:   0.0344
```

Os quatro modelos, quando utilizados como **deslocamentos de valor**, reduziram fortemente o IC.

Isso indica que essas operações, na forma em que foram implementadas, estão alterando a distribuição estatística dos símbolos.

Portanto, elas não se comportam como uma simples transposição.

---

# 8. O Ponto Central da Descoberta

Aqui está a parte mais importante do experimento.

Se a estrutura matemática do *Liber Primus* estivesse simplesmente substituindo os valores das runas por outros valores, seria esperado que operações desse tipo alterassem significativamente a distribuição estatística.

Foi exatamente isso que ocorreu nos Testes 1–4.

Por outro lado, uma transposição verdadeira não precisa modificar os valores.

Ela pode ser representada conceitualmente assim:

```text
ANTES:

A B C D E F G

DEPOIS:

D F A G C B E
```

Os símbolos continuam sendo os mesmos.

Somente suas posições foram alteradas.

Consequentemente:

```text
Frequência dos símbolos → preservada
IC global                → preservado
Ordem dos símbolos       → alterada
```

Esse comportamento é compatível com a direção que a investigação começou a apontar.

---

# 9. Resultado 3 — O Teste Não-Linear do MDC

O quinto teste apresentou:

```text
IC = 0.0614
```

Esse resultado é muito diferente dos quatro anteriores.

Comparação:

```text
Original:                  0.0670

MDC Posição × Valor:       0.0614

Fibonacci mod 29:          0.0374
Linha 14×14:               0.0358
Coluna 14×14:              0.0367
Linha + Coluna:            0.0344
```

O resultado de **0,0614** permanece muito mais próximo do IC original do que os resultados dos quatro deslocamentos de valor.

Isso indica que a transformação baseada em MDC está preservando uma parcela muito maior da estrutura estatística original.

Esse comportamento é compatível com a hipótese de que o MDC esteja relacionado à **organização estrutural ou posicional** das runas, em vez de simplesmente substituir seus valores.

---

# 10. O Que o Teste de IC Permite Concluir

O experimento fornece três observações importantes.

### Observação 1 — O texto original possui IC elevado

```text
IC = 0.0670
```

A sequência possui uma estrutura estatística compatível com linguagem natural.

### Observação 2 — Transformações aditivas destroem essa estrutura

Os Testes 1–4 produziram ICs entre:

```text
0.0344 e 0.0374
```

Isso mostra que, quando as estruturas de Fibonacci e das matrizes são utilizadas como operações de alteração de valor, a distribuição estatística é fortemente modificada.

### Observação 3 — A transformação baseada em MDC preserva muito mais da estrutura

O Teste 5 produziu:

```text
IC = 0.0614
```

Esse resultado é próximo do IC original de:

```text
0.0670
```

Portanto, entre os cinco modelos testados, o modelo baseado em MDC foi o que mais preservou a estrutura estatística original.

---

# 11. A Nova Hipótese

Os resultados modificam a interpretação da teoria.

A hipótese inicial investigava se:

```text
Fibonacci
+
Módulo 29
+
Matriz
+
MDC
```

poderiam estar sendo utilizados para transformar diretamente os valores das runas.

Os resultados do teste de IC sugerem uma possibilidade diferente:

```text
Valores das runas
        ↓
     preservados
        ↓
Estrutura matemática
        ↓
determina posições
        ↓
reorganização espacial
        ↓
sequência original
```

Ou seja:

> **A matemática pode estar funcionando como uma regra de roteamento das runas, e não necessariamente como uma cifra de substituição dos valores.**

Essa é a principal mudança conceitual produzida pelo experimento.

---

# 12. Relação com as Descobertas Anteriores

Essa hipótese também conecta diretamente os resultados deste experimento com a análise anterior da Libus Prime Theory.

Anteriormente foram encontrados:

```text
Módulo 29
      ↓
Fibonacci
      ↓
Período de Pisano = 14
      ↓
Matrizes
      ↓
MDC
      ↓
Invariantes
```

Agora, o teste de IC adiciona uma nova possibilidade:

```text
Módulo 29
      ↓
Fibonacci
      ↓
Geometria
      ↓
MDC
      ↓
ROTA / POSIÇÃO
      ↓
REORDENAÇÃO DAS RUNAS
```

Nesse modelo, Fibonacci e MDC não seriam necessariamente o conteúdo da cifra.

Eles poderiam ser parte da **regra que determina onde cada runa deve ser colocada ou de onde deve ser retirada**.

---

# 13. Por Que a Matriz 14×14 Continua Importante

A análise anterior encontrou uma relação entre:

```text
29 → Fibonacci → período de Pisano → 14
```

e também observou estruturas de MDC nas matrizes testadas.

A nova análise torna a dimensão 14×14 ainda mais interessante como objeto de investigação.

Isso não significa que a matriz 14×14 esteja definitivamente comprovada como a estrutura utilizada pelo *Liber Primus*.

Significa que ela possui uma justificativa matemática concreta dentro da teoria e deve ser testada como uma possível malha de roteamento.

---

# 14. Novo Modelo da Libus Prime Theory

A teoria pode agora ser representada em duas etapas.

## Camada 1 — Estrutura matemática

```text
Gematria Primus
      ↓
Módulo 29
      ↓
Fibonacci
      ↓
Período de Pisano
      ↓
Geometria / Matriz
      ↓
MDC
```

## Camada 2 — Roteamento

```text
MDC + posição + Fibonacci
            ↓
      regra de roteamento
            ↓
     nova posição da runa
            ↓
       reorganização
            ↓
       texto original
```

A investigação passa, portanto, de uma tentativa de descobrir uma simples transformação de valores para uma tentativa de descobrir uma **função de permutação das posições**.

---

# 15. Veredito Experimental

O teste de IC não demonstra sozinho qual é a cifra utilizada na Página 57.

Entretanto, ele produz uma evidência importante:

> **Os modelos que alteram diretamente os valores das runas reduzem drasticamente o IC, enquanto o modelo baseado em MDC preserva muito mais da estrutura estatística original.**

O resultado:

```text
IC original:       0.0670
IC do modelo MDC:  0.0614
```

é particularmente relevante para a investigação.

Isso fortalece a hipótese de que a estrutura matemática descoberta pela **Libus Prime Theory** possa estar relacionada à **posição e à organização das runas**, e não simplesmente à substituição de seus valores.

A hipótese de trabalho passa então a ser:

> **A Página 57 pode utilizar uma transformação de transposição ou uma permutação posicional na qual as runas preservam seus valores, enquanto uma estrutura matemática determina sua organização espacial.**

---

# 16. Próxima Etapa — Engenharia Reversa da Permutação

A partir deste resultado, a próxima etapa deixa de ser procurar apenas uma transformação numérica.

O objetivo passa a ser descobrir uma possível **permutação das posições**.

O próximo motor deverá testar:

### 1. Construção da matriz 14×14

Distribuir as runas na malha seguindo diferentes convenções de preenchimento.

### 2. Rotas de Fibonacci

Testar sequências de posições derivadas de Fibonacci módulo 29.

### 3. Invariantes de MDC

Utilizar os MDCs encontrados anteriormente para determinar possíveis conexões entre posições.

### 4. Permutações

Gerar mapas:

```text
posição original → nova posição
```

e também:

```text
nova posição → posição original
```

### 5. Teste de reconstrução

Depois de aplicar cada possível rota, calcular novamente:

* IC;
* frequência dos símbolos;
* distribuição de n-gramas;
* coerência linguística;
* e consistência entre diferentes trechos.

### 6. Teste de embaralhamento

Comparar a rota encontrada contra versões aleatoriamente embaralhadas.

O objetivo é verificar se a mesma estrutura matemática produz resultados significativamente diferentes quando a ordem original é destruída.

---

# 17. Estado Atual da Investigação

A Libus Prime Theory possui agora duas linhas experimentais complementares:

```text
ANÁLISE ESTRUTURAL
       ↓
Módulo 29
Fibonacci
Matrizes
MDC
       ↓
Identificação de invariantes


ANÁLISE ESTATÍSTICA
       ↓
Índice de Coincidência
       ↓
Teste de transformações
       ↓
Preservação / alteração da estrutura
```

As duas linhas apontam para a mesma pergunta:

> **A matemática encontrada no *Liber Primus* está transformando os valores das runas ou determinando a posição delas?**

Os resultados atuais favorecem a investigação da segunda possibilidade.

A próxima fase é descobrir a **regra exata de permutação**.

---

## Libus Prime Theory

**Nink**

> **Gematria → Módulo 29 → Fibonacci → Geometria → MDC → Posição → Permutação**
>
> A investigação agora busca reconstruir a rota matemática que pode estar organizando as runas do *Liber Primus*.
