# ============================================================
# GOLD INSTITUTIONAL EDGE — LIVE DASHBOARD
# Full single-page functional site with live data
# ============================================================

import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import requests
import plotly.graph_objects as go
from datetime import datetime, date
import pytz
import time

st.set_page_config(
    page_title="Gold Institutional Edge",
    page_icon="🏅",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── FULL CSS ─────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=DM+Sans:wght@300;400;500;600;700&display=swap');

:root {
  --gold: #C9922A;
  --gold-light: #F0C060;
  --bg: #080B12;
  --bg2: #0D1117;
  --bg3: #131920;
  --bg4: #1A2332;
  --border: rgba(201,146,42,0.15);
  --border-strong: rgba(201,146,42,0.35);
  --text: #E8E6DE;
  --text2: #8A9BB0;
  --text3: #4A5A6A;
  --green: #00D395;
  --green-dim: rgba(0,211,149,0.1);
  --green-border: rgba(0,211,149,0.25);
  --red: #FF4D6A;
  --red-dim: rgba(255,77,106,0.1);
  --red-border: rgba(255,77,106,0.25);
  --blue: #4A9EDB;
  --blue-dim: rgba(74,158,219,0.1);
  --amber: #F0A030;
  --amber-dim: rgba(240,160,48,0.1);
  --mono: 'JetBrains Mono', monospace;
  --sans: 'DM Sans', system-ui, sans-serif;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, .stApp {
  font-family: var(--sans) !important;
  background: var(--bg) !important;
  color: var(--text) !important;
  -webkit-font-smoothing: antialiased;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none; }

/* ── TOPBAR ── */
.topbar {
  background: var(--bg2);
  border-bottom: 1px solid var(--border);
  padding: 14px 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 100;
}
.topbar-left { display: flex; align-items: center; gap: 12px; }
.topbar-logo {
  font-family: var(--mono);
  font-size: 13px;
  font-weight: 700;
  color: var(--gold-light);
  letter-spacing: 0.05em;
}
.topbar-version {
  font-family: var(--mono);
  font-size: 10px;
  color: var(--text3);
  background: var(--bg3);
  border: 1px solid var(--border);
  padding: 2px 8px;
  border-radius: 4px;
}
.topbar-right { display: flex; align-items: center; gap: 16px; }
.live-badge {
  display: flex;
  align-items: center;
  gap: 6px;
  font-family: var(--mono);
  font-size: 10px;
  color: var(--green);
  letter-spacing: 0.1em;
  text-transform: uppercase;
}
.live-dot {
  width: 6px; height: 6px;
  border-radius: 50%;
  background: var(--green);
  animation: blink 1.4s infinite;
}
@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.2; }
}
.topbar-time {
  font-family: var(--mono);
  font-size: 11px;
  color: var(--text3);
}

/* ── PAGE WRAPPER ── */
.page { padding: 24px 32px 60px; max-width: 1400px; margin: 0 auto; }

/* ── HERO SIGNAL BANNER ── */
.hero-bull {
  background: linear-gradient(135deg, rgba(0,211,149,0.08) 0%, rgba(0,211,149,0.03) 100%);
  border: 1px solid var(--green-border);
  border-left: 4px solid var(--green);
  border-radius: 12px;
  padding: 24px 32px;
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
}
.hero-bear {
  background: linear-gradient(135deg, rgba(255,77,106,0.08) 0%, rgba(255,77,106,0.03) 100%);
  border: 1px solid var(--red-border);
  border-left: 4px solid var(--red);
  border-radius: 12px;
  padding: 24px 32px;
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
}
.hero-neutral {
  background: linear-gradient(135deg, rgba(240,160,48,0.08) 0%, rgba(240,160,48,0.03) 100%);
  border: 1px solid rgba(240,160,48,0.25);
  border-left: 4px solid var(--amber);
  border-radius: 12px;
  padding: 24px 32px;
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
}
.hero-left { display: flex; align-items: center; gap: 20px; }
.hero-icon { font-size: 40px; line-height: 1; }
.hero-direction {
  font-size: 32px;
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1;
  margin-bottom: 4px;
}
.hero-sub {
  font-size: 13px;
  color: var(--text2);
  line-height: 1.5;
}
.hero-right { display: flex; gap: 12px; flex-wrap: wrap; }
.hero-tag {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 6px;
  padding: 8px 14px;
  font-family: var(--mono);
  font-size: 11px;
  text-align: center;
}
.hero-tag-label { color: var(--text3); margin-bottom: 2px; }
.hero-tag-value { color: var(--text); font-weight: 700; font-size: 13px; }

/* ── SCORE BAR ── */
.score-bar-wrap {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 16px 24px;
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  gap: 24px;
  flex-wrap: wrap;
}
.score-num-big {
  font-family: var(--mono);
  font-size: 36px;
  font-weight: 700;
  line-height: 1;
}
.score-label-area { flex: 1; min-width: 160px; }
.score-title { font-size: 13px; color: var(--text2); margin-bottom: 6px; }
.score-bar-bg {
  height: 8px;
  background: var(--bg4);
  border-radius: 4px;
  overflow: hidden;
  flex: 1;
  min-width: 120px;
}
.score-bar-fill {
  height: 100%;
  border-radius: 4px;
  transition: width 0.5s ease;
}
.score-verdict {
  font-family: var(--mono);
  font-size: 11px;
  padding: 4px 12px;
  border-radius: 20px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-weight: 700;
  white-space: nowrap;
}

/* ── METRIC GRID ── */
.metric-row {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 12px;
  margin-bottom: 20px;
}
.metric-row-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-bottom: 20px;
}
.metric-card {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 16px 18px;
  position: relative;
  overflow: hidden;
}
.metric-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: var(--border);
}
.metric-card.bull::before { background: var(--green); }
.metric-card.bear::before { background: var(--red); }
.metric-card.gold::before { background: var(--gold); }
.metric-card.blue::before { background: var(--blue); }
.metric-card.amber::before { background: var(--amber); }

.mc-label {
  font-family: var(--mono);
  font-size: 9px;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--text3);
  margin-bottom: 8px;
}
.mc-value {
  font-family: var(--mono);
  font-size: 20px;
  font-weight: 700;
  color: var(--text);
  line-height: 1;
  margin-bottom: 4px;
}
.mc-sub {
  font-size: 11px;
  color: var(--text3);
  margin-top: 4px;
}
.mc-green { color: var(--green) !important; }
.mc-red   { color: var(--red)   !important; }
.mc-gold  { color: var(--gold-light) !important; }
.mc-blue  { color: var(--blue)  !important; }
.mc-amber { color: var(--amber) !important; }

/* ── SECTION HEADER ── */
.sec-head {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 12px;
  margin-top: 28px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.sec-head::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--border);
}

/* ── CHART CARD ── */
.chart-card {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 20px;
}
.chart-card-header {
  padding: 14px 20px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.chart-card-title {
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text2);
}

/* ── CONFLUENCE CHECKLIST ── */
.checklist {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: 10px;
  overflow: hidden;
  margin-bottom: 20px;
}
.checklist-header {
  background: rgba(201,146,42,0.06);
  border-bottom: 1px solid var(--border);
  padding: 12px 18px;
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.15em;
  color: var(--gold-light);
  text-transform: uppercase;
}
.check-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 12px 18px;
  border-bottom: 1px solid rgba(201,146,42,0.05);
}
.check-item:last-child { border-bottom: none; }
.check-icon {
  font-size: 14px;
  margin-top: 1px;
  flex-shrink: 0;
  width: 20px;
  text-align: center;
}
.check-body { flex: 1; }
.check-name {
  font-size: 13px;
  font-weight: 500;
  color: var(--text);
  margin-bottom: 2px;
}
.check-name.pass { color: var(--green); }
.check-name.fail { color: var(--text3); }
.check-name.warn { color: var(--amber); }
.check-detail { font-size: 11px; color: var(--text3); line-height: 1.4; }
.check-right {
  font-family: var(--mono);
  font-size: 11px;
  font-weight: 700;
  white-space: nowrap;
  padding: 2px 8px;
  border-radius: 4px;
}
.check-right.pass { color: var(--green); background: var(--green-dim); }
.check-right.fail { color: var(--red);   background: var(--red-dim);   }
.check-right.warn { color: var(--amber); background: var(--amber-dim); }
.check-right.info { color: var(--blue);  background: var(--blue-dim);  }

/* ── TRADE LEVELS ── */
.trade-panel {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: 10px;
  overflow: hidden;
  margin-bottom: 20px;
}
.trade-panel-header {
  background: rgba(201,146,42,0.06);
  border-bottom: 1px solid var(--border);
  padding: 12px 18px;
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.15em;
  color: var(--gold-light);
  text-transform: uppercase;
}
.trade-level-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 11px 18px;
  border-bottom: 1px solid rgba(201,146,42,0.05);
}
.trade-level-row:last-child { border-bottom: none; }
.tl-left { display: flex; align-items: center; gap: 10px; }
.tl-dot {
  width: 8px; height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}
.tl-name { font-size: 13px; color: var(--text2); }
.tl-desc { font-size: 11px; color: var(--text3); }
.tl-price {
  font-family: var(--mono);
  font-size: 15px;
  font-weight: 700;
  color: var(--text);
}

/* ── COT HISTORY ── */
.cot-row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 18px;
  border-bottom: 1px solid rgba(201,146,42,0.05);
}
.cot-row:last-child { border-bottom: none; }
.cot-date { font-family: var(--mono); font-size: 11px; color: var(--text3); width: 90px; flex-shrink: 0; }
.cot-bar-wrap { flex: 1; height: 6px; background: var(--bg4); border-radius: 3px; overflow: hidden; }
.cot-bar-fill { height: 100%; border-radius: 3px; }
.cot-val { font-family: var(--mono); font-size: 11px; font-weight: 700; width: 80px; text-align: right; flex-shrink: 0; }

/* ── ALERTS PANEL ── */
.alert-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 10px 18px;
  border-bottom: 1px solid rgba(201,146,42,0.05);
}
.alert-item:last-child { border-bottom: none; }
.alert-time { font-family: var(--mono); font-size: 10px; color: var(--text3); width: 70px; flex-shrink: 0; padding-top: 2px; }
.alert-msg { font-size: 12px; color: var(--text2); line-height: 1.5; }

/* ── KILL ZONE INDICATOR ── */
.kz-on {
  display: inline-flex; align-items: center; gap: 6px;
  background: var(--green-dim);
  border: 1px solid var(--green-border);
  border-radius: 6px;
  padding: 4px 10px;
  font-family: var(--mono);
  font-size: 10px;
  color: var(--green);
  font-weight: 700;
  letter-spacing: 0.05em;
}
.kz-off {
  display: inline-flex; align-items: center; gap: 6px;
  background: rgba(74,90,106,0.15);
  border: 1px solid rgba(74,90,106,0.2);
  border-radius: 6px;
  padding: 4px 10px;
  font-family: var(--mono);
  font-size: 10px;
  color: var(--text3);
  letter-spacing: 0.05em;
}

/* ── INFO BOX ── */
.info-strip {
  background: var(--blue-dim);
  border: 1px solid rgba(74,158,219,0.2);
  border-radius: 8px;
  padding: 10px 16px;
  font-size: 12px;
  color: var(--text2);
  margin-bottom: 16px;
  line-height: 1.5;
}

/* ── FOOTER ── */
.footer {
  text-align: center;
  padding: 24px;
  font-family: var(--mono);
  font-size: 10px;
  color: var(--text3);
  border-top: 1px solid var(--border);
  margin-top: 40px;
  letter-spacing: 0.05em;
}

/* ── STREAMLIT OVERRIDES ── */
div[data-testid="stButton"] button {
  background: var(--bg3) !important;
  color: var(--text2) !important;
  border: 1px solid var(--border) !important;
  border-radius: 6px !important;
  font-family: var(--mono) !important;
  font-size: 11px !important;
  padding: 6px 16px !important;
  letter-spacing: 0.05em !important;
}
div[data-testid="stButton"] button:hover {
  border-color: var(--gold) !important;
  color: var(--gold-light) !important;
}

/* ── RESPONSIVE ── */
@media (max-width: 900px) {
  .page { padding: 16px 16px 60px; }
  .metric-row { grid-template-columns: repeat(3, 1fr); }
  .metric-row-4 { grid-template-columns: repeat(2, 1fr); }
  .topbar { padding: 12px 16px; }
  .hero-left { gap: 12px; }
  .hero-direction { font-size: 24px; }
}
@media (max-width: 600px) {
  .metric-row { grid-template-columns: repeat(2, 1fr); }
  .hero-icon { font-size: 28px; }
  .hero-direction { font-size: 20px; }
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# DATA FUNCTIONS
# ══════════════════════════════════════════════════════════════

@st.cache_data(ttl=60)
def fetch_gold():
    try:
        tk   = yf.Ticker("GC=F")
        hist = tk.history(period="2d", interval="5m")
        if hist.empty:
            return None
        price    = round(float(hist["Close"].iloc[-1]), 2)
        prev     = round(float(hist["Close"].iloc[0]),  2)
        chg      = round(price - prev, 2)
        chg_pct  = round((chg / prev) * 100, 2)
        high_day = round(float(hist["High"].iloc[-288:].max()), 2)
        low_day  = round(float(hist["Low"].iloc[-288:].min()),  2)

        # VWAP
        today = hist[hist.index.date == hist.index[-1].date()]
        if not today.empty:
            today = today.copy()
            today["TP"]   = (today["High"] + today["Low"] + today["Close"]) / 3
            today["TPxV"] = today["TP"] * today["Volume"]
            vwap = round(
                float(today["TPxV"].cumsum().iloc[-1]
                      / today["Volume"].cumsum().iloc[-1]), 2
            )
        else:
            vwap = None

        return {
            "price": price, "prev": prev,
            "chg": chg, "chg_pct": chg_pct,
            "high": high_day, "low": low_day,
            "vwap": vwap,
            "above_vwap": price > vwap if vwap else None,
            "hist": hist,
        }
    except Exception:
        return None


@st.cache_data(ttl=300)
def fetch_options():
    try:
        gld  = yf.Ticker("GLD")
        xau  = yf.Ticker("GC=F")
        gp   = float(gld.history(period="1d")["Close"].iloc[-1])
        xp   = float(xau.history(period="1d")["Close"].iloc[-1])
        mult = xp / gp
        exp  = gld.options[0]
        ch   = gld.option_chain(exp)
        calls = ch.calls[ch.calls["openInterest"] > 10].copy()
        puts  = ch.puts[ch.puts["openInterest"]  > 10].copy()
        if calls.empty or puts.empty:
            return None
        pw  = float(puts.loc[puts["openInterest"].idxmax(),  "strike"])
        cw  = float(calls.loc[calls["openInterest"].idxmax(),"strike"])

        # max pain
        strikes = sorted(set(calls["strike"].tolist() + puts["strike"].tolist()))
        pain = {}
        for s in strikes:
            pain[s] = (calls[calls["strike"] > s]["openInterest"].sum()
                     + puts[puts["strike"]  < s]["openInterest"].sum())
        mp = float(min(pain, key=pain.get))

        pc = round(puts["openInterest"].sum() / calls["openInterest"].sum(), 2)
        return {
            "put_wall":  round(pw  * mult, 2),
            "call_wall": round(cw  * mult, 2),
            "max_pain":  round(mp  * mult, 2),
            "pc_ratio":  pc,
            "expiry":    exp,
            "mult":      round(mult, 2),
            "error":     None,
        }
    except Exception as e:
        return {"error": str(e)}


@st.cache_data(ttl=3600)
def fetch_cot():
    try:
        url = (
            "https://publicreporting.cftc.gov/resource/jun7-fc8e.json"
            "?cftc_contract_market_code=088691"
            "&$order=report_date_as_yyyy_mm_dd DESC&$limit=12"
        )
        rows = requests.get(url, timeout=15).json()
        if len(rows) < 2:
            return None
        results = []
        for r in rows:
            ml = int(r.get("m_money_positions_long_all",  0))
            ms = int(r.get("m_money_positions_short_all", 0))
            results.append({
                "date":    r.get("report_date_as_yyyy_mm_dd","")[:10],
                "mm_long": ml, "mm_short": ms,
                "mm_net":  ml - ms,
            })
        nets = [r["mm_net"] for r in results]
        hi   = max(nets)
        lo   = min(nets)
        ipi  = round((nets[0] - lo) / (hi - lo) * 100, 1) if hi != lo else 50
        chg  = nets[0] - nets[1]
        acc  = (chg > 0 and nets[1] - nets[2] > 0) or (chg < 0 and nets[1] - nets[2] < 0)
        if   ipi > 75: bias = "STRONG BULLISH"
        elif ipi > 55: bias = "MILD BULLISH"
        elif ipi < 25: bias = "STRONG BEARISH"
        elif ipi < 45: bias = "MILD BEARISH"
        else:          bias = "NEUTRAL"
        return {
            "ipi": ipi, "bias": bias, "change": chg,
            "accelerating": acc,
            "mm_net":   nets[0],
            "mm_long":  results[0]["mm_long"],
            "mm_short": results[0]["mm_short"],
            "date":     results[0]["date"],
            "history":  results[:8],
        }
    except Exception:
        return None


@st.cache_data(ttl=300)
def fetch_dxy():
    try:
        d = yf.Ticker("DX-Y.NYB").history(period="6mo", interval="1wk")
        if d.empty:
            return None
        price   = round(float(d["Close"].iloc[-1]), 2)
        ema20   = round(float(d["Close"].ewm(span=20).mean().iloc[-1]), 2)
        above   = price > ema20
        trend   = "RISING" if d["Close"].iloc[-1] > d["Close"].iloc[-2] else "FALLING"
        return {"price": price, "ema20": ema20,
                "above_ema": above, "trend": trend}
    except Exception:
        return None


@st.cache_data(ttl=300)
def fetch_vix():
    try:
        d = yf.Ticker("^VIX").history(period="2d")
        if d.empty:
            return None
        v = round(float(d["Close"].iloc[-1]), 2)
        if   v > 40: regime = "CRISIS"
        elif v > 30: regime = "HIGH"
        elif v > 20: regime = "ELEVATED"
        else:        regime = "NORMAL"
        return {"value": v, "regime": regime}
    except Exception:
        return None


def is_kill_zone():
    h = datetime.now(pytz.utc).hour
    return (7 <= h < 10) or (12 <= h < 15)


def is_market_open():
    now = datetime.now(pytz.utc)
    return now.weekday() < 5 and (1 <= now.hour < 22)


def score_setup(gold, opts, cot, dxy, vix):
    """Returns score out of 14 and a breakdown list."""
    s = 0
    items = []

    # IPI (max 2)
    if cot:
        ipi = cot["ipi"]
        if ipi > 75 or ipi < 25:
            s += 2
            items.append(("IPI Extreme", "pass", f"IPI = {ipi}", "+2"))
        elif ipi > 55 or ipi < 45:
            s += 1
            items.append(("IPI Directional", "pass", f"IPI = {ipi}", "+1"))
        else:
            items.append(("IPI Neutral Zone", "fail", f"IPI = {ipi} — no trade week", "0"))

        # Momentum (max 1)
        if cot["accelerating"]:
            s += 1
            items.append(("COT Momentum Accelerating", "pass",
                           "2 consecutive weeks same direction", "+1"))
        else:
            items.append(("COT Momentum", "fail", "Not accelerating", "0"))
    else:
        items.append(("COT / IPI", "warn", "Data unavailable", "?"))

    # Real Yields — not fetched live (manual check note)
    items.append(("Real Yields", "info",
                   "Check FRED manually each Monday (DFII10)", "?"))

    # DXY (max 1)
    if dxy:
        if not dxy["above_ema"] and dxy["trend"] == "FALLING":
            s += 1
            items.append(("DXY Alignment", "pass",
                           f"DXY {dxy['price']} below 20W EMA {dxy['ema20']} and falling", "+1"))
        elif dxy["above_ema"] and dxy["trend"] == "RISING":
            items.append(("DXY Headwind", "fail",
                           f"DXY {dxy['price']} above 20W EMA {dxy['ema20']} and rising", "−1"))
        else:
            items.append(("DXY Neutral", "warn",
                           f"DXY {dxy['price']} vs EMA {dxy['ema20']} — mixed", "0"))
    else:
        items.append(("DXY", "warn", "Unavailable", "?"))

    # VIX (not scored but shown)
    if vix:
        if vix["regime"] == "NORMAL":
            items.append(("VIX Regime", "pass",
                           f"VIX {vix['value']} — normal environment", "✓"))
        elif vix["regime"] == "CRISIS":
            items.append(("VIX Crisis", "fail",
                           f"VIX {vix['value']} — PAUSE ALL TRADING", "✗"))
        else:
            items.append(("VIX Elevated", "warn",
                           f"VIX {vix['value']} — reduce size 25%", "!"))

    # Options (max 2)
    if opts and not opts.get("error"):
        if gold:
            pw_dist  = abs(gold["price"] - opts["put_wall"])
            cw_dist  = abs(gold["price"] - opts["call_wall"])
            near_pct = min(pw_dist, cw_dist) / gold["price"] * 100
            if near_pct <= 0.5:
                s += 1
                items.append(("Wall Proximity", "pass",
                               f"Price within 0.5% of key wall", "+1"))
            else:
                items.append(("Wall Proximity", "fail",
                               f"Price {round(min(pw_dist,cw_dist),1)} from nearest wall", "0"))
        items.append(("Wall OI", "info",
                       "Check OI decay manually each morning", "?"))
        if opts["pc_ratio"] > 1.3:
            s += 1
            items.append(("P/C Ratio Bullish", "pass",
                           f"P/C = {opts['pc_ratio']} — institutions hedging longs", "+1"))
        else:
            items.append(("P/C Ratio", "warn",
                           f"P/C = {opts['pc_ratio']}", "0"))
    else:
        items.append(("Options Data", "warn", "Markets closed or data error", "?"))

    # Structure (manual — shown as reminders)
    items.append(("Weekly Structure", "info",
                   "Check 200W EMA on TradingView each Monday", "?"))
    items.append(("4H Structure", "info",
                   "Check higher highs/lows on 4H chart", "?"))

    # VWAP (max 1)
    if gold and gold["vwap"]:
        ab = gold["above_vwap"]
        disp = abs(gold["price"] - gold["vwap"])
        if disp >= 5:
            s += 1
            items.append(("VWAP Displacement", "pass",
                           f"${disp:.1f} displacement — meaningful sweep", "+1"))
        else:
            items.append(("VWAP Displacement", "fail",
                           f"Only ${disp:.1f} from VWAP — not enough", "0"))

    # Kill zone (max 1)
    if is_kill_zone():
        s += 1
        items.append(("Kill Zone Active", "pass",
                       "London or New York session active", "+1"))
    else:
        h = datetime.now(pytz.utc).hour
        items.append(("Kill Zone", "fail",
                       f"UTC {h:02d}:xx — outside London/NY window", "0"))

    return min(s, 14), items


def build_chart(gold, opts):
    if not gold or gold.get("hist") is None:
        return None
    try:
        hist = gold["hist"].copy()
        hist = hist[hist.index.date == hist.index[-1].date()]
        hist = hist.tail(100)

        if hist.empty:
            return None

        # VWAP
        hist["TP"]   = (hist["High"] + hist["Low"] + hist["Close"]) / 3
        hist["TPxV"] = hist["TP"] * hist["Volume"]
        hist["VWAP"] = hist["TPxV"].cumsum() / hist["Volume"].cumsum()

        fig = go.Figure()

        # Candles
        fig.add_trace(go.Candlestick(
            x=hist.index,
            open=hist["Open"], high=hist["High"],
            low=hist["Low"],   close=hist["Close"],
            name="XAUUSD",
            increasing_fillcolor="#00D395",
            increasing_line_color="#00D395",
            decreasing_fillcolor="#FF4D6A",
            decreasing_line_color="#FF4D6A",
            line_width=1,
        ))

        # VWAP
        fig.add_trace(go.Scatter(
            x=hist.index, y=hist["VWAP"],
            name="VWAP",
            line=dict(color="#4A9EDB", width=1.5, dash="dot"),
            mode="lines",
        ))

        # Walls
        if opts and not opts.get("error"):
            for lvl, clr, nm in [
                (opts["put_wall"],  "#00D395", f"Put Wall ${opts['put_wall']:,.0f}"),
                (opts["call_wall"], "#FF4D6A", f"Call Wall ${opts['call_wall']:,.0f}"),
                (opts["max_pain"],  "#F0C060", f"Max Pain ${opts['max_pain']:,.0f}"),
            ]:
                fig.add_hline(
                    y=lvl, line_color=clr,
                    line_width=1.2, line_dash="dash",
                    annotation_text=f"  {nm}",
                    annotation_position="left",
                    annotation_font_color=clr,
                    annotation_font_size=10,
                )

        fig.update_layout(
            paper_bgcolor="#0D1117",
            plot_bgcolor="#0D1117",
            font=dict(color="#8A9BB0", family="DM Sans"),
            xaxis=dict(
                showgrid=True, gridcolor="#131920",
                rangeslider=dict(visible=False),
                color="#4A5A6A",
            ),
            yaxis=dict(
                showgrid=True, gridcolor="#131920",
                color="#4A5A6A", side="right",
                tickformat=",.0f",
            ),
            legend=dict(
                bgcolor="#0D1117", bordercolor="#131920",
                borderwidth=1, font=dict(size=10),
                orientation="h",
                yanchor="bottom", y=1.02,
                xanchor="left", x=0,
            ),
            margin=dict(l=10, r=80, t=10, b=20),
            height=400,
            hovermode="x unified",
        )
        fig.update_traces(selector=dict(type="candlestick"), xaxis="x")
        return fig
    except Exception:
        return None


def build_cot_chart(cot):
    if not cot:
        return None
    try:
        df = pd.DataFrame(cot["history"]).sort_values("date")
        colors = ["#00D395" if v > 0 else "#FF4D6A" for v in df["mm_net"]]
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df["date"], y=df["mm_net"],
            marker_color=colors,
            name="MM Net",
            hovertemplate="<b>%{x}</b><br>Net: %{y:,}<extra></extra>",
        ))
        fig.add_hline(y=0, line_color="#4A5A6A", line_width=1)
        fig.update_layout(
            paper_bgcolor="#0D1117",
            plot_bgcolor="#0D1117",
            font=dict(color="#8A9BB0"),
            xaxis=dict(showgrid=False, color="#4A5A6A", tickangle=-30),
            yaxis=dict(showgrid=True, gridcolor="#131920",
                       color="#4A5A6A", tickformat=","),
            height=220,
            margin=dict(l=10, r=10, t=10, b=40),
            showlegend=False,
        )
        return fig
    except Exception:
        return None


# ══════════════════════════════════════════════════════════════
# MAIN APP
# ══════════════════════════════════════════════════════════════
def main():
    utc_now = datetime.now(pytz.utc)
    in_kz   = is_kill_zone()
    in_mkt  = is_market_open()

    # ── LOAD ALL DATA ────────────────────────────────────────
    with st.spinner(""):
        gold = fetch_gold()
        opts = fetch_options()
        cot  = fetch_cot()
        dxy  = fetch_dxy()
        vix  = fetch_vix()

    score, score_items = score_setup(gold, opts, cot, dxy, vix)

    # ── DETERMINE OVERALL BIAS ───────────────────────────────
    bias_str   = cot["bias"]   if cot  else "UNKNOWN"
    ipi_val    = cot["ipi"]    if cot  else 50
    vix_val    = vix["value"]  if vix  else 0
    vix_regime = vix["regime"] if vix  else "UNKNOWN"

    is_bull    = "BULLISH" in bias_str
    is_bear    = "BEARISH" in bias_str
    is_neutral = "NEUTRAL" in bias_str or "UNKNOWN" in bias_str
    vix_crisis = vix_val > 40 if vix else False

    # ── TOPBAR ───────────────────────────────────────────────
    kz_html = (
        '<span class="kz-on"><span class="live-dot"></span>KILL ZONE</span>'
        if in_kz else
        '<span class="kz-off">● OUTSIDE KILL ZONE</span>'
    )
    st.markdown(f"""
    <div class="topbar">
      <div class="topbar-left">
        <span class="topbar-logo">🏅 GOLD INSTITUTIONAL EDGE</span>
        <span class="topbar-version">V2.0</span>
      </div>
      <div class="topbar-right">
        {kz_html}
        <span class="live-badge">
          <span class="live-dot"></span>LIVE
        </span>
        <span class="topbar-time">{utc_now.strftime('%a %d %b · %H:%M UTC')}</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── OPEN PAGE WRAPPER ─────────────────────────────────────
    st.markdown('<div class="page">', unsafe_allow_html=True)

    # ── HERO BIAS BANNER ─────────────────────────────────────
    price_now = gold["price"] if gold else "N/A"
    chg_now   = gold["chg"]   if gold else 0
    chg_pct   = gold["chg_pct"] if gold else 0
    chg_sign  = "+" if chg_now >= 0 else ""

    if vix_crisis:
        hero_class = "hero-bear"
        hero_icon  = "🚨"
        hero_color = "#FF4D6A"
        hero_dir   = "TRADING PAUSED"
        hero_sub   = "VIX above 40 — crisis regime. No edge in this environment. Wait for VIX to fall below 30."
    elif is_bull:
        hero_class = "hero-bull"
        hero_icon  = "🟢"
        hero_color = "#00D395"
        hero_dir   = "BULLISH BIAS"
        hero_sub   = (
            f"COT: Managed Money positioned LONG · IPI = {ipi_val} · "
            f"Only take BUY setups this week · "
            f"Wait for Put Wall touch + VWAP reclaim"
        )
    elif is_bear:
        hero_class = "hero-bear"
        hero_icon  = "🔴"
        hero_color = "#FF4D6A"
        hero_dir   = "BEARISH BIAS"
        hero_sub   = (
            f"COT: Managed Money positioned SHORT · IPI = {ipi_val} · "
            f"Only take SELL setups this week · "
            f"Wait for Call Wall touch + VWAP rejection"
        )
    else:
        hero_class = "hero-neutral"
        hero_icon  = "⚪"
        hero_color = "#F0A030"
        hero_dir   = "NEUTRAL — NO TRADES"
        hero_sub   = (
            f"COT: No clear institutional direction · IPI = {ipi_val} · "
            f"IPI in neutral zone (45–55) · "
            f"No new positions this week"
        )

    opts_ok = opts and not opts.get("error")
    pw_str  = f"${opts['put_wall']:,.0f}"    if opts_ok else "N/A"
    cw_str  = f"${opts['call_wall']:,.0f}"   if opts_ok else "N/A"
    mp_str  = f"${opts['max_pain']:,.0f}"    if opts_ok else "N/A"

    st.markdown(f"""
    <div class="{hero_class}">
      <div class="hero-left">
        <div class="hero-icon">{hero_icon}</div>
        <div>
          <div class="hero-direction" style="color:{hero_color}">{hero_dir}</div>
          <div class="hero-sub">{hero_sub}</div>
        </div>
      </div>
      <div class="hero-right">
        <div class="hero-tag">
          <div class="hero-tag-label">GOLD PRICE</div>
          <div class="hero-tag-value">${price_now:,.2f}</div>
        </div>
        <div class="hero-tag">
          <div class="hero-tag-label">TODAY</div>
          <div class="hero-tag-value" style="color:{'#00D395' if chg_now>=0 else '#FF4D6A'}">{chg_sign}{chg_now} ({chg_sign}{chg_pct}%)</div>
        </div>
        <div class="hero-tag">
          <div class="hero-tag-label">IPI SCORE</div>
          <div class="hero-tag-value">{ipi_val}</div>
        </div>
        <div class="hero-tag">
          <div class="hero-tag-label">SETUP SCORE</div>
          <div class="hero-tag-value" style="color:{'#00D395' if score>=7 else '#F0A030' if score>=5 else '#FF4D6A'}">{score}/14</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── SCORE BAR ─────────────────────────────────────────────
    score_pct = round((score / 14) * 100)
    if score >= 9:
        s_color  = "#00D395"
        s_text   = "ELITE SETUP"
        s_class  = "pass"
        s_bg     = "rgba(0,211,149,0.12)"
        s_brd    = "rgba(0,211,149,0.3)"
    elif score >= 7:
        s_color  = "#4A9EDB"
        s_text   = "VALID — TRADE IT"
        s_class  = "pass"
        s_bg     = "rgba(74,158,219,0.12)"
        s_brd    = "rgba(74,158,219,0.3)"
    elif score >= 5:
        s_color  = "#F0A030"
        s_text   = "MARGINAL — SKIP"
        s_class  = "warn"
        s_bg     = "rgba(240,160,48,0.12)"
        s_brd    = "rgba(240,160,48,0.3)"
    else:
        s_color  = "#FF4D6A"
        s_text   = "NO SETUP — WAIT"
        s_class  = "fail"
        s_bg     = "rgba(255,77,106,0.12)"
        s_brd    = "rgba(255,77,106,0.3)"

    st.markdown(f"""
    <div class="score-bar-wrap">
      <div>
        <div class="mc-label" style="margin-bottom:4px">CONFLUENCE SCORE</div>
        <div class="score-num-big" style="color:{s_color}">{score}</div>
      </div>
      <div class="score-label-area">
        <div class="score-title">Out of 14 possible points</div>
        <div class="score-bar-bg">
          <div class="score-bar-fill"
               style="width:{score_pct}%;background:{s_color}"></div>
        </div>
      </div>
      <div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center">
        <div class="score-verdict"
             style="background:{s_bg};border:1px solid {s_brd};color:{s_color}">
          {s_text}
        </div>
        {'<div class="score-verdict" style="background:rgba(0,211,149,0.1);border:1px solid rgba(0,211,149,0.25);color:#00D395">SIZE UP 1.5×</div>' if score >= 9 else ''}
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── TOP METRIC STRIP ──────────────────────────────────────
    st.markdown('<div class="sec-head">Live Market Data</div>',
                unsafe_allow_html=True)

    vwap_val  = gold["vwap"]   if gold and gold["vwap"] else None
    above_v   = gold["above_vwap"] if gold else None
    high_val  = gold["high"]   if gold else None
    low_val   = gold["low"]    if gold else None

    vwap_color = "mc-green" if above_v else "mc-red"
    vwap_sub   = "Price above VWAP ↑" if above_v else "Price below VWAP ↓"
    vwap_top   = "bull" if above_v else "bear"
    price_top  = "bull" if (chg_now >= 0 if gold else False) else "bear"

    dxy_color = "mc-red" if (dxy and dxy["above_ema"]) else "mc-green"
    dxy_top   = "bear"   if (dxy and dxy["above_ema"]) else "bull"

    vix_color = (
        "mc-green" if vix_regime == "NORMAL" else
        "mc-red"   if vix_regime in ("HIGH","CRISIS") else
        "mc-amber"
    )
    vix_top = (
        "bull" if vix_regime == "NORMAL" else
        "bear" if vix_regime in ("HIGH","CRISIS") else
        "amber"
    )

    st.markdown(f"""
    <div class="metric-row">
      <div class="metric-card {price_top}">
        <div class="mc-label">Gold Price</div>
        <div class="mc-value mc-gold">${price_now:,.2f}</div>
        <div class="mc-sub" style="color:{'#00D395' if chg_now>=0 else '#FF4D6A'}">
          {chg_sign}{chg_now} ({chg_sign}{chg_pct}%) today
        </div>
      </div>
      <div class="metric-card {vwap_top}">
        <div class="mc-label">VWAP</div>
        <div class="mc-value {vwap_color}">${f"{vwap_val:,.2f}" if vwap_val else "N/A"}</div>
        <div class="mc-sub">{vwap_sub}</div>
      </div>
      <div class="metric-card bull">
        <div class="mc-label">Put Wall — Support</div>
        <div class="mc-value mc-green">{pw_str}</div>
        <div class="mc-sub">
          {f"${abs(gold['price'] - opts['put_wall']):,.0f} from price" if gold and opts_ok else "Options data unavailable"}
        </div>
      </div>
      <div class="metric-card bear">
        <div class="mc-label">Call Wall — Resistance</div>
        <div class="mc-value mc-red">{cw_str}</div>
        <div class="mc-sub">
          {f"${abs(opts['call_wall'] - gold['price']):,.0f} from price" if gold and opts_ok else "Options data unavailable"}
        </div>
      </div>
      <div class="metric-card gold">
        <div class="mc-label">Max Pain</div>
        <div class="mc-value mc-gold">{mp_str}</div>
        <div class="mc-sub">Weekly expiry magnet</div>
      </div>
      <div class="metric-card amber">
        <div class="mc-label">Day Range</div>
        <div class="mc-value mc-amber">
          ${f"{gold['low']:,.0f}" if gold else "N/A"}–${f"{gold['high']:,.0f}" if gold else "N/A"}
        </div>
        <div class="mc-sub">
          Range: ${f"{round(gold['high']-gold['low'],1):,.1f}" if gold else "N/A"}
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── SECOND METRIC ROW ─────────────────────────────────────
    ipi_color = (
        "mc-green" if ipi_val > 55 else
        "mc-red"   if ipi_val < 45 else
        "mc-amber"
    )
    cot_chg   = cot["change"] if cot else 0
    cot_date  = cot["date"]   if cot else "N/A"
    pc_val    = opts["pc_ratio"] if opts_ok else None
    pc_color  = "mc-green" if (pc_val and pc_val > 1.0) else "mc-amber"

    st.markdown(f"""
    <div class="metric-row-4">
      <div class="metric-card {'bull' if ipi_val>55 else 'bear' if ipi_val<45 else 'amber'}">
        <div class="mc-label">IPI Score</div>
        <div class="mc-value {ipi_color}">{ipi_val}</div>
        <div class="mc-sub">{bias_str} · as of {cot_date}</div>
      </div>
      <div class="metric-card {'bull' if cot_chg>0 else 'bear'}">
        <div class="mc-label">COT Weekly Change</div>
        <div class="mc-value {'mc-green' if cot_chg>0 else 'mc-red'}">
          {'↑' if cot_chg>0 else '↓'} {abs(cot_chg):,}
        </div>
        <div class="mc-sub">Managed Money net contracts</div>
      </div>
      <div class="metric-card {vix_top}">
        <div class="mc-label">VIX Regime</div>
        <div class="mc-value {vix_color}">{vix_val if vix else 'N/A'}</div>
        <div class="mc-sub">{vix_regime} — {'normal, trade freely' if vix_regime=='NORMAL' else 'reduce size 25%' if vix_regime=='ELEVATED' else 'reduce size 50%' if vix_regime=='HIGH' else 'PAUSE ALL TRADING'}</div>
      </div>
      <div class="metric-card {dxy_top}">
        <div class="mc-label">DXY — US Dollar</div>
        <div class="mc-value {dxy_color}">{dxy['price'] if dxy else 'N/A'}</div>
        <div class="mc-sub">{'Above' if dxy and dxy['above_ema'] else 'Below'} 20W EMA {f'({dxy[\"ema20\"]})' if dxy else ''} · {dxy['trend'] if dxy else ''}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── TWO COLUMN LAYOUT ─────────────────────────────────────
    col1, col2 = st.columns([3, 2], gap="medium")

    with col1:
        # CHART
        st.markdown('<div class="sec-head">Price Chart — 5 Min with Key Levels</div>',
                    unsafe_allow_html=True)
        fig = build_chart(gold, opts)
        if fig:
            st.plotly_chart(fig, use_container_width=True,
                            config={"displayModeBar": False})
        else:
            st.markdown("""
            <div class="info-strip">
              ⏸ Chart unavailable — markets may be closed
              or data provider is slow. Refresh in a moment.
            </div>
            """, unsafe_allow_html=True)

        # COT CHART
        st.markdown('<div class="sec-head">COT — Managed Money Net Position (8 Weeks)</div>',
                    unsafe_allow_html=True)
        fig2 = build_cot_chart(cot)
        if fig2:
            st.plotly_chart(fig2, use_container_width=True,
                            config={"displayModeBar": False})
        else:
            st.markdown("""
            <div class="info-strip">
              COT data unavailable. Try refreshing.
            </div>
            """, unsafe_allow_html=True)

    with col2:
        # TRADE LEVELS
        st.markdown('<div class="sec-head">Trade Levels — Current Setup</div>',
                    unsafe_allow_html=True)

        if gold and opts_ok:
            p     = gold["price"]
            v     = gold["vwap"] or p
            atr_e = 28.0  # estimated daily ATR — user should check chart
            stop_dist = round(1.5 * atr_e, 2)

            if is_bull:
                entry = p
                stop  = round(opts["put_wall"] - stop_dist, 2)
                risk  = round(entry - stop, 2)
                tp1   = round(entry + risk * 1.0, 2)
                tp2   = round(entry + risk * 2.0, 2)
                tp3   = round(opts["max_pain"],    2)
                tp4   = round(opts["call_wall"],   2)
                dot_entry = "#FFFFFF"
                dot_stop  = "#FF4D6A"
            else:
                entry = p
                stop  = round(opts["call_wall"] + stop_dist, 2)
                risk  = round(stop - entry, 2)
                tp1   = round(entry - risk * 1.0, 2)
                tp2   = round(entry - risk * 2.0, 2)
                tp3   = round(opts["max_pain"],    2)
                tp4   = round(opts["put_wall"],    2)
                dot_entry = "#FFFFFF"
                dot_stop  = "#FF4D6A"

            levels = [
                (dot_stop,  "#FF4D6A", "STOP LOSS",
                 f"${stop:,.2f}", f"1.5× ATR below Put Wall · Risk = ${risk:,.2f}"),
                (dot_entry, "#FFFFFF", "ENTRY",
                 f"${entry:,.2f}", "Current price after VWAP reclaim"),
                ("#00D395", "#00D395", "TP 1  — Close 40%",
                 f"${tp1:,.2f}", "1:1 R/R · Move SL to entry"),
                ("#00D395", "#4A9EDB", "TP 2  — Close 30%",
                 f"${tp2:,.2f}", "1:2 R/R · Move SL to TP1"),
                ("#00D395", "#F0C060", "TP 3  — Close 20%",
                 f"${tp3:,.2f}", "Max Pain level · Move SL to TP2"),
                ("#00D395", "#C9922A", "TP 4  — Close 10%",
                 f"${tp4:,.2f}", "Opposite wall · Full move target"),
            ]
            rows = ""
            for _, dot_c, name, price_str, desc in levels:
                rows += f"""
                <div class="trade-level-row">
                  <div class="tl-left">
                    <div class="tl-dot" style="background:{dot_c}"></div>
                    <div>
                      <div class="tl-name">{name}</div>
                      <div class="tl-desc">{desc}</div>
                    </div>
                  </div>
                  <div class="tl-price">{price_str}</div>
                </div>"""

            st.markdown(f"""
            <div class="trade-panel">
              <div class="trade-panel-header">
                {'🟢 LONG SETUP (BUY)' if is_bull else '🔴 SHORT SETUP (SELL)' if is_bear else '⚪ NEUTRAL — NO TRADE'}
                &nbsp;&nbsp;·&nbsp;&nbsp; Risk = ${risk:,.2f} per unit
              </div>
              {rows}
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="info-strip">
              ⚠️ Stop distance uses estimated ATR of $28.
              Check your chart for the real 14-period Daily ATR
              and adjust accordingly.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="info-strip">
              Trade levels require live price and options data.
              Options data is available Mon–Fri during US market hours.
            </div>
            """, unsafe_allow_html=True)

        # CONFLUENCE CHECKLIST
        st.markdown('<div class="sec-head">Confluence Checklist</div>',
                    unsafe_allow_html=True)

        rows_html = ""
        for name, state, detail, pts in score_items:
            icon = "✅" if state == "pass" else "❌" if state == "fail" else "⚠️" if state == "warn" else "ℹ️"
            rows_html += f"""
            <div class="check-item">
              <div class="check-icon">{icon}</div>
              <div class="check-body">
                <div class="check-name {state}">{name}</div>
                <div class="check-detail">{detail}</div>
              </div>
              <div class="check-right {state}">{pts}</div>
            </div>"""

        st.markdown(f"""
        <div class="checklist">
          <div class="checklist-header">Score: {score}/14 — {'TRADE ✓' if score>=7 else 'DO NOT TRADE ✗'}</div>
          {rows_html}
        </div>
        """, unsafe_allow_html=True)

    # ── OPTIONS DETAIL ROW ────────────────────────────────────
    st.markdown('<div class="sec-head">Options Intelligence</div>',
                unsafe_allow_html=True)

    col3, col4, col5, col6 = st.columns(4, gap="medium")

    with col3:
        if opts_ok:
            pc  = opts["pc_ratio"]
            if   pc > 1.3: pc_sent = "Heavy put loading — bullish"
            elif pc > 1.0: pc_sent = "Mild put premium — normal"
            elif pc > 0.7: pc_sent = "Balanced"
            else:          pc_sent = "Call-heavy — caution"
            st.markdown(f"""
            <div class="metric-card {'bull' if pc>1.0 else 'amber'}">
              <div class="mc-label">Put/Call Ratio</div>
              <div class="mc-value {'mc-green' if pc>1.0 else 'mc-amber'}">{pc}</div>
              <div class="mc-sub">{pc_sent}</div>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="metric-card">
              <div class="mc-label">Put/Call Ratio</div>
              <div class="mc-value mc-amber">N/A</div>
            </div>""", unsafe_allow_html=True)

    with col4:
        if opts_ok:
            st.markdown(f"""
            <div class="metric-card gold">
              <div class="mc-label">Options Expiry</div>
              <div class="mc-value mc-gold" style="font-size:15px">{opts['expiry']}</div>
              <div class="mc-sub">Nearest weekly contract</div>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="metric-card">
              <div class="mc-label">Options Expiry</div>
              <div class="mc-value mc-amber">N/A</div>
            </div>""", unsafe_allow_html=True)

    with col5:
        if opts_ok:
            st.markdown(f"""
            <div class="metric-card blue">
              <div class="mc-label">GLD→XAUUSD Mult</div>
              <div class="mc-value mc-blue">{opts['mult']}×</div>
              <div class="mc-sub">Live conversion factor</div>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="metric-card">
              <div class="mc-label">Multiplier</div>
              <div class="mc-value mc-amber">N/A</div>
            </div>""", unsafe_allow_html=True)

    with col6:
        if in_kz:
            kz_msg   = "ACTIVE NOW"
            kz_col   = "mc-green"
            kz_top   = "bull"
            kz_sub   = "London 07–10 or NY 12–15 UTC"
        else:
            h_now = utc_now.hour
            if h_now < 7:
                mins = (7 - h_now) * 60
                kz_msg = f"London in ~{mins}min"
            elif 10 <= h_now < 12:
                mins = (12 - h_now) * 60
                kz_msg = f"NY open in ~{mins}min"
            elif h_now >= 15:
                kz_msg = "Next: Tomorrow 07:00"
            else:
                kz_msg = "Inactive"
            kz_col = "mc-amber"
            kz_top = "amber"
            kz_sub = "Outside London/NY window"
        st.markdown(f"""
        <div class="metric-card {kz_top}">
          <div class="mc-label">Kill Zone</div>
          <div class="mc-value {kz_col}" style="font-size:15px">{kz_msg}</div>
          <div class="mc-sub">{kz_sub}</div>
        </div>""", unsafe_allow_html=True)

    # ── REFRESH BUTTON + LAST UPDATED ─────────────────────────
    st.markdown('<div class="sec-head">Controls</div>',
                unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns([1, 1, 1, 3])
    with c1:
        if st.button("🔄 Refresh All Data"):
            fetch_gold.clear()
            fetch_options.clear()
            fetch_cot.clear()
            fetch_dxy.clear()
            fetch_vix.clear()
            st.rerun()
    with c2:
        if st.button("📊 Reload Chart"):
            fetch_gold.clear()
            st.rerun()
    with c3:
        if st.button("📋 Reload COT"):
            fetch_cot.clear()
            st.rerun()
    with c4:
        st.markdown(f"""
        <div style="padding:8px 0;font-family:var(--mono);
             font-size:10px;color:var(--text3)">
          Last loaded: {utc_now.strftime('%H:%M:%S UTC')} ·
          Price refreshes every 60s ·
          Options every 5min ·
          COT every hour
        </div>
        """, unsafe_allow_html=True)

    # ── FOOTER ───────────────────────────────────────────────
    st.markdown("""
    <div class="footer">
      GOLD INSTITUTIONAL EDGE V2.0 &nbsp;·&nbsp;
      Data: Yahoo Finance / CFTC Public API &nbsp;·&nbsp;
      For educational purposes only &nbsp;·&nbsp;
      Not financial advice
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ── AUTO REFRESH EVERY 60 SECONDS ────────────────────────
    time.sleep(60)
    fetch_gold.clear()
    st.rerun()


if __name__ == "__main__":
    main()
