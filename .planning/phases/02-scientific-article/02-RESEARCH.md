# Phase 2 Research: SBC Article Format & Academic Standards

**Date:** 2026-07-09  
**Scope:** SBC format standards, academic article structure, scientific writing conventions (Portuguese), common pitfalls

---

## 1. SBC FORMAT STANDARDS (Verified)

### Paper Structure
- **Page format:** A4, single column
- **Margins:** top 3.5cm, bottom 2.5cm, left/right 3.0cm
- **First page:** Title (16pt bold centered), Authors (12pt bold centered), Affiliation, Email (Courier 10pt)

### Typography
- **Body text:** Times New Roman 12pt, 6pt space before paragraphs
- **Section titles:** 13pt bold, flush left, 12pt space before
- **Subsection titles:** 12pt bold, flush left
- **First paragraph:** not indented; subsequent: 1.27cm indent
- **Abstract/Resumo:** 12pt Times, indented 0.8cm both sides, ≤10 lines each

### Critical: Table & Figure Formatting
- **Table captions:** ABOVE table (SBC standard), Helvetica 10pt bold
- **Figure captions:** BELOW figure, Helvetica 10pt bold
- Caption indentation: <1 line centered; >1 line justified & indented 0.8cm

### References
- Style: SBC (`sbc.bst` BibTeX style)
- Citation format: `[author:year]` brackets (e.g., `[huffman1952]`)
- Font: 12pt, 6pt spacing before each reference
- Indentation: first line not indented; subsequent lines 0.5cm indent

### Length Constraint
**8–10 pages maximum** including figures, tables, references

---

## 2. RECOMMENDED SECTION BREAKDOWN

| Section | Pages | Purpose |
|---------|-------|---------|
| Introduction | 1.0–1.5 | Context, problem importance, contribution novelty |
| Problem Statement | 0.5–0.75 | Realistic use case (code repository), research questions |
| Related Work | 0.75–1.0 | Foundational papers (Huffman, Ziv-Lempel, Welch) |
| Theoretical Foundation | 1.25–1.75 | Algorithm explanations, pseudocode, complexities |
| Computational Application | 0.75–1.0 | Implementation details, data structures, experimental protocol |
| Results & Analysis | 1.75–2.25 | Dataset, results by category, 3 figures, correlations |
| Conclusions | 0.75–1.0 | Research questions answered, recommendations, future work |
| References | 0.5–1.0 | SBC formatted bibliography |

---

## 3. SCIENTIFIC WRITING STANDARDS (PORTUGUESE)

### Formal Conventions
- Use "norma culta" (standard Portuguese) — avoid colloquialisms
- Academic tone: formal, objective, precise
- Passive voice strategically; not exclusively
- Paragraph structure: topic sentence → development → conclusion

### Abstract/Resumo Formula (max 10 lines)
1. **Context/motivation** (1 line)
2. **Problem** (1 line)
3. **Methodology** (2 lines)
4. **Key results** (2 lines)
5. **Implication/contribution** (1 line)

### Result Interpretation Patterns
- "A Tabela X mostra que..." (introduce table)
- "Esse resultado confirma a predição teórica de que [algorithm] é melhor em [condition] porque..." (explain)
- "Em contraste, [algorithm] expandiu o arquivo em [cases] devido ao [mechanism]" (contrast)

---

## 4. COMMON PITFALLS IN COMPRESSION ALGORITHM PAPERS

| Pitfall | Solution |
|---------|----------|
| **Abstract >10 lines** | Write abstract last; count lines strictly |
| **Table captions below tables** | Use `\caption{...}` BEFORE table in LaTeX |
| **Citation inconsistency** | Use BibTeX with `sbc.bst` exclusively (`[author:year]` format) |
| **Algorithm unexplained** | Include: intuition → pseudocode → data structures → complexity → example |
| **Results not interpreted** | 1–2 paragraphs per table/figure explaining patterns, causation |
| **Conclusions cite new papers** | SBC forbids new citations in conclusions |
| **Language bias in comparison** | Report all metrics neutrally: "A wins at X; B wins at Y" |
| **Portuguese grammar errors** | Proofread for "naturalidade"; write natively, not translated |
| **Repository link missing** | Cite GitHub repo with full URL in Application section |
| **Page overflow** | Plan sections upfront; verify page count weekly; cut verbosity |

---

## 5. CURRENT ARTICLE STATUS

✓ Complete 7-section structure (Intro → Problem → Related → Theory → Application → Results → Conclusions)  
✓ SBC template applied (`\usepackage{sbc-template}`)  
✓ Abstract + Resumo present (verify line count ≤ 10 each)  
✓ 3 figures included (compression ratio, execution time, memory)  
✓ 3 tables (comparison, dataset, results)  
✓ BibTeX bibliography initialized (referencias.bib)  

**Article file:** `/Users/gabryelboer/Documents/ufabc-trab-compression/article/artigo.tex`  
**Output PDF:** `/Users/gabryelboer/Documents/ufabc-trab-compression/article/artigo.pdf`

---

## 6. PHASE 2 SCOPE

Phase 2 is **NOT** about writing the article from scratch. The draft exists and is substantially complete. Phase 2 focuses on:

1. **Verification:** Compile PDF, verify page count ≤10
2. **Format Audit:** Abstract/resumo line count, table caption positioning, citation consistency
3. **Polish:** Portuguese proofread, figure references, repository link validation
4. **Finalization:** BibTeX cycle, requirements cross-check, submission readiness

**Timeline:** 7–8 working days (verification + refinement, not authoring)

---

*Research completed: 2026-07-09*
