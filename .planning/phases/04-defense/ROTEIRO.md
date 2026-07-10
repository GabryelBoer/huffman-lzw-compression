# Roteiro de Apresentação — Defesa Oral (15 min)

**Fonte:** `slides/slides.tex` (10 frames) + `article/artigo.tex` (números exatos).
**Regra de ouro:** frases curtas, olhar para a banca, avançar no tempo. Ninguém lê o slide em voz alta — o slide apoia, quem fala é você.

## Mapa de timing

| Slide | Título | Duração | Acumulado |
|-------|--------|---------|-----------|
| 1 | Capa / Grupo | 2:00 | 2:00 |
| 2 | O Problema (1/2) | 1:30 | 3:30 |
| 3 | O Problema (2/2) — questões de pesquisa | 1:30 | **5:00 ✔ CHECKPOINT 1** |
| 4 | Trabalhos Relacionados | 1:00 | 6:00 |
| 5 | Algoritmo de Huffman | 1:30 | 7:30 |
| 6 | Algoritmo LZW | 1:30 | 9:00 |
| 7 | Resultados — Taxa de compressão | 1:30 | **10:30 ✔ CHECKPOINT 2 (aos 10:00 devem estar iniciando o slide 7)** |
| 8 | Resultados — Tempo | 1:00 | 11:30 |
| 9 | Resultados — Memória | 1:30 | **13:00 ✔ CHECKPOINT 3 (aos 13:00 devem estar iniciando o slide 10)** |
| 10 | Conclusões + convite a perguntas | 1:30–2:00 | 14:30–15:00 |

**Checkpoints (cronometrista do grupo confere no relógio):**
- **5 min:** terminando o Slide 3. Atrasado? Cortar detalhes do Slide 4 (falar só Shannon → Huffman → LZ → Welch em uma frase).
- **10 min:** iniciando o Slide 7. Atrasado? Nos slides 8 e 9, falar apenas a mensagem central de cada um (1 frase por gráfico).
- **13 min:** iniciando o Slide 10. Atrasado? Ir direto ao fechamento: "sem vencedor absoluto" + contribuição inédita + convite a perguntas.

---

## Slide 1 — Capa / Grupo (2:00) — ABERTURA

**Mensagem central:** somos o grupo X, comparamos Huffman e LZW em código-fonte e trazemos uma contribuição inédita mensurável.

**Falar (quem somos → o que fizemos → qual a contribuição):**
- "Bom dia/boa tarde. Somos [nomes e matrículas]. Nosso trabalho compara os algoritmos de Huffman e LZW na compressão lossless de código-fonte."
- "Implementamos os dois algoritmos do zero em Python, construímos um benchmark reproduzível com 12 experimentos e validamos a integridade lossless com SHA-256 em todos eles."
- "Nossa contribuição inédita: um framework que correlaciona entropia de Shannon e repetição lexical com o desempenho relativo — ele explica POR QUE cada algoritmo vence em cada tipo de arquivo."
- "Todo o código, dados e scripts estão públicos neste repositório GitHub" (apontar a URL no slide).

**Transição:** "Primeiro, por que comprimir código-fonte é um problema relevante?"

---

## Slide 2 — O Problema: por que comprimir código-fonte? (1:30)

**Mensagem central:** o volume de código armazenado cresce rápido e cada ponto percentual de compressão vira economia real.

**Apoios:**
- Plataformas de hospedagem mantêm centenas de milhões de repositórios.
- Backups incrementais, CI/CD e monorepos multiplicam cópias do mesmo conteúdo.
- Cada ponto percentual de redução economiza armazenamento, banda e tempo de transferência.
- Nosso estudo de caso: compressão lossless para armazenamento e versionamento de repositórios.

**Transição:** "Mas código-fonte não é texto comum — ele tem uma dualidade que torna a comparação interessante."

---

## Slide 3 — O Problema: dualidade do código-fonte (1:30) → CHECKPOINT 5 min

**Mensagem central:** código-fonte tem DOIS tipos de redundância — estatística (bytes) e de subsequências (tokens) — e cada algoritmo explora um deles.

**Apoios:**
- Distribuição de bytes desigual: espaços, chaves, aspas, palavras reservadas.
- Tokens repetidos (`def`, `import`, `return`) e indentação sistemática.
- Huffman explora a desigualdade de frequências; LZW explora a repetição de subsequências.
- Quatro questões de pesquisa (ler as duas primeiras, resumir as demais): qual algoritmo vence em cada perfil; qual gasta menos memória e tempo; como entropia e repetição lexical se correlacionam com o resultado; em quais critérios do enunciado cada método é mais efetivo.

**Transição:** "Essas questões se apoiam em 70 anos de teoria — vejamos rapidamente."

---

## Slide 4 — Trabalhos Relacionados (1:00)

**Mensagem central:** os dois algoritmos representam as duas linhagens históricas da compressão sem perdas — e nenhum trabalho anterior fez a correlação que fazemos.

**Apoios (não ler tudo — narrar a linha do tempo):**
- Shannon (1948) define a entropia como limite inferior de bits por símbolo; Huffman (1952) é o clássico da vertente estatística.
- Ziv e Lempel (1977/78) criam a compressão por dicionário; Welch (1984) simplifica no LZW.
- Trabalhos recentes (Nambiar 2025; Shrividhiya 2021) comparam ou combinam os dois, mas em outros domínios.
- **Diferencial nosso:** nenhuma referência consultada aplica simultaneamente entropia de Shannon + repetição lexical + validação SHA-256 em conjunto heterogêneo .py/.c/log.

**Transição:** "Como funciona cada algoritmo? Começando pelo Huffman."

---

## Slide 5 — Algoritmo de Huffman (1:30)

**Mensagem central:** Huffman dá códigos curtos a símbolos frequentes, usando min-heap e árvore binária construída de baixo para cima.

**Apoios:**
- Conta frequências, insere no min-heap, combina os dois menores pesos até restar a raiz. Esquerda = 0, direita = 1.
- Complexidade: O(n log n) para a árvore (n ≤ 256 símbolos de byte) + O(m) para codificar o arquivo de m bytes.
- Precisa transmitir a tabela de frequências no header — overhead que pesa em arquivos pequenos.
- Forte em distribuição desigual de frequências; fraco em capturar padrões longos repetidos (blocos inteiros).

**Transição:** "O LZW ataca exatamente essa fraqueza."

---

## Slide 6 — Algoritmo LZW (1:30)

**Mensagem central:** LZW substitui subsequências repetidas por referências a um dicionário construído durante a própria leitura — sem transmitir metadados.

**Apoios:**
- Dicionário (tabela hash) inicializado com os 256 bytes; códigos de 16 bits, limite de 4096 entradas na nossa implementação.
- Uma única passada, O(m) amortizado.
- Ponto elegante: o decodificador reconstrói o MESMO dicionário só lendo os códigos — nada de dicionário no arquivo.
- Forte em repetição de subsequências (tokens, linhas de log); fraco em arquivos pequenos ou de alta entropia, onde o overhead dos códigos pode até EXPANDIR o arquivo.

**Transição:** "Teoria posta — o que os 12 experimentos mostraram?"

---

## Slide 7 — Resultados: Taxa de Compressão (1:30) → CHECKPOINT 10 min

**Narrativa (o que o gráfico mostra → por quê → o que concluímos):**
- **O que mostra:** em Python médio, Huffman vence (1.73 vs. 1.66 no `requests_sessions.py`); no arquivo de alta entropia, Huffman comprime 1.28 enquanto o LZW EXPANDE para 0.75. Já no C (`jansson_dump.c`), LZW vira o jogo: 1.90 vs. 1.73. E no log, LZW dispara: 6.76, ou 85.2% de economia.
- **Por quê:** o arquivo de alta entropia tem 6.02 bits de entropia e repetição lexical ZERO — não há padrões para alimentar o dicionário do LZW; Huffman ainda explora a desigualdade residual de frequências. O `jansson_dump.c` tem a MAIOR repetição lexical do conjunto (0.20) — prato cheio para o dicionário. No log, linhas quase idênticas viram subsequências longas referenciadas repetidamente.
- **Concluímos:** o perfil do arquivo (entropia + repetição lexical) PREDIZ o vencedor — essa é exatamente a nossa contribuição.

**Transição:** "E em tempo de execução?"

---

## Slide 8 — Resultados: Tempo de Execução (1:00)

**Narrativa:**
- **O que mostra:** tempos de compressão similares na maioria dos arquivos, apesar da vantagem teórica O(m) do LZW.
- **Por quê:** com n ≤ 256, o log n do Huffman é praticamente constante; a diferença real aparece na DEScompressão.
- **Concluímos:** LZW descomprime ~2.5× mais rápido em arquivos médios (13.4 ms vs. 34.1 ms) — relevante em cenários "comprime uma vez, descomprime muitas".

**Transição:** "O terceiro critério, memória, inverte o placar."

---

## Slide 9 — Resultados: Uso de Memória (1:30) → CHECKPOINT 13 min

**Narrativa:**
- **O que mostra:** Huffman é 5 a 10× mais eficiente em memória — 110 KB contra 871 KB no maior arquivo Python.
- **Por quê:** o custo do LZW é o dicionário adaptativo em memória; o do Huffman é só a árvore + tabela de códigos.
- **Concluímos:** somando ao slide anterior — LZW expande arquivos pequenos (−1.6%) e de alta entropia (−33.6%) — cada algoritmo tem um nicho claro. Não existe vencedor absoluto.

**Transição:** "O que levamos disso tudo?"

---

## Slide 10 — Conclusões (1:30–2:00) — FECHAMENTO

**Mensagem central:** não há vencedor absoluto; o perfil do arquivo decide — e nós criamos a ferramenta que faz essa predição.

**Falar:**
- "Sem vencedor absoluto: Huffman para restrição de memória, alta entropia e arquivos pequenos; LZW para padrões repetitivos e descompressão rápida em arquivos médios."
- "Foram 12 experimentos, todos com integridade lossless validada por SHA-256, mais 14 testes automatizados de round-trip."
- **Contribuição inédita (dizer explicitamente, nomeando-a):** "Nossa contribuição inédita é o **framework de benchmark que correlaciona entropia de Shannon e repetição lexical com o desempenho relativo dos algoritmos** — ele explica por que um método vence em um arquivo e falha em outro, algo que nenhuma das referências consultadas faz em conjunto heterogêneo de Python, C e log."
- "Trabalhos futuros: repositórios completos, integração com Git e variantes adaptativas e híbridas."
- **Convite:** "Código, dados e scripts estão no repositório público. Obrigado — estamos à disposição para perguntas."

---

## Números que NÃO podem sair errados na fala

| Fato | Número exato |
|------|--------------|
| Python médio (requests_sessions.py) | Huffman 1.73 vs. LZW 1.66 |
| C (jansson_dump.c) | LZW 1.90 vs. Huffman 1.73 (rep. lexical 0.20) |
| Alta entropia (6.02 bits) | Huffman 1.28 vs. LZW 0.75 (expansão de 33.6%) |
| Log (access.log) | LZW 6.76, economia 85.2% |
| Arquivo pequeno (1 KB) | LZW expande: −1.6% |
| Memória | Huffman 110 KB vs. LZW 871 KB (5–10×) |
| Descompressão | LZW ~2.5× mais rápido (13.4 ms vs. 34.1 ms) |
| Complexidade | Huffman O(n log n)+O(m); LZW O(m) amortizado |
| Dicionário LZW | 4096 entradas, códigos de 16 bits |
| Validação | SHA-256 em 12/12 experimentos; 14 testes round-trip |
