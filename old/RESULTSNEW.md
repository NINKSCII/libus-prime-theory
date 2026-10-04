# Libus Prime Theory v4.0

## Validação Empírica da Assinatura Estrutural da Cifra

**Motor:** Libus Prime Analysis Engine v4.0
**Foco:** Validação empírica da anomalia algébrica e mapeamento da máquina de estados
**Autor:** Nink

---

## 1. Introdução

O presente documento consolida a fase de testes realizada sobre a Página 55 do *Liber Primus* (Cicada 3301).

A *Libus Prime Theory* originalmente propunha que a cifra poderia conter uma estrutura algébrica não linear descrita pela relação:

**`(15x + 27y) mod 29`**

Entretanto, os testes subsequentes mostraram que utilizar essa relação diretamente como mecanismo de descriptografia não produzia um *plaintext* legível. Isso criou uma aparente contradição: a relação apresentava uma frequência de correspondência significativamente superior à linha de base aleatória, mas não funcionava como uma chave de descriptografia direta.

A revisão da hipótese levou a uma mudança fundamental na interpretação da equação.

Em vez de representar diretamente a chave, **`(15x + 27y) mod 29` passou a ser tratada como uma possível assinatura estrutural do próprio texto cifrado**.

A partir dessa distinção, a teoria passou a separar dois componentes:

1. **Camada estrutural:** responsável por características internas da sequência de runas cifradas;
2. **Camada de estado:** responsável pela evolução do deslocamento utilizado na descriptografia.

O objetivo desta versão é documentar os resultados experimentais que sustentam essa separação e estabelecer os próximos testes necessários.

---

# 2. Hipótese da Máquina de Estados

A segunda camada da teoria considera que o deslocamento utilizado pela cifra não é necessariamente constante.

O modelo investigado utiliza uma sequência de números primos e a Função Totiente de Euler:

**`kᵢ = φ(pᵢ) mod 29`**

onde:

* `pᵢ` representa o primo associado ao estado `i`;
* `φ` representa a Função Totiente de Euler;
* `kᵢ` representa o deslocamento utilizado naquele estado;
* todas as operações são realizadas módulo 29.

Como os valores `pᵢ` são primos, vale:

**`φ(p) = p − 1`**

para `p` primo.

O modelo também incorpora uma regra de interrupção de estado denominada **Literal F Rule**, ou **F-skip**.

Nesse modelo, quando o *plaintext* produzido em uma determinada posição corresponde à runa **F**, cujo valor na Gematria Primus utilizada pelo motor é `0`, o contador de estados não avança.

Assim, conceitualmente:

**Se `Pᵢ = F`:**

`estado(i+1) = estado(i)`

**Caso contrário:**

`estado(i+1) = estado(i) + 1`

Essa regra transforma a sequência de deslocamentos em uma máquina dependente do próprio resultado da descriptografia.

Isso é importante porque significa que uma pequena defasagem inicial pode alterar o estado futuro de toda a sequência.

---

# 3. O Teste de Três Eixos

Para determinar qual componente da sequência apresenta a anomalia associada à expressão:

**`(15x + 27y) mod 29`**

o Libus Prime Analysis Engine v4.0 aplicou a mesma relação em três estruturas distintas:

### Eixo P — Plaintext

A relação foi aplicada sobre a sequência correspondente ao texto original supostamente recuperado.

### Eixo K — Key / Estado

A relação foi aplicada sobre os valores associados ao fluxo da sequência de primos e seus deslocamentos.

### Eixo C — Ciphertext

A relação foi aplicada diretamente sobre as runas cifradas originais.

A linha de base para uma correspondência modular aleatória em um espaço de 29 valores é:

**`1 / 29 ≈ 3,45%`**

Os testes da Página 55 produziram:

| Estrutura          | Correspondência |
| ------------------ | --------------: |
| Plaintext (P)      |       **2,70%** |
| Chave / Estado (K) |       **1,35%** |
| Ciphertext (C)     |      **13,51%** |
| Linha de base      |     **≈ 3,45%** |

O resultado mais relevante é a diferença entre o comportamento da cifra e os outros dois eixos.

A relação apresentou aproximadamente quatro vezes a frequência esperada pela linha de base dentro da sequência cifrada, enquanto não apresentou comportamento equivalente no plaintext ou no fluxo de chave testado.

---

# 4. Interpretação da Anomalia

Os resultados não indicam que a expressão:

**`(15x + 27y) mod 29`**

seja, por si só, uma chave de descriptografia.

Na realidade, o experimento aponta para uma interpretação diferente:

> **A relação pode estar descrevendo uma propriedade estrutural da sequência cifrada.**

Essa distinção resolve o aparente paradoxo observado nos testes anteriores.

Se a relação fosse diretamente o mecanismo responsável pela recuperação do plaintext, seria esperado que sua aplicação produzisse uma transformação consistente em direção a uma linguagem legível.

Isso não ocorreu.

Por outro lado, a relação apresentou uma concentração de correspondências muito maior quando aplicada diretamente ao ciphertext.

Portanto, a hipótese atualmente investigada é:

**`15x + 27y mod 29` → assinatura estrutural**

e não:

**`15x + 27y mod 29` → chave de descriptografia**

Essa mudança de interpretação preserva a observação experimental original sem atribuir à equação uma função que os testes não demonstraram.

---

# 5. A Hipótese de Realimentação

Uma possível explicação para uma assinatura desse tipo seria a existência de um mecanismo de **realimentação**, no qual valores anteriores da sequência influenciam valores posteriores.

A expressão:

**`Aᵢ = (15Cᵢ₋₁ + 27Cᵢ) mod 29`**

possui exatamente essa característica: o resultado depende de dois estados consecutivos da sequência cifrada.

Isso torna a relação compatível, em termos estruturais, com modelos de recorrência ou sistemas de realimentação.

Um **LFSR (Linear Feedback Shift Register)** é uma das possíveis estruturas matemáticas que apresentam esse tipo de comportamento.

Entretanto, o teste realizado **não demonstra que o Liber Primus utiliza especificamente um LFSR**.

Portanto, nesta versão da teoria, LFSR deve ser tratado como:

> **uma hipótese de implementação compatível com a assinatura observada, e não como uma conclusão estabelecida.**

O objetivo dos próximos experimentos será determinar se a assinatura pode ser explicada por um mecanismo de estado específico.

---

# 6. Aplicação da Máquina de Estados

Após separar a assinatura estrutural da possível chave, o motor passou a testar a segunda camada independentemente.

O modelo utilizado foi:

**`kᵢ = φ(pᵢ) mod 29`**

seguido pela transformação:

**`Pᵢ = (Cᵢ − kᵢ) mod 29`**

com aplicação da regra F-skip sobre o estado.

Foram testados diferentes pontos de partida da sequência de primos, incluindo:

`2, 3, 5, 7, ...`

O objetivo desse procedimento foi verificar se uma eventual diferença entre a posição real da máquina e a posição assumida pelo motor poderia explicar os resultados incompletos obtidos anteriormente.

Entre os testes realizados, o melhor resultado registrado ocorreu com início no **primo 7**, correspondente ao índice 3 da sequência utilizada pelo motor, combinado com a regra de F-skip.

O resultado alcançou **Language Score = 200**.

Entretanto, o texto obtido ainda não constitui um *plaintext* completo e inequívoco.

---

# 7. O Limite Experimental da Página 55

A Página 55 contém aproximadamente **76 runas** na transcrição utilizada no experimento.

Esse tamanho de amostra é particularmente relevante porque o modelo investigado possui uma característica diferente de uma cifra simples.

O estado futuro depende do estado anterior e, potencialmente, do próprio resultado da descriptografia.

Consequentemente:

**erro inicial → estado incorreto → próximo deslocamento incorreto → novo estado incorreto → divergência progressiva**

Em uma sequência curta, torna-se difícil distinguir entre:

* uma chave parcialmente correta;
* um estado inicial incorreto;
* uma regra de transição incompleta;
* um erro de transcrição;
* ou simplesmente uma coincidência estatística.

Portanto, o resultado da Página 55 deve ser interpretado como **evidência experimental para orientar a próxima etapa**, e não como uma descriptografia concluída.

A limitação observada não demonstra que o modelo seja impossível de testar. Ela indica que a Página 55, isoladamente, possui pouca informação para validar de forma robusta uma máquina de estados com realimentação.

---

# 8. Relação Entre as Duas Camadas

A teoria agora pode ser representada por duas funções distintas.

### Camada 1 — Assinatura estrutural

**`Aᵢ = (15Cᵢ₋₁ + 27Cᵢ) mod 29`**

Essa camada procura identificar uma propriedade interna da sequência cifrada.

### Camada 2 — Máquina de estados

**`kᵢ = φ(pᵢ) mod 29`**

e:

**`Pᵢ = (Cᵢ − kᵢ) mod 29`**

com:

**F-skip → alteração da progressão do estado**

A hipótese central passa a ser que essas duas estruturas **não precisam desempenhar a mesma função**.

A primeira pode identificar a estrutura ou o estado da cifra.

A segunda pode determinar o deslocamento necessário para recuperar o plaintext.

O próximo objetivo, portanto, não é simplesmente maximizar um *Language Score*.

É determinar se existe uma relação mensurável entre:

**assinatura → estado → deslocamento → plaintext**

---

# 9. Teste de Sincronia

O próximo experimento deverá comparar, posição por posição:

* `Aᵢ = (15Cᵢ₋₁ + 27Cᵢ) mod 29`;
* primo atualmente utilizado;
* `φ(pᵢ) mod 29`;
* estado da máquina;
* valor do ciphertext;
* valor do plaintext;
* ocorrência de F-skip.

A pergunta central será:

> **A assinatura algébrica contém informação suficiente para identificar ou prever mudanças no estado da máquina?**

Caso exista uma correlação consistente entre esses elementos em diferentes regiões do texto, a hipótese de que `15x + 27y` representa uma estrutura de estado ganhará suporte adicional.

Caso a relação desapareça quando aplicada a outras páginas, sua importância deverá ser reavaliada.

---

# 10. Controle Contra Coincidências

Como a relação `15x + 27y` foi encontrada através da exploração de múltiplas combinações possíveis, sua frequência observada não deve ser interpretada isoladamente como uma prova estatística definitiva.

O espaço pesquisado contém:

**29 × 29 = 841 combinações possíveis de `(X,Y)`**

Portanto, uma validação mais forte precisa comparar o resultado observado com controles apropriados.

O motor deverá testar, por exemplo:

1. sequências aleatoriamente embaralhadas;
2. páginas diferentes;
3. outras combinações `(X,Y)`;
4. permutações preservando a distribuição das runas;
5. a mesma estatística em regiões independentes da página.

O objetivo é verificar se a relação:

**`(15,27)`**

continua apresentando comportamento anômalo quando submetida a dados que preservem algumas características estatísticas da cifra, mas eliminem sua ordem original.

Se a anomalia desaparecer após a destruição da ordem, isso fortalecerá a interpretação de que ela depende da estrutura sequencial do ciphertext.

---

# 11. Estado Atual da Teoria

Com os experimentos realizados até o momento, a *Libus Prime Theory* pode ser resumida da seguinte maneira:

### Observação experimental

A relação:

**`(15x + 27y) mod 29`**

apresentou **13,51% de correspondências** na sequência cifrada analisada, contra uma linha de base de aproximadamente **3,45%**.

### Interpretação atual

A relação é tratada como uma **possível assinatura estrutural do ciphertext**, e não como uma chave de descriptografia direta.

### Modelo criptográfico investigado

A descriptografia é modelada por uma sequência de estados baseada em:

**primos → φ(primo) → deslocamento módulo 29**

com uma possível regra de interrupção associada ao valor F.

### Resultado da Página 55

A aplicação do modelo produziu resultados parciais, incluindo um **Language Score de 200**, mas não recuperou um plaintext completo e inequívoco.

### Hipótese ainda não demonstrada

A relação entre a assinatura `(15,27)` e a máquina de estados ainda precisa ser demonstrada experimentalmente.

---

# 12. Próxima Etapa: Escala

A próxima etapa lógica é abandonar a dependência exclusiva da Página 55 e aplicar o mesmo motor a uma página não resolvida significativamente maior.

O objetivo não será simplesmente procurar uma sequência que "pareça inglês".

O objetivo será verificar se as mesmas propriedades estruturais sobrevivem quando o número de observações aumenta.

O experimento deverá procurar:

**1. Persistência da assinatura `(15,27)`**

A relação continua apresentando excesso de correspondências?

**2. Persistência entre páginas**

A mesma relação aparece em outras páginas não resolvidas?

**3. Sincronia**

As alterações observadas na assinatura coincidem com alterações previstas no estado?

**4. Robustez**

O comportamento permanece quando submetido a controles aleatórios e permutações?

**5. Recuperação**

A máquina de estados produz texto linguisticamente consistente sem depender de otimização excessiva do *Language Score*?

---

# 13. Conclusão

A principal modificação introduzida nesta versão da *Libus Prime Theory* não elimina a descoberta original.

Ela redefine sua função dentro do modelo.

A expressão:

**`(15x + 27y) mod 29`**

não deve mais ser tratada como uma chave direta de descriptografia.

Os experimentos realizados indicam que ela possui uma frequência de correspondência elevada dentro da sequência cifrada analisada, tornando plausível a hipótese de que represente uma **assinatura estrutural ou propriedade de recorrência do ciphertext**.

Paralelamente, a teoria mantém a hipótese de uma segunda camada baseada em:

**primos + Função Totiente de Euler + máquina de estados + F-skip**

Essa separação explica por que a descoberta algébrica e a descriptografia direta produziram resultados diferentes.

A Página 55, portanto, não é considerada uma solução completa. Ela funciona como um **ambiente de teste controlado** no qual a assinatura foi inicialmente identificada e a arquitetura da hipótese pôde ser refinada.

O próximo estágio consiste em verificar se essas mesmas propriedades permanecem presentes em uma sequência muito maior.

Se a assinatura, a máquina de estados e a relação entre ambas forem reproduzidas independentemente em outras páginas, a hipótese ganhará uma base experimental significativamente mais forte.

---

**Libus Prime Theory**
*Nink — Libus Prime Analysis Engine v4.0*
*Validação Empírica da Assinatura Estrutural da Cifra do Liber Primus*
