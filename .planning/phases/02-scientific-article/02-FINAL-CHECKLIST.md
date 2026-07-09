# Phase 2 — Final SBC Submission Checklist

**Article:** `article/artigo.pdf` (9 pages, 314 KB)
**Compiled:** 2026-07-09 — pdflatex → bibtex → pdflatex ×2, zero errors/warnings
**Status:** READY FOR SUBMISSION

---

## Compilation & Structure

- [x] PDF compiles without fatal errors (full cycle: pdflatex → bibtex → pdflatex ×2)
- [x] Page count: **9 pages** (limit 8–10) — "Output written on artigo.pdf (9 pages, 314122 bytes)"
- [x] Zero undefined citation warnings in final log
- [x] Zero BibTeX warnings/errors
- [x] No missing fonts or missing figure files in compile log
- [x] Encoding: utf8 inputenc + T1 fontenc + babel brazilian

## Title Page

- [x] Title present: "Comparação de Huffman e LZW na Compressão Lossless de Código-Fonte"
- [x] Authors + institution (UFABC, Santo André -- SP) + email present
- [x] SBC template (`sbc-template.sty`) applied; 12pt article class

## Abstract & Resumo

- [x] Abstract (English): 7 lines in PDF (≤10) — objective, methodology, results, implication
- [x] Resumo (Portuguese): 7 lines in PDF (≤10) — parallel structure, natural Portuguese with correct accents
- [x] No citations inside abstract/resumo

## Sections (all present)

- [x] 1. Introdução (~1.2–1.4 pages: context, quantitative motivation, domain specificity, method lineage, contribution, methodology preview, roadmap)
- [x] 2. Problema de Pesquisa (realistic case + 4 research questions)
- [x] 3. Trabalhos Relacionados (8 works discussed)
- [x] 4. Fundamentação Teórica (Huffman, LZW, comparison table)
- [x] 5. Aplicação Computacional (implementation + experimental protocol)
- [x] 6. Análise dos Resultados (interpretation + theory-vs-practice)
- [x] 7. Conclusões e Trabalhos Futuros (answers all 4 RQs, no new citations)
- [x] Referências (10 entries)

## Tables & Figures (SBC positioning)

- [x] Tabela 1 (Comparação teórica): caption ABOVE table ✓, referenced in text ✓
- [x] Tabela 2 (Perfil do conjunto de dados): caption ABOVE table ✓, referenced ✓
- [x] Tabela 3 (Resultados do benchmark): caption ABOVE table ✓, referenced ✓
- [x] Figura 1 (fig-ratio.png): caption BELOW figure ✓, referenced ✓
- [x] Figura 2 (fig-tempo.png): caption BELOW figure ✓, referenced ✓
- [x] Figura 3 (fig-memoria.png): caption BELOW figure ✓, referenced ✓
- [x] All captions in correct Portuguese with accents

## Bibliography

- [x] 10 BibTeX entries (≥10 required)
- [x] 7 Qualis A sources: Proc. IRE (Huffman 1952), IEEE Computer (Welch 1984), IEEE Trans. IT (Ziv/Lempel 1977, 1978), Bell Syst. Tech. J. (Shannon 1948), JACM (Storer/Szymanski 1982), CACM (Witten et al. 1987)
- [x] All 10 entries cited in text (artigo.bbl contains exactly 10 \bibitem)
- [x] Citations in SBC [author year] format, verified via pdftotext (e.g., [Huffman 1952], [Storer and Szymanski 1982])
- [x] `sbc.bst` bibliography style applied; alphabetical ordering
- [x] No citations introduced in Conclusões

## Reproducibility

- [x] GitHub repository link present in Aplicação Computacional: https://github.com/GabryelBoer/huffman-lzw-compression
- [x] Experimental protocol described (run-all.sh, 12 experiments, SHA-256 validation)

## Portuguese (norma culta)

- [x] Full accent correction pass completed (~120+ words fixed across all sections, captions, and section titles)
- [x] Verb "é" vs conjunction "e" disambiguated throughout
- [x] Residual regex scan over 60+ known patterns: clean
- [x] Academic tone: no first-person singular, no colloquialisms
- [x] T1 fontenc added for correct hyphenation of accented words

---

*Checklist generated during Task 8 — Phase 2 execution, 2026-07-09*
