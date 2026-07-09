# Requirements: Compressão Huffman vs LZW (AED-II)

**Defined:** 2026-07-09
**Core Value:** Comparação experimental rigorosa Huffman vs LZW com análise teórica e prática.

## v1 Requirements

### Documentação (Artigo Científico)

- [ ] **DOC-01**: Título conciso, objetivo, com palavras-chave no início
- [ ] **DOC-02**: Resumo (Abstract) contendo objetivo, contextualização, metodologia, resultados
- [ ] **DOC-03**: Introdução com contexto, formulação do problema, objetivo, justificativa
- [ ] **DOC-04**: Seção "Problema de Pesquisa" com caso real/realístico (código-fonte)
- [ ] **DOC-05**: Revisão Bibliográfica com artigos Qualis e teses/dissertações
- [ ] **DOC-06**: Explicação da Aplicação Computacional (algoritmos, estruturas, complexidades)
- [ ] **DOC-07**: Análise de Resultados com comparação teórica e prática
- [ ] **DOC-08**: Conclusões gerais e trabalhos futuros (3 parágrafos obrigatórios)
- [ ] **DOC-09**: Redação em português norma culta, claro, objetivo, conciso
- [ ] **DOC-10**: Formatação SBC (8-10 páginas máximo total)

### Apresentação (Slides)

- [ ] **SLD-01**: Slide 1 — Apresentação do grupo (nomes, matrícula)
- [ ] **SLD-02**: Slides 2-3 — Explicação problema de pesquisa (caso de uso)
- [ ] **SLD-03**: Slide 4 — Trabalhos relacionados (estado da arte)
- [ ] **SLD-04**: Slides 5-6 — Algoritmos e estruturas (Huffman e LZW)
- [ ] **SLD-05**: Slides 7-9 — Experimentos e análise resultados (teóricos + práticos)
- [ ] **SLD-06**: Slide 10 — Conclusões e trabalhos futuros
- [ ] **SLD-07**: Link para repositório em algum slide (será acessado na apresentação)
- [ ] **SLD-08**: Formato PDF, máximo 10 slides, visual adequado
- [ ] **SLD-09**: Upload em Moodle antes da apresentação (tarefa "SUBMISSÃO DE SLIDES")

### Código Repositório

- [ ] **CODE-01**: README.md explicando projeto, caso de uso, estrutura
- [ ] **CODE-02**: README com instruções para executar experimentos
- [ ] **CODE-03**: README com explicação dos resultados obtidos
- [ ] **CODE-04**: Documentação de complexidade de tempo (teórica + prática)
- [ ] **CODE-05**: Documentação de complexidade de espaço (teórica + prática)
- [ ] **CODE-06**: Comparação: tempo prático vs esperado (complexidade)
- [ ] **CODE-07**: Análise de facilidade de implementação (Huffman vs LZW)
- [ ] **CODE-08**: Código-fonte bem estruturado e comentado
- [ ] **CODE-09**: Testes validando round-trip (compressão → descompressão)
- [ ] **CODE-10**: Repositório público acessível no dia da apresentação

### Validação Acadêmica

- [ ] **VAL-01**: Todos os alunos presentes na defesa oral
- [ ] **VAL-02**: Domínio do assunto demonstrado na apresentação
- [ ] **VAL-03**: Correção das informações técnicas verificada
- [ ] **VAL-04**: Qualidade visual da apresentação adequada
- [ ] **VAL-05**: Inteligibilidade, objetividade, concisão demonstradas
- [ ] **VAL-06**: Contribuição inédita/nova identificável
- [ ] **VAL-07**: Atingimento níveis de aprendizagem: ANÁLISE, AVALIAÇÃO, CRIAÇÃO

## v2 Requirements

### Melhorias Futuras

- Publicação em periódico indexado Qualis
- Implementação de outros algoritmos de compressão (RLE, LZSS, PPM)
- Interface gráfica para visualização de árvore Huffman e dicionário LZW
- Análise de diferentes estruturas de dados para dicionário LZW

## Out of Scope

| Feature | Reason |
|---------|--------|
| Compressão com perda (lossy) | Trabalho enfatiza lossless; compressão com perda é escopo diferente |
| Arquivo único vs stream | Foco em compressão de arquivo completo, não streaming |
| Otimização de velocidade em C/C++ | Implementação educacional em Python é suficiente |
| Suporte a formato comprimido padrão (gzip, bzip2) | Implementação manual dos algoritmos é requisito |
| Interface gráfica | Análise numérica é foco, não UI |

## Traceability

| Requirement | Fase | Status |
|-------------|------|--------|
| DOC-01 | 2 | Pending |
| DOC-02 | 2 | Pending |
| DOC-03 | 2 | Pending |
| DOC-04 | 2 | Pending |
| DOC-05 | 2 | Pending |
| DOC-06 | 2 | Pending |
| DOC-07 | 2 | Pending |
| DOC-08 | 2 | Pending |
| DOC-09 | 2 | Pending |
| DOC-10 | 2 | Pending |
| SLD-01 | 3 | Pending |
| SLD-02 | 3 | Pending |
| SLD-03 | 3 | Pending |
| SLD-04 | 3 | Pending |
| SLD-05 | 3 | Pending |
| SLD-06 | 3 | Pending |
| SLD-07 | 3 | Pending |
| SLD-08 | 3 | Pending |
| SLD-09 | 3 | Pending |
| CODE-01 | 1 | Pending |
| CODE-02 | 1 | Pending |
| CODE-03 | 1 | Pending |
| CODE-04 | 1 | Pending |
| CODE-05 | 1 | Pending |
| CODE-06 | 1 | Pending |
| CODE-07 | 1 | Pending |
| CODE-08 | 1 | Pending |
| CODE-09 | 1 | Pending |
| CODE-10 | 1 | Pending |
| VAL-01 | 4 | Pending |
| VAL-02 | 4 | Pending |
| VAL-03 | 4 | Pending |
| VAL-04 | 4 | Pending |
| VAL-05 | 4 | Pending |
| VAL-06 | 4 | Pending |
| VAL-07 | 4 | Pending |

**Coverage:**
- v1 requirements: 37 total
- Mapped to phases: 37
- Unmapped: 0 ✓

---
*Requirements defined: 2026-07-09*
*Last updated: 2026-07-09 after requirements scoping*
