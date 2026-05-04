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
  50%       { opacity: 0.2; }
}
.topbar-time {
  font-family: var(--mono);
  font-size: 11px;
  color: var(--text3);
}

.page { padding: 24px 32px 60px; max-width: 1400px; margin: 0 auto; }

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
.hero-sub { font-size: 13px; color: var(--text2); line-height: 1.5; }
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
.score-bar-fill { height: 100%; border-radius: 4px; }
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
.metric-card.bull::before   { background: var(--green); }
.metric-card.bear::before   { background: var(--red);   }
.metric-card.gold::before   { background: var(--gold);  }
.metric-card.blue::before   { background: var(--blue);  }
.metric-card.amber::before  { background: var(--amber); }

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
.mc-sub  { font-size: 11px; color: var(--text3); margin-top: 4px; }
.mc-green { color: var(--green)      !important; }
.mc-red   { color: var(--red)        !important; }
.mc-gold  { color: var(--gold-light) !important; }
.mc-blue  { color: var(--blue)       !important; }
.mc-amber { color: var(--amber)      !important; }

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
.check-icon { font-size: 14px; margin-top: 1px; flex-shrink: 0; width: 20px; text-align: center; }
.check-body { flex: 1; }
.check-name { font-size: 13px; font-weight: 500; color: var(--text); margin-bottom: 2px; }
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
.tl-left  { display: flex; align-items: center; gap: 10px; }
.tl-dot   { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
.tl-name  { font-size: 13px; color: var(--text2); }
.tl-desc  { font-size: 11px; color: var(--text3); }
.tl-price { font-family: var(--mono); font-size: 15px; font-weight: 700; color: var(--text); }

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

.kz-on {
  display: inline-flex; align-items: center; gap: 6px;
  background: var(--green-dim);
  border: 1px solid var(--green-border);
  border-radius: 6px; padding: 4px 10px;
  font-family: var(--mono); font-size: 10px;
  color: var(--green); font-weight: 700;
}
.kz-off {
  display: inline-flex; align-items: center; gap: 6px;
  background: rgba(74,90,106,0.15);
  border: 1px solid rgba(74,90,106,0.2);
  border-radius: 6px; padding: 4px 10px;
  font-family: var(--mono); font-size: 10px;
  color: var(--text3);
}

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

@media (max-width: 900px) {
  .page { padding: 16px 16px 60px; }
  .metric-row { grid-template-columns: repeat(3, 1fr); }
  .metric-row-4 { grid-template-columns: repeat(2, 1fr); }
  .topbar { padding: 12px 16px; }
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

        today = hist[hist.index.date == hist.index[-1].date()].copy()
        vwap  = None
        if not today.empty:
            today["TP"]   = (today["High"] + today["Low"] + today["Close"]) / 3
            today["TPxV"] = today["TP"] * today["Volume"]
            cum_v = today["Volume"].cumsum().iloc[-1]
            if cum_v > 0:
                vwap = round(float(today["TPxV"].cumsum().iloc[-1] / cum_v), 2)

        return {
            "price": price, "prev": prev,
            "chg": chg, "chg_pct": chg_pct,
            "high": high_day, "low": low_day,
            "vwap": vwap,
            "above_vwap": (price > vwap) if vwap else None,
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
        pw = float(puts.loc[puts["openInterest"].idxmax(),   "strike"])
        cw = float(calls.loc[calls["openInterest"].idxmax(), "strike"])
        strikes = sorted(set(calls["strike"].tolist() + puts["strike"].tolist()))
        pain = {}
        for s in strikes:
            pain[s] = (
                calls[calls["strike"] > s]["openInterest"].sum()
              + puts[puts["strike"]  < s]["openInterest"].sum()
            )
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
                "date":     r.get("report_date_as_yyyy_mm_dd", "")[:10],
                "mm_long":  ml,
                "mm_short": ms,
                "mm_net":   ml - ms,
            })
        nets = [r["mm_net"] for r in results]
        hi   = max(nets)
        lo   = min(nets)
        ipi  = round((nets[0] - lo) / (hi - lo) * 100, 1) if hi != lo else 50.0
        chg  = nets[0] - nets[1]
        acc  = (
            (chg > 0 and (nets[1] - nets[2]) > 0)
            or (chg < 0 and (nets[1] - nets[2]) < 0)
        )
        if   ipi > 75: bias = "STRONG BULLISH"
        elif ipi > 55: bias = "MILD BULLISH"
        elif ipi < 25: bias = "STRONG BEARISH"
        elif ipi < 45: bias = "MILD BEARISH"
        else:          bias = "NEUTRAL"
        return {
            "ipi":          ipi,
            "bias":         bias,
            "change":       chg,
            "accelerating": acc,
            "mm_net":       nets[0],
            "mm_long":      results[0]["mm_long"],
            "mm_short":     results[0]["mm_short"],
            "date":         results[0]["date"],
            "history":      results[:8],
        }
    except Exception:
        return None


@st.cache_data(ttl=300)
def fetch_dxy():
    try:
        d     = yf.Ticker("DX-Y.NYB").history(period="6mo", interval="1wk")
        if d.empty:
            return None
        price = round(float(d["Close"].iloc[-1]), 2)
        ema20 = round(float(d["Close"].ewm(span=20).mean().iloc[-1]), 2)
        trend = "RISING" if d["Close"].iloc[-1] > d["Close"].iloc[-2] else "FALLING"
        return {
            "price":     price,
            "ema20":     ema20,
            "above_ema": price > ema20,
            "trend":     trend,
        }
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
    s     = 0
    items = []
    opts_ok = opts and not opts.get("error")

    # IPI (max 2)
    if cot:
        ipi = cot["ipi"]
        if ipi > 75 or ipi < 25:
            s += 2
            items.append(("IPI Extreme", "pass",
                           "IPI = " + str(ipi) + " — strong institutional conviction", "+2"))
        elif ipi > 55 or ipi < 45:
            s += 1
            items.append(("IPI Directional", "pass",
                           "IPI = " + str(ipi) + " — mild directional bias", "+1"))
        else:
            items.append(("IPI Neutral Zone", "fail",
                           "IPI = " + str(ipi) + " — no trade this week", "0"))

        # COT Momentum (max 1)
        if cot["accelerating"]:
            s += 1
            items.append(("COT Momentum Accelerating", "pass",
                           "2 consecutive weeks same direction", "+1"))
        else:
            items.append(("COT Momentum", "fail",
                           "Not accelerating week-over-week", "0"))
    else:
        items.append(("COT / IPI", "warn", "Data unavailable", "?"))

    # Real Yields (manual check note)
    items.append(("Real Yields", "info",
                   "Check FRED manually each Monday — fred.stlouisfed.org/series/DFII10", "?"))

    # DXY (max 1)
    if dxy:
        dxy_price = str(dxy["price"])
        dxy_ema   = str(dxy["ema20"])
        dxy_trend = dxy["trend"]
        if not dxy["above_ema"] and dxy["trend"] == "FALLING":
            s += 1
            items.append(("DXY Alignment", "pass",
                           "DXY " + dxy_price + " below 20W EMA " + dxy_ema + " and falling", "+1"))
        elif dxy["above_ema"] and dxy["trend"] == "RISING":
            items.append(("DXY Headwind", "fail",
                           "DXY " + dxy_price + " above 20W EMA " + dxy_ema + " and rising", "−1"))
        else:
            items.append(("DXY Neutral", "warn",
                           "DXY " + dxy_price + " vs EMA " + dxy_ema + " — mixed signal", "0"))
    else:
        items.append(("DXY", "warn", "Data unavailable", "?"))

    # VIX (shown but not scored)
    if vix:
        vix_str = str(vix["value"])
        reg     = vix["regime"]
        if reg == "NORMAL":
            items.append(("VIX Regime", "pass",
                           "VIX " + vix_str + " — normal environment, trade freely", "✓"))
        elif reg == "CRISIS":
            items.append(("VIX Crisis", "fail",
                           "VIX " + vix_str + " — PAUSE ALL TRADING", "✗"))
        else:
            items.append(("VIX Elevated", "warn",
                           "VIX " + vix_str + " — reduce position size 25%", "!"))
    else:
        items.append(("VIX", "warn", "Data unavailable", "?"))

    # Options proximity (max 1)
    if opts_ok and gold:
        pw_dist  = abs(gold["price"] - opts["put_wall"])
        cw_dist  = abs(gold["price"] - opts["call_wall"])
        near     = min(pw_dist, cw_dist)
        near_pct = near / gold["price"] * 100
        if near_pct <= 0.5:
            s += 1
            items.append(("Wall Proximity", "pass",
                           "Price within 0.5% of a key options wall", "+1"))
        else:
            items.append(("Wall Proximity", "fail",
                           "Price $" + str(round(near, 1)) + " from nearest wall", "0"))
    else:
        items.append(("Wall Proximity", "warn",
                       "Options data unavailable — markets may be closed", "?"))

    # P/C Ratio (max 1)
    if opts_ok:
        pc = opts["pc_ratio"]
        if pc > 1.3:
            s += 1
            items.append(("P/C Ratio Bullish", "pass",
                           "P/C = " + str(pc) + " — institutions heavily hedging longs", "+1"))
        else:
            items.append(("P/C Ratio", "warn",
                           "P/C = " + str(pc) + " — no strong put loading signal", "0"))
    else:
        items.append(("P/C Ratio", "warn", "Options data unavailable", "?"))

    # OI decay reminder
    items.append(("Wall OI Decay", "info",
                   "Check OI at wall strike every morning — decay >25% = reduce size", "?"))

    # Structure reminders
    items.append(("Weekly Structure", "info",
                   "Check 200W EMA on TradingView each Monday morning", "?"))
    items.append(("4H Structure", "info",
                   "Confirm higher highs / higher lows on 4H chart before entry", "?"))

    # VWAP displacement (max 1)
    if gold and gold["vwap"]:
        disp = abs(gold["price"] - gold["vwap"])
        if disp >= 5:
            s += 1
            items.append(("VWAP Displacement", "pass",
                           "$" + str(round(disp, 1)) + " displacement — meaningful liquidity sweep", "+1"))
        else:
            items.append(("VWAP Displacement", "fail",
                           "Only $" + str(round(disp, 1)) + " from VWAP — not a real sweep yet", "0"))
    else:
        items.append(("VWAP", "warn", "VWAP data unavailable", "?"))

    # Kill zone (max 1)
    if is_kill_zone():
        s += 1
        items.append(("Kill Zone Active", "pass",
                       "London (07–10 UTC) or New York (12–15 UTC) is active now", "+1"))
    else:
        h = datetime.now(pytz.utc).hour
        items.append(("Kill Zone", "fail",
                       "UTC " + str(h).zfill(2) + ":xx — outside London and NY windows", "0"))

    return min(s, 14), items


def build_chart(gold, opts):
    if not gold or gold.get("hist") is None:
        return None
    try:
        hist = gold["hist"].copy()
        today_date = hist.index[-1].date()
        hist = hist[hist.index.date == today_date].tail(100)
        if hist.empty:
            return None

        hist["TP"]   = (hist["High"] + hist["Low"] + hist["Close"]) / 3
        hist["TPxV"] = hist["TP"] * hist["Volume"]
        cum_v = hist["Volume"].cumsum()
        hist["VWAP"] = hist["TPxV"].cumsum() / cum_v.replace(0, float("nan"))

        fig = go.Figure()

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

        fig.add_trace(go.Scatter(
            x=hist.index, y=hist["VWAP"],
            name="VWAP",
            line=dict(color="#4A9EDB", width=1.5, dash="dot"),
            mode="lines",
        ))

        opts_ok = opts and not opts.get("error")
        if opts_ok:
            for lvl, clr, nm in [
                (opts["put_wall"],  "#00D395",
                 "Put Wall $" + str(f"{opts['put_wall']:,.0f}")),
                (opts["call_wall"], "#FF4D6A",
                 "Call Wall $" + str(f"{opts['call_wall']:,.0f}")),
                (opts["max_pain"],  "#F0C060",
                 "Max Pain $" + str(f"{opts['max_pain']:,.0f}")),
            ]:
                fig.add_hline(
                    y=lvl, line_color=clr,
                    line_width=1.2, line_dash="dash",
                    annotation_text="  " + nm,
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
        return fig
    except Exception:
        return None


def build_cot_chart(cot):
    if not cot:
        return None
    try:
        df     = pd.DataFrame(cot["history"]).sort_values("date")
        colors = ["#00D395" if v > 0 else "#FF4D6A" for v in df["mm_net"]]
        fig    = go.Figure()
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
# MAIN
# ══════════════════════════════════════════════════════════════
def main():
    utc_now = datetime.now(pytz.utc)
    in_kz   = is_kill_zone()

    # ── LOAD DATA ─────────────────────────────────────────────
    gold = fetch_gold()
    opts = fetch_options()
    cot  = fetch_cot()
    dxy  = fetch_dxy()
    vix  = fetch_vix()

    opts_ok = opts and not opts.get("error")
    score, score_items = score_setup(gold, opts, cot, dxy, vix)

    # ── BIAS ──────────────────────────────────────────────────
    bias_str   = cot["bias"]    if cot  else "UNKNOWN"
    ipi_val    = cot["ipi"]     if cot  else 50.0
    vix_val    = vix["value"]   if vix  else 0
    vix_regime = vix["regime"]  if vix  else "UNKNOWN"
    is_bull    = "BULLISH"  in bias_str
    is_bear    = "BEARISH"  in bias_str
    vix_crisis = vix_val > 40

    # ── SAFE VALUE STRINGS ────────────────────────────────────
    price_now = gold["price"]   if gold else 0.0
    chg_now   = gold["chg"]     if gold else 0.0
    chg_pct   = gold["chg_pct"] if gold else 0.0
    chg_sign  = "+" if chg_now >= 0 else ""

    vwap_val  = gold["vwap"]       if gold else None
    above_v   = gold["above_vwap"] if gold else None
    high_val  = gold["high"]       if gold else None
    low_val   = gold["low"]        if gold else None

    pw_str = "$" + f"{opts['put_wall']:,.0f}"   if opts_ok else "N/A"
    cw_str = "$" + f"{opts['call_wall']:,.0f}"  if opts_ok else "N/A"
    mp_str = "$" + f"{opts['max_pain']:,.0f}"   if opts_ok else "N/A"

    # ── TOPBAR ────────────────────────────────────────────────
    kz_html = (
        '<span class="kz-on"><span class="live-dot"></span>KILL ZONE ACTIVE</span>'
        if in_kz else
        '<span class="kz-off">● OUTSIDE KILL ZONE</span>'
    )
    st.markdown(
        '<div class="topbar">'
        '<div class="topbar-left">'
        '<span class="topbar-logo">🏅 GOLD INSTITUTIONAL EDGE</span>'
        '<span class="topbar-version">V2.0</span>'
        '</div>'
        '<div class="topbar-right">'
        + kz_html +
        '<span class="live-badge"><span class="live-dot"></span>LIVE</span>'
        '<span class="topbar-time">'
        + utc_now.strftime("%a %d %b · %H:%M UTC") +
        '</span>'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="page">', unsafe_allow_html=True)

    # ── HERO BANNER ───────────────────────────────────────────
    if vix_crisis:
        hero_class = "hero-bear"
        hero_icon  = "🚨"
        hero_color = "#FF4D6A"
        hero_dir   = "TRADING PAUSED"
        hero_sub   = (
            "VIX above 40 — crisis regime active. "
            "No edge exists in this environment. "
            "Wait for VIX to fall below 30 before resuming."
        )
    elif is_bull:
        hero_class = "hero-bull"
        hero_icon  = "🟢"
        hero_color = "#00D395"
        hero_dir   = "BULLISH BIAS"
        hero_sub   = (
            "COT: Managed Money positioned LONG  ·  "
            "IPI = " + str(ipi_val) + "  ·  "
            "Only take BUY setups this week  ·  "
            "Wait for Put Wall touch + VWAP reclaim"
        )
    elif is_bear:
        hero_class = "hero-bear"
        hero_icon  = "🔴"
        hero_color = "#FF4D6A"
        hero_dir   = "BEARISH BIAS"
        hero_sub   = (
            "COT: Managed Money positioned SHORT  ·  "
            "IPI = " + str(ipi_val) + "  ·  "
            "Only take SELL setups this week  ·  "
            "Wait for Call Wall touch + VWAP rejection"
        )
    else:
        hero_class = "hero-neutral"
        hero_icon  = "⚪"
        hero_color = "#F0A030"
        hero_dir   = "NEUTRAL — NO TRADES"
        hero_sub   = (
            "COT: No clear institutional direction  ·  "
            "IPI = " + str(ipi_val) + "  ·  "
            "IPI in neutral zone (45–55)  ·  "
            "No new positions this week"
        )

    score_color = (
        "#00D395" if score >= 9 else
        "#4A9EDB" if score >= 7 else
        "#F0A030" if score >= 5 else
        "#FF4D6A"
    )

    chg_color_hero = "#00D395" if chg_now >= 0 else "#FF4D6A"
    price_str      = f"${price_now:,.2f}" if price_now else "N/A"
    chg_str        = chg_sign + str(chg_now) + " (" + chg_sign + str(chg_pct) + "%)"

    st.markdown(
        '<div class="' + hero_class + '">'
        '<div class="hero-left">'
        '<div class="hero-icon">' + hero_icon + '</div>'
        '<div>'
        '<div class="hero-direction" style="color:' + hero_color + '">' + hero_dir + '</div>'
        '<div class="hero-sub">' + hero_sub + '</div>'
        '</div>'
        '</div>'
        '<div class="hero-right">'
        '<div class="hero-tag">'
        '<div class="hero-tag-label">GOLD PRICE</div>'
        '<div class="hero-tag-value">' + price_str + '</div>'
        '</div>'
        '<div class="hero-tag">'
        '<div class="hero-tag-label">TODAY</div>'
        '<div class="hero-tag-value" style="color:' + chg_color_hero + '">' + chg_str + '</div>'
        '</div>'
        '<div class="hero-tag">'
        '<div class="hero-tag-label">IPI SCORE</div>'
        '<div class="hero-tag-value">' + str(ipi_val) + '</div>'
        '</div>'
        '<div class="hero-tag">'
        '<div class="hero-tag-label">SETUP SCORE</div>'
        '<div class="hero-tag-value" style="color:' + score_color + '">' + str(score) + '/14</div>'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    # ── SCORE BAR ─────────────────────────────────────────────
    score_pct = round((score / 14) * 100)
    if score >= 9:
        s_color  = "#00D395"
        s_text   = "ELITE SETUP"
        s_bg     = "rgba(0,211,149,0.12)"
        s_brd    = "rgba(0,211,149,0.3)"
        s_extra  = (
            '<div class="score-verdict" '
            'style="background:rgba(0,211,149,0.1);'
            'border:1px solid rgba(0,211,149,0.25);color:#00D395">'
            'SIZE UP 1.5×</div>'
        )
    elif score >= 7:
        s_color  = "#4A9EDB"
        s_text   = "VALID — TRADE IT"
        s_bg     = "rgba(74,158,219,0.12)"
        s_brd    = "rgba(74,158,219,0.3)"
        s_extra  = ""
    elif score >= 5:
        s_color  = "#F0A030"
        s_text   = "MARGINAL — SKIP"
        s_bg     = "rgba(240,160,48,0.12)"
        s_brd    = "rgba(240,160,48,0.3)"
        s_extra  = ""
    else:
        s_color  = "#FF4D6A"
        s_text   = "NO SETUP — WAIT"
        s_bg     = "rgba(255,77,106,0.12)"
        s_brd    = "rgba(255,77,106,0.3)"
        s_extra  = ""

    st.markdown(
        '<div class="score-bar-wrap">'
        '<div>'
        '<div class="mc-label" style="margin-bottom:4px">CONFLUENCE SCORE</div>'
        '<div class="score-num-big" style="color:' + s_color + '">' + str(score) + '</div>'
        '</div>'
        '<div class="score-label-area">'
        '<div class="score-title">Out of 14 possible points</div>'
        '<div class="score-bar-bg">'
        '<div class="score-bar-fill" style="width:' + str(score_pct) + '%;background:' + s_color + '"></div>'
        '</div>'
        '</div>'
        '<div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center">'
        '<div class="score-verdict" style="background:' + s_bg + ';border:1px solid ' + s_brd + ';color:' + s_color + '">'
        + s_text +
        '</div>'
        + s_extra +
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    # ── ROW 1 — 6 METRIC CARDS ───────────────────────────────
    st.markdown(
        '<div class="sec-head">Live Market Data</div>',
        unsafe_allow_html=True,
    )

    vwap_color = "mc-green" if above_v else "mc-red"
    vwap_sub   = "Price above VWAP ↑" if above_v else "Price below VWAP ↓"
    vwap_top   = "bull" if above_v else "bear"
    price_top  = "bull" if chg_now >= 0 else "bear"

    vwap_str   = ("$" + f"{vwap_val:,.2f}") if vwap_val else "N/A"
    high_str   = ("$" + f"{high_val:,.0f}") if high_val else "N/A"
    low_str    = ("$" + f"{low_val:,.0f}")  if low_val  else "N/A"
    range_str  = ("$" + f"{round(high_val - low_val, 1):,.1f}") if (high_val and low_val) else "N/A"

    pw_dist_str = ""
    cw_dist_str = ""
    if gold and opts_ok:
        pw_dist_str = "$" + f"{abs(gold['price'] - opts['put_wall']):,.0f}" + " from price"
        cw_dist_str = "$" + f"{abs(opts['call_wall'] - gold['price']):,.0f}" + " from price"

    st.markdown(
        '<div class="metric-row">'

        '<div class="metric-card ' + price_top + '">'
        '<div class="mc-label">Gold Price</div>'
        '<div class="mc-value mc-gold">$' + f"{price_now:,.2f}" + '</div>'
        '<div class="mc-sub" style="color:' + ("#00D395" if chg_now >= 0 else "#FF4D6A") + '">'
        + chg_sign + str(chg_now) + " (" + chg_sign + str(chg_pct) + "%) today"
        '</div>'
        '</div>'

        '<div class="metric-card ' + vwap_top + '">'
        '<div class="mc-label">VWAP</div>'
        '<div class="mc-value ' + vwap_color + '">' + vwap_str + '</div>'
        '<div class="mc-sub">' + vwap_sub + '</div>'
        '</div>'

        '<div class="metric-card bull">'
        '<div class="mc-label">Put Wall — Support</div>'
        '<div class="mc-value mc-green">' + pw_str + '</div>'
        '<div class="mc-sub">' + (pw_dist_str if pw_dist_str else "Options data unavailable") + '</div>'
        '</div>'

        '<div class="metric-card bear">'
        '<div class="mc-label">Call Wall — Resistance</div>'
        '<div class="mc-value mc-red">' + cw_str + '</div>'
        '<div class="mc-sub">' + (cw_dist_str if cw_dist_str else "Options data unavailable") + '</div>'
        '</div>'

        '<div class="metric-card gold">'
        '<div class="mc-label">Max Pain</div>'
        '<div class="mc-value mc-gold">' + mp_str + '</div>'
        '<div class="mc-sub">Weekly expiry price magnet</div>'
        '</div>'

        '<div class="metric-card amber">'
        '<div class="mc-label">Day Range</div>'
        '<div class="mc-value mc-amber">' + low_str + ' – ' + high_str + '</div>'
        '<div class="mc-sub">Range: ' + range_str + '</div>'
        '</div>'

        '</div>',
        unsafe_allow_html=True,
    )

    # ── ROW 2 — 4 METRIC CARDS ───────────────────────────────
    ipi_color = (
        "mc-green" if ipi_val > 55 else
        "mc-red"   if ipi_val < 45 else
        "mc-amber"
    )
    ipi_top = (
        "bull" if ipi_val > 55 else
        "bear" if ipi_val < 45 else
        "amber"
    )
    cot_chg  = cot["change"] if cot else 0
    cot_date = cot["date"]   if cot else "N/A"
    cot_arr  = "↑" if cot_chg > 0 else "↓"
    cot_col  = "mc-green" if cot_chg > 0 else "mc-red"
    cot_top  = "bull" if cot_chg > 0 else "bear"

    vix_color = (
        "mc-green" if vix_regime == "NORMAL"   else
        "mc-red"   if vix_regime in ("HIGH", "CRISIS") else
        "mc-amber"
    )
    vix_top_c = (
        "bull"  if vix_regime == "NORMAL" else
        "bear"  if vix_regime in ("HIGH", "CRISIS") else
        "amber"
    )
    vix_sub = (
        "Normal — trade freely"     if vix_regime == "NORMAL"   else
        "Elevated — reduce size 25%" if vix_regime == "ELEVATED" else
        "High — reduce size 50%"     if vix_regime == "HIGH"     else
        "CRISIS — PAUSE ALL TRADING"
    )

    # Build DXY strings without backslashes in f-string
    if dxy:
        dxy_price_str = str(dxy["price"])
        dxy_ema_str   = str(dxy["ema20"])
        dxy_trend_str = dxy["trend"]
        dxy_above_str = "Above" if dxy["above_ema"] else "Below"
        dxy_sub_str   = dxy_above_str + " 20W EMA (" + dxy_ema_str + ") · " + dxy_trend_str
        dxy_val_str   = dxy_price_str
        dxy_color_str = "mc-red" if dxy["above_ema"] else "mc-green"
        dxy_top_str   = "bear"   if dxy["above_ema"] else "bull"
    else:
        dxy_val_str   = "N/A"
        dxy_sub_str   = "Data unavailable"
        dxy_color_str = "mc-amber"
        dxy_top_str   = "amber"

    st.markdown(
        '<div class="metric-row-4">'

        '<div class="metric-card ' + ipi_top + '">'
        '<div class="mc-label">IPI Score</div>'
        '<div class="mc-value ' + ipi_color + '">' + str(ipi_val) + '</div>'
        '<div class="mc-sub">' + bias_str + ' · as of ' + cot_date + '</div>'
        '</div>'

        '<div class="metric-card ' + cot_top + '">'
        '<div class="mc-label">COT Weekly Change</div>'
        '<div class="mc-value ' + cot_col + '">' + cot_arr + ' ' + f"{abs(cot_chg):,}" + '</div>'
        '<div class="mc-sub">Managed Money net contracts</div>'
        '</div>'

        '<div class="metric-card ' + vix_top_c + '">'
        '<div class="mc-label">VIX Regime</div>'
        '<div class="mc-value ' + vix_color + '">' + str(vix_val if vix else "N/A") + '</div>'
        '<div class="mc-sub">' + vix_sub + '</div>'
        '</div>'

        '<div class="metric-card ' + dxy_top_str + '">'
        '<div class="mc-label">DXY — US Dollar</div>'
        '<div class="mc-value ' + dxy_color_str + '">' + dxy_val_str + '</div>'
        '<div class="mc-sub">' + dxy_sub_str + '</div>'
        '</div>'

        '</div>',
        unsafe_allow_html=True,
    )

    # ── TWO COLUMN LAYOUT ─────────────────────────────────────
    col1, col2 = st.columns([3, 2], gap="medium")

    with col1:
        st.markdown(
            '<div class="sec-head">Price Chart — 5 Min Candles with Key Levels</div>',
            unsafe_allow_html=True,
        )
        fig = build_chart(gold, opts)
        if fig:
            st.plotly_chart(fig, use_container_width=True,
                            config={"displayModeBar": False})
        else:
            st.markdown(
                '<div class="info-strip">'
                '⏸ Chart unavailable — markets may be closed. '
                'Click Refresh All Data to try again.'
                '</div>',
                unsafe_allow_html=True,
            )

        st.markdown(
            '<div class="sec-head">COT — Managed Money Net Position (8 Weeks)</div>',
            unsafe_allow_html=True,
        )
        fig2 = build_cot_chart(cot)
        if fig2:
            st.plotly_chart(fig2, use_container_width=True,
                            config={"displayModeBar": False})
        else:
            st.markdown(
                '<div class="info-strip">COT chart unavailable. Try refreshing.</div>',
                unsafe_allow_html=True,
            )

    with col2:
        # TRADE LEVELS
        st.markdown(
            '<div class="sec-head">Trade Levels — Current Setup</div>',
            unsafe_allow_html=True,
        )

        if gold and opts_ok:
            p         = gold["price"]
            atr_est   = 28.0
            stop_dist = round(1.5 * atr_est, 2)

            if is_bull:
                entry = p
                stop  = round(opts["put_wall"] - stop_dist, 2)
                risk  = round(entry - stop, 2)
                tp1   = round(entry + risk * 1.0, 2)
                tp2   = round(entry + risk * 2.0, 2)
                tp3   = round(opts["max_pain"],   2)
                tp4   = round(opts["call_wall"],  2)
                header_str = "🟢 LONG SETUP (BUY) · Risk = $" + f"{risk:,.2f}" + " per unit"
            else:
                entry = p
                stop  = round(opts["call_wall"] + stop_dist, 2)
                risk  = round(stop - entry, 2)
                tp1   = round(entry - risk * 1.0, 2)
                tp2   = round(entry - risk * 2.0, 2)
                tp3   = round(opts["max_pain"],   2)
                tp4   = round(opts["put_wall"],   2)
                header_str = "🔴 SHORT SETUP (SELL) · Risk = $" + f"{risk:,.2f}" + " per unit"

            levels = [
                ("#FF4D6A", "STOP LOSS",
                 "$" + f"{stop:,.2f}",
                 "1.5× ATR below Put Wall · Risk = $" + f"{risk:,.2f}"),
                ("#FFFFFF", "ENTRY",
                 "$" + f"{entry:,.2f}",
                 "Current price — enter after VWAP reclaim"),
                ("#00D395", "TP 1 — Close 40%",
                 "$" + f"{tp1:,.2f}",
                 "1:1 R/R · Move stop loss to entry (breakeven)"),
                ("#4A9EDB", "TP 2 — Close 30%",
                 "$" + f"{tp2:,.2f}",
                 "1:2 R/R · Move stop loss to TP1"),
                ("#F0C060", "TP 3 — Close 20%",
                 "$" + f"{tp3:,.2f}",
                 "Max Pain level · Move stop loss to TP2"),
                ("#C9922A", "TP 4 — Close 10%",
                 "$" + f"{tp4:,.2f}",
                 "Opposite options wall · Full institutional move"),
            ]

            rows_html = ""
            for dot_c, name, price_str_lv, desc in levels:
                rows_html += (
                    '<div class="trade-level-row">'
                    '<div class="tl-left">'
                    '<div class="tl-dot" style="background:' + dot_c + '"></div>'
                    '<div>'
                    '<div class="tl-name">' + name + '</div>'
                    '<div class="tl-desc">' + desc + '</div>'
                    '</div>'
                    '</div>'
                    '<div class="tl-price">' + price_str_lv + '</div>'
                    '</div>'
                )

            st.markdown(
                '<div class="trade-panel">'
                '<div class="trade-panel-header">' + header_str + '</div>'
                + rows_html +
                '</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                '<div class="info-strip">'
                '⚠️ Stop distance uses estimated ATR of $28. '
                'Check your chart for the real 14-period Daily ATR and adjust.'
                '</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div class="info-strip">'
                'Trade levels require live price and options data. '
                'Options data is available Mon–Fri during US market hours (14:30–21:00 UTC).'
                '</div>',
                unsafe_allow_html=True,
            )

        # CONFLUENCE CHECKLIST
        st.markdown(
            '<div class="sec-head">Confluence Checklist</div>',
            unsafe_allow_html=True,
        )

        trade_verdict = "TRADE ✓" if score >= 7 else "DO NOT TRADE ✗"
        rows_c = ""
        for name, state, detail, pts in score_items:
            icon = (
                "✅" if state == "pass" else
                "❌" if state == "fail" else
                "⚠️" if state == "warn" else
                "ℹ️"
            )
            rows_c += (
                '<div class="check-item">'
                '<div class="check-icon">' + icon + '</div>'
                '<div class="check-body">'
                '<div class="check-name ' + state + '">' + name + '</div>'
                '<div class="check-detail">' + detail + '</div>'
                '</div>'
                '<div class="check-right ' + state + '">' + pts + '</div>'
                '</div>'
            )

        st.markdown(
            '<div class="checklist">'
            '<div class="checklist-header">Score: ' + str(score) + '/14 — ' + trade_verdict + '</div>'
            + rows_c +
            '</div>',
            unsafe_allow_html=True,
        )

    # ── OPTIONS DETAIL ROW ────────────────────────────────────
    st.markdown(
        '<div class="sec-head">Options Intelligence</div>',
        unsafe_allow_html=True,
    )

    col3, col4, col5, col6 = st.columns(4, gap="medium")

    with col3:
        if opts_ok:
            pc = opts["pc_ratio"]
            if   pc > 1.3: pc_sent = "Heavy put loading — institutions hedging longs"
            elif pc > 1.0: pc_sent = "Mild put premium — normal hedging"
            elif pc > 0.7: pc_sent = "Balanced put/call ratio"
            else:          pc_sent = "Call-heavy — speculative buying"
            pc_col = "mc-green" if pc > 1.0 else "mc-amber"
            pc_top = "bull"     if pc > 1.0 else "amber"
            st.markdown(
                '<div class="metric-card ' + pc_top + '">'
                '<div class="mc-label">Put / Call Ratio</div>'
                '<div class="mc-value ' + pc_col + '">' + str(pc) + '</div>'
                '<div class="mc-sub">' + pc_sent + '</div>'
                '</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div class="metric-card">'
                '<div class="mc-label">Put / Call Ratio</div>'
                '<div class="mc-value mc-amber">N/A</div>'
                '<div class="mc-sub">Options data unavailable</div>'
                '</div>',
                unsafe_allow_html=True,
            )

    with col4:
        if opts_ok:
            st.markdown(
                '<div class="metric-card gold">'
                '<div class="mc-label">Options Expiry</div>'
                '<div class="mc-value mc-gold" style="font-size:15px">' + opts["expiry"] + '</div>'
                '<div class="mc-sub">Nearest weekly GLD contract</div>'
                '</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div class="metric-card">'
                '<div class="mc-label">Options Expiry</div>'
                '<div class="mc-value mc-amber">N/A</div>'
                '</div>',
                unsafe_allow_html=True,
            )

    with col5:
        if opts_ok:
            st.markdown(
                '<div class="metric-card blue">'
                '<div class="mc-label">GLD → XAUUSD Multiplier</div>'
                '<div class="mc-value mc-blue">' + str(opts["mult"]) + '×</div>'
                '<div class="mc-sub">Live conversion factor</div>'
                '</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div class="metric-card">'
                '<div class="mc-label">GLD Multiplier</div>'
                '<div class="mc-value mc-amber">N/A</div>'
                '</div>',
                unsafe_allow_html=True,
            )

    with col6:
        h_now = utc_now.hour
        if in_kz:
            kz_msg = "ACTIVE NOW"
            kz_col = "mc-green"
            kz_top = "bull"
            kz_sub = "London 07–10 UTC or NY 12–15 UTC"
        else:
            kz_top = "amber"
            kz_col = "mc-amber"
            if h_now < 7:
                kz_msg = "London in ~" + str((7 - h_now) * 60) + "min"
                kz_sub = "Next kill zone: London 07:00 UTC"
            elif 10 <= h_now < 12:
                kz_msg = "NY in ~" + str((12 - h_now) * 60) + "min"
                kz_sub = "Next kill zone: New York 12:00 UTC"
            elif h_now >= 15:
                kz_msg = "Tomorrow 07:00"
                kz_sub = "All kill zones closed for today"
            else:
                kz_msg = "Inactive"
                kz_sub = "Outside London and NY windows"

        st.markdown(
            '<div class="metric-card ' + kz_top + '">'
            '<div class="mc-label">Kill Zone Status</div>'
            '<div class="mc-value ' + kz_col + '" style="font-size:15px">' + kz_msg + '</div>'
            '<div class="mc-sub">' + kz_sub + '</div>'
            '</div>',
            unsafe_allow_html=True,
        )

    # ── REFRESH CONTROLS ──────────────────────────────────────
    st.markdown(
        '<div class="sec-head">Controls</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns([1, 1, 1, 3])
    with c1:
        if st.button("🔄 Refresh All"):
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
        st.markdown(
            '<div style="padding:8px 0;font-family:var(--mono);font-size:10px;color:var(--text3)">'
            'Loaded: ' + utc_now.strftime("%H:%M:%S UTC") +
            ' · Price refreshes every 60s'
            ' · Options every 5min'
            ' · COT every hour'
            '</div>',
            unsafe_allow_html=True,
        )

    # ── FOOTER ────────────────────────────────────────────────
    st.markdown(
        '<div class="footer">'
        'GOLD INSTITUTIONAL EDGE V2.0 &nbsp;·&nbsp; '
        'Data: Yahoo Finance / CFTC Public API &nbsp;·&nbsp; '
        'For educational purposes only &nbsp;·&nbsp; '
        'Not financial advice'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # ── AUTO REFRESH EVERY 60 SECONDS ─────────────────────────
    time.sleep(60)
    fetch_gold.clear()
    st.rerun()


if __name__ == "__main__":
    main()
