# Phase 4 Audit: Preparação para Defesa Oral

**Data de execução:** 2026-07-10
**Plano:** `.planning/phases/04-defense/04-01-PLAN.md`
**Status geral:** ✅ Todas as tasks (0–4) executadas. Deliverables completos. Pendências humanas listadas ao final.

---

## Resultado por Task

### Task 0 — Sanity check da demo live: ✅ PASSOU (com 1 finding relevante)

| Verificação | Resultado |
|-------------|-----------|
| `./run-all.sh` local | ✅ Exit 0 — "Benchmark concluido: 12 registros" + gráficos gerados |
| `pytest tests/` (via `.venv/bin/python -m pytest`) | ✅ **14/14 passed** (0.05 s) |
| Clone fresco real do GitHub | ✅ `git clone https://github.com/GabryelBoer/huffman-lzw-compression` funcionou (repo público e acessível) |
| README seguido literalmente no clone | ✅ `python3 -m venv .venv` → `pip install -r requirements.txt` → `bash run-all.sh` — **zero divergências entre README e realidade**. Benchmark completo (12 registros) e gráficos gerados no clone |
| pytest no clone fresco | ✅ 14/14 passed |
| Contingência commitada no remoto | ✅ 7 CSVs em `results/` + 3 PNGs em `benchmark-plots/` presentes no HEAD remoto (`6fbb2fb`) |

**O risco documentado no research (`.venv/bin/python` hardcoded em run-all.sh) NÃO se materializou:** o README instrui explicitamente a criação do venv antes de rodar o script, e o fluxo funciona de ponta a ponta. Nenhuma correção de README/run-all.sh foi necessária.

### 🔶 FINDING (não crítico, mas requer decisão do grupo): divergência local ↔ remoto

- O `main` local está **16 commits à frente** de `origin/main` (0 atrás — histórias compatíveis, fast-forward possível).
- O HEAD remoto é `6fbb2fb chore: remove article e slides do repositorio remoto` — ou seja, o repo público foi **deliberadamente curado** para NÃO conter `article/`, `slides/` nem `.planning/`.
- Os 16 commits locais não pushados incluem `.planning/` (Phases 1–4), o artigo LaTeX e os slides.
- **Impacto na defesa:** NENHUM — o remoto (o que o professor vê) está completo e funcional para a demo. O clone fresco validou exatamente o estado remoto.
- **Decisão conservadora tomada:** NÃO fazer push. A curadoria do remoto parece intencional (commit explícito de remoção). A "decisão de visibilidade" do plano fica resolvida de fato: `.planning/` já NÃO está exposto no repo público.
- **Ação humana:** grupo confirmar que o estado do remoto é o desejado para o dia da defesa (ver Pendências).

### Task 1 — ROTEIRO.md: ✅ COMPLETO
- Speaker notes para os 10 frames de `slides/slides.tex`; abertura de 2 min (quem somos → o que fizemos → contribuição).
- Cada slide: mensagem central (1 frase) + 2–4 apoios + transição.
- Slides 7–9 com narrativa "o que o gráfico mostra → por quê → o que concluímos".
- Timing acumulado soma 14:30–15:00 (≤15 min) com checkpoints em 5:00 / 10:00 / 13:00 e planos de corte por checkpoint.
- Fechamento nomeia a contribuição inédita explicitamente ("framework de benchmark que correlaciona entropia de Shannon e repetição lexical...").
- Tabela final de "números que não podem sair errados" conferida contra `article/artigo.tex`.

### Task 2 — QA-BANK.md: ✅ COMPLETO
- **22 perguntas** (≥20): Algoritmos 6, Complexidade 4, Resultados 7, Metodologia 4, Níveis de aprendizagem 1.
- Respostas de 2–5 frases com números exatos do artigo (1.73/1.66; 1.90 vs 1.73; 1.28 vs 0.75 / −33.6%; 6.76 / 85.2%; −1.6%; 110.4 vs 870.7 KB; 13.4 vs 34.1 ms; 6.02 bits; rep. lexical 0.20/0.13/0.00; SHA-256 12/12; 14 testes).
- VAL-07 mapeado explicitamente (Q22: ANÁLISE / AVALIAÇÃO / CRIAÇÃO).
- Seção final "Pergunta sem resposta preparada" com protocolo de 3 passos + exemplo aplicado + proibições.

### Task 3 — DEMO-CHECKLIST.md: ✅ COMPLETO
- Pré-defesa (véspera): repo público, re-teste de clone fresco (comandos exatos validados na Task 0), clone local pronto, aba do GitHub aberta.
- Roteiro da demo live de 2–3 min (estrutura → execução → resultados) com narração sugerida.
- Contingência nível 1 (execução falha → CSVs/PNGs commitados no GitHub, README renderiza os gráficos) e nível 2 (sem internet → clone local + PDFs offline).
- Itens de backup: PDFs em 2 dispositivos + pendrive + matriz de decisão rápida.

### Task 4 — DIA-DA-DEFESA.md: ✅ COMPLETO
- **VAL-01 em destaque máximo** no topo (nota ZERO se faltar integrante), com confirmações D-7/D-1 e tabela de presença por integrante.
- Logística (15 min antes na sala, projetor, áudio, slides abertos, adaptador HDMI).
- Postura (falar para a banca, transições combinadas).
- Divisão de falas por bloco de slides e divisão do Q&A por categoria (placeholders `[Nome ___]` para o grupo preencher).
- ≥2 ensaios cronometrados com tabela de registro de tempos por checkpoint.

---

## Tabela VAL-01–07

| Req | Critério | Status | Evidência |
|-----|----------|--------|-----------|
| VAL-01 | Todos presentes (nota ZERO se faltante) | ⚠ **Requer ação humana** | `DIA-DA-DEFESA.md` §VAL-01 — confirmações D-7/D-1 e presença no dia são atos humanos; material de controle pronto |
| VAL-02 | Domínio do assunto | ✓ Preparado | `ROTEIRO.md` (10 slides) + `QA-BANK.md` (22 Q&A); estudo pelo grupo é ação humana |
| VAL-03 | Correção técnica | ✓ Preparado | Números do Q&A e roteiro conferidos contra `article/artigo.tex` (Tabelas 1–3) nesta execução |
| VAL-04 | Qualidade visual/áudio/postura | ⚠ **Requer ação humana** | Slides ✓ (Phase 3); postura/áudio dependem de ensaio — checklist em `DIA-DA-DEFESA.md` |
| VAL-05 | Clareza, objetividade, concisão | ⚠ **Requer ação humana** | Roteiro com timing ≤15 min pronto; ≥2 ensaios cronometrados pendentes (tabela de registro criada) |
| VAL-06 | Contribuição inédita identificável | ✓ Preparado | Nomeada no fechamento do `ROTEIRO.md` e na Q22/Q19 do `QA-BANK.md`: framework entropia de Shannon + repetição lexical |
| VAL-07 | Níveis ANÁLISE/AVALIAÇÃO/CRIAÇÃO | ✓ Preparado | `QA-BANK.md` Q22 — resposta modelo conectando os três níveis |

---

## Findings do clone fresco (detalhe)

1. **Clone público OK** — `git clone` sem autenticação funcionou; professor conseguirá acessar live.
2. **README fiel à realidade** — os 4 comandos do "Como Executar" reproduzem o benchmark completo sem nenhum ajuste. Zero divergências registradas.
3. **Contingência disponível** — `results/*.csv` (7 arquivos) e `benchmark-plots/*.png` (3 arquivos) commitados no HEAD remoto; README do remoto renderiza os gráficos.
4. **Remoto curado ≠ local** — remoto não contém `article/`, `slides/`, `.planning/` (removidos em `6fbb2fb`); local está 16 commits à frente. Sem impacto na demo; ver pendência 2.
5. Diretório de teste usado: `~/.claude/jobs/89c39027/tmp/fresh-clone-test/` (descartável).

## Decisões registradas (conservadoras)

1. **Nenhum push ao remoto** — curadoria do repo público parece intencional; push exporia `.planning/`, artigo e slides. Decisão delegada ao grupo.
2. **Modificações locais não commitadas fora do escopo** (`README.md` +26/−5 com tabelas de complexidade de sessão anterior; jitter de timing em `results/*.csv` e `benchmark-plots/tempo-execucao.png` gerado pelas re-execuções do benchmark) — **deixadas como estavam**, não pertencem à Phase 4. Registradas como pendência 3.
3. Deliverables mantidos em `.planning/` versionado localmente — como o `.planning/` não é pushado ao remoto, o material de estudo não fica exposto ao professor (resolve a "decisão de visibilidade" do plano a favor da privacidade).

## Pendências humanas

1. **[VAL-01 — crítico]** Preencher nomes/telefones e executar confirmações D-7/D-1 em `DIA-DA-DEFESA.md`.
2. **[Repo]** Confirmar que o estado do remoto (`6fbb2fb`, sem artigo/slides/planning) é o desejado para o dia da defesa; se quiserem atualizar resultados/README no remoto, fazer push seletivo e re-testar clone fresco na véspera (`DEMO-CHECKLIST.md` §1).
3. **[Higiene do worktree]** Decidir commit/descarte das modificações locais pré-existentes (README.md com tabelas Big-O + CSVs/PNG re-gerados).
4. **[Ensaios]** Realizar ≥2 ensaios cronometrados e registrar tempos na tabela de `DIA-DA-DEFESA.md`; preencher divisão de falas e de categorias de Q&A.
5. **[Slides]** Nomes e matrículas ainda são placeholder em `slides/slides.tex` (pendência herdada da Phase 3) — preencher e recompilar o PDF antes da defesa.
6. **[Backups]** Gerar PDFs (slides + artigo) e montar o pendrive conforme `DEMO-CHECKLIST.md` §5.

---
*Audit gerado na execução da Phase 4 — 2026-07-10*
