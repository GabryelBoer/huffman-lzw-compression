# Slide 1: Apresentacao do Grupo

**Comparacao Huffman vs LZW em Codigo-Fonte**

- Disciplina: AED-II - UFABC
- Integrantes: [nomes do grupo]
- Repositorio: https://github.com/GabryelBoer/huffman-lzw-compression

---

# Slide 2: Problema de Pesquisa (1/2)

**Estudo de caso:** compressao lossless de codigo-fonte (.py, .c)

**Cenario realista:**
- Backups de repositorios
- Transferencia entre ambientes
- Versionamento de software

**Pergunta:** qual algoritmo e mais efetivo?

---

# Slide 3: Problema de Pesquisa (2/2)

**Criterios de comparacao:**
- Complexidade de tempo
- Complexidade de espaco
- Tempo pratico de execucao
- Facilidade de implementacao

**Hipoteses:**
- LZW melhor em padroes repetitivos
- Huffman melhor em frequencias desiguais
- Resultado depende do perfil do arquivo

---

# Slide 4: Trabalhos Relacionados

- Sayood: fundamentos de compressao
- Nambiar et al.: Huffman vs LZW em rede
- Shrividhiya et al.: hibrido Huffman+LZW

**Diferencial:** benchmark com correlacao perfil-desempenho em codigo-fonte

---

# Slide 5: Huffman

- Min-heap + arvore binaria
- Codigos por frequencia de simbolos
- O(n log n) + O(m)
- Envia tabela de frequencias

---

# Slide 6: LZW

- Dicionario hash adaptativo
- Captura padroes repetidos
- O(m) amortizado
- Dicionario reconstruido na decodificacao

---

# Slide 7: Experimentos (1/3)

**Dataset:**
- 4 arquivos .py/.c
- 1 log baseline

**Metricas:**
- Taxa, tempo, memoria
- Entropia, repeticao lexical
- Validacao SHA-256

---

# Slide 8: Experimentos (2/3)

| Arquivo | Huffman | LZW |
|---------|---------|-----|
| requests_sessions.py | 1.73 | 1.66 |
| jansson_dump.c | 1.73 | 1.90 |
| encoder_sample.py | 1.19 | 0.98 |
| high_entropy_payload.py | 1.28 | 0.75 |

---

# Slide 9: Experimentos (3/3)

**Graficos:** benchmark-plots/

- Huffman: menos memoria
- LZW: melhor em C repetitivo e logs
- Sem vencedor absoluto em codigo-fonte

---

# Slide 10: Conclusoes

- Huffman: memoria, arquivos pequenos, alta entropia
- LZW: padroes repetitivos, descompressao rapida
- Facilidade: empate tecnico
- Futuro: repositorios completos, integracao Git

**Repositorio:** https://github.com/GabryelBoer/huffman-lzw-compression
