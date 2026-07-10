# Checklist da Demo Live + Plano de Contingência

**Contexto:** o professor pode acessar o repositório GitHub durante a apresentação e pedir execução ao vivo.
**Repo público:** `https://github.com/GabryelBoer/huffman-lzw-compression`
**Status verificado em 2026-07-10 (Task 0):** clone fresco + `python3 -m venv .venv` + `pip install -r requirements.txt` + `bash run-all.sh` funcionou de ponta a ponta (12 registros, gráficos gerados, 14/14 testes no clone). Contingência commitada no remoto: 7 CSVs em `results/` + 3 PNGs em `benchmark-plots/`.

---

## 1. Pré-defesa (véspera — responsável: __________)

- [ ] Confirmar que o repo continua **público**: abrir a URL em janela anônima do browser.
- [ ] Rodar o teste de clone fresco na véspera (repetir o que foi validado na Task 0):
  ```bash
  git clone https://github.com/GabryelBoer/huffman-lzw-compression /tmp/demo-teste
  cd /tmp/demo-teste
  python3 -m venv .venv && source .venv/bin/activate
  pip install -r requirements.txt
  bash run-all.sh
  ```
  Saída esperada: `Benchmark concluido: 12 registros em .../results/compression-summary.csv` + `Graficos salvos em .../benchmark-plots`.
- [ ] Rodar os testes no clone: `.venv/bin/python -m pytest tests/` → **14 passed**.
- [ ] Deixar um clone local PRONTO (com venv já criado) no notebook da apresentação — é o plano B se a internet falhar.
- [ ] Browser do notebook da apresentação com **aba já aberta** no repo GitHub (página inicial, README renderizado com os gráficos).
- [ ] ATENÇÃO: `run-all.sh` exige o venv criado (`\.venv/bin/python` no script). Sem `python3 -m venv .venv` + `pip install`, a execução falha. Nunca pular os passos do README.

## 2. Roteiro da demo live (2–3 min)

1. **(30 s) Estrutura:** abrir o repo no browser e mostrar `src/` — módulos separados: `src/huffman/`, `src/lzw/`, `src/io/bitstream.py`, `src/benchmark/`. Frase: "implementação do zero, modular, com testes".
2. **(60–90 s) Execução:** no terminal do clone local já preparado, rodar `bash run-all.sh`. Enquanto roda (poucos segundos), narrar: "o script comprime e descomprime os 6 arquivos com os 2 algoritmos, valida SHA-256 em cada um e gera CSVs e gráficos".
3. **(30–60 s) Resultado:** abrir `results/compression-summary.csv` (ou o README, que já exibe os gráficos) e apontar 2 números: log 6.76 pelo LZW e alta entropia 0.75 (expansão). Frase de fechamento: "qualquer pessoa reproduz isso com 4 comandos do README".

**Opção mais segura (se o tempo estiver apertado):** pular a execução (passo 2) e mostrar direto os resultados commitados — README renderiza os 3 PNGs no próprio GitHub.

## 3. Contingência nível 1 — execução live falha

Sintoma: `run-all.sh` dá erro na frente do professor (venv quebrado, dependência, path).

- **Ação imediata (não depurar ao vivo!):** "temos os resultados da última execução commitados no repositório" → abrir no GitHub:
  - `results/compression-summary.csv` (12 linhas, uma por experimento, com hash de validação)
  - `benchmark-plots/compression-ratio.png`, `tempo-execucao.png`, `memoria.png`
  - O README já exibe os 3 gráficos renderizados — caminho mais rápido.
- Frase de transição: "o benchmark é reproduzível — estes são os artefatos gerados pelo próprio script; o professor pode clonar e re-executar seguindo o README".

## 4. Contingência nível 2 — sem internet

Sintoma: GitHub não abre / rede da sala caiu.

- Usar o **clone local já preparado** (item 1): mostrar estrutura com `ls src/`, rodar `bash run-all.sh` localmente, abrir os PNGs de `benchmark-plots/` no visualizador de imagens.
- Slides e artigo: usar os **PDFs offline** (item 5) — nenhum passo da apresentação depende de internet.

## 5. Itens de backup (levar no dia)

- [ ] PDF dos slides em **2 dispositivos** (notebook principal + notebook reserva de outro integrante).
- [ ] PDF do artigo nos mesmos 2 dispositivos.
- [ ] **Pendrive** com: PDF dos slides, PDF do artigo, clone do repo (com `results/` e `benchmark-plots/` populados).
- [ ] Celular com o repo GitHub acessível (4G como rota alternativa de internet, se permitido).

---

## Matriz de decisão rápida (colar no notebook)

| Situação | Ação |
|----------|------|
| Tudo funciona | Demo completa (estrutura → run-all.sh → resultados) |
| run-all.sh falha | NÃO depurar. GitHub → README com gráficos + CSV commitado |
| Sem internet | Clone local + PNGs locais + PDFs offline |
| Sem notebook principal | Notebook reserva ou pendrive em máquina da sala |
