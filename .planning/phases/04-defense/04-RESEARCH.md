# Phase 4 Research: Defesa Oral

**Date:** 2026-07-09
**Scope:** Critérios de avaliação, materiais de preparação possíveis, riscos da demo live

---

## 1. Natureza da fase

Phase 4 é executada por HUMANOS (defesa presencial). O que o GSD pode entregar é **material de preparação**:
1. Roteiro de apresentação (speaker notes por slide, timing)
2. Banco de Q&A antecipado (perguntas prováveis + respostas fundamentadas)
3. Checklist de demo live + plano de contingência
4. Checklist dia-da-defesa mapeando VAL-01–07

## 2. Critérios do professor (VAL-01–07, do ROADMAP)

| Req | Critério | Material de preparação |
|-----|----------|------------------------|
| VAL-01 | Todos presentes (nota ZERO se faltante) | Checklist logístico |
| VAL-02 | Domínio: responde perguntas sobre Huffman/LZW, resultados, decisões | Q&A bank |
| VAL-03 | Correção técnica: complexidades, números, conclusões coerentes | Q&A com números exatos do artigo |
| VAL-04 | Qualidade visual: slides ok (✓ Phase 3), áudio claro, postura | Checklist + ensaio |
| VAL-05 | Inteligibilidade: claro, objetivo, conciso | Roteiro com frases curtas + ensaio cronometrado |
| VAL-06 | Contribuição inédita identificável | Resposta preparada: framework entropia+repetição lexical |
| VAL-07 | Níveis: ANÁLISE, AVALIAÇÃO, CRIAÇÃO | Mapeamento explícito no Q&A |

## 3. Fatos técnicos-chave (fonte: artigo Phase 2 — números para o Q&A)

- **Huffman:** min-heap + árvore binária; O(n log n) construção (n≤256) + O(m) codificação; header com tabela de frequências; memória 20–110 KB
- **LZW:** dicionário hash, 4096 entradas, códigos 16 bits; O(m) amortizado; dicionário reconstruído na decodificação (não transmitido); memória 98–871 KB
- **Por quê Huffman vence em alta entropia (6.02 bits):** LZW depende de padrões repetidos — distribuição quase uniforme não alimenta o dicionário; Huffman ainda explora desigualdade residual de frequências (1.28 vs 0.75 — LZW EXPANDE 33.6%)
- **Por quê LZW expande arquivos pequenos (1 KB):** códigos de 16 bits por sequência + dicionário frio no início; overhead supera ganho (−1.6%)
- **Por quê LZW domina no log (6.76, 85.2%):** linhas quase idênticas → subsequências longas entram no dicionário e são referenciadas repetidamente
- **Por quê C (jansson_dump.c) favorece LZW (1.90 vs 1.73):** maior repetição lexical do conjunto (0.20)
- **Validação lossless:** SHA-256 original vs descomprimido, 12/12 experimentos; 14 testes round-trip (vazio, 1 byte, repetitivo, 256 bytes)
- **Contribuição inédita:** correlação sistemática entropia de Shannon + repetição lexical → desempenho relativo, em conjunto heterogêneo .py/.c/log

## 4. Demo live — riscos (owner notes do ROADMAP)

- Professor ACESSA o repositório GitHub durante a apresentação
- `run-all.sh` usa `.venv/bin/python` — SÓ funciona com venv criado; clone fresco do professor NÃO roda sem setup (risco: instruções do README precisam cobrir isso)
- Contingência obrigatória: resultados já executados (CSVs + PNGs commitados) mostráveis se execução live falhar

## 5. Timing

- 15 min máx total; 2 min abertura; ~1.5 min/slide
- Ensaio cronometrado é o único mitigador confiável de estouro

---
*Research completed: 2026-07-09 (inline — conteúdo derivado do artigo e ROADMAP)*
