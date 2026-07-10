# Banco de Q&A Antecipado — Defesa Oral

**Regra:** respostas curtas (2–5 frases), sempre com o número exato do artigo quando aplicável. Nível: responder para um professor de AED-II — precisão técnica sem enrolação.
**Fonte dos números:** `article/artigo.tex` (Tabelas 1–3 e Seção 5).

Total: **22 perguntas** em 5 categorias + protocolo de resposta para pergunta imprevista.

---

## Categoria 1 — Algoritmos (6 perguntas)

**Q1. Como o Huffman constrói a árvore de códigos?**
De baixo para cima, de forma gulosa. Contamos a frequência de cada byte, inserimos cada símbolo em uma fila de prioridade (min-heap) e combinamos iterativamente os dois nós de menor peso em um nó pai, até restar um único nó — a raiz. Os códigos saem do percurso da árvore: esquerda é bit 0, direita é bit 1. Assim símbolos frequentes ficam perto da raiz e recebem códigos curtos.

**Q2. Por que usar min-heap e não uma lista ordenada?**
Porque a operação dominante é extrair os dois menores pesos repetidamente. No heap, extração e inserção custam O(log n); com lista ordenada, manter a ordenação a cada inserção custaria O(n) por operação. Com n ≤ 256 símbolos, o heap dá a construção em O(n log n). Usamos o `heapq` do Python com desempate determinístico para garantir round-trip consistente.

**Q3. Como o LZW reconstrói o dicionário na decodificação sem que ele seja transmitido?**
O decodificador executa a mesma lógica do codificador em espelho: começa com o mesmo dicionário inicial (os 256 bytes) e, a cada código lido, adiciona ao dicionário a entrada que o codificador teria adicionado naquele ponto (sequência anterior + primeiro byte da atual). Como ambos seguem regras determinísticas idênticas, os dicionários evoluem em sincronia. É por isso que o LZW não precisa de metadados extras — vantagem direta sobre o Huffman, que transmite a tabela de frequências no header.

**Q4. Qual é o caso especial do LZW na decodificação e como vocês o trataram?**
É quando o decodificador recebe um código que ainda não existe no seu dicionário — acontece quando o codificador usa uma entrada recém-criada imediatamente (padrão do tipo cScSc). Nesse caso, a sequência é necessariamente a anterior concatenada com o seu próprio primeiro byte, e o decoder a constrói diretamente. Nossa implementação trata esse caso e ele é coberto pelos 14 testes de round-trip.

**Q5. Por que o limite de 4096 entradas no dicionário?**
Para evitar crescimento ilimitado de memória — o dicionário é o custo dominante de espaço do LZW. 4096 = 2^12 entradas é um valor clássico (usado no GIF) que equilibra capacidade de capturar padrões e consumo de memória. Mesmo com esse teto, o LZW chegou a 871 KB de pico contra 110 KB do Huffman no mesmo arquivo — sem o limite, seria pior.

**Q6. Por que códigos de 16 bits, se 4096 entradas cabem em 12 bits?**
Escolha de simplicidade de implementação: 16 bits alinham com 2 bytes exatos, dispensando empacotamento de bits de largura variável na fronteira do LZW. O custo é overhead por código — visível nos arquivos pequenos, onde o LZW expandiu (−1.6% no arquivo de 1 KB). Reconhecemos como trade-off: códigos de largura variável (12 bits crescendo dinamicamente) melhorariam a taxa e seriam uma extensão natural.

---

## Categoria 2 — Complexidade (4 perguntas)

**Q7. De onde vem o O(n log n) do Huffman?**
Da construção da árvore: são até n inserções e 2(n−1) extrações no min-heap, cada uma O(log n), com n limitado a 256 símbolos de byte. A codificação do arquivo em si é O(m), com m o tamanho em bytes. Logo o total é O(n log n) + O(m) — e como n ≤ 256, na prática o termo dominante é o O(m).

**Q8. Por que o LZW é O(m) amortizado e não O(m) estrito?**
Porque cada consulta e inserção no dicionário usa tabela hash, cujo custo é O(1) amortizado — colisões e redimensionamentos podem custar mais em operações individuais, mas o custo médio por byte é constante. Como cada byte do arquivo é processado uma única vez em uma única passada, o total é O(m) amortizado.

**Q9. Qual a complexidade de espaço de cada algoritmo?**
Huffman: árvore + tabela de códigos, ambas O(n) com n ≤ 256, mais o header de frequências no arquivo — espaço praticamente constante e pequeno (20–110 KB de pico nos experimentos). LZW: dominado pelo dicionário em memória, limitado a 4096 entradas, mas cada entrada guarda uma sequência de bytes — na prática, 98 a 871 KB de pico. Essa diferença estrutural explica o Huffman ser 5 a 10× mais econômico em memória.

**Q10. A teoria bateu com a prática nos tempos medidos?**
Parcialmente — e essa é uma das análises do trabalho. O LZW tem vantagem teórica O(m), mas os tempos de COMPRESSÃO foram similares, porque com n ≤ 256 o log n do Huffman é quase constante. A diferença prática relevante apareceu na DEScompressão de arquivos médios: LZW 13.4 ms contra 34.1 ms do Huffman, cerca de 2.5× mais rápido — o decoder Huffman percorre a árvore bit a bit, enquanto o LZW faz lookups diretos de código.

---

## Categoria 3 — Resultados (7 perguntas)

**Q11. Por que o Huffman vence no arquivo de alta entropia?**
O `high_entropy_payload.py` tem entropia de 6.02 bits e repetição lexical zero — distribuição quase uniforme, sem padrões repetidos para alimentar o dicionário do LZW. O Huffman ainda explora a desigualdade residual de frequências e comprime a taxa 1.28. O LZW não só perde: EXPANDE o arquivo para taxa 0.75, ou seja, economia de −33.6%.

**Q12. Por que o LZW expande arquivos pequenos?**
No `encoder_sample.py` (1 KB), o LZW deu taxa 0.98 — expansão de 1.6%. Dois motivos: cada código emitido ocupa 16 bits fixos, e no início o dicionário está "frio" — só contém bytes isolados, então as primeiras emissões trocam 1 byte por 2. Em arquivo pequeno, o dicionário não tem tempo de aquecer e o overhead supera o ganho — exatamente a limitação teórica prevista.

**Q13. Por que o LZW domina no log com 6.76?**
O `access.log` tem linhas quase idênticas: IPs, timestamps e rotas repetem estruturas longas. Essas subsequências entram no dicionário e passam a ser referenciadas por um único código de 16 bits, repetidamente. Resultado: taxa 6.76 com 85.2% de economia, contra 1.89 do Huffman — o contraste mais extremo do benchmark, e o motivo de usarmos o log como baseline de controle fora do domínio de código.

**Q14. Por que o arquivo C favorece o LZW?**
O `jansson_dump.c` tem a maior repetição lexical do conjunto: 0.20 — um em cada cinco tokens é palavra reservada ou padrão recorrente de C. Isso alimenta bem o dicionário, e o LZW alcança 1.90 contra 1.73 do Huffman, além de descomprimir mais rápido (9.0 ms vs. 13.5 ms). O Huffman mantém a vantagem de memória (66 KB vs. 568 KB).

**Q15. Qual algoritmo vocês escolheriam para comprimir código-fonte em geral?**
Depende do perfil e da restrição — essa é a conclusão central. Para Python típico (entropia moderada, repetição lexical baixa, ~0.13), Huffman venceu em taxa (1.73 vs. 1.66) e memória. Para C repetitivo ou logs, LZW. Se a restrição é memória, Huffman sempre; se é velocidade de descompressão em arquivos médios, LZW. Nosso framework de perfil (entropia + repetição lexical) permite fazer essa escolha por arquivo, antes de comprimir.

**Q16. Qual o trade-off de memória entre os dois?**
Huffman usou de 20 a 110 KB de pico; LZW de 98 a 871 KB — diferença de 5 a 10×. A causa é estrutural: o espaço do Huffman é limitado pela árvore de no máximo 256 folhas, enquanto o LZW mantém um dicionário adaptativo com até 4096 sequências em memória. Medimos com `tracemalloc` em todos os 12 experimentos.

**Q17. LZW venceu em descompressão — isso importa na prática?**
Sim, no cenário do estudo de caso: repositórios são comprimidos uma vez e lidos muitas vezes (restores de backup, checkouts, caches de CI). LZW descomprimiu `requests_sessions.py` em 13.4 ms contra 34.1 ms do Huffman — ~2.5× mais rápido. Em pipelines que descomprimem milhares de arquivos, essa diferença acumula.

---

## Categoria 4 — Metodologia (4 perguntas)

**Q18. Por que SHA-256 para validar, e não comparação byte a byte?**
Usamos os dois níveis: os 14 testes automatizados de round-trip comparam bytes diretamente (`decode(encode(data)) == data`), e o benchmark valida cada experimento com SHA-256 do original contra o descomprimido — 12/12 passaram. O hash dá um certificado compacto e registrável de integridade lossless para cada experimento no CSV, e a probabilidade de colisão é desprezível na prática.

**Q19. Por que entropia de Shannon E repetição lexical? Uma só não bastava?**
Não, porque medem redundâncias diferentes — e essa dualidade é o coração do trabalho. A entropia H(x) = −Σ p(x_i) log2 p(x_i) captura a desigualdade estatística de bytes isolados (o que o Huffman explora); a repetição lexical mede a proporção de tokens repetidos (o que o LZW explora). O arquivo de alta entropia prova o ponto: entropia 6.02 + repetição 0.00 predisse corretamente Huffman 1.28 vs. LZW 0.75.

**Q20. Por que esses 6 arquivos? O conjunto não é pequeno?**
O conjunto foi desenhado para cobrir perfis distintos, não para volume: dois Python pequenos (~1–2 KB), um Python médio real da biblioteca `requests` (34 KB), um payload de alta entropia (controle negativo), um C open source com repetição lexical alta (`jansson_dump.c`) e um log como baseline de contraste. São 12 experimentos (6 arquivos × 2 algoritmos). Reconhecemos o tamanho como limitação — escala para repositórios completos é trabalho futuro declarado no artigo.

**Q21. Quais as limitações do estudo?**
Quatro principais: (i) conjunto de 6 arquivos — cobre perfis, mas não escala de repositório real; (ii) implementação em Python puro — tempos absolutos não são comparáveis a zlib/gzip em C, apenas os relativos entre os dois algoritmos; (iii) LZW com códigos fixos de 16 bits e teto de 4096 entradas — variantes adaptativas poderiam melhorar; (iv) não avaliamos híbridos (LZW+Huffman), que a literatura sugere. Todas viram trabalhos futuros.

---

## Categoria 5 — Níveis de aprendizagem (VAL-07)

**Q22. Em que níveis de aprendizagem este trabalho se enquadra? (ANÁLISE, AVALIAÇÃO, CRIAÇÃO)**
Resposta modelo — conectar os três explicitamente:
- **ANÁLISE:** decompusemos os dois algoritmos nos critérios do enunciado — complexidade de tempo, espaço, tempo prático e facilidade de implementação — e comparamos teoria contra medição em 12 experimentos.
- **AVALIAÇÃO:** julgamos, com evidência quantitativa, qual algoritmo é melhor em cada perfil: Huffman para memória, arquivos pequenos e alta entropia; LZW para padrões repetitivos e descompressão rápida — e justificamos por que não há vencedor absoluto.
- **CRIAÇÃO:** implementamos ambos do zero (heap/árvore, dicionário com caso especial, bitstream próprio) e criamos algo que não existia nas referências: o framework de benchmark que correlaciona entropia de Shannon e repetição lexical com o desempenho relativo, com validação SHA-256 e reprodutibilidade completa via repositório público.

---

## Seção final obrigatória — Pergunta sem resposta preparada

**Protocolo de resposta honesta (3 passos, nunca inventar número):**

1. **Reconhecer o limite do estudo:** "Essa medição específica não fez parte do nosso escopo."
2. **Conectar ao que FOI medido:** "O que podemos afirmar com os nossos dados é [fato mais próximo com número exato]."
3. **Propor como trabalho futuro:** "Seria uma extensão natural do framework — o benchmark já está estruturado para acrescentar essa métrica/arquivo."

**Exemplo aplicado:** "Professor, não medimos X; nosso escopo foi comparar taxa, tempo, memória e integridade em 6 perfis de arquivo. O dado mais próximo que temos é [ex.: memória de pico via tracemalloc, 110 vs. 871 KB]. Medir X seria extensão direta do nosso benchmark, e listamos isso como trabalho futuro."

**Proibições:**
- NÃO inventar número que não está no artigo.
- NÃO responder "não sei" seco — sempre executar os 3 passos.
- NÃO discutir com a banca; se a crítica for procedente, reconhecer: "É uma limitação justa; declaramos ela na Seção de Conclusões."

**Perguntas prováveis deste tipo (sem dado medido):** "e o gzip/zlib, como se compara?", "e em arquivos binários?", "e com códigos LZW de largura variável?", "e o consumo de energia?". Para todas: passos 1→2→3.
