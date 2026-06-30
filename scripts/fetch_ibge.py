#!/usr/bin/env python3
"""
Observatório Econômico de Caratinga — Pipeline ANUAL (IBGE)
Busca indicadores anuais via API SIDRA do IBGE e grava data/ibge_latest.json.

Indicadores (atualizam ~1x/ano conforme o IBGE divulga):
  - População: Censo 2022 (tabela 9514) + estimativa anual (tabela 6579)
  - PIB municipal a preços correntes e PIB per capita (tabela 5938)

Fonte: servicodados.ibge.gov.br (API v3 /agregados)
Município: Caratinga-MG (IBGE 3113404)

Robusto: cada chamada é isolada; se uma falhar, mantém o valor anterior
gravado em data/ibge_latest.json (não derruba o restante).
"""
import json
import logging
from datetime import datetime, timezone
from pathlib import Path

import requests

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)

MUNICIPIO = "3113404"
NOME = "Caratinga"
UF = "MG"
DATA_DIR = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)
OUT = DATA_DIR / "ibge_latest.json"


def sidra(table, var, period="last 1"):
    """Retorna (valor_float, ano_str) do último período não-nulo, ou (None, None)."""
    url = (
        f"https://servicodados.ibge.gov.br/api/v3/agregados/{table}"
        f"/periodos/{period}/variaveis/{var}"
        f"?localidades=N6[{MUNICIPIO}]&formato=JSON"
    )
    try:
        r = requests.get(url, timeout=45)
        r.raise_for_status()
        serie = r.json()[0]["resultados"][0]["series"][0]["serie"]
        for ano in sorted(serie.keys(), reverse=True):
            v = serie[ano]
            if v not in (None, "-", "...", "..", "X", ""):
                try:
                    return float(str(v).replace(".", "").replace(",", ".")), ano
                except ValueError:
                    continue
    except Exception as exc:
        log.warning(f"SIDRA tabela {table} var {var}: {exc}")
    return None, None


def load_existing():
    if OUT.exists():
        try:
            return json.loads(OUT.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def main():
    log.info("=== IBGE (anual) — Caratinga 3113404 ===")
    now = datetime.now(timezone.utc).isoformat()
    data = load_existing()
    data["municipio"] = MUNICIPIO
    data["municipio_nome"] = NOME
    data["uf"] = UF
    obtidos = []

    # População — Censo 2022 (tabela 9514, variável 93)
    pop_censo, ano_censo = sidra(9514, 93, "2022")
    if pop_censo:
        data["populacao_censo"] = int(pop_censo)
        data["populacao_censo_ano"] = ano_censo
        obtidos.append("populacao_censo")

    # População — estimativa anual mais recente (tabela 6579, variável 9324)
    pop_est, ano_est = sidra(6579, 9324, "last 1")
    if pop_est:
        data["populacao_estimada"] = int(pop_est)
        data["populacao_estimada_ano"] = ano_est
        obtidos.append("populacao_estimada")

    # PIB a preços correntes (tabela 5938, variável 37) — em R$ 1.000
    pib_mil, ano_pib = sidra(5938, 37, "last 1")
    if pib_mil:
        data["pib_total_mil_reais"] = int(pib_mil)
        data["pib_ano"] = ano_pib
        obtidos.append("pib_total_mil_reais")

    # PIB per capita (tabela 5938, variável 6575) — em R$
    pibpc, ano_pibpc = sidra(5938, 6575, "last 1")
    if pibpc:
        data["pib_per_capita"] = round(pibpc, 2)
        data["pib_per_capita_ano"] = ano_pibpc
        obtidos.append("pib_per_capita")
    elif pib_mil:
        base_pop = data.get("populacao_estimada") or data.get("populacao_censo")
        if base_pop:
            data["pib_per_capita"] = round(pib_mil * 1000 / base_pop, 2)
            data["pib_per_capita_ano"] = ano_pib
            data["pib_per_capita_calculado"] = True
            obtidos.append("pib_per_capita(calc)")

    data["updated_at"] = now
    data["fonte"] = "IBGE — API SIDRA (Censo 2022, Estimativas de População, PIB dos Municípios)"
    data["status"] = "ok" if obtidos else "sem_dados_mantendo_anteriores"

    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    log.info(f"Gravado {OUT.name} — campos obtidos: {obtidos or 'nenhum (mantidos anteriores)'}")


if __name__ == "__main__":
    main()
