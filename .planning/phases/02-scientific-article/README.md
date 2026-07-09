# Phase 2: Scientific Article Planning

**Project:** Huffman vs LZW Compression Comparison (AED-II)  
**Phase Goal:** Finalize and submit 8-10 page SBC-formatted scientific article  
**Duration:** 7–8 working days (16–24 hours effort)  
**Status:** ✓ VERIFIED & READY FOR EXECUTION

---

## Phase 2 Overview

Phase 2 is the **finalization and verification phase** for the scientific article. The article draft (artigo.tex) is substantially complete; Phase 2 focuses on:

- Verifying SBC format compliance
- Auditing content against requirements (DOC-01 to DOC-10)
- Ensuring Portuguese quality
- Managing page count (8–10 page limit)
- Conducting final proofread and citation audit
- Verifying reproducibility (GitHub link, run-all.sh functional)

**Phase 2 is NOT about writing the article from scratch.** All content (introduction, algorithms, results, conclusions) already exists and is substantially correct.

---

## Documents in This Directory

| Document | Purpose | Status |
|----------|---------|--------|
| **02-RESEARCH.md** | SBC format standards, academic writing patterns, common pitfalls | ✓ Complete |
| **02-01-PLAN.md** | Detailed 10-task execution plan with steps, dependencies, success criteria | ✓ Complete |
| **02-VERIFICATION.md** | Plan verification report, execution readiness checklist | ✓ Complete |
| **02-AUDIT.md** | Will be created during Task 1; tracks findings as execution progresses | (To create) |
| **02-FINAL-CHECKLIST.md** | Will be created during Task 8; SBC compliance checklist | (To create) |

---

## Quick Start

1. **Read:** `02-RESEARCH.md` (5 min) — understand SBC format and academic standards
2. **Execute:** Tasks 0–9 in `02-01-PLAN.md` following the 10-day sequence
3. **Track:** Update `02-AUDIT.md` as you find issues
4. **Verify:** Complete `02-FINAL-CHECKLIST.md` in Task 8
5. **Submit:** Upload final `artigo.pdf` to Moodle

---

## Key Success Criteria

✓ **Format Compliance:** SBC format verified (margins, fonts, table/figure positioning)  
✓ **Page Count:** 8–10 pages (hard limit)  
✓ **Requirements Met:** All 10 requirements (DOC-01 to DOC-10) satisfied  
✓ **Content Quality:** Portuguese proofread, clear interpretations of results  
✓ **Reproducibility:** GitHub repository link present, run-all.sh functional  
✓ **Citations:** BibTeX cycle complete, all citations in `[author:year]` format  

---

## Critical Details

### SBC Table & Figure Positioning (Most Common Error)
- **Tables:** Caption must be **ABOVE** table (not below)
- **Figures:** Caption must be **BELOW** figure (not above)
- Verify in compiled PDF, not just .tex source

### Page Count Management
- **Hard limit:** 8–10 pages including all figures, tables, and references
- **Monitor weekly** during tasks (especially Tasks 5–8)
- **Trim strategy:** Results interpretation first, then References, then Introduction if needed

### Portuguese Quality Matters
- Read aloud for naturalidade (should sound naturally written, not translated)
- Check verb agreement, preposition choice, academic tone
- Have native speaker proofread Task 7 if possible

### Abstract/Resumo Line Count
- Must be ≤10 lines each (line breaks count)
- Write abstract last (after all content is final)
- Use 5-part formula: context (1) → problem (1) → method (2) → results (2) → implication (1)

---

## File Locations

**Article files:**
- Source: `/Users/gabryelboer/Documents/ufabc-trab-compression/article/artigo.tex`
- Bibliography: `/Users/gabryelboer/Documents/ufabc-trab-compression/article/referencias.bib`
- Template: `/Users/gabryelboer/Documents/ufabc-trab-compression/article/sbc-template.sty`
- Output: `/Users/gabryelboer/Documents/ufabc-trab-compression/article/artigo.pdf`

**Benchmark data & figures:**
- Results CSV: `/Users/gabryelboer/Documents/ufabc-trab-compression/results/`
- Plots PNG: `/Users/gabryelboer/Documents/ufabc-trab-compression/benchmark-plots/`

---

## Task Summary

| Task | Duration | Owner | Key Output |
|------|----------|-------|-----------|
| **0: Prerequisite Check** | 5 min | Team | Confirm LaTeX, article.tex, references.bib, figures exist |
| **1: Compile & Audit** | 1–2 h | Team | Baseline PDF, initial format audit |
| **2: Content (Intro/Problem)** | 1–2 h | Team | Verify sections meet requirements |
| **3: Bibliography** | 1.5–2 h | Team | Audit references (≥10 entries, Qualis A/B) |
| **4: Algorithms** | 2–3 h | Team | Verify Huffman & LZW explanations complete |
| **5: Results** | 2–3 h | Team | Verify 3 figures + 3 tables with interpretation |
| **6: Conclusions & Abstract** | 2–3 h | Team | Refine conclusions + abstract (≤10 lines each) |
| **7: Portuguese Proofread** | 3–4 h | Team | Fix grammar, tone, naturalidade |
| **8: Format Audit & Compile** | 2–3 h | Team | Final SBC compliance check (margins, captions, citations) |
| **9: Requirements Check** | 1–2 h | Team | Cross-check all DOC-01 to DOC-10 |

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| PDF >10 pages | Monitor weekly; trim Results interpretation, References, or Introduction |
| Abstract >10 lines | Count lines in Task 1; refine early in Task 6 |
| Table captions incorrectly positioned | Verify in compiled PDF in Task 8; fix LaTeX if needed |
| Missing article.tex or references.bib | Task 0 prerequisite check catches this immediately |
| Portuguese grammar errors | Task 7 proofread with native speaker |
| Missing GitHub repository link | Task 8 format audit checks for it |
| LaTeX not installed | Task 0 checks `pdflatex --version` |

---

## Execution Timeline

**Solo (1 team member):** 7–8 working days  
**Parallel team (2–3 members):** ~4–5 calendar days

- Day 1: Tasks 0–3 (prerequisite check, compile, content review, bibliography)
- Days 2–3: Tasks 4–5 (algorithms, results interpretation)
- Days 4–5: Tasks 6–7 (conclusions, proofread)
- Days 6–7: Tasks 8–9 (format audit, final check)

---

## Next Action

**Begin Phase 2 Execution:**
1. Read `02-RESEARCH.md` (5 minutes)
2. Read `02-01-PLAN.md` overview (5 minutes)
3. Start Task 0: Prerequisite Check (5 minutes)

**Expected completion:** 7–8 working days  
**Submission deadline:** Coordinate with professor for Moodle deadline

---

*Phase 2 planning completed: 2026-07-09*  
*Status: ✓ VERIFIED & APPROVED FOR EXECUTION*
