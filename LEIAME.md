# Observatório Econômico de Caratinga — MG

**Iniciativa autoral independente**
**Por Wanderson Castro · Economista · CORECON-SP nº 38114**

---

## Estrutura da pasta

```
Observatorio_Caratinga/
├── caratinga_observatorio.html      ← Painel principal (abrir este arquivo no navegador)
├── prefeitura-de-caratinga-logo-4.png   ← Logo da Prefeitura usado no cabeçalho
├── LEIAME.md                        ← Este arquivo
│
├── data/        ← Dados (CAGED, RAIS, IBGE) em JSON / CSV
├── images/      ← Imagens, gráficos exportados, capturas
├── docs/        ← Documentos analíticos, relatórios, notas técnicas
└── scripts/     ← Scripts de coleta, ETL, atualização automática
```

## O que vai em cada pasta

**`data/`** — séries temporais e bases de dados:
- `caged_latest.json` (saldos mensais por seção CNAE)
- `rais_*.csv` (estoques anuais)
- `metadata.json` (controle de versão e datas de atualização)
- `ibge_*.json` (dados de PIB municipal, PAM, Pesquisa Pecuária)

**`images/`** — recursos visuais:
- Logos adicionais (UNEC, cooperativas, selo Matas de Minas, etc.)
- `og-preview.png` (imagem de preview para compartilhamento social)
- Capturas de tela de relatórios externos
- Gráficos exportados

**`docs/`** — produção analítica:
- Notas técnicas autorais
- Relatórios mensais / trimestrais
- Apresentações (`.pptx`)
- Documentos Word (`.docx`) e PDFs derivados

**`scripts/`** — automação:
- `update_caged.py` (ETL CAGED → JSON)
- `update_rais.py` (ETL RAIS)
- `fetch_ibge.py` (chamadas SIDRA)
- Workflows GitHub Actions (`.yml`)

---

## Identificação técnica

| Campo | Valor |
|---|---|
| Município | Caratinga |
| UF | Minas Gerais (MG) |
| Código IBGE | **3113404** |
| Microrregião | Caratinga (Vale do Rio Doce) |
| Mesorregião | Vale do Rio Doce |
| Indicação Geográfica | Matas de Minas (café) |
| Polo regional | ~30 municípios · ~250 mil habitantes |

---

## Fontes primárias

- **Novo CAGED / MTE** — admissões e desligamentos mensais
- **RAIS / MTE** — estoque anual de vínculos formais
- **IBGE SIDRA** — PIB municipal, PAM (café), Pesquisa Pecuária, Censo 2022
- **basedosdados.org** — microdados consolidados
- **Federação dos Cafeicultores das Matas de Minas** — dados da IG
- **INEP / MEC** — matrículas UNEC e demais

---

## Aviso

Este Observatório **não é produto institucional** de Conselho de Economia, Prefeitura ou Delegacia. É iniciativa técnica e voluntária do autor. Análises e teses interpretativas são de responsabilidade de Wanderson Castro. Os dados primários são públicos e auditáveis.
