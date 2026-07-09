# Phase 3 Research: Slides de Apresentação

**Date:** 2026-07-09
**Scope:** Ferramenta de geração, estrutura obrigatória, fontes de conteúdo, restrições

---

## 1. Ferramenta: LaTeX Beamer (decisão)

**Verificado localmente:** `beamer.cls` presente em `/usr/local/texlive/2026basic/` — nenhuma instalação extra necessária.

**Justificativa:**
- Mesmo toolchain do artigo (pdflatex já validado na máquina nesta fase)
- PDF nativo (requisito Moodle: SLD-09) — sem conversão
- Visual acadêmico consistente com o artigo
- Reutiliza diretamente as figuras PNG existentes
- Alternativas descartadas: Marp (instalação nova), PowerPoint (manual, fora do fluxo reproduzível), HTML→PDF (frágil)

**Tema recomendado:** `metropolis` NÃO disponível no basictex por padrão — usar tema built-in limpo (`Madrid`, `Frankfurt` ou `default` com customização mínima). Verificar com `kpsewhich beamerthememetropolis.sty` na Task 0; fallback: `Madrid` (sempre presente, header compacto, cores sóbrias).

**Compilação:** `pdflatex -interaction=nonstopmode slides.tex` (2 passes para outline/refs). Sem BibTeX — slides não usam bibliografia formal (trabalhos relacionados citados inline: "Huffman (1952)", "Welch (1984)").

## 2. Estrutura obrigatória (professor — ROADMAP Phase 3)

| Slide | Conteúdo | Fonte no artigo |
|-------|----------|-----------------|
| 1 | Grupo: nomes, matrículas, disciplina AED-II | ⚠ INPUT HUMANO (placeholder até nomes reais) |
| 2–3 | Problema: por quê comprimir código-fonte, importância | Seções Introdução + Problema de Pesquisa |
| 4 | Trabalhos relacionados | Seção Trabalhos Relacionados (6 obras principais) |
| 5–6 | Algoritmos: Huffman (heap/árvore), LZW (dicionário), complexidades | Seção Fundamentação Teórica + Tabela 1 |
| 7–9 | Experimentos: gráficos taxa/tempo/memória, análise | Seção Resultados + 3 figuras PNG + Tabelas 2–3 |
| 10 | Conclusão: qual melhor para código-fonte, futuras pesquisas | Seção Conclusões |
| (1 ou 10) | Link GitHub (acessado ao vivo na defesa) | `github.com/GabryelBoer/huffman-lzw-compression` |

**Limite HARD: 10 slides** (sem contar... não — 10 total, incluindo capa). Título/capa = slide 1 (grupo).

## 3. Figuras disponíveis

- `benchmark-plots/compression-ratio.png` (51.7 KB)
- `benchmark-plots/tempo-execucao.png` (55.1 KB)
- `benchmark-plots/memoria.png` (50.6 KB)
- (cópias em `article/fig-*.png` — usar as de `benchmark-plots/` como fonte canônica; ou copiar para `slides/`)

## 4. Restrições e armadilhas

| Restrição | Implicação |
|-----------|------------|
| Máx 15 min, ~1.5 min/slide | Slides auto-explicativos mas ENXUTOS — bullets, não parágrafos |
| Legível sem narração | Fonte ≥ tamanho padrão beamer; máx ~6 bullets/slide |
| Sem vídeos/gravações/fotos | Conteúdo estático, demonstração live só do repositório |
| Sem poluição visual | 1 ideia central por slide; gráficos ocupam slide quase inteiro |
| Overflow de texto Beamer | Frame com muito conteúdo corta silenciosamente — revisar cada frame no PDF |
| Acentuação PT-BR | UTF-8 + T1 fontenc desde o início (lição da Phase 2 — NUNCA acentuar nomes de arquivos/labels) |
| Números do benchmark | Copiar EXATOS do artigo (taxa 1.73/1.66, memória 110/871 KB, log 6.76, etc.) |

## 5. Dados-chave para os slides de resultados (extraídos do artigo)

- **Python médio (requests_sessions.py):** Huffman taxa 1.73 vs LZW 1.66; memória 110 KB vs 871 KB; descompressão LZW 2.5× mais rápida
- **C (jansson_dump.c):** LZW vence taxa (1.90 vs 1.73) — maior repetição lexical (0.20)
- **Alta entropia (6.02 bits):** Huffman 1.28 vs LZW 0.75 (LZW EXPANDE 33.6%)
- **Arquivo pequeno (1 KB):** LZW expande (−1.6%); Huffman 15.9% economia
- **Log baseline:** LZW 6.76 (85.2% economia) vs Huffman 1.89 — contraste extremo
- **Conclusão:** sem vencedor absoluto; Huffman = memória/entropia/pequenos; LZW = repetição/velocidade descompressão

## 6. Escopo Phase 3

Criar do zero (não existe slides/ ainda):
1. `slides/slides.tex` (Beamer, 10 frames)
2. `slides/apresentacao.pdf` (compilado)
3. Cópia das 3 figuras ou path relativo `../benchmark-plots/`

**Timeline:** 1–2 dias (conteúdo já existe no artigo; trabalho é destilação + layout)

---
*Research completed: 2026-07-09 (inline — Beamer verificado localmente, conteúdo derivado do artigo Phase 2)*
