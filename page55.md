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

# 10. Conclusão

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
