# Observatório Econômico de Caratinga — MG

**Iniciativa autoral independente · Por Wanderson Castro · Economista · CORECON-SP nº 38114**

Painel de inteligência territorial sobre o mercado de trabalho formal e a economia de
**Caratinga (MG)** — IBGE **3113404**, Vale do Rio Doce / Matas de Minas.

> ⚠️ **Iniciativa independente.** Não constitui produto institucional de Conselho de
> Economia, Prefeitura ou Delegacia. As análises e teses são de responsabilidade do autor.
> Os dados primários são públicos e auditáveis (CAGED/MTE, RAIS, IBGE).

---

## ▶️ Como abrir

Abra o arquivo **`index.html`** no navegador (duplo clique) ou acesse a versão publicada
(GitHub Pages). O painel é **autossuficiente**: funciona offline, sem instalação, e os
gráficos carregam a partir de dados embutidos — se houver `data/caged_latest.json`,
ele é usado automaticamente; caso contrário, o painel cai para os dados de demonstração.

## 📂 Estrutura da pasta

```
Observatorio_Caratinga/
├── index.html                       ← Painel principal (abra este arquivo)
├── prefeitura-de-caratinga-logo-4.png   ← Logo usado no cabeçalho
├── README.md                        ← Este arquivo
│
├── data/        ← Dados em JSON (CAGED + âncoras oficiais IBGE)
│   ├── caged_latest.json   (série mensal + seções CNAE + âncoras IBGE)
│   └── metadata.json       (versão, fontes e data de atualização)
├── images/      ← Imagens e preview social (og-preview.png)
├── docs/        ← Notas técnicas, relatórios, apresentações
└── scripts/     ← Coleta / ETL / atualização (GitHub Actions)
```

## 📊 O painel (8 abas)

1. **CAGED Mensal** — admissões, desligamentos, saldo e estoque, com validação pelo print oficial.
2. **Caratinga em Números (IBGE)** — população, PIB, salário, café e ocupação (dados oficiais).
3. **Perfil dos Empregos** — escolaridade, gênero, faixa etária e salário por setor.
4. **Economia Setorial** — estrutura CNAE com *drill-down* clicável (seção → divisão → subclasse).
5. **Diagnóstico Polo Regional** — função de Caratinga como hub de ~30 municípios.
6. **Qualificação & Capital Humano** — UNEC, retenção de jovens e sobrequalificação.
7. **Projeções 2026–2030** — três cenários + comparativo com polos do Leste de Minas.
8. **Diagnóstico Estrutural + Teses** — quociente locacional, rotatividade e 5 teses autorais.

## 🔢 Âncoras oficiais (IBGE — Caratinga 3113404)

| Indicador | Valor | Fonte / ano |
|---|---|---|
| População | **87.360 hab** | Censo 2022 |
| PIB per capita | **R$ 32.870** | PIB Municipal 2023 (262º de 853 em MG) |
| PIB total | **R$ 2,28 bi** | Contas Municipais 2021 |
| Pessoal ocupado formal | **26.892** | CEMPRE 2023 |
| Emprego com carteira | **~21,8 mil** | IBGE Cidades |
| Salário médio formal | **1,9 SM** (~R$ 2,2 mil) | IBGE 2023 |
| Café (lavoura) | **~330 mil sacas · 13.600 ha** | entre os 20 maiores de MG · IBGE PAM / EMATER-MG |

> A série mensal do CAGED é **estimativa calibrada** (a substituir por microdados oficiais);
> as âncoras acima são **oficiais**. O estoque do painel (~21,5 mil) está alinhado ao
> emprego com carteira assinada do IBGE (~21,8 mil).

## 🔄 Atualização

`scripts/` + GitHub Actions (`.github/workflows`) atualizam `data/` periodicamente
(CAGED é liberado ~dia 20 de cada mês). O painel lê `data/caged_latest.json` quando disponível.

---

**Autoria:** Wanderson Castro · Economista · CORECON-SP nº 38114 · iniciativa técnica e independente.
