# libus-prime-theory
# Abordagem de Engenharia Reversa e Criptoanálise do Liber Primus (Cicada 3301)

### Proposta de um Sistema de Duas Camadas: Funções Posicionais Não-Lineares e Invariantes Geométricos por MDC

*Autor: Nink*

---

# 1. Introdução e Premissas Fundamentais

O Liber Primus, associado ao enigma da Cicada 3301 de 2014, permanece parcialmente não resolvido. O conjunto LP2 possui 58 páginas, das quais 56 continuam sem uma solução aceita pela comunidade. As páginas que já foram decifradas apresentam diferentes mecanismos criptográficos, incluindo variantes de Vigenère, substituições e transformações baseadas em números primos e na função totiente de Euler.

A presente investigação propõe uma mudança de perspectiva na análise do livro.

Grande parte das abordagens trata a *Gematria Primus* como uma tabela fixa de correspondência entre runas e valores numéricos e as páginas cifradas principalmente como sequências lineares de símbolos.

Esta proposta investiga a possibilidade de que o Liber Primus possua uma estrutura matemática mais profunda, na qual a própria organização das runas, seus valores e a geometria das páginas possam participar do mecanismo criptográfico.

A hipótese parte da máxima associada à Cicada 3301:

> *"Tudo o que você precisa está dentro deste livro."*

A proposta investiga duas camadas matemáticas potencialmente interligadas:

1. *Uma Camada Estrutural/Geométrica:* na qual as páginas podem ser representadas como matrizes numéricas, permitindo a busca de invariantes derivados de suas propriedades aritméticas e espaciais.

2. *Uma Camada Posicional:* na qual os valores e relações da Gematria Primus podem apresentar uma regra dependente da posição, composição ou ordenação dos caracteres, em vez de serem interpretados somente como uma tabela estática.

A hipótese central é que essas duas camadas possam produzir informações complementares sobre a transformação criptográfica utilizada nas páginas ainda não resolvidas.

---

# 2. Teoria 1 — A Engrenagem do MDC Universal

A primeira teoria propõe que parte da informação necessária para determinar a transformação criptográfica possa estar contida na própria estrutura matemática das páginas.

Em vez de procurar inicialmente uma chave externa, a proposta é investigar se a página cifrada contém *invariantes aritméticos capazes de indicar sua própria transformação*.

## 2.1 O Mecanismo de Análise Matricial

O Liber Primus apresenta páginas cuja organização visual pode assumir estruturas diferentes de um texto linear convencional.

Quando as runas são convertidas para seus respectivos valores da Gematria Primus, essas estruturas podem ser representadas como conjuntos ou *matrizes algébricas discretas*.

A partir dessa representação, propõe-se investigar sistematicamente:

* *MDC de vetores lineares:* MDC entre elementos pertencentes à mesma linha ou coluna;
* *MDC inter-blocos:* MDC entre somas ou resultados obtidos de blocos adjacentes;
* *Diferenças entre elementos:* variações numéricas nas direções horizontal, vertical e diagonal;
* *Relações de coprimalidade:* regiões onde diferentes elementos apresentam MDC igual a 1;
* *Padrões diagonais e geométricos:* relações que possam depender da posição dos valores dentro da página;
* *Relações modulares:* resíduos obtidos pela redução dos valores em módulo 29.

O objetivo não é assumir que o MDC seja necessariamente a chave, mas verificar se ele funciona como um *operador capaz de revelar uma estrutura recorrente*.

## 2.2 O Objetivo Estrutural

O MDC seria utilizado como uma possível *engrenagem de redução e filtragem matemática*.

Caso a disposição dos valores das páginas tenha sido construída de maneira deliberada, operações de divisibilidade, diferenças e modularidade poderiam produzir números ou relações que se repetem entre regiões diferentes da página ou entre páginas distintas.

Esses resultados seriam candidatos a *invariantes matemáticos*.

Se um determinado invariante demonstrar uma relação consistente com os deslocamentos necessários para decifrar diferentes páginas, ele poderia fornecer uma pista sobre o mecanismo de geração ou seleção da chave.

A hipótese estrutural, portanto, é:

> *A geometria numérica de uma página pode conter informações capazes de indicar como seus símbolos devem ser reorganizados ou transformados.*

---

# 3. Teoria 2 — A Função Algébrica de Posição: O Peso Dinâmico das Letras

A segunda teoria investiga a própria construção e organização da *Gematria Primus*.

Se existe uma estrutura matemática interna no Liber Primus, é possível que as relações entre as runas também apresentem propriedades que possam ser exploradas para descobrir essa estrutura.

A hipótese não afirma inicialmente que a tabela da Gematria seja incorreta ou que seus valores devam ser substituídos.

Ela propõe testar se *relações entre os valores das runas podem ser descritas por uma função dependente de posição, composição ou ordenação*.

---

## 3.1 Isolamento e Mapeamento das Relações Rúnicas

Para testar essa possibilidade, são analisadas runas compostas e relações entre caracteres que apresentam inversões ou rearranjos.

Alguns exemplos observados são:

### Par 1 — EA / AE

$$
EA=109
$$

$$
AE=101
$$

Logo:

$$
109-101=\mathbf{8}
$$

### Par 2 — OE / EO

$$
OE=83
$$

$$
EO=41
$$

Logo:

$$
83-41=\mathbf{42}
$$

### Par 3 — Relação adicional

Outro conjunto analisado produz:

$$
107-79=\mathbf{28}
$$

resultando no conjunto de diferenças:

$$
\mathbf{8,\ 42,\ 28}
$$

Essas diferenças não permanecem constantes entre os casos analisados.

Isso torna pouco provável, dentro dessa amostra, que uma simples regra do tipo:

$$
X-Y=C
$$

com uma constante universal \(C\), seja suficiente para descrever todas as relações observadas.

A hipótese passa então a considerar a possibilidade de um *peso posicional ou dinâmico*, no qual a posição e/ou composição dos caracteres influencia o valor produzido.

---

# 3.2 O Mecanismo do Peso Não-Linear

Para representar matematicamente essa possibilidade, propõe-se uma função genérica de acoplamento:

$$
f(x,y)=X(x)\cdot x+Y(y)\cdot y
$$

onde \(X(x)\) e \(Y(y)\) não precisam ser constantes fixas.

Esses coeficientes poderiam depender de fatores como:

* posição do caractere;
* posição da runa no alfabeto;
* composição da runa;
* ordem dos caracteres;
* ou alguma sequência matemática subjacente.

A função acima não é apresentada como a fórmula definitiva da Gematria Primus.

Ela funciona como um *modelo experimental* para testar se as relações observadas podem ser descritas por uma regra posicional.

---

# 4. Teste Prático Realimentado — Cruzamento das Teorias e a Conexão Fibonacci

O ponto central da proposta é cruzar as duas teorias.

As diferenças encontradas na análise posicional:

$$
8,\quad42,\quad28
$$

são submetidas à operação modular definida pela estrutura do alfabeto rúnico.

Como a Gematria Primus utiliza 29 posições, aplica-se:

$$
\bmod 29
$$

aos valores obtidos.

### Caso 1

$$
8\bmod29=\mathbf{8}
$$

### Caso 2

$$
42\bmod29=\mathbf{13}
$$

### Caso 3

$$
28\bmod29=\mathbf{28}
$$

O resultado é:

$$
\mathbf{8,\ 13,\ 28}
$$

---

# 4.1 A Observação de Fibonacci

Os valores:

$$
8\quad\text{e}\quad13
$$

são termos consecutivos da sequência de Fibonacci:

$$
\dots,3,5,\mathbf{8},\mathbf{13},21,34,\dots
$$

Essa ocorrência é particularmente interessante porque Fibonacci constitui uma das estruturas matemáticas que podem ser investigadas no contexto do Liber Primus.

Entretanto, nesta etapa, o resultado deve ser tratado como *uma pista estatística e uma hipótese de trabalho*, e não como prova de que Fibonacci governa a Gematria.

A observação permite formular uma hipótese mais específica:

> *Talvez determinadas relações posicionais das runas sejam produzidas ou moduladas por uma progressão recorrente, possivelmente relacionada à sequência de Fibonacci.*

Essa hipótese pode então ser testada sobre uma quantidade muito maior de relações rúnicas.

Se o mesmo comportamento aparecer repetidamente em pares e estruturas que não foram utilizados para formular a hipótese, sua relevância matemática aumentará.

---

# 4.2 Da Relação Posicional à Função de Transição

A partir dessa possibilidade, o modelo pode evoluir de uma função estática para uma *função de transição recorrente*.

Em vez de assumir imediatamente uma fórmula específica, a investigação pode testar estruturas como:

$$
x_{n+1}=F(x_n,x_{n-1})
$$

ou representações matriciais do tipo:

$$
\mathbf{x}_{n+1}=M\mathbf{x}_n
$$

incluindo sequências relacionadas a Fibonacci entre os candidatos.

A ideia fundamental permanece:

> *A posição de um caractere pode determinar ou modificar seu peso dentro de uma estrutura matemática recorrente.*

---

# 5. Cruzamento das Duas Teorias — Modelo de Sistema Unificado

As duas teorias podem então ser reunidas em um único modelo de engenharia reversa:

text
┌───────────────────────────────────────────────────────────────┐
│              CAMADA 1 — FUNÇÃO POSICIONAL                     │
│                                                               │
│  Relações entre runas → Pesos posicionais → Padrões recorrentes│
│                                      │                        │
│                                      ▼                        │
│                       Valores / diferenças                    │
└───────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌───────────────────────────────────────────────────────────────┐
│              CAMADA 2 — ESTRUTURA GEOMÉTRICA                  │
│                                                               │
│  Página → Matriz numérica → MDC + módulo 29 + relações locais │
│                                      │                        │
│                                      ▼                        │
│                         Invariantes                           │
└───────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌───────────────────────────────────────────────────────────────┐
│                    POSSÍVEL RESULTADO                         │
│                                                               │
│             Vetor de deslocamento / transformação              │
│                   / possível chave estrutural                 │
└───────────────────────────────────────────────────────────────┘


Nesse modelo, a primeira camada investiga a possibilidade de uma *lei posicional interna* para as relações entre as runas.

A segunda camada investiga se a *organização geométrica dos valores na página* produz invariantes matemáticos.

A hipótese final é que essas duas camadas possam alimentar-se mutuamente:

$$
\boxed{
\text{Relações Rúnicas}
\rightarrow
\text{Função Posicional}
\rightarrow
\text{Estrutura da Página}
\rightarrow
\text{Invariantes}
\rightarrow
\text{Transformação Criptográfica}
}
$$

Nesse cenário, a função posicional poderia fornecer informações sobre a estrutura dos valores rúnicos, enquanto a geometria das páginas poderia atuar como mecanismo de filtragem ou validação dessas relações.

O objetivo seria verificar se ambas convergem para os mesmos parâmetros de transformação.

---

# 6. Veredito da Engenharia Reversa e Próximos Passos

A presente proposta *não afirma ter quebrado a cifra do *Liber Primus**.

Ela apresenta uma hipótese de engenharia reversa baseada na possibilidade de que exista uma relação entre:

$$
\boxed{
\text{Gematria}
\leftrightarrow
\text{Posição}
\leftrightarrow
\text{Geometria}
\leftrightarrow
\text{Aritmética Modular}
}
$$

Os resultados iniciais que motivam a investigação incluem:

* diferenças posicionais como \(8\), \(42\) e \(28\);
* redução dessas diferenças em módulo 29;
* surgimento de \(8\) e \(13\);
* relação desses valores com termos consecutivos de Fibonacci;
* possibilidade de invariantes derivados da estrutura geométrica das páginas;
* possibilidade de utilização do MDC como operador estrutural.

Nenhum desses elementos, isoladamente, demonstra o mecanismo da cifra.

A força da hipótese deverá ser determinada pela *reprodutibilidade dos padrões em dados independentes* e pela capacidade de produzir previsões verificáveis.

## Próximos passos

### 1. Desenvolvimento de algoritmos automatizados

Implementar rotinas em Python/C++ capazes de representar as páginas como matrizes numéricas e calcular:

* MDC;
* diferenças;
* coprimalidade;
* relações diagonais;
* padrões de vizinhança;
* resíduos módulo 29.

### 2. Teste dos invariantes

Verificar se determinados valores ou estruturas aparecem com frequência significativamente maior do que seria esperado em matrizes aleatórias ou em diferentes permutações dos mesmos dados.

### 3. Teste da hipótese de Fibonacci

Aplicar o mesmo procedimento a um conjunto muito maior de relações rúnicas, verificando se a ocorrência de Fibonacci permanece ou desaparece quando a amostra é ampliada.

### 4. Teste das funções posicionais

Comparar diferentes modelos:

$$
\text{linear}
$$

$$
\text{quadrático}
$$

$$
\text{recorrente}
$$

$$
\text{matricial}
$$

e verificar qual deles, se algum, consegue reproduzir as relações observadas sem depender de ajustes feitos posteriormente.

### 5. Aplicação às páginas não resolvidas

Somente depois de estabelecer uma regra consistente nos dados conhecidos, aplicar os mesmos algoritmos às páginas ainda não resolvidas.

O objetivo final é encontrar uma transformação que não apenas produza uma saída aparentemente legível, mas que seja:

$$
\boxed{
\text{reproduzível}
+
\text{consistente}
+
\text{matematicamente justificável}
}
$$

Se as duas camadas convergirem repetidamente para os mesmos parâmetros de transformação, isso constituirá uma evidência muito mais forte de que a estrutura matemática proposta possui relação real com o mecanismo criptográfico do Liber Primus.
