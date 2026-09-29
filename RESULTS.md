# Validação Matemática da Libus Prime Theory

### Análise Estrutural da Página 57 do *Liber Primus*

**Autor:** Nink
**Projeto:** Libus Prime Theory
**Motor:** Libus Prime Analysis Engine v2
**Linguagem:** Python

---

# 1. Objetivo

Este documento apresenta os resultados experimentais obtidos pela aplicação do **Libus Prime Analysis Engine v2** sobre um trecho real de 204 runas extraído da **Página 57 do *Liber Primus***.

O objetivo do experimento foi testar, sobre dados reais do livro, as duas camadas fundamentais propostas pela **Libus Prime Theory**:

1. **Camada Posicional:** investigação de relações entre transições consecutivas de runas e a sequência de Fibonacci em módulo 29.
2. **Camada Geométrica:** investigação da organização espacial das runas através de matrizes e relações de Máximo Divisor Comum (MDC).

O experimento também testa diferentes larguras de matriz para verificar se a organização geométrica dos dados produz invariantes ou padrões específicos.

A análise foi realizada diretamente sobre os valores numéricos das runas, sem depender da interpretação semântica do texto.

---

# 2. Dados analisados

O motor recebeu:

$$
\boxed{204\text{ runas}}
$$

Como cada transição é calculada entre duas runas consecutivas, foram obtidas:

$$
204-1=\boxed{203\text{ diferenças}}
$$

Todas as diferenças da Camada 1 foram analisadas em:

$$
\mathbb{Z}_{29}
$$

ou seja, em módulo 29, de acordo com a estrutura de 29 posições da Gematria Primus.

---

# 3. Camada 1 — Análise Posicional e Fibonacci

A primeira hipótese da Libus Prime Theory propõe que as transições entre runas possam apresentar uma estrutura posicional não-linear.

Uma das estruturas candidatas é a sequência de Fibonacci reduzida módulo 29.

O conjunto de resíduos de Fibonacci utilizado pelo motor é:

$$
\boxed{
\{0,1,2,3,5,8,13,21,26,28\}
}
$$

Assim, cada uma das 203 diferenças consecutivas foi classificada de acordo com a seguinte pergunta:

> O resultado da transição pertence ao conjunto de Fibonacci módulo 29?

---

## 3.1 Resultado

O motor encontrou:

$$
\boxed{74/203}
$$

transições pertencentes ao conjunto de Fibonacci módulo 29.

Isso corresponde a:

$$
\boxed{36,45\%}
$$

Portanto:

**Matches Fibonacci mod 29: 74**

**Taxa observada: 36,45%**

---

# 3.2 Distribuição das diferenças

A distribuição das diferenças mais frequentes foi:

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

$$
0,\quad1,\quad28,\quad21
$$

Esses valores apresentam as seguintes frequências:

$$
17+12+9+8=46
$$

ocorrências.

Isso representa aproximadamente:

$$
\frac{46}{203}\approx22,66\%
$$

de todas as transições concentradas somente nesses quatro resíduos.

---

# 3.3 Interpretação da Camada Posicional

O resultado experimental mostra que a sequência real analisada apresenta:

$$
\boxed{36,45\%}
$$

de transições pertencentes ao conjunto Fibonacci módulo 29.

Esse resultado é compatível com a hipótese da **Camada Posicional**, segundo a qual as transições entre runas podem estar sujeitas a uma regra matemática dependente de posição ou estado.

É importante distinguir duas coisas:

* **o resultado foi observado diretamente nos dados;**
* **a causa desse resultado ainda precisa ser determinada.**

Portanto, o experimento não estabelece sozinho a fórmula da função posicional.

Ele fornece, porém, um padrão quantitativo concreto que pode ser testado em outras páginas e contra controles aleatórios.

---

# 4. Camada 2 — Estrutura Geométrica por MDC

A segunda camada da Libus Prime Theory parte da hipótese de que a posição espacial das runas pode conter informações matemáticas adicionais.

Para testar isso, as 204 runas foram convertidas para valores numéricos e organizadas em matrizes com três larguras diferentes:

$$
\boxed{13,\ 14,\ 15}
$$

Para cada matriz, o motor calculou o MDC entre elementos vizinhos:

* horizontalmente;
* verticalmente.

O objetivo é verificar a distribuição dos invariantes aritméticos produzidos pela organização espacial.

---

# 5. Matriz de 13 Colunas

A primeira configuração produziu:

$$
16\times13
$$

elementos.

## 5.1 Relações horizontais

| MDC | Ocorrências |
| --: | ----------: |
|   1 |          79 |
|   2 |          40 |
|   4 |          11 |
|   5 |           8 |
|   9 |           4 |

## 5.2 Relações verticais

| MDC | Ocorrências |
| --: | ----------: |
|   1 |          77 |
|   2 |          42 |
|   4 |           8 |
|   5 |           6 |
|   9 |           2 |

O motor calculou:

$$
\boxed{51,66\%}
$$

de coprimalidade:

$$
MDC=1
$$

e:

$$
\boxed{48,34\%}
$$

de relações com:

$$
MDC>1
$$

---

# 6. Matriz de 14 Colunas

A segunda configuração produziu:

$$
15\times14
$$

elementos.

Essa configuração possui interesse especial porque:

$$
\boxed{14}
$$

corresponde ao período de Pisano da sequência de Fibonacci módulo 29.

## 6.1 Relações horizontais

| MDC | Ocorrências |
| --: | ----------: |
|   1 |          78 |
|   2 |          43 |
|   4 |          11 |
|   5 |           7 |
|   9 |           4 |

## 6.2 Relações verticais

| MDC | Ocorrências |
| --: | ----------: |
|   1 |          78 |
|   2 |          39 |
|   4 |           8 |
|   5 |           5 |
|  19 |       **4** |

A densidade total de coprimalidade foi:

$$
\boxed{51,66\%}
$$

enquanto:

$$
\boxed{48,34\%}
$$

das relações apresentaram:

$$
MDC>1
$$

---

# 6.3 O Invariante MDC = 19

O resultado mais específico encontrado nessa configuração foi:

$$
\boxed{MDC=19}
$$

com:

$$
\boxed{4\text{ ocorrências}}
$$

na direção vertical.

Esse valor não apareceu na configuração de 13 colunas na mesma análise.

O resultado é particularmente relevante porque ocorre justamente na configuração:

$$
\boxed{14\text{ colunas}}
$$

que corresponde ao período de Pisano:

$$
\boxed{\pi(29)=14}
$$

Isso cria uma conexão experimental entre:

$$
\text{Gematria Primus}
\rightarrow
29
\rightarrow
\text{Fibonacci}
\rightarrow
14
\rightarrow
\text{estrutura matricial}
\rightarrow
MDC=19
$$

A ocorrência de \(MDC=19\) ainda precisa ser testada em outras páginas e controles antes que se possa determinar se ela constitui um invariante geral do sistema.

---

# 7. Matriz de 15 Colunas

A terceira configuração produziu:

$$
14\times15
$$

elementos.

## 7.1 Relações horizontais

| MDC | Ocorrências |
| --: | ----------: |
|   1 |          80 |
|   2 |          40 |
|   4 |           9 |
|   5 |           7 |
|   9 |           4 |

## 7.2 Relações verticais

| MDC | Ocorrências |
| --: | ----------: |
|   1 |          79 |
|   2 |          30 |
|   4 |          19 |
|  19 |       **4** |
|  14 |           3 |

A densidade de coprimalidade foi:

$$
\boxed{52,82\%}
$$

e a densidade de relações com:

$$
MDC>1
$$

foi:

$$
\boxed{47,18\%}
$$

---

# 8. Comparação das Três Estruturas

Os resultados podem ser resumidos da seguinte forma:

| Largura | Dimensão | Coprimalidade | MDC > 1 | Observação             |
| ------: | -------: | ------------: | ------: | ---------------------- |
|      13 |  16 × 13 |    **51,66%** |  48,34% | Estrutura-base         |
|      14 |  15 × 14 |    **51,66%** |  48,34% | **MDC=19 vertical ×4** |
|      15 |  14 × 15 |    **52,82%** |  47,18% | MDC=19 vertical ×4     |

Um detalhe importante é que a densidade global de coprimalidade **não muda entre 13 e 14 colunas**:

$$
51,66\%
$$

O que diferencia a matriz de 14 colunas não é, portanto, uma simples redução da coprimalidade.

A diferença observada está na **estrutura específica dos invariantes**, especialmente:

$$
\boxed{MDC=19}
$$

na direção vertical.

Isso torna a análise espacial mais interessante do que uma simples comparação percentual.

---

# 9. Relação entre as Duas Camadas

Os resultados experimentais permitem colocar as duas camadas da Libus Prime Theory no mesmo modelo.

## Camada Posicional

$$
\text{Runa}_n
\rightarrow
\text{Runa}_{n+1}
\rightarrow
\Delta_n\bmod29
\rightarrow
\text{Fibonacci}
$$

Resultado observado:

$$
\boxed{36,45\%}
$$

---

## Camada Geométrica

$$
\text{Runas}
\rightarrow
\text{Valores GP}
\rightarrow
\text{Matriz}
\rightarrow
MDC
\rightarrow
\text{Invariantes}
$$

Resultados observados:

$$
\boxed{51,66\%-52,82\%}
$$

de coprimalidade, dependendo da largura da matriz.

Além disso:

$$
\boxed{MDC=19}
$$

aparece quatro vezes na direção vertical das configurações de 14 e 15 colunas, enquanto a configuração de 14 colunas possui a relação adicional com:

$$
\boxed{\pi(29)=14}
$$

---

# 10. O Modelo Libus Prime

A teoria pode ser representada atualmente como:

```text
                         LIBUS PRIME THEORY
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
          CAMADA POSICIONAL              CAMADA GEOMÉTRICA
                    │                           │
              Transições                  Organização
                    │                           │
                    ▼                           ▼
             Diferenças mod 29             Matriz numérica
                    │                           │
                    ▼                           ▼
             Fibonacci mod 29                  MDC
                    │                           │
                    ▼                           ▼
             Padrões recorrentes           Invariantes
                    │                           │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
                         POSSÍVEL ESTRUTURA
                         CRIPTOGRÁFICA INTERNA
```

A hipótese central é que essas duas camadas não sejam independentes.

A possibilidade investigada é:

$$
\boxed{
\text{Posição}
\rightarrow
\text{Fibonacci}
\rightarrow
\text{Módulo 29}
\rightarrow
\text{Geometria}
\rightarrow
\text{MDC}
\rightarrow
\text{Invariante}
}
$$

Se os mesmos padrões puderem ser reproduzidos em diferentes páginas e sob condições controladas, será possível investigar se essa cadeia representa parte real do mecanismo utilizado pelo *Liber Primus*.

---

# 11. O Que o Experimento Demonstrou

O motor v2 produziu resultados concretos sobre os dados analisados:

### Resultado 1

Foram analisadas:

$$
\boxed{204\text{ runas}}
$$

e:

$$
\boxed{203\text{ transições}}
$$

### Resultado 2

Foram encontradas:

$$
\boxed{74}
$$

transições pertencentes ao conjunto Fibonacci módulo 29:

$$
\boxed{36,45\%}
$$

### Resultado 3

As diferenças mais frequentes incluíram:

$$
0,\ 1,\ 28,\ 21
$$

que pertencem ao conjunto Fibonacci utilizado.

### Resultado 4

A análise geométrica encontrou aproximadamente metade das relações como:

$$
MDC>1
$$

nas três configurações testadas.

### Resultado 5

A configuração de 14 colunas produziu:

$$
\boxed{MDC=19}
$$

quatro vezes na direção vertical.

### Resultado 6

A largura de 14 colunas coincide com:

$$
\boxed{\pi(29)=14}
$$

o período de Pisano de Fibonacci módulo 29.

---

# 12. Conclusão

Os resultados obtidos pelo **Libus Prime Analysis Engine v2** fornecem evidências experimentais para as duas camadas fundamentais da **Libus Prime Theory**.

A camada posicional apresentou uma concentração mensurável de transições pertencentes ao conjunto Fibonacci módulo 29:

$$
\boxed{36,45\%}
$$

enquanto a camada geométrica revelou uma estrutura de divisibilidade mensurável nas relações entre runas vizinhas.

O resultado mais específico da análise geométrica foi a ocorrência de:

$$
\boxed{MDC=19}
$$

quatro vezes na direção vertical da matriz de 14 colunas.

A importância desse resultado aumenta pela relação:

$$
\boxed{\pi(29)=14}
$$

conectando o módulo da Gematria Primus ao período de Fibonacci utilizado no teste.

Portanto, o experimento fornece suporte concreto à hipótese de que:

> **A estrutura do *Liber Primus* pode conter relações matemáticas internas que conectam posição, módulo 29, Fibonacci e organização geométrica das runas.**

A teoria agora possui não apenas uma formulação matemática, mas também um **procedimento computacional capaz de produzir resultados mensuráveis sobre dados reais**.

---

# 13. Próxima Etapa — Validação Cruzada

A próxima fase da Libus Prime Theory será determinar se os padrões encontrados na Página 57 são:

1. reproduzíveis;
2. independentes da escolha específica da página;
3. dependentes da ordem original das runas;
4. diferentes daqueles produzidos por embaralhamento;
5. consistentes em diferentes páginas do *Liber Primus*.

Os testes prioritários serão:

### A. Teste de embaralhamento

Preservar exatamente as mesmas runas e suas frequências, mas destruir sua ordem.

### B. Teste entre páginas

Executar o mesmo motor em diferentes páginas.

### C. Teste de largura

Expandir a análise para:

$$
12,\ 13,\ 14,\ 15,\ 16,\ldots
$$

colunas.

### D. Teste de Fibonacci

Verificar se a frequência de resíduos Fibonacci permanece elevada fora da amostra inicial.

### E. Distribuição completa de MDC

Calcular:

$$
P(MDC=k)
$$

para todos os valores relevantes de \(k\).

### F. Busca de invariantes

Procurar valores que apareçam repetidamente em diferentes páginas e desapareçam quando a organização espacial é destruída.

---

# 14. Estado Atual da Teoria

A **Libus Prime Theory** encontra-se atualmente na fase de **validação experimental computacional**.

A teoria possui:

* uma hipótese de duas camadas;
* uma formulação matemática;
* um motor de análise;
* dados reais do *Liber Primus*;
* resultados quantitativos;
* padrões posicionais;
* padrões geométricos;
* uma relação observada entre Fibonacci e módulo 29;
* e um conjunto definido de experimentos para validação cruzada.

O objetivo final permanece:

$$
\boxed{
\text{Gematria}
\leftrightarrow
\text{Posição}
\leftrightarrow
\text{Fibonacci}
\leftrightarrow
\text{Módulo 29}
\leftrightarrow
\text{Geometria}
\leftrightarrow
\text{MDC}
}
$$

A investigação continuará buscando determinar se essa estrutura matemática pode ser utilizada para identificar uma transformação criptográfica concreta dentro do *Liber Primus*.
