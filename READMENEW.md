# Libus Prime Theory v2.1

## Abordagem de Engenharia Reversa e Criptoanálise do Liber Primus

**Autor:** Nink
**Método:** Libus Prime Analysis Engine
**Foco:** Estrutura matemática, análise posicional e máquinas de estado
**Objetivo:** Investigar se as páginas não resolvidas do *Liber Primus* podem ser descritas por um sistema matemático interno composto por uma assinatura estrutural e uma máquina de estados modular.

---

# 1. Introdução

O *Liber Primus*, associado ao enigma Cicada 3301, apresenta páginas escritas em runas que utilizam a Gematria Primus como sistema de representação numérica.

A proposta da **Libus Prime Theory** parte de uma hipótese diferente da criptoanálise tradicional:

> A sequência de runas pode não ser apenas um texto cifrado linear. A própria estrutura matemática da sequência pode participar do mecanismo de geração da cifra.

Em vez de tratar cada runa apenas como uma letra substituída, a investigação considera simultaneamente:

```text
Runa
 ↓
Valor Gematria
 ↓
Posição
 ↓
Estado
 ↓
Relação com runas vizinhas
 ↓
Transformação modular
```

A teoria atualmente é composta por duas camadas principais:

### Camada 1 — Assinatura Estrutural

Uma relação matemática observável dentro do ciphertext.

### Camada 2 — Máquina de Estados

Um mecanismo dinâmico capaz de produzir os deslocamentos necessários para transformar o ciphertext em plaintext.

A hipótese central é que essas duas camadas podem estar relacionadas, mas **não necessariamente executam a mesma função**.

---

# 2. Camada 1 — A Assinatura Estrutural

A primeira descoberta importante surgiu da análise das transições entre valores da Gematria Primus.

Para cada posição, foram considerados três valores:

```text
x = valor da runa anterior
y = valor da runa atual
z = valor da próxima runa
```

O motor procurou funções da forma:

```math
z = f(x,y) \pmod{29}
```

entre todas as combinações lineares possíveis dentro do módulo 29.

---

# 3. A Anomalia 15x + 27y

A função que apresentou o maior número de correspondências na análise da Página 55 foi:

```math
\boxed{z=(15x+27y)\mod29}
```

O resultado observado foi:

```text
Ciphertext → 13,51%
Baseline   → ≈3,45%
```

A relação apresentou, portanto, aproximadamente quatro vezes a frequência esperada para uma previsão aleatória de um valor entre 29 possibilidades.

Esse resultado foi o ponto de partida para a segunda etapa da investigação.

---

# 4. O Que a Assinatura Significa

Uma das primeiras interpretações seria:

```text
15x + 27y
       ↓
próxima runa
```

e, consequentemente, tentar utilizar a fórmula diretamente como mecanismo de descriptografia.

Os experimentos mostraram que essa abordagem não produziu plaintext coerente.

Isso levou a uma mudança conceitual importante.

A função não precisa ser a chave.

Ela pode ser uma **assinatura estrutural do processo que produziu o ciphertext**.

O modelo passa então a ser:

```text
PLAINtext
    ↓
Máquina criptográfica
    ↓
Ciphertext
    ↓
┌───────────────────────┐
│ assinatura estrutural │
│ (15x + 27y) mod 29    │
└───────────────────────┘
```

Nesse modelo, a equação descreve uma propriedade do resultado final, mas não necessariamente a transformação inversa.

---

# 5. Teste C × P × K

Para investigar essa possibilidade, a relação foi comparada entre diferentes componentes do sistema:

```text
C = Ciphertext
P = Plaintext
K = Key
```

Os resultados observados foram:

```text
Ciphertext → 13,51%
Plaintext   →  2,70%
Key         →  1,35%
```

A concentração da relação no ciphertext é compatível com a interpretação de que:

```text
15x + 27y
```

não representa simplesmente uma propriedade do idioma ou da chave.

Ela parece estar mais fortemente associada à **estrutura do texto cifrado**.

### Importante

Esse resultado sustenta a hipótese de uma assinatura estrutural, mas sozinho não demonstra qual algoritmo produziu essa assinatura.

Portanto, a teoria não precisa assumir que o mecanismo seja especificamente um LFSR.

A hipótese mais geral é:

> **O ciphertext pode possuir uma dinâmica de geração de estados cuja assinatura observável é aproximada por `(15x + 27y) mod 29`.**

Um LFSR seria apenas uma das possíveis implementações desse comportamento.

---

# 6. A Máquina de Estados

A segunda camada surgiu quando a investigação voltou à relação entre:

```text
PRIMES
TOTIENT
MOD 29
```

A ideia é que a chave não seja uma sequência fixa.

Em vez disso, existe um **estado interno** que determina qual elemento da sequência matemática deve ser utilizado em cada posição.

Definimos:

```text
s_i = estado da máquina na posição i
```

e:

```text
p_i = número primo utilizado no estado i
```

Como os primos são coprimos com eles mesmos:

```math
\phi(p_i)=p_i-1
```

O deslocamento associado ao estado pode então ser definido como:

```math
k_i=\phi(p_i)\mod29
```

e, portanto:

```math
\boxed{k_i=(p_i-1)\mod29}
```

---

# 7. A Máquina Não é Apenas uma Sequência

O ponto mais importante da teoria é que:

```text
p0, p1, p2, p3, ...
```

não precisa ser consumida obrigatoriamente uma vez por caractere.

Existe uma variável de estado:

```text
s_i
```

que determina qual primo será utilizado.

Podemos representar:

```math
p_i=P(s_i)
```

onde `P` é a sequência dos números primos.

O estado seguinte é determinado por uma função:

```math
s_{i+1}=G(s_i,P_i,C_i)
```

Essa formulação permite incorporar o comportamento do **F-skip**.

---

# 8. Regra do F-Skip

A regra proposta para o mecanismo é:

Se o resultado decifrado na posição atual corresponde ao valor da runa `F`, o contador da sequência de primos não avança.

Matematicamente:

```math
s_{i+1}=
\begin{cases}
s_i, & \text{se } P_i=F\\
s_i+1, & \text{caso contrário}
\end{cases}
```

Essa é uma característica extremamente importante.

A chave deixa de ser:

```text
K0 K1 K2 K3 K4 K5...
```

e passa a ser:

```text
K0 K1 K2 K2 K3 K4 K4 K5...
```

dependendo dos estados produzidos durante a própria descriptografia.

Isso cria uma **realimentação condicional**.

---

# 9. O Problema da Circularidade

A máquina possui uma característica interessante:

Para descobrir o plaintext:

```text
C_i - k_i
```

precisamos saber `k_i`.

Mas para saber qual será o próximo `k_i`, precisamos saber se:

```text
P_i = F
```

Portanto:

```text
Ciphertext
    ↓
estado atual
    ↓
primo
    ↓
φ(primo)
    ↓
plaintext candidato
    ↓
P_i = F ?
   ↙     ↘
 SIM     NÃO
  ↓        ↓
mantém    avança
estado    estado
```

Isso transforma o problema em uma **máquina de estados dependente da própria saída**.

Essa característica explica por que ataques que assumem uma chave linear simples podem falhar mesmo quando a matemática utilizada na chave é relativamente simples.

---

# 10. O Novo Papel da Assinatura 15x + 27y

A partir daqui surge uma hipótese mais específica.

Em vez de usar:

```text
15x + 27y
```

como chave de descriptografia, podemos tratá-la como um possível **observador do estado da máquina**.

Definimos:

```math
A_i=(15C_{i-1}+27C_i)\mod29
```

e comparamos `A_i` com:

```text
estado atual
estado anterior
próximo estado
```

A pergunta passa a ser:

> A assinatura 15/27 consegue identificar onde a máquina muda de estado?

Essa é uma hipótese nova e testável.

---

# 11. A Hipótese do Detector de Estado

Se a assinatura estiver relacionada à máquina, podemos procurar:

```text
A_i
 ↓
15C_{i-1}+27C_i mod29
```

e marcar todas as posições onde ocorre uma correspondência com a próxima runa.

Depois, essas posições são comparadas com:

```text
F-SKIP
mudança de primo
mudança de estado
limites de palavras
```

O objetivo é verificar se existe uma correlação:

```text
Assinatura
     ↓
mudança estatística
     ↓
mudança de estado
```

Caso a relação apareça de forma consistente, a função deixa de ser apenas uma curiosidade estatística e passa a possuir uma possível função operacional dentro do modelo.

---

# 12. Modelo Matemático Unificado

A teoria pode agora ser representada por três objetos:

### Ciphertext

```math
C_i\in\mathbb{Z}_{29}
```

### Estado

```math
s_i\in\mathbb{N}
```

### Chave dinâmica

```math
k_i=\phi(p_{s_i})\mod29
```

A descriptografia candidata seria:

```math
P_i=(C_i-k_i)\mod29
```

e a atualização do estado:

```math
s_{i+1}=
\begin{cases}
s_i, & P_i=F\\
s_i+1, & P_i\neq F
\end{cases}
```

Enquanto isso, a assinatura estrutural seria:

```math
A_i=(15C_{i-1}+27C_i)\mod29
```

O sistema completo passa então a ser:

```text
                 LIBUS PRIME THEORY v2.1

                         │
                         ▼
                   CIPHERTEXT
                         │
             ┌───────────┴───────────┐
             │                       │
             ▼                       ▼
      ASSINATURA                  ESTADO
       ESTRUTURAL               DA MÁQUINA
             │                       │
             │                 número primo
             │                       │
             │                  φ(primo)
             │                       │
             │                       ▼
             │                 deslocamento
             │                       │
             │                       ▼
             │                 plaintext
             │                       │
             │                       ▼
             │                    F-SKIP
             │                       │
             └───────────┬───────────┘
                         ▼
                  NOVO ESTADO
```

---

# 13. O Que Mudou em Relação à Teoria Original

A versão inicial tentava encontrar:

```text
uma fórmula
      ↓
uma chave
      ↓
plaintext
```

A versão 2.1 propõe algo diferente:

```text
estrutura
   +
estado
   +
chave dinâmica
   +
regra de transição
   ↓
sistema criptográfico
```

Isso é uma mudança importante.

Não estamos mais procurando apenas um número mágico.

Estamos tentando reconstruir **uma máquina**.

---

# 14. A Hipótese da Assinatura

A teoria passa a considerar três possibilidades para `15x + 27y`:

### Hipótese A — Assinatura de geração

A equação surge como consequência do mecanismo que gerou o ciphertext.

### Hipótese B — Detector de estado

A equação identifica regiões ou posições relacionadas às mudanças da máquina.

### Hipótese C — Componente criptográfico

A equação participa diretamente da geração da chave ou do deslocamento.

A investigação não deve escolher uma dessas possibilidades antecipadamente.

O próximo motor deverá testá-las separadamente.

---

# 15. Teste de Independência

Existe um teste particularmente importante para diferenciar uma descoberta real de uma coincidência.

Depois de encontrar:

```math
15x+27y
```

não devemos apenas verificar novamente a mesma página.

Devemos aplicar exatamente a mesma função em:

```text
outras páginas
outras regiões
sequências embaralhadas
sequências aleatórias
```

e comparar os resultados.

Se a frequência de correspondência permanecer significativamente maior nas páginas reais do que nos controles aleatórios, a hipótese estrutural ganha suporte.

Se desaparecer nos controles e também em outras páginas, a hipótese perde força.

---

# 16. Teste de Sincronia

O experimento mais importante da próxima etapa será verificar se a assinatura e a máquina estão sincronizadas.

Para cada posição `i`, registrar:

```text
i
C_i
C_{i-1}
A_i
p_i
φ(p_i)
estado s_i
P_i
F-skip?
```

Isso produzirá uma tabela semelhante a:

```text
i | C | A | primo | φ(p) | estado | P | skip
------------------------------------------------
0 |   |   |       |      |        |   |
1 |   |   |       |      |        |   |
2 |   |   |       |      |        |   |
...
```

Essa tabela permitirá procurar uma relação que não é visível olhando apenas para o score final.

---

# 17. Teste da Hipótese Central

A principal previsão da Libus Prime Theory v2.1 passa a ser:

> **Se `(15x + 27y) mod 29` for uma assinatura estrutural real do mecanismo, sua distribuição deverá apresentar alguma relação reproduzível com os estados da máquina de primos e totiente.**

Isso produz uma previsão concreta.

Não basta encontrar:

```text
13,51%
```

uma vez.

É necessário descobrir se:

```text
assinatura
     ↕
estado
```

apresenta correlação em diferentes conjuntos de dados.

Essa é uma previsão falsificável.

---

# 18. O Papel da Geometria

A antiga hipótese do MDC continua registrada, mas passa a ocupar uma posição diferente no modelo.

Os testes matriciais mostraram uma densidade de coprimalidade próxima à esperada para estruturas aleatórias.

Isso enfraquece a hipótese de que:

```text
MDC = chave
```

Mas não elimina completamente a possibilidade de que a geometria tenha outra função.

A geometria pode, por exemplo, atuar como:

```text
organização
        ↓
ordenação
        ↓
seleção de sequência
        ↓
estado inicial
```

Portanto, em vez de procurar um número secreto escondido no MDC, a investigação pode procurar uma **regra de ordenação ou sincronização**.

---

# 19. Uma Nova Pergunta: Qual é o Estado Inicial?

A máquina proposta possui um problema ainda não resolvido:

```text
s_0 = ?
```

Se o primeiro primo utilizado for conhecido, a sequência pode ser iniciada.

Mas se o estado inicial for desconhecido, diferentes valores de `s_0` podem produzir diferentes descriptografias.

Portanto, uma nova variável deve ser introduzida:

```math
s_0\in\{0,1,2,\ldots\}
```

O objetivo não deve ser escolher o `s_0` que simplesmente produz o maior score.

Deve-se procurar um estado inicial que:

1. produza plaintext coerente;
2. mantenha a regra do F-skip;
3. mantenha a mesma lógica em outras regiões;
4. não dependa de ajustes manuais;
5. seja compatível com a assinatura estrutural.

---

# 20. O Problema da Amostra Curta

A Página 55 contém apenas uma quantidade limitada de símbolos.

Isso cria um problema importante.

Uma máquina com:

```text
estado inicial desconhecido
+
sequência de primos
+
F-skip
+
transformação modular
```

pode produzir vários candidatos plausíveis em uma amostra curta.

Por isso:

```text
score alto
```

não é suficiente.

O verdadeiro objetivo passa a ser:

```text
solução
     =
coerência
+
reprodutibilidade
+
estabilidade
+
previsibilidade
```

---

# 21. O Teste Definitivo da Teoria

A teoria poderá ser submetida a um teste muito mais forte:

### Etapa 1

Determinar os parâmetros utilizando uma página ou região.

### Etapa 2

Congelar todos os parâmetros.

### Etapa 3

Aplicar a mesma máquina a uma segunda região.

### Etapa 4

Não modificar:

```text
primos
φ
F-skip
estado inicial
15/27
```

### Etapa 5

Comparar os resultados.

Se uma regra encontrada em uma região funcionar novamente sem reajuste, isso será muito mais informativo do que qualquer score isolado.

---

# 22. O Que a Teoria Afirma Atualmente

A Libus Prime Theory v2.1 não precisa afirmar:

> “A cifra foi quebrada.”

Ela pode fazer uma afirmação mais precisa:

> **Existe uma hipótese experimental segundo a qual o ciphertext do Liber Primus apresenta uma assinatura posicional detectável em módulo 29, enquanto o mecanismo de transformação pode ser modelado como uma máquina de estados baseada em primos, função totiente e transições condicionais.**

O papel exato da assinatura `15x + 27y` continua sendo uma questão experimental.

---

# 23. Estado Atual do Modelo

```text
                LIBUS PRIME THEORY v2.1
                         │
                         ▼
                 GEMATRIA PRIMUS
                         │
                         ▼
                     MOD 29
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
       ASSINATURA                 ESTADO
       15x + 27y                s_i
             │                       │
             │                       ▼
             │                    primo
             │                       │
             │                       ▼
             │                  φ(primo)
             │                       │
             │                       ▼
             │                 deslocamento
             │                       │
             │                       ▼
             │                  plaintext
             │                       │
             │                       ▼
             │                    F-SKIP
             │                       │
             └───────────┬───────────┘
                         ▼
                  NOVO ESTADO
```

---

# 24. Próximos Experimentos

A próxima versão do **Libus Prime Analysis Engine** deverá priorizar:

### 1. Reconstrução da máquina

Implementar formalmente:

```math
k_i=\phi(p_{s_i})\mod29
```

e:

```math
s_{i+1}=G(s_i,P_i)
```

---

### 2. Detector 15/27

Calcular:

```math
A_i=(15C_{i-1}+27C_i)\mod29
```

para todas as posições.

---

### 3. Correlação com o estado

Comparar `A_i` com:

```text
s_i
p_i
φ(p_i)
P_i
F-skip
```

---

### 4. Busca do estado inicial

Testar diferentes `s_0`, mas validar por coerência e generalização, não apenas por score.

---

### 5. Controle aleatório

Executar exatamente o mesmo algoritmo em:

```text
ciphertext real
shuffle das runas
sequências aleatórias
```

para medir a frequência de falsos positivos.

---

### 6. Validação cruzada

Descobrir parâmetros em uma região e testar em outra sem reajuste.

---

# 25. Conclusão

A evolução da Libus Prime Theory pode ser resumida em uma mudança fundamental:

```text
ANTES

"Qual é a chave?"

↓

AGORA

"Qual é a máquina que produz e atualiza a chave?"
```

A função:

```math
\boxed{(15x+27y)\mod29}
```

é tratada como uma possível **assinatura estrutural**, enquanto:

```math
\boxed{k_i=\phi(p_{s_i})\mod29}
```

representa a hipótese de **chave dinâmica**.

A regra:

```math
P_i=F \Rightarrow s_{i+1}=s_i
```

introduz a realimentação necessária para transformar a sequência de primos em uma máquina de estados.

O modelo completo passa a ser:

```text
CIPHERTEXT
    ↓
assinatura estrutural
    ↓
estado atual
    ↓
primo
    ↓
totiente
    ↓
deslocamento
    ↓
plaintext
    ↓
regra de transição
    ↓
novo estado
    ↺
```

O próximo objetivo da investigação não é maximizar um score.

É descobrir se essas duas camadas realmente **convergem para a mesma máquina matemática**.

Se a assinatura `15x + 27y` puder ser relacionada de maneira reproduzível aos estados da sequência de primos e da função totiente, a hipótese ganhará uma previsão concreta e testável.

Se essa relação não existir, a função deverá ser reinterpretada ou abandonada.

Esse é o próximo teste decisivo da **Libus Prime Theory v2.1**.
