# Libus Prime Theory

## Validação Matemática e Análise Estrutural do *Liber Primus*

**Autor:** Nink
**Projeto:** Libus Prime Theory
**Motor:** Libus Prime Analysis Engine v2
**Linguagem:** Python

---

## 1. Objetivo

A **Libus Prime Theory** propõe que o *Liber Primus* possa conter uma estrutura matemática interna relacionada à posição das runas, ao módulo 29, à sequência de Fibonacci e à organização geométrica dos valores da Gematria Primus.

O motor **Libus Prime Analysis Engine v2** foi desenvolvido para testar essas relações diretamente sobre dados reais do livro.

Neste experimento foram analisadas **204 runas da Página 57 do *Liber Primus***, utilizando duas camadas principais:

1. **Camada Posicional** — análise das diferenças entre runas consecutivas e comparação com Fibonacci em módulo 29.
2. **Camada Geométrica** — organização dos valores das runas em matrizes e análise dos MDCs entre posições vizinhas.

Também foram testadas diferentes larguras de matriz para verificar se determinados padrões permanecem ou surgem em configurações específicas.

---

# 2. Dados analisados

O trecho utilizado contém:

* **204 runas**
* **203 diferenças consecutivas**

As diferenças foram calculadas entre cada par de runas consecutivas.

Todas as diferenças da primeira camada foram analisadas em **módulo 29**, seguindo a estrutura de 29 posições da Gematria Primus.

---

# 3. Camada 1 — Análise Posicional e Fibonacci

A primeira camada investiga a possibilidade de que as transições entre runas sejam determinadas por uma regra posicional ou não-linear.

Uma das estruturas testadas é a sequência de Fibonacci reduzida módulo 29.

Os resíduos utilizados pelo motor foram:

```text
0, 1, 2, 3, 5, 8, 13, 21, 26, 28
```

Cada uma das 203 diferenças foi então classificada de acordo com a seguinte condição:

> A diferença entre as duas runas pertence ao conjunto de Fibonacci módulo 29?

## Resultado

O motor encontrou:

**74 de 203 transições**

pertencentes ao conjunto Fibonacci módulo 29.

Isso corresponde a:

**36,45%**

### Resultado principal

```text
204 runas
203 diferenças
74 matches com Fibonacci mod 29
36,45% de correspondência
```

---

## 3.1 Diferenças mais frequentes

| Diferença | Ocorrências | Fibonacci mod 29 |
| --------: | ----------: | :--------------: |
|         0 |          17 |         ✓        |
|        10 |          13 |                  |
|         1 |          12 |         ✓        |
|         6 |          11 |                  |
|        27 |          10 |                  |
|        28 |           9 |         ✓        |
|        25 |           9 |                  |
|        14 |           9 |                  |
|        21 |           8 |         ✓        |
|         4 |           8 |                  |

Entre os dez valores mais frequentes, quatro pertencem ao conjunto Fibonacci utilizado:

```text
0, 1, 28, 21
```

Esses quatro valores aparecem:

```text
17 + 12 + 9 + 8 = 46 vezes
```

Ou aproximadamente:

**22,66% das 203 transições.**

---

## 3.2 Interpretação da Camada Posicional

O resultado mostra uma presença mensurável de resíduos pertencentes ao conjunto Fibonacci módulo 29 dentro das transições analisadas.

Isso é compatível com a hipótese da **Camada Posicional** da Libus Prime Theory.

A proposta é que as transições entre runas possam depender não apenas do valor individual de cada runa, mas também de sua posição ou de algum estado matemático associado à sequência.

O experimento não determina sozinho qual seria essa função.

O ponto importante é que a hipótese produz um padrão que pode ser medido diretamente e testado em outras partes do livro.

---

# 4. Camada 2 — Estrutura Geométrica por MDC

A segunda camada parte da possibilidade de que a disposição espacial das runas também carregue informação matemática.

As 204 runas foram convertidas em valores numéricos e organizadas em matrizes com diferentes larguras:

```text
13 colunas
14 colunas
15 colunas
```

Para cada configuração, o motor calculou o **MDC entre runas vizinhas**:

* horizontalmente;
* verticalmente.

O objetivo é identificar possíveis invariantes aritméticos relacionados à organização espacial dos valores.

---

# 5. Matriz de 13 Colunas

A primeira configuração produziu uma matriz:

```text
16 × 13
```

## Relações horizontais

| MDC | Ocorrências |
| --: | ----------: |
|   1 |          79 |
|   2 |          40 |
|   4 |          11 |
|   5 |           8 |
|   9 |           4 |

## Relações verticais

| MDC | Ocorrências |
| --: | ----------: |
|   1 |          77 |
|   2 |          42 |
|   4 |           8 |
|   5 |           6 |
|   9 |           2 |

### Densidades

**MDC = 1:** 51,66%

**MDC > 1:** 48,34%

---

# 6. Matriz de 14 Colunas

A segunda configuração produziu:

```text
15 × 14
```

A largura de 14 colunas possui uma relação particularmente interessante com a teoria, pois **14 é o período de Pisano da sequência de Fibonacci módulo 29**.

## Relações horizontais

| MDC | Ocorrências |
| --: | ----------: |
|   1 |          78 |
|   2 |          43 |
|   4 |          11 |
|   5 |           7 |
|   9 |           4 |

## Relações verticais

| MDC | Ocorrências |
| --: | ----------: |
|   1 |          78 |
|   2 |          39 |
|   4 |           8 |
|   5 |           5 |
|  19 |       **4** |

### Densidades

**MDC = 1:** 51,66%

**MDC > 1:** 48,34%

---

## 6.1 O MDC = 19

Na configuração de 14 colunas, o motor encontrou:

```text
MDC = 19
```

**4 vezes na direção vertical.**

Esse resultado chama atenção porque a matriz possui exatamente **14 colunas**, enquanto 14 é o período de Pisano de Fibonacci módulo 29.

A relação observada pode ser representada como:

```text
Gematria Primus
      ↓
     29
      ↓
  Fibonacci
      ↓
     14
      ↓
   Matriz
      ↓
    MDC
      ↓
     19
```

O MDC 19 também aparece na configuração de 15 colunas, portanto sua presença não é exclusiva da largura 14.

O interesse da configuração de 14 colunas está na combinação entre a largura da matriz e o período de Fibonacci módulo 29.

---

# 7. Matriz de 15 Colunas

A terceira configuração produziu:

```text
14 × 15
```

## Relações horizontais

| MDC | Ocorrências |
| --: | ----------: |
|   1 |          80 |
|   2 |          40 |
|   4 |           9 |
|   5 |           7 |
|   9 |           4 |

## Relações verticais

| MDC | Ocorrências |
| --: | ----------: |
|   1 |          79 |
|   2 |          30 |
|   4 |          19 |
|  19 |       **4** |
|  14 |           3 |

### Densidades

**MDC = 1:** 52,82%

**MDC > 1:** 47,18%

---

# 8. Comparação das Matrizes

| Largura | Dimensão | Coprimalidade | MDC > 1 | Observação         |
| ------: | :------: | ------------: | ------: | ------------------ |
|      13 |  16 × 13 |        51,66% |  48,34% | Estrutura-base     |
|      14 |  15 × 14 |        51,66% |  48,34% | MDC 19 vertical ×4 |
|      15 |  14 × 15 |        52,82% |  47,18% | MDC 19 vertical ×4 |

Um ponto importante é que a densidade de coprimalidade das matrizes de 13 e 14 colunas é exatamente a mesma:

```text
51,66%
```

Portanto, o interesse da matriz de 14 colunas não está em uma simples diferença percentual.

O aspecto mais específico está na distribuição dos invariantes, especialmente na ocorrência de:

```text
MDC = 19
```

na direção vertical.

---

# 9. Relação entre as Duas Camadas

As duas camadas podem ser representadas da seguinte maneira.

## Camada Posicional

```text
Runa(n) → Runa(n+1)
              ↓
         diferença
              ↓
           mod 29
              ↓
        Fibonacci
```

Resultado observado:

**74 de 203 transições — 36,45%**

---

## Camada Geométrica

```text
Runas
  ↓
Valores da Gematria Primus
  ↓
Matriz
  ↓
MDC entre vizinhos
  ↓
Invariantes
```

Resultados observados:

**51,66% a 52,82% de coprimalidade**, dependendo da largura da matriz.

Além disso, o valor:

```text
MDC = 19
```

aparece 4 vezes verticalmente nas matrizes de 14 e 15 colunas.

---

# 10. Modelo da Libus Prime Theory

A estrutura atual da teoria pode ser representada assim:

```text
                  LIBUS PRIME THEORY
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
      CAMADA POSICIONAL       CAMADA GEOMÉTRICA
              │                     │
              ▼                     ▼
       Transições             Organização espacial
              │                     │
              ▼                     ▼
       Diferenças mod 29       Matriz numérica
              │                     │
              ▼                     ▼
       Fibonacci mod 29             MDC
              │                     │
              ▼                     ▼
        Padrões recorrentes     Invariantes
              │                     │
              └──────────┬──────────┘
                         │
                         ▼
              POSSÍVEL ESTRUTURA
              CRIPTOGRÁFICA INTERNA
```

A hipótese central da teoria é que as duas camadas possam estar relacionadas.

A cadeia investigada é:

```text
Posição
   ↓
Fibonacci
   ↓
Módulo 29
   ↓
Geometria
   ↓
MDC
   ↓
Invariante
```

A possibilidade investigada é que essas relações façam parte de uma estrutura matemática interna do *Liber Primus*.

---

# 11. O Que o Motor v2 Encontrou

O experimento produziu os seguintes resultados principais:

### 1. Dados analisados

```text
204 runas
203 transições
```

### 2. Fibonacci módulo 29

```text
74 matches
36,45%
```

### 3. Resíduos Fibonacci entre os mais frequentes

```text
0
1
28
21
```

### 4. Estrutura geométrica

As três larguras testadas produziram aproximadamente metade das relações com:

```text
MDC > 1
```

### 5. MDC = 19

O motor encontrou:

```text
4 ocorrências
```

de MDC 19 verticalmente na matriz de 14 colunas.

O mesmo valor também apareceu 4 vezes verticalmente na matriz de 15 colunas.

### 6. Relação com Fibonacci

A largura de 14 colunas coincide com o período de Pisano de Fibonacci módulo 29.

---

# 12. Conclusão

Os resultados obtidos pelo **Libus Prime Analysis Engine v2** fornecem suporte experimental às duas camadas fundamentais da **Libus Prime Theory**.

A primeira camada encontrou uma frequência de:

**36,45% de transições pertencentes ao conjunto Fibonacci módulo 29.**

A segunda camada encontrou padrões mensuráveis de divisibilidade entre runas vizinhas quando os valores são organizados espacialmente em matrizes.

O resultado mais específico observado foi a presença de:

```text
MDC = 19
```

quatro vezes na direção vertical das matrizes de 14 e 15 colunas.

A configuração de 14 colunas possui ainda uma relação estrutural importante com a teoria:

```text
período de Pisano de Fibonacci mod 29 = 14
```

Assim, os dados obtidos sustentam a investigação da seguinte estrutura:

```text
Gematria
   ↕
Posição
   ↕
Fibonacci
   ↕
Módulo 29
   ↕
Geometria
   ↕
MDC
```

A teoria deixa de ser apenas uma formulação abstrata e passa a possuir um **procedimento computacional reproduzível**, capaz de produzir resultados quantitativos sobre dados reais do *Liber Primus*.

---

# 13. Próxima Etapa — Validação Cruzada

O próximo objetivo é determinar se os padrões encontrados são específicos da organização original do *Liber Primus*.

Os principais testes serão:

### A. Teste de embaralhamento

Manter exatamente as mesmas runas e suas frequências, mas destruir a ordem original.

### B. Teste entre páginas

Executar o mesmo motor em diferentes páginas do *Liber Primus*.

### C. Teste de largura

Expandir a análise para diferentes larguras:

```text
12, 13, 14, 15, 16, ...
```

### D. Teste de Fibonacci

Verificar se a frequência de resíduos Fibonacci permanece elevada em outras amostras.

### E. Distribuição completa de MDC

Analisar a frequência de cada valor de MDC encontrado.

### F. Busca de invariantes

Procurar valores que apareçam repetidamente em diferentes páginas e verificar se desaparecem quando a organização espacial é destruída.

---

# 14. Estado Atual da Libus Prime Theory

A **Libus Prime Theory** possui atualmente:

* uma hipótese de duas camadas;
* uma formulação matemática;
* um motor de análise em Python;
* dados reais do *Liber Primus*;
* resultados quantitativos;
* análise posicional;
* análise geométrica;
* relações com Fibonacci;
* análise em módulo 29;
* análise por MDC;
* testes com diferentes larguras de matriz;
* e uma metodologia definida para validação cruzada.

O objetivo final da investigação é determinar se a combinação:

```text
Gematria
↔
Posição
↔
Fibonacci
↔
Módulo 29
↔
Geometria
↔
MDC
```

pode revelar uma transformação matemática ou estrutura criptográfica concreta dentro do *Liber Primus*.

---

## Libus Prime Theory

**Nink — Libus Prime Analysis Engine v2**

> Investigando a estrutura matemática interna do *Liber Primus* através de análise posicional, Fibonacci, módulo 29, geometria e teoria dos números.

