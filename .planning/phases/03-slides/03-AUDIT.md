# Phase 3 Audit: Slides de Apresentação

**Date:** 2026-07-09
**Status:** COMPLETE PENDING HUMAN INPUT (gate: placeholder de autoria no slide 1)
**Deliverables:** `slides/slides.tex`, `slides/apresentacao.pdf` (10 páginas)

---

## Resultado por Task

| Task | Resultado | Evidência |
|------|-----------|-----------|
| 0: Prerequisites | ✓ | `beamer.cls` presente; `beamerthememetropolis.sty` AUSENTE → fallback tema `Madrid` (decisão do plano); `slides/` criado; 3 figuras copiadas de `article/fig-*.png` (fonte canônica, nomes ASCII) |
| 1: slides.tex | ✓ | 10 frames, Beamer 12pt Madrid, `[utf8]{inputenc}` + `[T1]{fontenc}` + `[brazilian]{babel}` + `lmodern`; máx 6 bullets/frame; números copiados exatos do artigo |
| 2: Compilação | ✓ | 2 passes pdflatex; `Output written on slides.pdf (10 pages, 361613 bytes)`; grep `Overfull \vbox` e `Overfull \hbox` → ZERO warnings após iteração |
| 3: Audit visual/conteúdo | ✓ | pdftotext: 10 páginas; todos os números conferem com o artigo; acentuação correta (0 mojibake); GitHub nos slides 1 e 10; AED-II no slide 1 |
| 4: Cross-check + commit | ✓ | Tabela SLD abaixo; `slides/` está no `.gitignore` (linha 13, junto com `article/`) → apenas `.planning/` commitado |

## Iterações de layout (Task 2)

1. **Overfull hbox 112.6pt em todos os frames:** footline do tema Madrid estourava com autor/instituto longos → corrigido com formas curtas `\author[Grupo]{...}` e `\institute[UFABC]{...}`.
2. **Overfull vbox nos frames 7–9 (figuras):** `height=0.62\textheight` + bullets não cabiam → reduzido para 0.55 (frame 7, 2 bullets longos) e 0.58 (frames 8–9), `center` env trocado por `\centering` (economiza espaço vertical).
3. **Fontes Type 3 (bitmap) detectadas via `pdffonts`:** cm-super ausente no basictex fazia T1 cair em fontes bitmap, degradando qualidade visual em projeção (risco SLD-08) → adicionado `\usepackage{lmodern}` (disponível no basictex). Resultado: 100% fontes vetoriais Type 1, e extração de texto do PDF passou a mapear a ligadura "ff" corretamente ("Huffman" extraível).

## Tabela SLD-01–09

| Req | Status | Evidência |
|-----|--------|-----------|
| SLD-01 | ⚠ | Slide 1 tem disciplina AED-II, UFABC e placeholder `[Nomes e matrículas dos integrantes]` — nomes reais são PENDÊNCIA HUMANA |
| SLD-02 | ✓ | Slides 2–3: crescimento de repositórios/CI/monorepos + dualidade bytes×tokens + 4 questões de pesquisa |
| SLD-03 | ✓ | Slide 4: Shannon 1948, Huffman 1952, Ziv-Lempel 1977/1978, Welch 1984, Nambiar 2025, Shrividhiya 2021 (1 linha cada) + diferencial |
| SLD-04 | ✓ | Slide 5 (Huffman: min-heap, árvore, O(n log n)+O(m)) e slide 6 (LZW: hash, 4096 entradas, 16 bits, O(m) amortizado) |
| SLD-05 | ✓ | Slides 7–9 com fig-ratio/fig-tempo/fig-memoria + destaques: 1.73/1.66, 1.90, 1.28/0.75, 6.76 (85.2%), 2.5× (13.4/34.1 ms), 110/871 KB, −1.6%/−33.6% |
| SLD-06 | ✓ | Slide 10: sem vencedor absoluto, perfis Huffman/LZW, SHA-256, futuras pesquisas (repositórios, Git, híbridos) |
| SLD-07 | ✓ | `github.com/GabryelBoer/huffman-lzw-compression` presente nos slides 1 E 10 (verificado por página via pdftotext) |
| SLD-08 | ✓ | PDF, exatamente 10 páginas, zero overfull, fontes vetoriais (pdffonts sem Type 3), figuras renderizadas |
| SLD-09 | ⚠ | PDF pronto para upload no Moodle, MAS submissão bloqueada pelo gate de autoria (SLD-01) — upload é ação humana |

## Conferência de números (artigo → slides, cópia exata)

- requests_sessions.py: Huffman 1.73 / LZW 1.66; memória 110 KB vs 871 KB; descompressão 13.4 ms vs 34.1 ms (≈2.5×) ✓
- jansson_dump.c: LZW 1.90 vs Huffman 1.73 ✓
- Alta entropia (6.02 bits): Huffman 1.28 vs LZW 0.75 (−33.6%) ✓
- Arquivo pequeno: LZW −1.6%; Huffman 15.9% (implícito via bullets de expansão) ✓
- access.log: LZW 6.76 com 85.2% de economia vs Huffman 1.89 (fig) ✓

## Pendências humanas (GATE — fase NÃO é submission-ready)

1. **Substituir placeholder de autoria** em `slides/slides.tex` (linha `\author[Grupo]{[Nomes e matrículas dos integrantes]}`) pelos nomes e matrículas reais, e **recompilar** (2× `pdflatex -interaction=nonstopmode slides.tex && cp slides.pdf apresentacao.pdf`).
2. **Inspeção visual final** do `slides/apresentacao.pdf` (cores/legibilidade em projetor).
3. **Upload no Moodle** (SLD-09) após itens 1–2.
4. Mesma pendência de autoria existe no artigo (Phase 2) — sincronizar nomes nos dois documentos.

## Notas e decisões

- **Versionamento:** `slides/` está no `.gitignore` (padrão do projeto, igual a `article/`). Decisão conservadora: NÃO remover do .gitignore (respeita escolha explícita do usuário na Phase 2); artefatos ficam locais, reproduzíveis a partir deste audit + artigo. Somente `.planning/` foi commitado.
- **Artefatos pré-existentes em `slides/`:** havia um `slides.md` (2 KB) e um `apresentacao.pdf` antigo (7.2 KB) de tentativa anterior; o PDF foi sobrescrito pela compilação nova (353 KB); `slides.md` ficou intocado (fora de escopo — pode ser removido manualmente).
- **Identificadores ASCII:** todos os nomes de arquivo (`fig-ratio.png`, `fig-tempo.png`, `fig-memoria.png`, `slides.tex`, `apresentacao.pdf`) e nenhum label acentuado — lição da Phase 2 aplicada.
- **Timing:** 10 slides × ~1.5 min ≈ 15 min ✓ dentro do limite da defesa.

---
*Audit completed: 2026-07-09*
