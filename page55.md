# Libus Prime Theory

## Validação Matemática e Análise Estrutural do *Liber Primus* (Cicada 3301)

**Autor:** Nink
**Projeto:** Libus Prime Theory
**Motor:** Libus Prime Analysis Engine v2
**Linguagem:** Python

---

## 1. Objetivo

A **Libus Prime Theory** propõe que o *Liber Primus* possa conter uma estrutura matemática interna relacionada à **posição das runas**, aos valores da **Gematria Primus**, ao **módulo 29**, à sequência de **Fibonacci** e à organização geométrica dos valores dentro da página.

Neste experimento, o **Libus Prime Analysis Engine v2** foi aplicado exclusivamente às **runas originais da Página 55**, com o objetivo de investigar duas camadas fundamentais da teoria:

* **Camada Posicional:** investigação de relações algébricas entre runas consecutivas, incluindo a função
  **`f(x,y) = (X·x + Y·y) mod 29`**
  e transições relacionadas a Fibonacci módulo 29.

* **Camada Geométrica:** organização dos valores das runas em uma matriz de **14 colunas** e análise dos **MDCs entre posições horizontalmente adjacentes**.

O objetivo desta etapa **não é declarar a cifra resolvida**, mas identificar padrões matemáticos que possam indicar uma estrutura interna e orientar os próximos testes.

---

# 2. Dados Analisados

O experimento utiliza exclusivamente a transcrição das runas da **Página 55**.

### Dados de entrada

* **Página analisada:** 55
* **Runas extraídas:** 76
* **Transições consecutivas analisadas:** 74
* **Módulo utilizado:** 29
* **Coeficientes testados:** `X,Y ∈ {0,...,28}`
* **Total de combinações testadas:** 29 × 29 = **841**

Os valores numéricos das runas foram obtidos através da **Gematria Primus** utilizada pelo motor.

---

# 3. Camada Posicional — Busca por Função Algébrica

A primeira camada investiga a possibilidade de que a próxima runa não dependa apenas de uma substituição estática, mas também dos valores das runas que a precedem.

Foi testada a hipótese:

**`z = (X·x + Y·y) mod 29`**

onde:

* `x` = valor da runa anterior;
* `y` = valor da runa atual;
* `z` = valor previsto para a próxima posição;
* `X` e `Y` = coeficientes desconhecidos.

O motor realizou uma busca exaustiva pelas **841 combinações possíveis** de `X` e `Y`.

## Resultado

A combinação que apresentou o maior número de correspondências foi:

**`X = 15`**
**`Y = 27`**

Correspondendo, pela Gematria Primus utilizada no experimento, a:

* `15` → ᛋ
* `27` → ᛡ

A função encontrada foi:

**`f(x,y) = (15x + 27y) mod 29`**

### Correspondências observadas

A função apresentou:

**10 correspondências em 74 transições**

ou:

**13,51% de correspondência.**

---

# 4. Comparação com a Linha de Base

Em um modelo em que cada uma das **29 possibilidades** tivesse a mesma probabilidade de aparecer na posição seguinte, a probabilidade de uma previsão específica acertar seria:

**`1 / 29 ≈ 3,45%`**

O resultado observado para a melhor função foi:

**13,51%**

Isso corresponde a aproximadamente:

**3,92 × a taxa de uma previsão aleatória individual.**

Esse resultado é **interessante como sinal exploratório**, pois a melhor função encontrada apresentou uma taxa de correspondência superior à linha de base utilizada no teste.

### Porém, existe uma consideração importante

O motor testou **841 funções diferentes** e selecionou posteriormente aquela que apresentou o maior número de correspondências.

Portanto, o resultado de 13,51% **não pode, isoladamente, ser tratado como prova de que essa função é a regra real da página**.

O próximo passo necessário é verificar se o mesmo padrão:

1. aparece em outras páginas;
2. permanece significativo quando comparado com páginas aleatorizadas;
3. continua funcionando fora dos dados utilizados para encontrar os coeficientes;
4. produz uma sequência coerente quando utilizado de forma reversa.

Essa etapa é fundamental para distinguir uma **estrutura real** de uma coincidência estatística produzida pela busca entre muitas hipóteses.

---

# 5. Camada Geométrica — Estrutura por MDC

A segunda camada investiga a possibilidade de que a **posição espacial das runas** contenha informação adicional.

Os valores da Página 55 foram organizados em uma matriz com:

**14 colunas**

A escolha de 14 está relacionada à hipótese da teoria envolvendo o **Período de Pisano de Fibonacci módulo 29**.

Com 76 valores, a organização produz uma estrutura:

**6 × 14**

com posições vazias no final da matriz.

O motor então calculou o **MDC (Máximo Divisor Comum)** entre valores horizontalmente adjacentes.

O objetivo é verificar se determinados valores de MDC aparecem com frequência suficiente para sugerir um possível invariante estrutural.

### Resultado observado

Na saída analisada, os valores mais frequentes incluíram:

| MDC | Ocorrências |
| --: | ----------: |
|   1 |          42 |
|   2 |          13 |
|   3 |           6 |

O resultado mostra uma presença significativa de pares **coprimos (MDC = 1)**.

A densidade calculada pelo motor para `MDC = 1` foi:

**60,00%**

Esse valor deve ser tratado como uma **observação estrutural**, e não como evidência independente de uma cifra.

A comparação com uma distribuição teórica de números aleatórios pode ser utilizada posteriormente para verificar se essa densidade é realmente anômala.

---

# 6. Modelo Atual da Libus Prime Theory

A teoria atualmente pode ser representada por duas possíveis camadas complementares:

```text
                    LIBUS PRIME THEORY
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
      CAMADA POSICIONAL          CAMADA GEOMÉTRICA
              │                         │
              ▼                         ▼
     Relações entre runas       Organização espacial
        consecutivas                 da página
              │                         │
              ▼                         ▼
     f(x,y) = (Xx + Yy) mod 29       Matriz 6×14
              │                         │
              ▼                         ▼
        X = 15, Y = 27            Análise de MDC
              │                         │
              ▼                         ▼
       10 / 74 = 13,51%             MDC = 1
              │                         │
              └────────────┬────────────┘
                           │
                           ▼
                HIPÓTESE DE ESTRUTURA
                  MATEMÁTICA INTERNA
```

A hipótese central é que o mecanismo do *Liber Primus* possa não depender exclusivamente de uma **chave estática**, mas possivelmente de uma **regra dinâmica de transformação** na qual a posição e os valores das runas participem do processo.

A função encontrada:

**`(15x + 27y) mod 29`**

é, neste momento, uma **candidata experimental** dentro dessa hipótese.

---

# 7. O Que o Experimento Demonstra

Os resultados permitem estabelecer algumas observações concretas:

### Confirmado pelo experimento

* A Página 55 possui **76 runas** na entrada analisada.
* Foram testadas **841 combinações** de coeficientes.
* A combinação `X=15, Y=27` apresentou o maior número de correspondências dentro do conjunto testado.
* Essa combinação produziu **10 acertos em 74 transições (13,51%)**.
* A taxa observada é superior à linha de base simples de `1/29 ≈ 3,45%`.
* A organização em 14 colunas permite investigar uma possível estrutura geométrica relacionada ao módulo 29.

### Ainda não demonstrado

O experimento **não demonstra, sozinho**, que:

* `X=15, Y=27` sejam os coeficientes verdadeiros;
* a função seja utilizada pelo autor do *Liber Primus*;
* a página utilize uma função não-linear real;
* a cifra tenha sido quebrada;
* Vigenère tenha sido definitivamente descartada;
* a função produza o plaintext correto.

Essas questões exigem testes adicionais.

---

# 8. Próxima Etapa — Engenharia Reversa da Função

O próximo passo da pesquisa será testar a hipótese de inversão da função encontrada.

Partindo de:

**`z = (15x + 27y) mod 29`**

será investigada a possibilidade de recuperar uma das variáveis a partir das demais.

Por exemplo, se:

**`z`** = valor observado da próxima runa
**`x`** = valor da runa anterior
**`y`** = valor desconhecido

poderemos investigar:

**`y = (z - 15x) · 27⁻¹ mod 29`**

desde que o inverso modular de `27` exista módulo 29.

A sequência recuperada será então comparada com possíveis estruturas linguísticas e estatísticas.

---

# 9. Testes de Validação Necessários

Para determinar se o padrão encontrado representa uma propriedade real do *Liber Primus*, a próxima versão do motor deverá executar testes adicionais:

### 1. Teste em outras páginas

Aplicar a mesma análise a outras páginas do *Liber Primus* e verificar se os mesmos coeficientes ou relações reaparecem.

### 2. Teste de embaralhamento

Randomizar a ordem das runas da Página 55 e repetir o experimento.

Se o padrão desaparecer após o embaralhamento, isso poderá fornecer evidência de que a **ordem das runas** possui importância.

### 3. Teste de permutação

Gerar diversas permutações aleatórias da página e comparar a melhor pontuação obtida com a pontuação original.

### 4. Validação fora da amostra

Encontrar os coeficientes em uma parte da sequência e testá-los em outra parte que não participou da busca.

### 5. Análise da inversão

Aplicar a função inversa e verificar se a sequência resultante apresenta características linguísticas significativamente diferentes das sequências aleatórias.

### 6. Comparação entre páginas

Verificar se `X=15, Y=27` é específico da Página 55 ou se aparece de maneira consistente em outras páginas.

---

# 9.5 Conclusão

O experimento realizado pelo **Libus Prime Analysis Engine v2** encontrou uma relação algébrica candidata na Página 55:

**`f(x,y) = (15x + 27y) mod 29`**

Essa função apresentou **10 correspondências em 74 transições (13,51%)**, enquanto uma previsão específica sob uma linha de base uniforme de 29 possibilidades teria probabilidade de **aproximadamente 3,45%** de acertar uma transição.

O resultado é **significativo como ponto de investigação**, mas ainda não constitui uma prova de que a função faça parte do mecanismo criptográfico original.

A partir deste ponto, a pesquisa deixa de buscar apenas padrões isolados e passa a investigar uma questão mais específica:

> **A relação encontrada permanece quando submetida a testes independentes, páginas diferentes, embaralhamento, validação fora da amostra e inversão matemática?**

Se a resposta for positiva e o mecanismo produzir uma estrutura linguística coerente, a hipótese de uma transformação posicional dinâmica ganhará suporte experimental muito mais forte.

---

## Libus Prime Theory

**Nink — Libus Prime Analysis Engine v2**

*Investigando a possível estrutura matemática interna do Liber Primus através de análise posicional, funções algébricas, módulo 29, Fibonacci, geometria e teoria dos números.*

# 10. Engenharia Reversa Cega — Primeiros Testes de Descriptografia

Após a identificação da função candidata

**`f(x,y) = (15x + 27y) mod 29`**

na análise estrutural da Página 55, o projeto avançou para uma nova etapa: a **Engenharia Reversa Cega**.

Nesta etapa, o objetivo deixou de ser apenas identificar correlações entre as runas e passou a ser testar se essas relações poderiam ser utilizadas para **reconstruir o texto original da página**.

A hipótese central continua sendo a existência de uma transformação dinâmica baseada nos valores das runas e no módulo 29, possivelmente combinada com uma sequência recorrente como Fibonacci.

---

# 11. A Engrenagem de Transições

Antes de tentar descriptografar diretamente a página, o motor analisou as transições entre os valores consecutivos da Gematria Primus.

Para duas runas consecutivas `a` e `b`, foi considerada a diferença modular:

**`d = (b - a) mod 29`**

A sequência inicial de transições observada na Página 55 foi:

**`[4, 23, 20, 26, 8, 2, 26, 5, 25, 26, 23, 17, 8, 23, 4, 27, 26, 22, 17, 25, 6, 26, ...]`**

Essa análise revelou uma característica relevante: determinados valores de transição aparecem repetidamente, incluindo o valor **26** em posições relativamente próximas.

Esse comportamento motivou a hipótese de que as diferenças entre runas poderiam não ser apenas ruído estatístico, mas representar parte de uma **regra de transformação interna**.

É importante, entretanto, distinguir a observação da interpretação:

> A repetição de uma transição demonstra que determinado deslocamento ocorre várias vezes; isoladamente, ela não demonstra que exista uma "engrenagem" criptográfica.

Por isso, a análise das transições foi utilizada como **ponto de partida para os testes seguintes**, e não como prova independente do mecanismo.

---

# 12. Motor de Descriptografia Dinâmica

Com a hipótese de uma estrutura dinâmica estabelecida, o motor passou a testar diferentes formas de aplicação de uma sequência recorrente sobre os valores da página.

Uma das hipóteses utilizadas foi a de uma sequência de **Fibonacci módulo 29**, combinada com os coeficientes encontrados anteriormente.

Foram testados quatro modelos principais:

| Teste       | Transformação                     | Language Score |
| ----------- | --------------------------------- | -------------: |
| **Teste 1** | Subtração direta por Fibonacci    |         **15** |
| **Teste 2** | Subtração por `15 × Fibonacci`    |         **30** |
| **Teste 4** | Combinação envolvendo `15x + 27y` |        **105** |
| **Teste 3** | Subtração por `27 × Fibonacci`    |        **135** |

O objetivo desses testes foi verificar se alguma transformação produzia uma sequência com características estatísticas mais próximas de linguagem natural.

---

# 13. O Resultado de Score 135

O maior resultado obtido nessa primeira rodada foi:

**Teste 3 — Score: 135**

enquanto a linha de referência utilizada pelo experimento foi:

**Score: 15**

Assim, o melhor resultado apresentou uma pontuação aproximadamente:

**`135 / 15 = 9×`**

maior que a linha de referência.

Esse aumento é relevante como **sinal experimental**, pois indica que a transformação associada ao coeficiente `27` produziu uma sequência considerada muito mais próxima do modelo linguístico utilizado pelo motor.

Entretanto, o score não deve ser interpretado isoladamente como uma prova de descriptografia.

Um Language Score mede apenas o quanto uma sequência se aproxima das características linguísticas esperadas pelo avaliador. Uma transformação incorreta também pode produzir pontuações elevadas por coincidência, especialmente quando várias transformações são testadas.

Portanto:

> **Score 135 é uma anomalia interessante e um candidato para investigação, não uma confirmação de plaintext.**

O fato mais importante é que o resultado permite reduzir o espaço de hipóteses e direcionar os próximos testes.

---

# 14. O Parafuso Faltante

Apesar do aumento significativo do Language Score, a sequência produzida pelo melhor teste **não apresentou texto legível**.

Isso cria uma questão central:

**Por que uma transformação produz uma pontuação linguística muito superior, mas não produz plaintext compreensível?**

Uma possibilidade é que a transformação encontrada represente apenas **uma das etapas do processo criptográfico**.

Nesse cenário, o mecanismo poderia ser representado como:

```text
RUNAS CIFRADAS
      │
      ▼
TRANSFORMAÇÃO POSICIONAL
      │
      ▼
SEQUÊNCIA INTERMEDIÁRIA
      │
      ▼
CAMADA ADICIONAL
      │
      ▼
PLAINTEXT
```

Isso introduz a hipótese de uma **camada intermediária** ainda não identificada.

---

# 15. Hipótese de uma Camada Atbash

Uma das possibilidades levantadas é a utilização de uma transformação semelhante ao **Atbash** após a aplicação da função dinâmica.

A hipótese seria:

### Etapa 1

Aplicar a transformação baseada na posição:

**`Fibonacci + coeficientes algébricos`**

### Etapa 2

Aplicar uma transformação espelhada sobre os valores resultantes.

### Etapa 3

Interpretar os valores obtidos como possíveis caracteres do plaintext.

O modelo hipotético seria:

```text
RUNA CIFRADA
      │
      ▼
FIBONACCI / MOD 29
      │
      ▼
COEFICIENTES 15 / 27
      │
      ▼
TRANSFORMAÇÃO INTERMEDIÁRIA
      │
      ▼
ATBASH / ESPELHAMENTO
      │
      ▼
POSSÍVEL PLAINTEXT
```

Essa hipótese ainda precisa ser testada experimentalmente.

O objetivo não é assumir que Atbash esteja presente, mas verificar se a aplicação dessa camada aumenta a coerência linguística de maneira **reprodutível e estatisticamente significativa**.

---

# 16. Hipótese Alternativa — Idioma do Plaintext

Outra possibilidade considerada pelo projeto é que o texto original não seja necessariamente inglês.

O *Liber Primus* apresenta referências linguísticas, filosóficas e literárias que tornam relevante testar mais de um modelo linguístico.

Por isso, além do avaliador de inglês, uma futura versão do motor poderá utilizar modelos estatísticos para:

* Inglês;
* Latim;
* Português, apenas como controle experimental;
* outros idiomas relevantes ao corpus analisado.

A hipótese do Latim é especialmente interessante porque o próprio título **Liber Primus** utiliza uma expressão latina.

Entretanto, o título por si só **não demonstra que o plaintext da Página 55 seja latino**.

A hipótese deverá ser testada comparando os scores obtidos por diferentes modelos linguísticos sobre as mesmas transformações.

---

# 17. Estado Atual da Hipótese

Após os experimentos realizados na Página 55, a Libus Prime Theory possui agora duas etapas experimentais distintas.

## Etapa A — Análise Estrutural

Foi encontrada a função candidata:

**`(15x + 27y) mod 29`**

com:

**10 correspondências em 74 transições = 13,51%**

A função apresentou o maior número de correspondências entre as 841 combinações testadas.

---

## Etapa B — Engenharia Reversa

A função e seus coeficientes foram incorporados a testes de descriptografia dinâmica.

O maior Language Score observado foi:

**135**

contra:

**15**

na linha de referência utilizada.

Isso representa aproximadamente **9× a pontuação da referência**.

Porém, o resultado ainda não produziu plaintext legível.

---

# 18. Modelo Atual da Teoria

A hipótese atual pode ser representada como:

```text
                 LIBUS PRIME THEORY
                         │
          ┌──────────────┴──────────────┐
          │                             │
          ▼                             ▼
  ANÁLISE ESTRUTURAL             ENGENHARIA REVERSA
          │                             │
          ▼                             ▼
  Gematria Primus                Fibonacci / mod 29
          │                             │
          ▼                             ▼
  Relações posicionais           Coeficientes 15 / 27
          │                             │
          ▼                             ▼
  f(x,y) = (15x + 27y) mod 29   Testes de transformação
          │                             │
          └──────────────┬──────────────┘
                         │
                         ▼
                SEQUÊNCIA INTERMEDIÁRIA
                         │
                 ┌───────┴───────┐
                 │               │
                 ▼               ▼
              ATBASH          IDIOMA
                 │               │
                 └───────┬───────┘
                         ▼
                  POSSÍVEL PLAINTEXT
```

Neste estágio, **Atbash e idioma alternativo são hipóteses**, enquanto os resultados de `X=15`, `Y=27` e do Language Score são observações experimentais.

---

# 19. Próximos Experimentos

A próxima versão do **Libus Prime Analysis Engine** deverá testar sistematicamente:

### 19.1 Inversão modular

Partindo de:

**`z = (15x + 27y) mod 29`**

testar a recuperação de `y` através do inverso modular de `27`.

Como:

**`gcd(27,29) = 1`**

o inverso modular existe.

A operação poderá ser escrita como:

**`y = (z - 15x) × 27⁻¹ mod 29`**

---

### 19.2 Atbash após a transformação

Executar:

```text
Transformação → Atbash → Language Score
```

e comparar com:

```text
Transformação → Language Score
```

---

### 19.3 Atbash antes da transformação

Testar também a ordem inversa:

```text
Atbash → Transformação → Language Score
```

Isso permitirá verificar se a posição da possível camada Atbash influencia o resultado.

---

### 19.4 Fibonacci com diferentes estados iniciais

Testar diferentes condições iniciais da sequência:

```text
F(0)=0, F(1)=1
F(0)=1, F(1)=1
```

e outras possibilidades justificadas matematicamente.

---

### 19.5 Teste de todas as combinações de operação

Em vez de assumir uma única ordem, o motor poderá testar sistematicamente:

```text
Fibonacci
     ↓
Coeficiente
     ↓
Atbash
```

```text
Atbash
     ↓
Fibonacci
     ↓
Coeficiente
```

```text
Coeficiente
     ↓
Fibonacci
     ↓
Atbash
```

e comparar os resultados através do mesmo sistema estatístico.

---

### 19.6 Validação fora da Página 55

Caso uma transformação apresente resultado promissor na Página 55, ela deverá ser aplicada a outras páginas.

O objetivo será verificar se o mecanismo é:

**específico da Página 55**

ou:

**uma propriedade geral do Liber Primus.**

---

# 20. Conclusão Atual

A pesquisa sobre a Página 55 avançou de uma simples análise de frequência para uma abordagem de **engenharia reversa experimental**.

A investigação encontrou uma função candidata:

**`f(x,y) = (15x + 27y) mod 29`**

e posteriormente utilizou os coeficientes encontrados em diferentes modelos de transformação.

O maior Language Score observado foi:

**135**

aproximadamente **9 vezes** a linha de referência utilizada no experimento.

Apesar disso, o resultado ainda não produziu plaintext legível.

Isso estabelece o próximo problema da pesquisa:

> **A transformação encontrada representa o mecanismo completo ou apenas uma camada intermediária da cifra?**

A partir daqui, a investigação passa a testar sistematicamente essa possibilidade através de **inversão modular, Fibonacci, Atbash, diferentes modelos linguísticos, permutações e validação cruzada em outras páginas**.

O objetivo permanece o mesmo: determinar se os padrões encontrados na Página 55 representam uma propriedade real da estrutura criptográfica do *Liber Primus* ou uma correlação estatística produzida pelo processo de busca.

---

## Libus Prime Theory


# Libus Prime Theory — Continuação da Fase 2

## Engenharia Reversa e Caça à Chave Dinâmica

**Atualização do Motor:** Libus Prime Analysis Engine v2.1
**Foco:** Página 55 do *Liber Primus* (Cicada 3301)
**Autor:** Nink

---

## 21. Fechamento dos Primeiros Testes de Engenharia Reversa

Após a identificação da relação candidata

```text
f(x,y) = (15x + 27y) mod 29
```

e dos primeiros testes com Fibonacci, a pesquisa avançou para uma etapa mais agressiva de engenharia reversa.

O objetivo deixou de ser apenas verificar se existia uma relação matemática entre as runas e passou a ser:

> **Descobrir se essa relação poderia ser utilizada como mecanismo real de geração ou recuperação da chave.**

Foram então testadas diferentes formas de transformar a relação posicional em uma chave dinâmica, incluindo:

* Fibonacci módulo 29;
* coeficientes 15 e 27;
* transformações Atbash;
* chaves dependentes da posição;
* sequências de números primos;
* progressões quadráticas;
* razão áurea;
* geração em cadeia;
* modelos semelhantes a LFSR;
* busca exaustiva de coeficientes e sementes.

Esses experimentos produziram resultados importantes, principalmente por eliminar algumas interpretações possíveis da hipótese original.

---

# 22. Teste de Atbash + Fibonacci

Uma das hipóteses levantadas durante a investigação foi a possibilidade de existir uma camada de **Atbash** integrada ao mecanismo.

A ideia era que a transformação da Página 55 pudesse ocorrer em múltiplas etapas:

```text
Runa cifrada
      ↓
Transformação dinâmica
      ↓
Fibonacci / coeficientes
      ↓
Atbash
      ↓
Texto
```

Também foram testadas variações nas quais o Atbash era aplicado antes da transformação principal.

O objetivo era verificar se o espelhamento do alfabeto poderia recuperar alguma estrutura linguística que não aparecia na transformação matemática isolada.

### Resultado

Os testes apresentaram redução dos scores.

O maior resultado observado nessa família de transformações foi:

```text
Score máximo = 90
```

Além da redução do score, os textos produzidos perderam a estrutura linguística observada nos experimentos anteriores.

### Interpretação

Dentro das condições testadas, a inclusão direta do Atbash não melhorou a descriptografia.

Portanto, o Atbash passa a ser tratado como uma **hipótese experimental enfraquecida para essa etapa específica**, e não como parte confirmada do mecanismo.

Isso não demonstra que o Atbash jamais possa aparecer em outra camada do *Liber Primus*; apenas indica que as combinações testadas não produziram evidência favorável.

---

# 23. Teste de Chaves Dependentes da Posição

A teoria original também permitia uma possibilidade diferente:

> Os coeficientes da transformação poderiam variar conforme a posição da runa.

Em vez de utilizar sempre os mesmos valores:

```text
X = 15
Y = 27
```

o motor passou a testar sequências nas quais os valores da chave eram determinados pelo índice da posição.

Foram testados três modelos principais.

### 23.1. Sequência de números primos

A chave foi construída utilizando a sequência:

```text
2, 3, 5, 7, 11, 13, ...
```

com redução módulo 29.

### 23.2. Sequência quadrática

O segundo modelo utilizou:

```text
1², 2², 3², 4², ...
```

também reduzidos módulo 29.

### 23.3. Razão áurea

O terceiro modelo utilizou a aproximação:

```text
floor(i × 1.618)
```

para produzir uma sequência dependente da posição.

---

## 24. Resultado das Chaves Posicionais

Os três modelos produziram o mesmo resultado experimental:

```text
Primos      → Score 45
Quadrados   → Score 45
Phi         → Score 45
```

O resultado foi interpretado como um nível de **ruído de fundo** dentro do sistema de pontuação utilizado.

Em uma sequência curta, transformações arbitrárias podem produzir coincidências linguísticas ocasionais, especialmente quando o score procura padrões de letras ou bigramas.

Assim, o Score 45 não foi considerado evidência de que qualquer uma dessas sequências faça parte da cifra.

### Estado da hipótese

Até esse ponto, não foi encontrada evidência experimental favorável para:

```text
Chave = função direta da posição baseada em primos
Chave = função quadrática da posição
Chave = função baseada na razão áurea
```

Esses modelos foram, portanto, retirados da linha principal de investigação.

---

# 25. A Hipótese da Reação em Cadeia

A hipótese seguinte partiu de uma característica fundamental da teoria:

> Uma runa poderia participar da determinação da próxima runa.

Isso transforma a cifra em um sistema de estado.

A relação candidata:

```text
z = (15x + 27y) mod 29
```

poderia então ser interpretada como uma função de retroalimentação.

Nesse modelo:

```text
Estado anterior
      ↓
     x, y
      ↓
15x + 27y
      ↓
   mod 29
      ↓
Novo estado
      ↓
Próximo ciclo
```

Essa interpretação é semelhante conceitualmente a um **Linear Feedback Shift Register (LFSR)**, no qual valores anteriores alimentam o cálculo do próximo estado.

O objetivo era descobrir se a equação identificada na Fase 1 poderia funcionar não apenas como uma relação estatística, mas como um verdadeiro gerador de chave.

---

# 26. Busca pelas Sementes Iniciais

Para testar o modelo em cadeia, o motor não assumiu que a primeira chave era conhecida.

Foram testadas as possibilidades de semente inicial dentro do módulo 29.

O resultado mais interessante apareceu com:

```text
Semente = 2
```

A sequência produzida apresentou o início:

```text
THRERL...
```

Embora o restante não formasse texto legível, os primeiros caracteres chamaram atenção por apresentarem:

```text
THR
```

Esse fragmento é compatível, por coincidência estatística, com inícios de palavras frequentes do inglês, como:

```text
THREE
THERE
THROUGH
```

O resultado motivou uma busca muito maior.

---

# 27. O Quebrador LFSR Total

O próximo passo foi abandonar a escolha manual dos coeficientes.

O motor passou a testar sistematicamente:

```text
X = 0 ... 28
Y = 0 ... 28
```

e as possibilidades de sementes iniciais.

Como existem:

```text
29 × 29 = 841
```

combinações de coeficientes e:

```text
841
```

combinações para as duas sementes iniciais, o espaço total explorado foi:

```text
841 × 841 = 707.281
```

combinações.

Esse experimento constituiu o **Quebrador LFSR Total**.

---

# 28. Resultado da Busca de 707.281 Combinações

A busca encontrou um conjunto de parâmetros com um score extremamente alto:

```text
X  = 1
Y  = 22

K0 = 15
K1 = 28

Score = 500
```

O texto produzido começava aproximadamente como:

```text
GYYLTHTHTHTHEOTREOM...
```

O resultado parecia inicialmente significativo por causa do score elevado.

Entretanto, a inspeção da própria sequência revelou um problema fundamental.

O texto não apresentava uma estrutura linguística coerente.

Apesar disso, continha repetidamente padrões como:

```text
TH
THE
```

O algoritmo estava sendo recompensado por produzir fragmentos que pareciam inglês, mesmo quando o conjunto completo não correspondia a palavras ou frases reais.

---

# 29. Descoberta da Maximização Gananciosa

O resultado de Score 500 levou à identificação de uma limitação importante no sistema de pontuação.

O algoritmo de avaliação podia favorecer sequências que repetissem determinados padrões linguísticos de alta frequência.

Isso criou um tipo de **maximização gananciosa (*Greedy Maximization*)**.

Em vez de procurar:

> uma sequência que forme uma mensagem coerente,

o sistema estava, em determinadas condições, procurando:

> uma sequência que maximize localmente os padrões recompensados pelo score.

Essa diferença é fundamental.

Uma sequência como:

```text
TH
THE
TH
THE
TH
```

pode acumular muitos pontos em um sistema baseado em padrões frequentes, mas isso não significa que ela represente uma mensagem real.

Portanto:

```text
Score alto ≠ plaintext correto
```

Esse experimento demonstrou que o score precisava ser tratado com muito mais cuidado.

---

# 30. A Importância dos Falsos Positivos

O experimento do LFSR mostrou que uma busca matemática pode encontrar soluções que parecem extremamente boas segundo uma métrica, mas que não possuem significado linguístico real.

Isso introduziu uma nova preocupação metodológica na pesquisa:

### O motor precisa diferenciar:

```text
Padrão estatístico
        ≠
Estrutura linguística
        ≠
Plaintext real
```

Um resultado deve, portanto, ser analisado não apenas pelo score numérico, mas também por características como:

* coerência das palavras;
* estrutura de frases;
* distribuição de letras;
* consistência entre diferentes regiões do texto;
* reprodução do resultado em outras páginas;
* estabilidade quando os parâmetros são alterados;
* desempenho fora da amostra utilizada na descoberta.

Essa distinção passa a ser uma parte importante da metodologia do Libus Prime Theory.

---

# 31. O Que o LFSR Total Eliminou

Apesar de o resultado final não produzir plaintext, o experimento foi útil para testar uma interpretação específica da teoria.

A hipótese era:

```text
15x + 27y
        ↓
gerador de estado
        ↓
chave
        ↓
plaintext
```

A busca de 707.281 combinações mostrou que é possível produzir scores altos utilizando esse tipo de mecanismo.

Porém, o maior score encontrado também apresentou características de falso positivo.

Dessa forma, **o modelo de LFSR puro não apresentou uma solução linguística coerente para a Página 55**.

Isso enfraquece a interpretação de que a função encontrada na Fase 1 seja, por si só, um gerador completo da chave.

---

# 32. O Que os Experimentos Revelaram Sobre a Estrutura

A Fase 2 não produziu a descriptografia da Página 55.

Entretanto, ela adicionou informações importantes ao modelo.

Até este ponto, foram observadas três camadas distintas de comportamento:

### Camada 1 — Estrutura matemática

A relação:

```text
f(x,y) = (15x + 27y) mod 29
```

apresentou uma frequência de acertos superior à linha de base durante a análise inicial.

### Camada 2 — Transformações dinâmicas

Quando a relação foi combinada com Fibonacci e outras operações, alguns scores aumentaram significativamente.

O maior resultado inicial dessa família foi:

```text
Score = 135
```

### Camada 3 — Falsos positivos

Quando o mecanismo foi transformado em um gerador de chave em cadeia e submetido a uma busca exaustiva, apareceu:

```text
Score = 500
```

mas o texto correspondente não era coerente.

Isso demonstrou que a função de avaliação também precisa ser considerada durante a engenharia reversa.

---

# 33. Novo Estado da Teoria

Depois dos experimentos da Fase 2, a hipótese de trabalho passou a ser representada da seguinte maneira:

```text
┌──────────────────────────────┐
│       LIBER PRIMUS           │
└──────────────┬───────────────┘
               ↓
       Estrutura em runas
               ↓
       Gematria Primus
               ↓
       Módulo 29
               ↓
      Relação posicional
               ↓
      ┌────────────────┐
      │ 15x + 27y      │
      └───────┬────────┘
              ↓
      Camada dinâmica ?
              ↓
       Chave / Estado ?
              ↓
       Transformação ?
              ↓
          Inglês ?
```

A principal questão deixou de ser simplesmente:

> “Qual é a fórmula?”

e passou a ser:

> **“Qual é o papel da fórmula dentro do mecanismo completo?”**

Ela pode representar uma chave, uma transformação intermediária, uma relação entre estados ou apenas uma propriedade estrutural ainda não compreendida.

Os experimentos realizados até agora não permitem decidir entre essas possibilidades.

---

# 34. Hipótese da Cifra Híbrida

Com o enfraquecimento do modelo de geração algébrica pura, surgiu uma nova direção de investigação.

A cifra pode combinar mais de um mecanismo.

Um modelo possível seria:

```text
Texto original
      ↓
Chave-palavra
      ↓
Transformação semelhante a Vigenère
      ↓
Transposição / permutação
      ↓
Transformação modular
      ↓
Runas
```

ou, em ordem diferente:

```text
Texto
 ↓
Transformação estrutural
 ↓
Chave dinâmica
 ↓
Módulo 29
 ↓
Runas
```

Essa hipótese ainda não foi demonstrada.

Ela representa uma direção experimental baseada no fato de que nenhum dos mecanismos isolados testados até agora produziu uma solução linguística consistente.

---

# 35. Relação com Vigenère

Os resultados da Fase 2 também levaram a uma reconsideração da hipótese de uma cifra semelhante a Vigenère.

A pesquisa não demonstrou que uma cifra do tipo Vigenère esteja presente na Página 55.

Da mesma forma, os experimentos realizados não são suficientes para declarar que Vigenère esteja definitivamente descartada.

A hipótese passa a ser:

```text
Vigenère isolada
        ↓
não explica os resultados observados

Vigenère + transformação estrutural
        ↓
hipótese ainda não testada completamente
```

Isso abre espaço para investigar se uma chave-palavra poderia coexistir com uma transformação matemática ou estrutural.

---

# 36. O Problema do Índice de Coincidência

A pesquisa também passou a considerar que uma transformação estrutural poderia alterar significativamente as estatísticas tradicionais da cifra.

Se uma etapa de transposição ou transformação dinâmica reorganizar as posições das letras, métodos estatísticos tradicionais podem perder eficiência.

Isso significa que um baixo ou estranho Índice de Coincidência não necessariamente elimina a possibilidade de uma substituição linguística subjacente.

A hipótese passa a ser:

```text
Texto em inglês
      ↓
Substituição
      ↓
Transposição / transformação
      ↓
Cifra final
```

Nesse cenário, analisar somente a distribuição final das letras pode não ser suficiente.

Essa possibilidade deverá ser testada experimentalmente antes de ser considerada parte da teoria.

---

# 37. O Que Foi Eliminado e o Que Continua Aberto

### Hipóteses enfraquecidas pelos testes

```text
Atbash direto + Fibonacci
Chave baseada somente em primos
Chave baseada somente em quadrados
Chave baseada somente em Phi
LFSR puro baseado em 15x + 27y
```

Esses modelos não produziram uma solução linguística consistente nas condições testadas.

### Hipóteses que continuam abertas

```text
Transformação híbrida
Chave-palavra + transformação estrutural
Transposição
Permutação das runas
Chave dinâmica não-LFSR
Uso intermediário de 15x + 27y
Combinação entre estrutura modular e contexto linguístico
```

Nenhuma dessas possibilidades deve ser considerada confirmada neste estágio.

---

# 38. Nova Metodologia de Validação

Os resultados do Score 500 demonstraram que a próxima etapa não pode depender somente da maximização de uma única métrica.

O motor deverá considerar múltiplos critérios.

Um candidato forte deverá apresentar simultaneamente:

```text
Score linguístico
       +
Palavras coerentes
       +
Estrutura de frase
       +
Estabilidade estatística
       +
Reprodução em outras páginas
       +
Validação fora da amostra
```

Isso reduz a possibilidade de que o motor encontre apenas uma sequência que explore uma falha da função de pontuação.

---

# 39. Próxima Direção Experimental

Com o ciclo de geração algébrica praticamente encerrado, a pesquisa pode avançar para uma abordagem mais estrutural.

Os próximos testes podem investigar:

1. **Permutação das posições das runas.**
2. **Transposição em matrizes.**
3. **Reordenação utilizando sequências derivadas do módulo 29.**
4. **Aplicação da função `(15x + 27y) mod 29` sobre posições diferentes.**
5. **Busca por uma chave-palavra combinada com a transformação modular.**
6. **Testes de transformação antes e depois da possível chave.**
7. **Validação da mesma regra em outras páginas.**
8. **Testes com dados embaralhados para medir falsos positivos.**
9. **Criação de uma função de score menos vulnerável à repetição de bigramas.**
10. **Teste fora da amostra para separar descoberta de validação.**

A prioridade passa a ser descobrir **como as operações se combinam**, e não apenas encontrar a operação que produz o maior número isolado.

---

# 40. Conclusão da Fase 2

A Fase 2 encerra o primeiro ciclo de tentativas de transformar a relação matemática encontrada na Fase 1 em um gerador direto de chave.

Os experimentos mostraram que:

```text
Fibonacci isolado
        ↓
não produz plaintext

Atbash + Fibonacci
        ↓
não melhora o resultado

Chaves posicionais simples
        ↓
produzem apenas score de fundo

LFSR puro
        ↓
pode gerar scores extremamente altos,
mas também produz falsos positivos
```

O resultado mais importante da fase não foi encontrar a chave, mas identificar uma limitação fundamental do processo de busca:

> **Uma função matemática capaz de maximizar um score linguístico não é necessariamente uma função capaz de recuperar o plaintext.**

O Score 500 demonstrou isso de maneira particularmente clara.

A função:

```text
f(x,y) = (15x + 27y) mod 29
```

continua sendo uma peça relevante da investigação, mas seu papel exato permanece em aberto.

A pesquisa agora entra em uma nova etapa:

```text
                 FASE 1
                    ↓
       Identificação da estrutura
                    ↓
                 FASE 2
                    ↓
      Engenharia reversa algébrica
                    ↓
       LFSR / Fibonacci / Atbash
                    ↓
          descoberta de falsos
             positivos
                    ↓
              FASE 3
                    ↓
      Engenharia estrutural da cifra
                    ↓
     Transposição / Permutação /
       Chave híbrida / Contexto
```

O próximo objetivo não será simplesmente encontrar o maior score.

Será encontrar uma transformação que produza **uma estrutura linguística coerente, reproduzível e validável independentemente**.

Esse será o próximo estágio da investigação do **Libus Prime Theory**.


**Nink — Libus Prime Analysis Engine v2**

*Investigando a possível estrutura matemática interna do Liber Primus através de análise posicional, funções algébricas, módulo 29, Fibonacci, geometria, teoria dos números e engenharia reversa criptográfica.*

