## 7. Atualização do Projeto: Teste de Estresse e Conclusão Estatística

Conforme proposto na seção de Próximos Passos (Itens 2, 3 e 4), esta tese foi submetida a testes computacionais automatizados para 
avaliar sua reprodutibilidade em escala global.

*   *Resultado do Teste da Função Posicional:* A ampliação da amostra para os demais pares de runas compostas do alfabeto revelou que os
*   resíduos modulares de Fibonacci ($8$ e $13$) ocorrem estritamente nos casos estudados ($AE/EA$ e $OE/EO$). O padrão não se estendeu para as outras permutações, indicando um fenômeno de *Apofenia/Overfitting* (coincidência estatística isolada).
*   *Resultado do Teste do MDC:* O cálculo do MDC aplicado às estruturas matriciais das páginas gerou valores unitários consistentes,
*   devido à natureza estritamente prima dos fatores isolados da Gematria Primus.

### Veredito Final
As hipóteses matemáticas iniciais foram formalmente *refutadas* pelos testes de estresse. Embora o modelo linear-dinâmico não descreva o mecanismo 
criptográfico global do Liber Primus, este repositório permanece ativo como um registro documental de modelagem algébrica de segurança, evidenciando
a importância do rigor metodológico e do descarte de falsos positivos na criptoanálise.


28 9 2026 22:52
---

## 8. Análise Detalhada dos Contraexemplos e Falsos Positivos

Para fins de registro metodológico e mapeamento da estrutura algébrica, foram isolados os fatores de quebra observados nos testes:

### 8.1. Ficha Técnica das Falhas
* **Menor Contraexemplo:** O ponto inicial de quebra ocorre nos compostos ímpares formados por primos $>3$, sendo o menor deles o **25** ($5 \times 5$), seguido por **35** ($5 \times 7$) e **49** ($7 \times 7$).
* **Comportamento por Intervalo:**
  * **1 a 100:** Alta precisão inicial (>80%), devido à baixa densidade de compostos ímpares sem fatores 2 ou 3.
  * **1 a 1.000:** A precisão cai para a faixa de ~60-70% à medida que surgem múltiplos de $5, 7, 11$ e $13$.
  * **1 a 10.000:** A margem de erro aumenta significativamente com a queda da densidade de primos ($\approx 12,2\%$).

### 8.2. Propriedades dos Falsos Positivos
* **Estrutura Modular ($n \pmod 6$):** Todos os falsos positivos pertencem estritamente às formas $6k + 1$ ou $6k - 1$. Isso demonstra que pertencer a $6k \pm 1$ é uma **condição necessária, mas não suficiente** para a primalidade.
* **Fatores Primos Recorrentes:** Os números que ultrapassam o filtro inicial são produtos diretos de primos menores:
  * $25 = 5 \times 5$
  * $35 = 5 \times 7$
  * $49 = 7 \times 7$
  * $77 = 7 \times 11$
  * $91 = 7 \times 13$

### 8.3. Conclusão Algorítmica
O modelo gera **falsos positivos** por capturar a simetria modular dos primos sem cancelar as tabelas de multiplicação geradas por primos subsequentes. O erro cresce de forma assintótica e previsível.
