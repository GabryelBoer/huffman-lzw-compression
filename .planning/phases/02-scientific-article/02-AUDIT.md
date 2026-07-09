# Phase 2 Audit Trail

**Started:** 2026-07-09 (Task 1: Compile & Initial Audit)  
**Status:** In Progress

---

## Task 1: Compile & Initial Audit

### Compilation Results
- **Status:** ✓ PASS
- **Output:** `artigo.pdf` (8 pages, 308 KB)
- **LaTeX packages installed:** titlesec, courier, ec, helvetic, psnfss
- **Compilation cycle:** 3 passes + BibTeX ✓

### Page Count Audit
- **Total pages:** 8 (within limit of 8–10) ✓
- **Content breakdown:**
  - Page 1: Title, authors, abstract, resumo
  - Pages 2–3: Introducao, Problema, Trabalhos Relacionados
  - Pages 3–4: Fundamentacao Teorica (Huffman, LZW, Comparacao)
  - Page 4: Aplicacao Computacional
  - Pages 5–7: Analise dos Resultados (tables, figures)
  - Page 8: Conclusoes, Trabalhos Futuros, Referencias

### Abstract/Resumo Line Count (Verified from Extracted PDF Text)
**Abstract (English, lines 10–16 in extracted text):**
```
This work presents a computational application for lossless compression of source code files using Huffman and LZW algorithms. The case study
focuses on Python and C files in a realistic scenario of software repository storage and versioning. Experiments were conducted on five code files and one
log baseline, measuring compression ratio, execution time, peak memory usage,
Shannon entropy and lexical repetition. Results indicate no absolute winner:
Huffman is more effective for memory usage, small files and high entropy; LZW
is more effective for repetitive patterns and fast decompression on medium files.
The public repository enables full reproducibility of all reported measurements.
```
**Actual line count in PDF:** 7 lines
**Status:** ✓ PASS (well within 10-line limit)

**Resumo (Portuguese, lines 17–23 in extracted text):**
```
Este trabalho apresenta uma aplicacao computacional de compressao lossless de arquivos de codigo-fonte utilizando os algoritmos de Huffman
e LZW. O estudo de caso foca em arquivos Python e C em cenario realista de
armazenamento e versionamento de repositorios de software. Foram conduzidos experimentos com cinco arquivos de codigo e um log de baseline, medindo
taxa de compressao, tempo de execucao, uso de memoria, entropia de Shannon
e repeticao lexical. Os resultados indicam que nao ha vencedor absoluto: Huffman e mais efetivo em memoria, arquivos pequenos e alta entropia; LZW e mais
efetivo em padroes repetitivos e descompressao rapida em arquivos medios. O
repositorio publico permite reproduzir integralmente as medicoes reportadas.
```
**Actual line count in PDF:** 7 lines
**Status:** ✓ PASS (well within 10-line limit)

### Section Completeness Check

| Section | Expected | Status | Notes |
|---------|----------|--------|-------|
| **Title & Authors** | ✓ | ✓ Present | Gabryel Boer + Integrantes |
| **Abstract (EN)** | ✓ | ✓ Present | ~9 lines, objective + methodology + results |
| **Resumo (PT)** | ✓ | ✓ Present | ~9 lines, parallel structure |
| **Introducao** | ✓ | ✓ Present | ~1.5 pages, context + contribution |
| **Problema de Pesquisa** | ✓ | ✓ Present | Realistic use case (code-source), 4 RQs |
| **Trabalhos Relacionados** | ✓ | ✓ Present | Sayood, Huffman, Ziv/Lempel, Welch, Nambiar, Shrividhiya |
| **Fundamentacao Teorica** | ✓ | ✓ Present | Huffman + LZW explanations + comparison table |
| **Aplicacao Computacional** | ✓ | ✓ Present | Implementation details, protocol, GitHub URL |
| **Analise dos Resultados** | ✓ | ✓ Present | Dataset table, results table, 3 figures |
| **Conclusoes** | ✓ | ✓ Present | Findings recap + future work |
| **Referencias** | ✓ | ✓ Present | BibTeX entries visible in PDF |

### Figure & Table Audit

**Tables expected:**
1. ✓ Table 1: Comparacao teorica (Huffman vs LZW) — present
2. ✓ Table 2: Perfil do conjunto de dados — present
3. ✓ Table 3: Resultados consolidados — present (assuming present, needs visual check)

**Figures expected:**
1. ? Figure 1: Compression Ratio (%) — to verify visually
2. ? Figure 2: Execution Time (ms) — to verify visually
3. ? Figure 3: Memory Usage (MB) — to verify visually

### Citation Audit

**BibTeX warnings during compilation:**
- ✓ Citation `huffman1952` — referenced, in bib
- ✓ Citation `welch1984` — referenced, in bib
- ✓ Citation `ziv1977` — referenced, in bib
- ✓ Citation `sayood2017` — referenced, in bib
- ✓ Citation `nambiar2025` — referenced, in bib
- ✓ Citation `shrividhiya2021` — referenced, in bib

**Status:** All citations resolved after BibTeX cycle ✓

### Format Issues Detected

| Issue | Severity | Location | Action |
|-------|----------|----------|--------|
| None detected at PDF level | - | - | Proceed to visual audit in Task 8 |

### Baseline Measurements

- **PDF file size:** 256 KB (after accent corrections)
- **Total word count (estimated):** ~2500 words
- **Figures present (estimated):** 3
- **Tables present (verified):** 3
- **References (estimated):** 6–8 entries

### Accent Corrections Applied

**Task 1 Addition:** Fixed ~40 Portuguese words to PT-BR norma culta:
- aplicacao → **aplicação**
- compressao → **compressão**
- codigo → **código**
- execucao → **execução**
- memoria → **memória**
- repeticao → **repetição**
- criterios → **critérios**
- nao → **não**
- (+ 32 more words corrected)

**Status:** ✓ Acentuation corrected, PDF recompiled successfully

---

## Task 2: Content Verification — Intro & Problem

- **Introduction:** ⚠ FINDING — only ~0.5 page (target 1.0–1.5). Content valid (context, objective, justification present) but undersized. → Resolved by Fix A (below).
- **Problem Statement:** ✓ PASS — realistic use case (code-source repositories), 4 explicit research questions, correct length.

## Task 3: Bibliography Audit

- **Count:** ⚠ FINDING — only 6 entries (minimum 10). → Resolved by Fix B (below).
- **Qualis A:** 3 of target 5 (IEEE Trans. IT, Proc. IRE, IEEE Computer). → Resolved by Fix B.
- **Format:** ✓ PASS — all entries have required fields; zero dangling citations.

---

## Fix A: Introduction Expansion (resolves Task 2 finding)

**Status:** ✓ DONE

Added 4 new paragraphs to Introdução (now 8 paragraphs, ~1.2–1.4 pages):
1. Quantitative context: repository growth, storage/transfer cost in backups, CI/CD, monorepos
2. Source code as distinct compression domain: syntactic structure, recurring tokens, indentation, byte-statistics vs subsequence-repetition duality
3. Method lineage: statistical coding founded on Shannon's information theory \cite{shannon1948} vs dictionary methods (Lempel-Ziv family \cite{ziv1977,ziv1978})
4. Methodology preview: reproducible benchmark, 12 experiments, SHA-256 validation, entropy + lexical repetition metrics

Evidence: "Problema de Pesquisa" now starts on page 2; "Trabalhos Relacionados" on page 3. PDF grew 8 → 9 pages (within 8–10 limit).

## Fix B: Bibliography Expansion (resolves Task 3 finding)

**Status:** ✓ DONE

Added 4 classic peer-reviewed entries to referencias.bib (total now **10 entries**):
- `shannon1948` (Bell System Technical Journal) — cited in Introdução and in Protocolo Experimental at the H(x) entropy formula
- `ziv1978` (IEEE Trans. Information Theory) — cited in Introdução and Trabalhos Relacionados (LZ77 → LZ78 → LZW lineage)
- `storer1982` (Journal of the ACM) — cited in Trabalhos Relacionados (theoretical foundation of textual substitution)
- `witten1987` (Communications of the ACM) — cited in Trabalhos Relacionados (arithmetic coding as statistical alternative to Huffman)

**Qualis A count: 7** (Proc. IRE, IEEE Computer, 2× IEEE Trans. IT, Bell Syst. Tech. J., JACM, CACM) — exceeds target of 5.
All 10 entries cited in text (artigo.bbl contains exactly 10 \bibitem entries; zero BibTeX warnings). No new citations in Conclusões (SBC rule respected).

**Critical repair found during Fix B:** the previous accent-correction pass had over-corrected identifiers, breaking the build silently:
- `\bibliography{referências}` → fixed to `\bibliography{referencias}` (file on disk is ASCII; artigo.bbl was 49 bytes = empty bibliography)
- `\includegraphics{fig-memória.png}` → fixed to `fig-memoria.png` (file on disk is ASCII)
- Labels `sec:aplicação` / `fig:memória` → normalized to ASCII `sec:aplicacao` / `fig:memoria`

## Task 4: Theoretical Foundation — ✓ PASS

- Huffman: intuition (greedy bottom-up), data structures (min-heap, binary tree), complexities O(n log n) construction + O(m) encoding, space (tree + code table + frequency header), limitation (symbol-by-symbol) — all present and correct.
- LZW: dictionary initialization (256 bytes), w+c extension rule, decoder special case, O(m) amortized with hash table, 4096-entry dictionary limit — all present and correct.
- Comparison table (Tabela 1): 8 criteria, all claims defensible from benchmark data (e.g., 870 KB vs 110 KB memory matches Tabela 3).
- No factual errors found; no corrections needed.

## Task 5: Results & Analysis — ✓ PASS

- 3 tables present and referenced: tab:comparacao, tab:dataset, tab:resultados.
- 3 figures present, referenced in text, and confirmed included in compile log: fig-ratio.png, fig-tempo.png, fig-memoria.png.
- Every result interpreted with mechanism (e.g., LZW expansion on small files explained by dictionary overhead; high-entropy payload penalizes dictionary compressors).
- Theory-practice connection explicit in subsection "Teoria versus prática".
- Neutral language throughout; both LZW wins (jansson_dump.c, access.log) and Huffman wins reported.

## Task 6: Conclusions & Abstract — ✓ PASS

- Conclusões answer all 4 research questions from Problema de Pesquisa: (i) rate per profile, (ii) memory/time in practice, (iii) entropy/lexical-repetition correlation, (iv) per-criterion effectiveness.
- Zero citations in Conclusões (SBC rule).
- Abstract: 7 lines in PDF (≤10 ✓). Resumo: 7 lines in PDF (≤10 ✓).
- Introduction expansion added context but did not change the paper's claims; abstract/resumo remain accurate — no adjustment needed. Resumo accents fixed (cenário, há, é, rápida, repositório público, medições).

## Task 7: Portuguese Proofread — ✓ PASS

Full rewrite pass applied over artigo.tex covering ALL remaining unaccented words (~120+ corrections), including:
- Verb "ser": "e" → "é" where verb (e.g., "O estudo de caso escolhido é a compressão", "A complexidade de tempo é O(n log n)"); conjunction "e" untouched.
- Systematic fixes: codificação, decodificação, Conclusões (incl. \section{}), validação, distribuição/distribuições, cenário(s), único/única, ótimo, mínima, até, há, histórico, características, número, público, disponíveis, necessária, ocorrências, proporção, relação, típica, evidências, preferível, restrição/restrições, avaliação, reproduzível/reproduzíveis, heterogêneo, geração, determinística, ordenação, concatenação, condição, prévia, início, próxima, extensão, alcançou, medições, repositório, não, são, está, estão, mantêm, lê, revisões, versões, distinção, construção, árvore/Árvore, símbolo(s), funções, serialização, técnico, critério(s), híbrida(s), diferença(s), frequência(s), prática, Fundamentação Teórica, Comparação Teórica, Correlação, Aplicação, Implementação.
- Table 1 caption and cells fixed (Comparação teórica, Critério, prévia, Não, Árvore, Dicionário, máx., reconstruído, Redundância, Frequência, Repetição, Cenário, Distribuição).
- Address fixed: Santo André.
- Residual scan (regex over 60+ known patterns): zero true positives remaining (only hits: conjunction "e" and ASCII filename fig-memoria.png, both correct).
- Preamble improvements: added `\usepackage[T1]{fontenc}` (correct hyphenation of accented words); `[brazil]` → `[brazilian]` in babel. Compiles clean.
- Academic tone: no first-person singular, no colloquialisms found.

## Task 8: Format Audit & Final Compilation — ✓ PASS

1. Full cycle compiled (pdflatex → bibtex → pdflatex ×2): zero errors, zero BibTeX warnings, zero undefined citations, no missing fonts/files.
2. **Page count: 9** ("Output written on artigo.pdf (9 pages, 314122 bytes)") — within 8–10 ✓
3. Table captions ABOVE tables (\caption precedes tabular in all 3 table envs); figure captions BELOW figures (\caption follows \includegraphics in all 3 figure envs) — SBC standard ✓
4. Citations verified in PDF text via pdftotext: [Huffman 1952], [Shannon 1948], [Ziv and Lempel 1978], [Storer and Szymanski 1982], [Witten et al. 1987], [Welch 1984, Ziv and Lempel 1977], etc. — SBC [author year] format ✓
5. GitHub repository link present in Aplicação Computacional: github.com/GabryelBoer/huffman-lzw-compression ✓
6. Zero "undefined citation" warnings in final log ✓
7. Final checklist created: `02-FINAL-CHECKLIST.md` ✓

---

## Task 9: Requirements Cross-Check

| Req | Requirement | Status | Evidence |
|-----|-------------|--------|----------|
| DOC-01 | Concise title with keywords | ✓ PASS | "Comparação de Huffman e LZW na Compressão Lossless de Código-Fonte" — algorithms + technique + domain |
| DOC-02 | Abstract + Resumo ≤10 lines with objective/methodology/results | ✓ PASS | 7 lines each in final PDF; 5-part structure present |
| DOC-03 | Introduction contextualizing problem, objective, justification | ✓ PASS | 8 paragraphs, ~1.2–1.4 pages after Fix A; context + lineage + contribution + preview |
| DOC-04 | Problem Statement with realistic case | ✓ PASS | Code-source repository storage/versioning; 4 explicit research questions |
| DOC-05 | Bibliography with peer-reviewed sources | ✓ PASS | 10 entries, 7 Qualis A (IEEE/ACM/Bell), all cited, zero warnings |
| DOC-06 | Algorithm explanation: structures, data, complexities | ✓ PASS | Huffman O(n log n)+O(m), LZW O(m) amortized, structures + comparison table |
| DOC-07 | Comparison theory vs practice | ✓ PASS | 3 tables + 3 figures, per-file interpretation, "Teoria versus prática" subsection |
| DOC-08 | Conclusions answering research questions | ✓ PASS | All 4 RQs answered; no new citations; future work grounded |
| DOC-09 | Portuguese norma culta | ✓ PASS | Full accent pass (~120+ fixes), residual scan clean, academic tone verified |
| DOC-10 | SBC format, 8–10 pages, captions positioned | ✓ PASS | 9 pages; table captions above, figure captions below; [author year] citations |

**Result: 10/10 PASS.** Article ready for submission.

---

## Issues Found & Resolved

1. **Broken bibliography (critical, latent):** previous accent pass renamed `\bibliography{referencias}` to `{referências}` — bibtex could not find the .bib, leaving an empty 49-byte .bbl. Fixed.
2. **Broken figure include (critical, latent):** `fig-memória.png` referenced but disk file is `fig-memoria.png`. Fixed.
3. **Undersized introduction:** resolved by Fix A (+4 paragraphs).
4. **Insufficient bibliography:** resolved by Fix B (6 → 10 entries, 3 → 7 Qualis A).
5. **~120+ missing accents:** resolved by full Task 7 rewrite pass.

---

*Audit started: 2026-07-09 20:14 GMT-3*
*Audit completed: 2026-07-09 (Fix A, Fix B, Tasks 4–9) — Phase 2 execution complete*
