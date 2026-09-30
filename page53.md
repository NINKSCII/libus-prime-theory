# Libus Prime Theory — Fase 5: O Furo da Cifra

**Motor:** Libus Prime Analysis Engine v5.0
**Foco:** Aplicação da Máquina de Estados nas runas não decifradas e teste de controle
**Autor:** Nink

---

## 1. Introdução

Esta fase registra os resultados de um experimento realizado a partir do mecanismo desenvolvido na Fase 4, que combina a **Função Totiente de Euler aplicada a primos** com uma **regra de F-skip baseada em estado**.

O objetivo desta etapa foi testar o mecanismo em dois contextos:

1. uma página do *Liber Primus* que já possui uma solução conhecida;
2. a seção de runas ainda não decifrada.

A intenção foi observar se o comportamento produzido pelo mecanismo seria diferente entre os dois casos.

Os resultados abaixo são **experimentais**. Eles ainda precisam ser reproduzidos em outras páginas, testados com diferentes condições e analisados independentemente antes que qualquer conclusão sobre o funcionamento real da cifra possa ser estabelecida.

---

## 2. Teste de Controle — Página 53

Como controle, o motor foi aplicado à Página 53, uma página que possui uma solução conhecida baseada em Vigenère.

### Resultado

* **Mecanismo:** F-skip no plaintext
* **Score de linguagem:** 130
* **Saída:**

```text
THPEOWRTHEGOYPSOLUDNJOAIAIWEAEODEARBPXAEDPINGXB...
```

A saída não apresentou plaintext legível.

Esse resultado fornece um ponto de comparação para os testes realizados posteriormente nas runas não decifradas.

---

## 3. Teste nas Runas Não Decifradas

Em seguida, o mesmo motor foi aplicado às **204 runas** da seção não decifrada associada à Página 57, após a palavra **"EMERGE"**.

Foi utilizada a regra de estado denominada **Literal F Rule**, na qual o contador de primos não avança quando tanto a runa cifrada quanto o plaintext resultante correspondem a F (valor 0).

### Melhor resultado encontrado

* **Mecanismo:** F-skip exato — Cipher = F e Plain = F
* **Índice inicial da sequência de primos:** 5
* **Primeiro primo utilizado:** 13
* **Score de linguagem:** 230

### Saída produzida

```text
BAEWTIAATHIAGBOIWHWREANGPBAEAYNGOENLFYEASCTOEEOEDULYOETHDGHXTHAENGIOMEATHDUSOEEDWEANGAEOGNSNAENGOYATHAERXMPWGEOLWBEANGPJXFWHIAMREAIAEADIBRFYXYAEAEGETHNEAYSPHAEIBJEOOELGHBDAETHWTXBGDUPOEXTHPDWTHOCLTNGNGIAMAETHIDEOWFBEOOXEAGAEDIATHPUEAIYDEAEAAEBUDEOONOPNOETIMIAUTCTEOHTH
```

O resultado não constitui, neste estágio, um plaintext legível completo. Entretanto, ele apresentou uma pontuação de linguagem maior que a obtida no teste de controle e contém algumas sequências que podem ser comparadas com estruturas do inglês.

---

## 4. Padrões Observados

Alguns fragmentos chamaram atenção durante a análise:

* `WREANGP` e `WBEANGP` apresentam semelhanças estruturais com **WARNING**.
* `AETH` e `AETHI` aparecem em diferentes pontos da saída.
* `AENGOY` contém sequências como `ENG` e `ANG`.
* `EOEDULY` apresenta uma terminação semelhante a `ELY`.
* `AENGIOMEATH` contém combinações que podem ser comparadas a estruturas como `ING` e `MEAT/DEATH`.

Essas semelhanças são apenas **observações do resultado atual**. Ainda não foi demonstrado que correspondam efetivamente a palavras ou trechos do plaintext original.

Também é possível que parte dessas estruturas seja produzida pelas características do próprio método de pontuação ou por coincidência estatística.

---

## 5. Diferença Entre os Testes

Até o momento, os experimentos produziram:

| Teste                | Mecanismo    | Índice inicial |   Score | Resultado                        |
| -------------------- | ------------ | -------------: | ------: | -------------------------------- |
| Página 53            | F-skip       |              — |     130 | Não legível                      |
| Runas não decifradas | F-skip exato |              5 | **230** | Texto com estruturas recorrentes |
| Outros testes        | Em análise   |              — |       — | A verificar                      |

A diferença entre os scores é um dos motivos pelos quais o resultado merece uma investigação adicional.

No entanto, **um score maior, por si só, não demonstra que o plaintext foi recuperado**. É necessário verificar se o comportamento permanece consistente quando o método é aplicado a outras páginas e sob condições controladas.

---

## 6. Próximo Experimento — Calibração de Offset

O próximo passo é testar diferentes posições iniciais da sequência de primos.

A hipótese é que uma diferença no ponto inicial poderia alterar o momento em que os eventos de F-skip acontecem e, consequentemente, modificar a sequência resultante.

O calibrador deverá testar sistematicamente diferentes offsets, por exemplo:

```text
Offset 0
Offset 1
Offset 2
Offset 3
...
```

Cada resultado poderá então ser comparado utilizando os mesmos critérios de avaliação.

O objetivo é verificar se existe um offset que produza uma melhora consistente na estrutura linguística, e não simplesmente selecionar manualmente uma saída que pareça mais próxima do inglês.

---

## 7. Estado Atual da Hipótese

Os resultados desta fase são **preliminares**.

Até agora, existem três conjuntos de testes/resultados que apresentam comportamento compatível com partes da hipótese, mas isso ainda representa uma quantidade pequena de evidência.

Para avançar, seria necessário:

* testar mais páginas não decifradas;
* repetir os experimentos de forma independente;
* comparar diferentes offsets;
* verificar se o mesmo mecanismo produz padrões consistentes;
* testar o método contra páginas com plaintext conhecido;
* analisar estatisticamente a frequência das estruturas encontradas;
* verificar se os resultados podem ser reproduzidos por outros pesquisadores.

Portanto, esta fase não apresenta uma solução definitiva para as runas não decifradas.

Ela registra apenas que **o mecanismo testado produziu um resultado estatisticamente e estruturalmente interessante o suficiente para justificar novos testes**.

---

## 8. Conclusão

A Fase 5 teve como objetivo aplicar a Máquina de Estados desenvolvida nas fases anteriores diretamente às runas não decifradas e comparar seu comportamento com uma página já conhecida.

O principal resultado observado foi um **score de linguagem de 230** nas runas não decifradas, acompanhado por diversas sequências que apresentam características semelhantes a estruturas do inglês.

O teste de controle na Página 53 produziu um resultado diferente, com **score 130** e sem plaintext legível.

Essas diferenças são interessantes, mas ainda não permitem determinar se o mecanismo corresponde à cifra original do *Liber Primus*.

O próximo passo será ampliar os testes e investigar principalmente a **sincronização da sequência de primos e o comportamento do F-skip em diferentes offsets e páginas**.

> **Resultado atual: interessante, mas ainda não conclusivo.**

---

**Libus Prime Theory**
*Nink — Libus Prime Analysis Engine v5.0*
