# Roadmap: Compressão Huffman vs LZW (AED-II)

## Overview

**4 fases** | **37 requirements mapped** | All v1 requirements covered ✓

| # | Phase | Goal | Requirements | Success Criteria |
|---|-------|------|--------------|------------------|
| 1 | Documentação de Código | README e análise de complexidade | CODE-01 to CODE-10 | ✓ Repositório pronto para benchmark |
| 2 | Artigo Científico | Documento 8-10 páginas formato SBC | DOC-01 to DOC-10 | Artigo completo e formatado |
| 3 | Slides Apresentação | 10 slides PDF com conteúdo estruturado | SLD-01 to SLD-09 | Slides prontos e em Moodle |
| 4 | Defesa Oral | Apresentação e validação final | VAL-01 to VAL-07 | ✓ Preparação completa (2026-07-10); defesa em si pendente (humano) |

---

## Phase 1: Documentação de Código

**Goal:** Melhorar README com explicações de experimentos, resultados e análises de complexidade; documentar código-fonte.

**Requirements:** CODE-01 to CODE-10

**Plan:** [01-01-PLAN.md](phases/01-code-documentation/01-01-PLAN.md)

- **7 Tasks:** README expansion (3 tasks) + Code documentation (2 tasks) + Validation (2 tasks)
- **Waves:** 1 (sequential phases) — Tasks 1, 4, 5 can parallelize in Wave 1; Tasks 2, 3, 6, 7 follow
- **Estimated duration:** 3-5 days (parallel execution)

**Success Criteria:**

1. README descreve projeto, caso de uso (compressão código-fonte), estrutura do repositório — **Task 1**
2. README inclui instruções passo-a-passo: instalação, execução benchmark, visualização resultados — **Tasks 1, 3**
3. Análise comparativa documentada: tempo prático vs complexidade teórica — **Task 3 (Results section)**
4. Complexidade de tempo explicada para Huffman e LZW (construção + execução) — **Task 2 (Table 1)**
5. Complexidade de espaço analisada (memória usada em benchmarks reais) — **Task 2 (Table 1 + 2)**
6. Facilidade de implementação comparada (linhas de código, estruturas usadas) — **Tasks 4, 5 (docstrings)**
7. Código-fonte comentado nas seções críticas (heap Huffman, dicionário LZW) — **Tasks 4, 5**
8. Testes de validação documentados (round-trip, SHA-256) — **Tasks 6, 7**
9. Repositório em estado executável (run-all.sh sem erros) — **Task 7**
10. README e código prontos para revisão de pares — **Task 7 (Peer Review Checklist)**

**Deliverables:**

- README.md atualizado (2.5-3.5 KB, 8 sections: Overview, Case Study, Algorithms, Complexity Analysis, Installation, Usage, Results, Validation)
- Documentação de complexidade (3-table approach: theory, empirical, correlation)
- Código comentado (module docstrings + function docstrings with Big-O + strategic inline comments)
- Testes validados (round-trip SHA-256 lossless verified)
- Repository peer-review ready (checklist 10/10)

**Owner Notes:**

- Use results CSV e gráficos existentes como evidência (Task 2, 3)
- Correlacionar complexidade teórica com tempos medidos (Task 2)
- Diferenciar: O(n), O(n log n), O(k log k) por fase algoritmo (Task 2)
- Strategic comments only at non-obvious decision points (heap, dictionary) (Tasks 4, 5)
- Benchmark must execute cleanly from fresh environment (Task 7)

---

## Phase 2: Artigo Científico

**Goal:** Escrever artigo científico 8-10 páginas seguindo formato SBC, com todas seções obrigatórias e análise completa.

**Requirements:** DOC-01 to DOC-10

**Success Criteria:**

1. Título conciso com palavras-chave; resumo contendo objetivo, metodologia, resultados
2. Introdução contextualiza problema, destaca objetivo, justifica escolha de Huffman vs LZW
3. Problema de pesquisa explica caso: compressão código-fonte vs dados genéricos
4. Revisão bibliográfica cita artigos Qualis + teses (Huffman clássico, LZW original, variações)
5. Explicação algoritmos: estruturas de dados, análise de complexidade, pseudo-código se necessário
6. Análise resultados compara: taxa compressão, tempo, memória, facilidade implementação
7. Conclusões recapitulam objetivo, sintetizam achados, indicam trabalhos futuros
8. Redação em português norma culta: ortografia, gramática, ordem direta, clareza
9. Formatação SBC: tabelas, figuras com referências, referências bibliográficas, total 8-10 páginas
10. Artigo revisado e corrigido (sem erros formais)

**Deliverables:**

- artigo.pdf (8-10 páginas, formato SBC)
- Todas seções preenchidas conforme normas
- Gráficos e tabelas integrados
- Referências bibliográficas corretas

**Owner Notes:**

- Use template SBC: https://www.sbc.org.br/wp-content/uploads/2024/07/modelosparapublicacaodeartigos.zip
- Máximo 10 páginas incluindo tudo (figuras, tabelas, referências)
- Consultar ComoEscrever.pdf para regras de escrita (português, formatação)
- Destaque a CONTRIBUIÇÃO INÉDITA (comparação Huffman vs LZW em código-fonte)

---

## Phase 3: Slides Apresentação

**Goal:** Criar 10 slides PDF estruturados para apresentação oral de máximo 15 minutos.

**Requirements:** SLD-01 to SLD-09

**Success Criteria:**

1. Slide 1 apresenta grupo: nomes, matrícula, disciplina AED-II
2. Slides 2-3 explicam problema: por quê compressão código-fonte, qual a importância
3. Slide 4 lista trabalhos relacionados: Huffman clássico, LZW original, variações/melhorias
4. Slides 5-6 detalham algoritmos: estruturas Huffman (heap/árvore), LZW (dicionário), complexidades
5. Slides 7-9 mostram experimentos: tabelas/gráficos de taxa/tempo/memória, análise comparativa
6. Slide 10 conclui: qual algoritmo é melhor para código-fonte, futuras pesquisas
7. Ao menos 1 slide menciona repositório GitHub (link será acessado live)
8. Visual adequado: fonte legível, cores consistentes, sem poluição visual
9. Slides em PDF submissível em Moodle
10. Tempos: 2 min para apresentação, ~1.5 min por slide, 15 min total máximo

**Deliverables:**

- apresentacao.pdf (10 slides)
- Estrutura conforme exigência do professor
- Pronto para submissão Moodle
- Pronto para apresentação live

**Owner Notes:**

- Máximo 10 slides é limit hard
- Slides devem ser auto-explicativos (legíveis sem narração)
- Gráficos podem vir diretamente de benchmark-plots/
- Não use vídeos, gravações, fotos — content ao vivo

---

## Phase 4: Defesa Oral

**Goal:** Realizar apresentação oral demonstrando domínio, correção técnica, qualidade visual e atingimento de níveis de aprendizagem.

**Requirements:** VAL-01 to VAL-07

**Success Criteria:**

1. Todos alunos grupo presentes na data/hora da defesa (nota zero se faltante)
2. Domínio assunto: responde perguntas sobre Huffman/LZW, análise resultados, decisões
3. Informações técnicas corretas: complexidades, resultados benchmark, conclusões coerentes
4. Qualidade visual: slides bem formatados, áudio claro, postura profissional
5. Inteligibilidade: apresentação clara, objetiva, concisa; sem "vira-linguanhas"
6. Contribuição inédita identificável: comparação Huffman vs LZW em código-fonte é novel
7. Níveis aprendizagem atingidos: ANÁLISE (comparou 2 algoritmos), AVALIAÇÃO (concluiu qual melhor), CRIAÇÃO (implementou + experimentou)

**Deliverables:**

- Apresentação oral realizada
- Repositório acessado e mostrado live
- Nota da defesa registrada
- Feedback do professor

**Owner Notes:**

- Professor acessará repositório GitHub durante apresentação
- Certifique-se que run-all.sh e código executam sem erro
- Prepare resposta para "Por quê Huffman/LZW ganha em código-fonte?"
- Tenha dados de backup (resultados já executados) se algo falhar live

---

## Phase Dependencies

```
Phase 1 (Documentação) ← Prerequisito para Phase 2 + Phase 3
    ↓
Phase 2 (Artigo) [paralelo com Phase 3]
Phase 3 (Slides)  [paralelo com Phase 2]
    ↓
Phase 4 (Defesa)
```

Phase 1 deve ser concluída primeiro (resulta em análises usadas por Phase 2 e 3).
Phase 2 e Phase 3 podem rodar em paralelo (ambas usam output de Phase 1).
Phase 4 é gate final — só após Phase 2 e 3 completos.

---

## Success Metrics

| Métrica | Critério | Status |
|---------|----------|--------|
| README completo | Instruções + análise complexidade | ✓ Done (Phase 1) |
| Artigo SBC válido | 8-10 págs, todas seções, formatado | ✓ Done (9 págs, 10 refs, DOC 10/10) |
| Slides estruturados | 10 slides, conteúdo mapping professor | ✓ Done (pendente: nomes reais + Moodle) |
| Apresentação realizada | 15 min máx, domínio demonstrado | Pending |
| Todos presentes | Defesa com grupo completo | Pending |
| Repositório acessível | GitHub público + link em slides | Pending |
| Contribuição inédita | Comparação Huffman vs LZW reconhecida | Pending |

---

## Timeline

Sem datas de entrega explícitas fornecidas pelo professor, fases executam ASAP:

1. **Phase 1**: ~3-5 dias (melhoria incremental README + análises)
2. **Phase 2**: ~5-7 dias (redação artigo, revisão, formatação)
3. **Phase 3**: ~2-3 dias (slides são incremental de Phase 2)
4. **Phase 4**: Data professor define (assumir 1-2 semanas após Phase 2/3 prontos)

Paralelizar Phase 2 e 3 economiza ~3-5 dias de wall-clock.

---
*Roadmap created: 2026-07-09*
*Last updated: 2026-07-09 after requirements scoping*
