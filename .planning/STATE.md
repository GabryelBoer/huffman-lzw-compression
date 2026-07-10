# Project State: Compressão Huffman vs LZW (AED-II)

## Project Reference

See: .planning/PROJECT.md (updated 2026-07-09)

**Core value:** Comparação experimental rigorosa Huffman vs LZW com análise teórica e prática.
**Current focus:** Phase 4 (Defense) — materiais de preparação completos; restam ações humanas (ensaios, presença, autoria nos slides)

## Current Status

| Aspect | Status | Notes |
|--------|--------|-------|
| Project Initialized | ✓ | All planning docs created |
| Codebase Map | ✓ | 7 documents in .planning/codebase/ |
| Requirements Scoped | ✓ | 37 requirements in 4 phases |
| Roadmap Created | ✓ | 4-phase plan, parallelizable |
| Code Status | ✓ | Huffman + LZW working, benchmark running |
| Config Set | ✓ | YOLO mode, coarse granularity, parallel execution |

## Roadmap at a Glance

1. **Phase 1: Documentation** (Code + README analysis)
   - Goals: README, complexity analysis, validation
   - Status: ✓ COMPLETE (2026-07-09) — 10/10 requirements, peer-review checklist 10/10

2. **Phase 2: Article** (Scientific paper, 8-10 pages, SBC format)
   - Goals: Full academic article with all required sections
   - Status: ✓ COMPLETE (2026-07-09) — artigo.pdf 9 páginas, 10 refs (7 Qualis A), DOC-01–10 10/10 PASS
   - Pendências humanas: nomes reais dos autores (placeholder), confirmar repo GitHub público, inspeção visual final do PDF

3. **Phase 3: Slides** (10-slide PDF presentation)
   - Goals: Presentation slides for 15-minute defense
   - Status: ✓ COMPLETE PENDING HUMAN INPUT (2026-07-09) — apresentacao.pdf 10 páginas, SLD-01–09: 7✓/2⚠ (ver 03-AUDIT.md)
   - Pendências humanas: substituir placeholder de nomes/matrículas no slide 1 + recompilar; upload no Moodle

4. **Phase 4: Defense** (Oral presentation)
   - Goals: Present work, demonstrate mastery, pass evaluation
   - Duration: Professor's schedule
   - Status: ✓ PREP COMPLETE (2026-07-10) — ROTEIRO.md, QA-BANK.md (22 Q&A), DEMO-CHECKLIST.md, DIA-DA-DEFESA.md; clone fresco validado (README fiel, 14/14 testes); ver 04-AUDIT.md
   - Pendências humanas: VAL-01 (confirmações de presença), ≥2 ensaios cronometrados, divisão de falas/Q&A, decisão sobre push ao remoto (local 16 commits à frente)

## Requirements by Phase

### Phase 1: Documentation (10 requirements)
- CODE-01: README project description
- CODE-02: README execution instructions
- CODE-03: README results explanation
- CODE-04: Time complexity documentation
- CODE-05: Space complexity documentation
- CODE-06: Practical vs theoretical complexity analysis
- CODE-07: Implementation difficulty comparison
- CODE-08: Well-commented source code
- CODE-09: Validation tests (round-trip)
- CODE-10: Public repository accessible

### Phase 2: Article (10 requirements)
- DOC-01: Title with keywords
- DOC-02: Abstract (objective, context, methodology, results)
- DOC-03: Introduction (context, problem, objective, justification)
- DOC-04: Problem explanation (real case: source code compression)
- DOC-05: Literature review (Qualis articles + theses)
- DOC-06: Computational application (algorithms, structures, complexities)
- DOC-07: Results analysis (theoretical + practical comparison)
- DOC-08: Conclusions & future work (3 paragraphs mandatory)
- DOC-09: Writing quality (Portuguese, clarity, objectivity)
- DOC-10: SBC format (8-10 pages total)

### Phase 3: Presentation (9 requirements)
- SLD-01: Slide 1 (Group presentation)
- SLD-02: Slides 2-3 (Problem explanation)
- SLD-03: Slide 4 (Related work)
- SLD-04: Slides 5-6 (Algorithms & structures)
- SLD-05: Slides 7-9 (Experiments & analysis)
- SLD-06: Slide 10 (Conclusions & future work)
- SLD-07: Repository link on slides
- SLD-08: PDF format, max 10 slides, adequate visual quality
- SLD-09: Upload to Moodle before presentation

### Phase 4: Defense (7 requirements)
- VAL-01: All students present
- VAL-02: Subject mastery demonstrated
- VAL-03: Technical correctness verified
- VAL-04: Visual quality adequate
- VAL-05: Clarity, objectivity, conciseness
- VAL-06: Novel contribution identified
- VAL-07: Learning levels achieved (ANALYSIS, EVALUATION, CREATION)

## Codebase Summary

**Repository:** https://github.com/GabryelBoer/huffman-lzw-compression

**Technology Stack:**
- Language: Python 3.11+
- Algorithms: Huffman (heap-based), LZW (hash dictionary)
- Case Study: Source code compression (.py, .c files) + access.log baseline
- Metrics: Compression ratio, time (ms), memory (KB), entropy, lexical repetition

**Structure:**
```
src/
  huffman/      # Huffman implementation
  lzw/          # LZW implementation
  io/           # Bitstream I/O
  benchmark/    # Comparison & metrics
data/           # Test files (.py, .c, .log)
results/        # CSV outputs
benchmark-plots/# PNG graphs
tests/          # Round-trip validation
```

**Validation:**
- Round-trip tests: SHA-256 verify (lossless)
- Benchmark runs on: requests_sessions.py, jansson_dump.c, access.log, etc.
- Outputs: CSV metrics + PNG graphs

## Key Findings (Current)

From benchmark run (in GitHub repo):

| Metric | Huffman | LZW | Winner |
|--------|---------|-----|--------|
| Avg compression ratio | 1.43 | 1.87 | LZW (esp. logs) |
| Memory usage | Low (20-110 KB) | High (260-870 KB) | Huffman |
| Decompression speed | Medium | Fast | LZW |
| High-entropy files | Good | Poor | Huffman |
| Repetitive code (C) | Medium | Best | LZW |

**Conclusion (draft):** No absolute winner. Trade-offs by file type.
- Huffman: Best for entropy, memory-constrained
- LZW: Best for repetitive patterns, speed

## Next Steps

1. **Human tasks (Phases 2–3 wrap-up):** substituir autoria placeholder em artigo.tex E slides/slides.tex (sincronizar nomes), recompilar ambos, inspecionar PDFs visualmente (repo GitHub público ✓ confirmado em 2026-07-10)
2. **Moodle:** upload de artigo.pdf e slides/apresentacao.pdf após resolver autoria (SLD-09)
3. **Phase 4 (humano):** preencher DIA-DA-DEFESA.md (nomes, confirmações VAL-01, divisão de falas/Q&A), realizar ≥2 ensaios cronometrados, montar backups do DEMO-CHECKLIST.md
4. **Repo:** decidir se sincroniza o remoto (local 16 commits à frente; remoto curado sem article/slides/.planning — ver 04-AUDIT.md)

---

*State initialized: 2026-07-09*
*Last phase transition: Phase 4 → prep complete, awaiting human rehearsals and defense day (2026-07-10)*
*All GSD-executable phases (1–4) complete*
