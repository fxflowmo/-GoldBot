# ============================================================
# GOLD INSTITUTIONAL EDGE V2.0
# Single-file Streamlit app — deploy free on Streamlit Cloud
# ============================================================

import streamlit as st

st.set_page_config(
    page_title="Gold Institutional Edge — V2.0",
    page_icon="🏅",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
  --gold: #C9922A;
  --gold-light: #F0C060;
  --gold-pale: #FDF5E0;
  --gold-dark: #7A5510;
  --bg: #0D0D0D;
  --bg2: #141414;
  --bg3: #1C1C1C;
  --bg4: #242424;
  --border: rgba(201,146,42,0.18);
  --border-strong: rgba(201,146,42,0.4);
  --text: #E8E6DE;
  --text2: #A8A49A;
  --text3: #6A6660;
  --green: #3DAA6A;
  --green-bg: rgba(61,170,106,0.1);
  --red: #D44;
  --red-bg: rgba(221,68,68,0.1);
  --blue: #4A9EDB;
  --blue-bg: rgba(74,158,219,0.1);
  --amber: #E09A2A;
  --amber-bg: rgba(224,154,42,0.1);
  --purple: #9B6FD4;
  --purple-bg: rgba(155,111,212,0.1);
  --mono: 'JetBrains Mono', monospace;
  --sans: 'DM Sans', system-ui, sans-serif;
}

* { box-sizing: border-box; }

body, .stApp {
  font-family: var(--sans) !important;
  background: #0D0D0D !important;
  color: var(--text) !important;
  -webkit-font-smoothing: antialiased;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

.v2-header {
  background: var(--bg2);
  border-bottom: 1px solid var(--border);
  padding: 48px 60px 40px;
  position: relative;
  overflow: hidden;
}
.v2-header::before {
  content: '';
  position: absolute;
  top: -60px; right: -60px;
  width: 300px; height: 300px;
  background: radial-gradient(circle, rgba(201,146,42,0.06) 0%, transparent 70%);
  pointer-events: none;
}
.header-tag {
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: 0.15em;
  color: var(--gold);
  text-transform: uppercase;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.header-tag::before {
  content: '';
  display: inline-block;
  width: 24px; height: 1px;
  background: var(--gold);
}
.v2-header h1 {
  font-size: 36px;
  font-weight: 600;
  color: var(--text);
  letter-spacing: -0.02em;
  line-height: 1.15;
  margin-bottom: 8px;
}
.v2-header h1 span { color: var(--gold-light); }
.header-sub {
  font-size: 15px;
  color: var(--text2);
  max-width: 560px;
  margin-bottom: 24px;
}
.version-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: var(--amber-bg);
  border: 1px solid var(--border-strong);
  color: var(--gold-light);
  font-family: var(--mono);
  font-size: 11px;
  padding: 4px 12px;
  border-radius: 20px;
  letter-spacing: 0.05em;
}

.v2-main {
  max-width: 960px;
  margin: 0 auto;
  padding: 48px 60px 80px;
}

.section-label {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.18em;
  color: var(--gold);
  text-transform: uppercase;
  margin-bottom: 10px;
  display: block;
}
.v2-h2 {
  font-size: 24px;
  font-weight: 500;
  letter-spacing: -0.015em;
  color: var(--text);
  margin-bottom: 20px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--border);
}
.v2-h3 {
  font-size: 16px;
  font-weight: 500;
  color: var(--text);
  margin: 28px 0 12px;
}
.v2-p {
  color: var(--text2);
  margin-bottom: 16px;
  font-size: 15px;
  line-height: 1.7;
}

.upgrade-banner {
  background: var(--amber-bg);
  border: 1px solid var(--border-strong);
  border-radius: 10px;
  padding: 16px 20px;
  margin-bottom: 24px;
  display: flex;
  gap: 12px;
  align-items: flex-start;
}
.upgrade-icon { font-size: 16px; margin-top: 1px; flex-shrink: 0; }
.upgrade-title {
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: 0.1em;
  color: var(--gold-light);
  text-transform: uppercase;
  margin-bottom: 4px;
}
.upgrade-text { font-size: 13px; color: var(--text2); margin: 0; }

.code-block {
  background: var(--bg3);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 20px 24px;
  font-family: var(--mono);
  font-size: 12px;
  line-height: 1.7;
  color: var(--text2);
  overflow-x: auto;
  margin: 16px 0;
  white-space: pre;
}
.c-gold   { color: var(--gold-light); }
.c-green  { color: var(--green); }
.c-red    { color: #DD4444; }
.c-blue   { color: var(--blue); }
.c-amber  { color: var(--amber); }
.c-purple { color: var(--purple); }
.c-dim    { color: var(--text3); }
.result   { color: var(--gold-light); font-weight: 700; }

.card-grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 20px 0; }
.card-grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; margin: 20px 0; }
.v2-card {
  background: var(--bg3);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 20px;
}
.v2-card-title {
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: 0.1em;
  color: var(--text3);
  text-transform: uppercase;
  margin-bottom: 8px;
}
.v2-card-value { font-size: 22px; font-weight: 500; color: var(--text); }
.v2-card-sub   { font-size: 12px; color: var(--text3); margin-top: 4px; }

.pill {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 3px 10px;
  border-radius: 20px;
  font-family: var(--mono);
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.05em;
}
.pill::before {
  content: '';
  width: 5px; height: 5px;
  border-radius: 50%;
  background: currentColor;
}
.pill-green { background: var(--green-bg);  color: var(--green);  border: 1px solid rgba(61,170,106,0.25); }
.pill-red   { background: var(--red-bg);    color: #DD4444;        border: 1px solid rgba(221,68,68,0.25); }
.pill-amber { background: var(--amber-bg);  color: var(--amber);  border: 1px solid rgba(224,154,42,0.25); }
.pill-blue  { background: var(--blue-bg);   color: var(--blue);   border: 1px solid rgba(74,158,219,0.25); }
.pill-grey  { background: rgba(100,100,100,0.1); color: var(--text3); border: 1px solid rgba(100,100,100,0.2); }

.score-table { width: 100%; border-collapse: collapse; margin: 16px 0; }
.score-table th {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--text3);
  padding: 10px 16px;
  text-align: left;
  border-bottom: 1px solid var(--border);
}
.score-table td {
  padding: 11px 16px;
  font-size: 13px;
  color: var(--text2);
  border-bottom: 1px solid rgba(201,146,42,0.07);
  vertical-align: middle;
}
.score-table tr:last-child td { border-bottom: none; }
.pts {
  font-family: var(--mono);
  font-size: 14px;
  font-weight: 700;
  color: var(--gold-light);
  text-align: right;
}
.row-header td {
  background: rgba(201,146,42,0.04);
  font-family: var(--mono);
  font-size: 10px;
  color: var(--text3);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 10px 16px 6px;
}

.compare-table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 13px; }
.compare-table thead th {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 10px 16px;
  text-align: left;
  border-bottom: 1px solid var(--border);
  color: var(--text3);
}
.compare-table td {
  padding: 11px 16px;
  border-bottom: 1px solid rgba(201,146,42,0.07);
  color: var(--text2);
  vertical-align: top;
}
.compare-table tr:last-child td { border-bottom: none; }
.compare-table td:first-child { font-size: 13px; color: var(--text); font-weight: 500; }
.td-old { color: var(--text3) !important; }
.td-new { color: var(--green) !important; }

.math-box {
  background: var(--bg3);
  border-left: 3px solid var(--gold);
  border-radius: 0 10px 10px 0;
  padding: 20px 24px;
  margin: 20px 0;
  font-family: var(--mono);
  font-size: 13px;
  line-height: 2;
  color: var(--text2);
  white-space: pre-wrap;
}

.warn-box {
  background: var(--red-bg);
  border: 1px solid rgba(221,68,68,0.2);
  border-radius: 10px;
  padding: 16px 20px;
  margin: 20px 0;
}
.warn-title {
  font-family: var(--mono);
  font-size: 11px;
  color: #DD4444;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 6px;
}
.info-box {
  background: var(--blue-bg);
  border: 1px solid rgba(74,158,219,0.2);
  border-radius: 10px;
  padding: 16px 20px;
  margin: 20px 0;
}
.info-title {
  font-family: var(--mono);
  font-size: 11px;
  color: var(--blue);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 6px;
}
.box-p { color: var(--text2); font-size: 13px; margin: 0; line-height: 1.7; }

.flow {
  background: var(--bg3);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 28px;
  margin: 20px 0;
}
.flow-step {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 24px;
  position: relative;
}
.flow-step:not(:last-child)::after {
  content: '';
  position: absolute;
  left: 14px; top: 32px;
  width: 1px;
  height: calc(100% + 8px);
  background: var(--border);
}
.flow-num {
  width: 30px; height: 30px;
  border-radius: 50%;
  border: 1px solid var(--border-strong);
  background: var(--bg4);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--mono);
  font-size: 11px;
  font-weight: 700;
  color: var(--gold);
  flex-shrink: 0;
  z-index: 1;
}
.flow-label { font-size: 14px; font-weight: 500; color: var(--text); margin-bottom: 4px; }
.flow-desc  { font-size: 13px; color: var(--text2); margin: 0; line-height: 1.6; }

.score-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 20px 0; }
.score-display {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 20px;
  background: var(--bg3);
  border: 1px solid var(--border);
  border-radius: 10px;
}
.score-circle {
  width: 72px; height: 72px;
  border-radius: 50%;
  border: 2px solid var(--gold);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  background: var(--amber-bg);
}
.score-num { font-family: var(--mono); font-size: 24px; font-weight: 700; color: var(--gold-light); line-height: 1; }
.score-max { font-family: var(--mono); font-size: 10px; color: var(--text3); }
.score-lbl { font-size: 14px; font-weight: 500; color: var(--text); margin-bottom: 4px; }
.score-dsc { font-size: 13px; color: var(--text2); line-height: 1.5; }

.cheat {
  background: var(--bg3);
  border: 1px solid var(--border-strong);
  border-radius: 12px;
  overflow: hidden;
}
.cheat-header {
  background: rgba(201,146,42,0.08);
  border-bottom: 1px solid var(--border);
  padding: 14px 20px;
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: 0.15em;
  color: var(--gold-light);
  text-transform: uppercase;
}
.cheat-body { padding: 8px 20px 16px; }
.cheat-row {
  display: flex;
  align-items: baseline;
  gap: 16px;
  padding: 9px 0;
  border-bottom: 1px solid rgba(201,146,42,0.07);
}
.cheat-row:last-child { border-bottom: none; }
.cheat-step {
  font-family: var(--mono);
  font-size: 11px;
  color: var(--gold);
  font-weight: 700;
  min-width: 60px;
  flex-shrink: 0;
}
.cheat-text { font-size: 13px; color: var(--text2); line-height: 1.5; }
.cheat-text strong { color: var(--text); font-weight: 500; }

.weekly-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 6px;
  margin: 16px 0;
}
.week-day {
  background: var(--bg3);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 10px 8px;
  text-align: center;
}
.week-day.active { border-color: var(--gold); background: var(--amber-bg); }
.week-day-name {
  font-family: var(--mono);
  font-size: 9px;
  letter-spacing: 0.1em;
  color: var(--text3);
  text-transform: uppercase;
  margin-bottom: 6px;
}
.week-day.active .week-day-name { color: var(--gold); }
.week-day-items { font-size: 10px; color: var(--text2); line-height: 1.6; }
.week-day.active .week-day-items { color: var(--gold-light); }

code {
  font-family: var(--mono);
  font-size: 12px;
  background: var(--bg4);
  border: 1px solid var(--border);
  padding: 1px 6px;
  border-radius: 4px;
  color: var(--gold-light);
}

.v2-hr { border: none; border-top: 1px solid var(--border); margin: 40px 0; }

.stTabs [data-baseweb="tab-list"] {
  background: #141414 !important;
  border-bottom: 1px solid rgba(201,146,42,0.18) !important;
  padding: 0 60px !important;
  gap: 0 !important;
  overflow-x: auto;
}
.stTabs [data-baseweb="tab"] {
  background: transparent !important;
  color: #6A6660 !important;
  border-bottom: 2px solid transparent !important;
  border-radius: 0 !important;
  padding: 14px 16px !important;
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 11px !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  white-space: nowrap;
}
.stTabs [aria-selected="true"] {
  color: #F0C060 !important;
  border-bottom-color: #C9922A !important;
}
.stTabs [data-baseweb="tab-highlight"] { display: none; }
div[data-testid="stTabsContent"] {
  background: #0D0D0D !important;
  padding: 0 !important;
}

@media (max-width: 700px) {
  .v2-main { padding: 24px 20px 60px; }
  .v2-header { padding: 32px 20px 28px; }
  .card-grid-2, .card-grid-3 { grid-template-columns: 1fr; }
  .score-grid { grid-template-columns: 1fr; }
  .weekly-grid { grid-template-columns: repeat(4, 1fr); }
  .v2-header h1 { font-size: 26px; }
  .stTabs [data-baseweb="tab-list"] { padding: 0 16px !important; }
}
</style>
""", unsafe_allow_html=True)


# ── HEADER ───────────────────────────────────────────────────
st.markdown("""
<div class="v2-header">
  <div class="header-tag">Quantitative Trading Framework</div>
  <h1>Gold Institutional Edge<br><span>Version 2.0</span></h1>
  <p class="header-sub">
    A fully rebuilt institutional-grade Gold trading system.
    Every component upgraded, every arbitrary parameter replaced
    with data-driven logic, every missing filter added.
  </p>
  <span class="version-badge">V2.0 — 10 System Upgrades Applied</span>
</div>
""", unsafe_allow_html=True)


# ── TABS ─────────────────────────────────────────────────────
tabs = st.tabs([
    "Overview",
    "Pillar 1 · IPI",
    "Pillar 2 · Macro",
    "Pillar 3 · Options",
    "Pillar 4 · Structure",
    "Entry System",
    "Stops & Sizing",
    "Scoring",
    "Routine",
    "Cheat Sheet",
])

def wrap(html):
    st.markdown(f'<div class="v2-main">{html}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# TAB 0 — OVERVIEW
# ══════════════════════════════════════════════════════════════
with tabs[0]:
    wrap("""
<span class="section-label">Upgrade Summary</span>
<div class="v2-h2">What changed from V1 — and why</div>
<p class="v2-p">
  V1 had a sound conceptual framework with four critical flaws:
  an arbitrary COT threshold, no macro context, static stop distances,
  and zero setup scoring. V2 fixes all four and adds six additional
  layers that institutional desks actually use.
</p>

<table class="compare-table">
<thead>
  <tr><th>Component</th><th>V1 — Original</th><th>V2 — Upgraded</th></tr>
</thead>
<tbody>
  <tr><td>COT Signal</td>
    <td class="td-old">Raw weekly change ±5,000 contracts</td>
    <td class="td-new">Normalized IPI Index (52-wk range) + momentum confirmation</td></tr>
  <tr><td>Macro Filter</td>
    <td class="td-old">Not present</td>
    <td class="td-new">Real yields, DXY, Gold/Silver ratio, VIX regime</td></tr>
  <tr><td>Options Walls</td>
    <td class="td-old">Raw OI snapshot, static</td>
    <td class="td-new">OI decay-adjusted, gamma-weighted, skew-informed</td></tr>
  <tr><td>Market Structure</td>
    <td class="td-old">Not present</td>
    <td class="td-new">4-pillar MTF framework (weekly → 4H → 15min → 5min)</td></tr>
  <tr><td>VWAP Entry</td>
    <td class="td-old">Any VWAP reclaim counts</td>
    <td class="td-new">Min $5 displacement + candlestick confirmation + volume</td></tr>
  <tr><td>Stop Placement</td>
    <td class="td-old">$8 fixed buffer</td>
    <td class="td-new">1.5× Daily ATR or structural swing low, whichever wider</td></tr>
  <tr><td>Position Sizing</td>
    <td class="td-old">1% flat risk per trade</td>
    <td class="td-new">Volatility-adjusted with 25% Kelly overlay + account heat limit</td></tr>
  <tr><td>News Filter</td>
    <td class="td-old">Manual footnote</td>
    <td class="td-new">Hard exclusion zones: FOMC, NFP, CPI, PPI, PCE ±60 min</td></tr>
  <tr><td>Seasonality</td>
    <td class="td-old">Not present</td>
    <td class="td-new">Monthly bias filter with historical Gold tendency data</td></tr>
  <tr><td>Setup Scoring</td>
    <td class="td-old">Not present</td>
    <td class="td-new">0–14 score system — only trade 7+, size up at 9–10</td></tr>
</tbody>
</table>

<div class="v2-hr"></div>
<div class="v2-h3">The Four Pillars at a Glance</div>
<div class="card-grid-2">
  <div class="v2-card">
    <div class="v2-card-title">Pillar 1 — IPI</div>
    <div class="v2-card-value" style="color:#F0C060;font-size:16px">Institutional Positioning</div>
    <div class="v2-card-sub" style="margin-top:8px;font-size:13px;color:#A8A49A;line-height:1.6">
      52-week normalized COT index.<br>
      Answers: <em>which direction is smart money pointed this week?</em>
    </div>
  </div>
  <div class="v2-card">
    <div class="v2-card-title">Pillar 2 — Macro</div>
    <div class="v2-card-value" style="color:#4A9EDB;font-size:16px">Context Filter</div>
    <div class="v2-card-sub" style="margin-top:8px;font-size:13px;color:#A8A49A;line-height:1.6">
      Real yields, DXY, VIX, seasonality.<br>
      Answers: <em>is the macro tailwind aligned?</em>
    </div>
  </div>
  <div class="v2-card">
    <div class="v2-card-title">Pillar 3 — Options</div>
    <div class="v2-card-value" style="color:#3DAA6A;font-size:16px">Price Level Intelligence</div>
    <div class="v2-card-sub" style="margin-top:8px;font-size:13px;color:#A8A49A;line-height:1.6">
      Put Wall, Call Wall, Max Pain, IV skew.<br>
      Answers: <em>where will price react this week?</em>
    </div>
  </div>
  <div class="v2-card">
    <div class="v2-card-title">Pillar 4 — Structure</div>
    <div class="v2-card-value" style="color:#9B6FD4;font-size:16px">Multi-Timeframe Context</div>
    <div class="v2-card-sub" style="margin-top:8px;font-size:13px;color:#A8A49A;line-height:1.6">
      Weekly → Daily → 4H → 5min alignment.<br>
      Answers: <em>is this candle in the right direction?</em>
    </div>
  </div>
</div>
""")


# ══════════════════════════════════════════════════════════════
# TAB 1 — IPI
# ══════════════════════════════════════════════════════════════
with tabs[1]:
    wrap("""
<span class="section-label">Pillar 1 — Upgraded</span>
<div class="v2-h2">Institutional Positioning Index (IPI)</div>

<div class="upgrade-banner">
  <div class="upgrade-icon">▲</div>
  <div>
    <div class="upgrade-title">V1 Flaw Corrected</div>
    <p class="upgrade-text">
      V1 used raw weekly contract change (±5,000 threshold). This is arbitrary
      and context-blind. A 5,000 contract swing means something completely
      different when total net positioning is at 50,000 vs 250,000. V2
      normalizes against the 52-week range to give a true extreme reading.
    </p>
  </div>
</div>

<div class="v2-h3">The IPI Formula</div>
<div class="math-box"><span class="c-dim">// Step 1: Calculate current Managed Money net position</span>
MM_Net_Now  = MM_Longs_This_Week  − MM_Shorts_This_Week
MM_Net_Prev = MM_Longs_Last_Week  − MM_Shorts_Last_Week

<span class="c-dim">// Step 2: Get 52-week high and low of MM_Net</span>
MM_Net_52w_High = max(MM_Net over past 52 weeks)
MM_Net_52w_Low  = min(MM_Net over past 52 weeks)

<span class="c-dim">// Step 3: Calculate the IPI (0–100 scale)</span>
<span class="result">IPI = (MM_Net_Now − MM_Net_52w_Low) / (MM_Net_52w_High − MM_Net_52w_Low) × 100</span>

<span class="c-dim">// Step 4: Add momentum confirmation</span>
Momentum      = MM_Net_Now  − MM_Net_Prev
Momentum_Prev = MM_Net_Prev − MM_Net_2wks_ago
<span class="result">Accelerating  = same sign AND abs(Momentum) > abs(Momentum_Prev)</span></div>

<div class="v2-h3">IPI Signal Thresholds</div>
<div class="code-block"><span class="c-green">IPI > 75  →  STRONG BULLISH</span>
  Near 52-week extreme long positioning.
  Only look for BUY setups. Strong institutional conviction.
  <span class="c-green">+ Accelerating momentum = +2 bonus points on Scoring System</span>

<span class="c-gold">IPI 55–75  →  MILD BULLISH</span>
  Moderate long bias. Valid for trades but lower conviction.
  Require higher confluence score (8+ instead of 7+).

<span class="c-amber">IPI 45–55  →  NEUTRAL ZONE</span>
  No clear directional edge from positioning.
  <span class="c-amber">SKIP THE WEEK. No new positions.</span>

<span class="c-gold">IPI 25–45  →  MILD BEARISH</span>
  Moderate short bias. Only look for SELL setups.
  Require higher confluence score (8+ instead of 7+).

<span class="c-red">IPI < 25  →  STRONG BEARISH</span>
  Near 52-week extreme short positioning.
  Only look for SELL setups. Strong institutional conviction.
  <span class="c-red">+ Accelerating momentum = +2 bonus points on Scoring System</span></div>

<div class="v2-h3">Adding Commercial Hedger Confirmation</div>
<p class="v2-p">
  Commercials in Gold are miners, producers, and jewelry manufacturers who
  are structurally net short. Their extreme positioning is a contrarian
  signal — when they are at historical extremes it often marks turning points.
</p>
<div class="code-block"><span class="c-dim">// Commercial Net Position (always negative in Gold)</span>
Comm_Net = Comm_Longs − Comm_Shorts
Comm_IPI = (Comm_Net − Comm_52w_Low) / (Comm_52w_High − Comm_52w_Low) × 100

<span class="c-green">Comm_IPI > 70  →  Producers NOT hedging aggressively = expect price to RISE</span>
   CONFIRMS bullish MM bias.

<span class="c-red">Comm_IPI < 30  →  Producers aggressively hedging = expect price to FALL</span>
   CONFIRMS bearish MM bias.

IPI Strong Bullish + Comm_IPI > 70 = <span class="c-green">MAX LONG CONVICTION  (+1 bonus point)</span>
IPI Strong Bearish + Comm_IPI < 30 = <span class="c-red">MAX SHORT CONVICTION (+1 bonus point)</span></div>

<div class="info-box">
  <div class="info-title">Data Source</div>
  <p class="box-p">
    CFTC Disaggregated COT Report — Gold Futures (/GC).
    Available free at cftc.gov every Friday ~15:30 EST.
    The 52-week high/low tracking needs to be done in a spreadsheet
    or automated via the CFTC public API.
    Minimum 12 weeks of data needed before the IPI is reliable.
  </p>
</div>
""")


# ══════════════════════════════════════════════════════════════
# TAB 2 — MACRO
# ══════════════════════════════════════════════════════════════
with tabs[2]:
    wrap("""
<span class="section-label">Pillar 2 — New Addition</span>
<div class="v2-h2">Macro Context Filter</div>

<div class="upgrade-banner">
  <div class="upgrade-icon">+</div>
  <div>
    <div class="upgrade-title">New in V2</div>
    <p class="upgrade-text">
      V1 had zero macro context. Trading Gold without knowing the direction of
      real yields and the Dollar is like sailing without checking wind direction.
      These filters take 5 minutes to check on Monday morning and eliminate an
      entire category of losing trades.
    </p>
  </div>
</div>

<div class="v2-h3">Filter 1 — Real Yields (Most Important Macro Input)</div>
<p class="v2-p">
  Gold is priced against real yields (nominal yield minus inflation expectation).
  Rising real yields increase the opportunity cost of holding Gold. Falling real
  yields are the single most powerful tailwind for Gold. This relationship is
  robust over decades.
</p>
<div class="code-block"><span class="c-dim">// US 10-Year TIPS Yield — Source: fred.stlouisfed.org/series/DFII10 (free, daily)</span>

<span class="c-green">Real Yields FALLING week-over-week  →  GOLD TAILWIND</span>
   Confirms bullish IPI bias. Adds +1 to scoring.

<span class="c-amber">Real Yields FLAT (±0.05% change)  →  NEUTRAL</span>
   No macro boost. Trade on other signals only.

<span class="c-red">Real Yields RISING week-over-week  →  GOLD HEADWIND</span>
   DOWNGRADE any bullish IPI reading by one tier.
   Strong Bullish IPI + Rising Real Yields = trade only on 9+.
   Bearish IPI confirmed. Adds +1 to short setups.</div>

<div class="v2-h3">Filter 2 — US Dollar Index (DXY)</div>
<p class="v2-p">
  Gold and the Dollar are inversely correlated roughly 75–80% of the time.
  Aligning with DXY direction adds a powerful macro tailwind.
</p>
<div class="code-block"><span class="c-dim">// Check DXY weekly direction — above or below 20-week EMA?</span>

<span class="c-green">DXY below 20W EMA and pointing DOWN  →  Dollar weakening</span>
   Adds +1 to Gold long setups.

<span class="c-amber">DXY flat / choppy  →  No contribution to scoring</span>

<span class="c-red">DXY above 20W EMA and pointing UP  →  Dollar strengthening</span>
   Subtracts 1 from Gold long setups. Adds +1 to short setups.

<span class="c-dim">// BONUS: DXY COT Index</span>
DXY MM IPI > 70 = additional Gold bearish headwind
DXY MM IPI < 30 = additional Gold bullish tailwind</div>

<div class="v2-h3">Filter 3 — VIX Regime</div>
<div class="code-block"><span class="c-green">VIX < 20  →  Normal risk environment. Trade normally.</span>

<span class="c-amber">VIX 20–30  →  Elevated. Widen stop to 2× ATR. Reduce size 25%.</span>

<span class="c-red">VIX > 30  →  CRISIS MODE. Gold can gap violently.</span>
   Options walls become unreliable. Only take 9+ setups.
   Size down to 50% of normal. Stop must be 2.5× ATR.

<span class="c-red">VIX > 40  →  PAUSE ALL TRADING until VIX falls below 30.</span>
   No edge exists in this environment for this system.</div>

<div class="v2-h3">Filter 4 — Seasonality</div>
<div class="code-block"><span class="c-green">HIGH-BIAS MONTHS (historically bullish tendency):</span>
  January    — Year-start institutional buying, India jewelry season
  July–Aug   — Pre-monsoon Indian demand, summer fund positioning
  September  — Diwali demand build-up, historically strong

<span class="c-amber">NEUTRAL MONTHS:</span>
  February, March, June, October, December

<span class="c-red">WEAK-BIAS MONTHS (historically flat-to-bearish tendency):</span>
  April      — Tax season liquidations, post-Chinese New Year lull
  May–June   — Historically Gold's weakest stretch of the year
  November   — Dollar often strengthens into year-end

<span class="c-dim">// During weak months: require 8+ score for longs.
// During strong months: 7 is sufficient.
// Never block trades entirely based on seasonality alone.</span></div>

<div class="warn-box">
  <div class="warn-title">Macro Context Is a Filter, Not a Trading Signal</div>
  <p class="box-p">
    None of these macro inputs generate entries. They adjust the bar for taking
    trades. A bearish macro backdrop means you need more confluence, not that
    you can never trade long. The market can and does ignore macro headwinds
    for weeks at a time.
  </p>
</div>
""")


# ══════════════════════════════════════════════════════════════
# TAB 3 — OPTIONS
# ══════════════════════════════════════════════════════════════
with tabs[3]:
    wrap("""
<span class="section-label">Pillar 3 — Upgraded</span>
<div class="v2-h2">Options Intelligence System</div>

<div class="upgrade-banner">
  <div class="upgrade-icon">▲</div>
  <div>
    <div class="upgrade-title">V1 Flaw Corrected</div>
    <p class="upgrade-text">
      V1 used a static OI snapshot with no time decay adjustment. A wall on
      Monday with 500K contracts is not the same wall on Thursday with 120K
      contracts remaining after rolling. V2 tracks OI velocity (building or
      decaying) and weights walls by time to expiry.
    </p>
  </div>
</div>

<div class="v2-h3">OI Decay-Adjusted Wall Strength</div>
<div class="code-block"><span class="c-dim">// Record OI at the Put Wall strike every morning.</span>
Monday    OI at $240 Put:  580,000 contracts  ← Baseline
Tuesday   OI at $240 Put:  560,000 contracts
Wednesday OI:              535,000 contracts
Thursday  OI:              290,000 contracts  ← ⚠️ Wall decaying fast

<span class="c-green">OI STABLE or INCREASING   →  Wall is Strong. Full confidence.</span>
<span class="c-amber">OI down 10–25% from Monday  →  Wall is Normal. Slight caution.</span>
<span class="c-red">OI down >25% from Monday   →  Wall is Weak. Reduce position size 30%.</span>
<span class="c-red">OI down >50% from Monday   →  Wall has failed. Do NOT use this level.</span>

<span class="c-dim">// Thursday warning: Near-term options expire Friday.
// By Thursday afternoon, near-term OI can drop 60–80%.
// Switch to NEXT WEEK's expiry for wall levels by Thursday.</span></div>

<div class="v2-h3">IV Skew — The Institutional Fear Gauge</div>
<p class="v2-p">
  Implied volatility skew (how much more expensive puts are vs calls) tells you
  what institutions are actually paying to hedge. An extreme skew shift is often
  a leading indicator before a wall is tested.
</p>
<div class="code-block"><span class="c-dim">// GLD 25-delta skew = IV of 25-delta puts minus IV of 25-delta calls
// Available free on Barchart.com or Market Chameleon</span>

Skew > +5%  →  Puts significantly more expensive than calls.
   Institutions paying UP for downside protection.
   Counterintuitively BULLISH — they are long and hedging.
   <span class="c-green">Reinforces Put Wall strength — strong support expected.</span>

Skew 2–5%   →  Normal slight put premium. No special signal.

Skew < 2%   →  Calls approaching put IV. Complacency.
   <span class="c-amber">Warning: Institutions not hedging = may not be as long.</span>
   Reduces confidence in Put Wall as support.

<span class="c-dim">// Skew SPIKE (sudden +3% or more in one day):</span>
   Someone just bought urgent put protection.
   <span class="c-amber">Check for news. Do not trade until spike is explained.</span></div>

<div class="v2-h3">Strong vs Weak Wall — Quick Reference</div>
<div class="code-block">STRONG WALL — all of these together:
  ✓  Strike has highest raw OI
  ✓  Strike is within 1–3% of current price (near the money)
  ✓  OI at that strike is stable or growing this week
  ✓  IV skew is elevated (puts expensive)
  ✓  Daily ATR puts current price within range of wall this session

WEAK WALL — any of these:
  ✗  Highest OI strike is >5% away from current price (far OTM)
  ✗  OI at strike has dropped >25% since Monday
  ✗  Another strike has OI within 80% of the "wall" strike
     (diffuse OI = no single magnet point)
  ✗  Major news event within 24 hours</div>

<div class="v2-h3">Max Pain — Honest Assessment</div>
<div class="info-box">
  <div class="info-title">Corrected Use Case</div>
  <p class="box-p">
    V1 presented Max Pain as an active price magnet driven by market maker
    activity. The academic evidence for this is thin. The more honest
    interpretation: Max Pain marks a zone of low gamma stress — neither calls
    nor puts are badly in the money. Price drifts into this zone when there is
    no directional catalyst. Use it as a <strong>TP2 in quiet mid-week sessions
    only</strong>, not as a reliable target during strong trending weeks or on
    news days.
  </p>
</div>
""")


# ══════════════════════════════════════════════════════════════
# TAB 4 — STRUCTURE
# ══════════════════════════════════════════════════════════════
with tabs[4]:
    wrap("""
<span class="section-label">Pillar 4 — New Addition</span>
<div class="v2-h2">Multi-Timeframe Structure Framework</div>

<div class="upgrade-banner">
  <div class="upgrade-icon">+</div>
  <div>
    <div class="upgrade-title">New in V2</div>
    <p class="upgrade-text">
      V1 had no market structure context whatsoever. Trading options walls
      without knowing the higher timeframe trend is like knowing where the
      speed bumps are but not what road you're on. The MTF framework takes
      10 minutes to check and fundamentally changes which setups you take.
    </p>
  </div>
</div>

<div class="v2-h3">The Four-Timeframe Stack</div>
<div class="flow">
  <div class="flow-step">
    <div class="flow-num">W</div>
    <div>
      <div class="flow-label">Weekly Chart — Trend Context (Check Monday, valid all week)</div>
      <p class="flow-desc">
        Is price above or below the 200-week EMA? Are weekly closes making
        higher highs / higher lows (uptrend) or lower highs / lower lows
        (downtrend)? This is your macro trend. Only take trades that align
        with the weekly structure. A Put Wall bounce in a weekly downtrend
        needs a 9+ score to trade.
      </p>
    </div>
  </div>
  <div class="flow-step">
    <div class="flow-num">D</div>
    <div>
      <div class="flow-label">Daily Chart — Swing Structure (Check each morning)</div>
      <p class="flow-desc">
        Previous day high (PDH) and previous day low (PDL) are key levels.
        Fair Value Gaps (FVGs — three-candle imbalances) act as magnets.
        Is today's open above or below yesterday's close? Daily VWAP from
        the prior session provides an additional reference for the first
        30 minutes of London.
      </p>
    </div>
  </div>
  <div class="flow-step">
    <div class="flow-num">4H</div>
    <div>
      <div class="flow-label">4-Hour Chart — Entry Bias (Check at session open)</div>
      <p class="flow-desc">
        The 4H chart shows the current swing structure. Only take longs when
        the 4H structure is making higher highs and higher lows. Only take
        shorts when it is making lower highs and lower lows. A Put Wall bounce
        where the 4H structure is still in a downswing = skip or require 9+.
      </p>
    </div>
  </div>
  <div class="flow-step">
    <div class="flow-num">5m</div>
    <div>
      <div class="flow-label">5-Minute Chart — Trigger Timeframe</div>
      <p class="flow-desc">
        This is where VWAP entries are executed. The 5-minute chart should
        confirm: liquidity sweep below the Put Wall, VWAP reclaim with minimum
        $5 displacement, volume spike on the reversal bar, and ideally a clear
        engulfing candle or pin bar as the entry signal.
      </p>
    </div>
  </div>
</div>

<div class="v2-h3">Structure Alignment Scoring</div>
<div class="code-block"><span class="c-green">Weekly UP + Daily UP + 4H UP + Near Put Wall</span>
→ <span class="c-green">Full alignment — highest probability long setup. Add +2 to score.</span>

<span class="c-gold">Weekly UP + Daily UP + 4H DOWN (pullback in uptrend)</span>
→ <span class="c-gold">Pullback into support — valid but not ideal. Add +1 to score.</span>

<span class="c-amber">Weekly UP + Daily DOWN + 4H DOWN</span>
→ <span class="c-amber">Counter-trend long attempt. Add +0. Requires 9+ score.</span>

<span class="c-red">Weekly DOWN + looking for long at Put Wall</span>
→ <span class="c-red">Structural headwind. Subtract 1. Requires 9+ score.</span></div>

<div class="info-box">
  <div class="info-title">Fair Value Gap (FVG) — the extra level V1 didn't know about</div>
  <p class="box-p">
    A Fair Value Gap is formed when three consecutive candles create an
    imbalance — the third candle's low is above the first candle's high
    (bullish FVG) or vice versa (bearish FVG). Price has a strong tendency
    to return and fill these gaps. On the daily chart, an unfilled bullish FVG
    sitting below the Put Wall is one of the most powerful entry confluences
    in the system. Mark them every morning.
  </p>
</div>
""")


# ══════════════════════════════════════════════════════════════
# TAB 5 — ENTRY SYSTEM
# ══════════════════════════════════════════════════════════════
with tabs[5]:
    wrap("""
<span class="section-label">Entry System — Upgraded</span>
<div class="v2-h2">The Precision Entry Protocol</div>

<div class="upgrade-banner">
  <div class="upgrade-icon">▲</div>
  <div>
    <div class="upgrade-title">V1 Flaw Corrected</div>
    <p class="upgrade-text">
      V1's VWAP entry had no minimum displacement rule. A 2-tick dip below
      VWAP counted the same as a $12 sweep. In practice, shallow VWAP
      violations are noise that fire false entries constantly. V2 requires a
      meaningful displacement plus candlestick confirmation plus volume
      validation.
    </p>
  </div>
</div>

<div class="v2-h3">Long Setup — Complete Entry Checklist</div>
<div class="code-block"><span class="c-gold">PRE-CONDITIONS (check before each session):</span>
  ✓  IPI ≥ 55 (bullish zone)
  ✓  Weekly structure: uptrend or at major support
  ✓  Real Yields: flat or falling
  ✓  DXY: below 20W EMA or flat
  ✓  VIX: below 30 (if 20–30, reduce size 25%)
  ✓  No high-impact news within 60 minutes (FOMC/NFP/CPI/PCE/PPI)
  ✓  Seasonality: not in a strong bearish month unless score 8+

<span class="c-gold">SETUP TRIGGER (requires ALL of the following):</span>
  ✓  Price within $5.00 of Put Wall     → Alert: APPROACHING
  ✓  Price touches Put Wall (≤$1.50)    → Alert: TOUCHED
  ✓  Price dips BELOW VWAP by ≥ $5.00  (liquidity sweep)
  ✓  Price closes BACK ABOVE VWAP on 5-minute candle

<span class="c-gold">ENTRY CONFIRMATION (requires at least ONE of):</span>
  ✓  Reversal candle is a bullish engulfing
     (body closes above previous candle high)
  ✓  Reversal candle is a hammer/pin bar
     (lower wick ≥ 2× body size)
  ✓  Volume on reversal candle ≥ 1.5× 20-bar average

<span class="c-gold">KILL ZONE (still required):</span>
  ✓  London:   07:00–10:00 UTC
  ✓  New York: 12:00–15:00 UTC

<span class="c-green">ALL PRE-CONDITIONS + TRIGGER + ONE CONFIRMATION = ENTER</span>
  → LONG at market on next 5-minute candle open
  → Set stop, TP1, TP2, TP3, TP4 immediately
  → Walk away from screen until first alert fires</div>

<div class="v2-h3">The Liquidity Sweep — Why It Matters</div>
<div class="code-block"><span class="c-dim">// What is a liquidity sweep?</span>
Large institutional traders need to FILL large orders.
To buy millions in Gold they need willing sellers.
The most willing sellers are retail traders with stops
just below support.

So institutions briefly push price below the Put Wall...
→ Retail longs are stopped out (their stops executed as sells)
→ Institutions absorb all that selling at a lower price
→ Price snaps back above the wall

<span class="c-green">The sweep below VWAP IS this process happening in real time.</span>

V1 said: wait for any VWAP dip and reclaim.
V2 says: the dip must be ≥$5 to be a real sweep, not noise.

<span class="c-gold">Bonus signal: sweep takes out the previous session's low (PDL)</span>
Price dips below PDL and immediately reverses with VWAP reclaim =
institutions hunting stops and absorbing supply.
Highest-probability long setup in the system.</div>

<div class="warn-box">
  <div class="warn-title">The One Rule That Will Save You Most</div>
  <p class="box-p">
    If price touches the Put Wall, sweeps below VWAP by $10+, but fails to
    close back above VWAP within 3 candles (15 minutes) — the setup has
    failed. The wall is being broken. Do not enter. Exit any existing longs.
    A genuine institutional defense closes above VWAP quickly and does not
    linger below it.
  </p>
</div>
""")


# ══════════════════════════════════════════════════════════════
# TAB 6 — STOPS & SIZING
# ══════════════════════════════════════════════════════════════
with tabs[6]:
    wrap("""
<span class="section-label">Risk Management — Upgraded</span>
<div class="v2-h2">ATR-Based Stops &amp; Volatility-Adjusted Sizing</div>

<div class="upgrade-banner">
  <div class="upgrade-icon">▲</div>
  <div>
    <div class="upgrade-title">V1 Flaw Corrected</div>
    <p class="upgrade-text">
      V1 used a fixed $8 stop buffer regardless of market conditions. At $2,000
      Gold this is 0.40%. At $3,200 Gold this is 0.25% — proportionally tighter,
      getting stopped out more easily. V2 uses Daily ATR so your stop scales
      with actual volatility.
    </p>
  </div>
</div>

<div class="v2-h3">Stop Placement — Two Methods, Use the Wider</div>
<div class="math-box"><span class="c-dim">// Method 1: ATR-Based Stop</span>
Daily_ATR = 14-period ATR on the Daily chart
Buffer    = 1.5 × Daily_ATR

<span class="result">Long Stop  = Put Wall  − Buffer</span>
<span class="result">Short Stop = Call Wall + Buffer</span>

<span class="c-dim">// Example: Daily ATR = $28. Buffer = $42.
// Put Wall at $3,150. Stop placed at $3,108.</span>

<span class="c-dim">// Method 2: Structural Stop</span>
Look at the 4H chart.
Find the most recent 4H swing low (for longs) or swing high (for shorts).
<span class="result">Stop = 1 tick below the 4H swing low</span>

<span class="c-dim">// Take whichever gives a WIDER stop.
// Never tighten the stop from these levels.
// Never widen the stop once set.</span>

<span class="c-dim">// VIX Adjustment:</span>
VIX 20–30:  multiply buffer by 1.3  (wider stop, smaller size)
VIX > 30:   multiply buffer by 1.7  (much wider, much smaller size)</div>

<div class="v2-h3">Position Sizing — Volatility-Adjusted</div>
<div class="math-box"><span class="c-dim">// Step 1: Dollar risk per unit</span>
<span class="result">Dollar_Risk_Per_Unit = Entry_Price − Stop_Price  (for longs)</span>

<span class="c-dim">// Step 2: Base position size</span>
Account_Size    = your total account value
Risk_Percent    = 1.0%  (or 0.5% for first 20 trades)
Max_Dollar_Risk = Account_Size × Risk_Percent
<span class="result">Base_Size = Max_Dollar_Risk / Dollar_Risk_Per_Unit</span>

<span class="c-dim">// Step 3: Setup score multiplier</span>
Score 9–10:  use 1.5× Base  ← size up on elite setups
Score 7–8:   use 1.0× Base  ← standard size
Score ≤ 6:   DO NOT TRADE

<span class="c-dim">// Step 4: Account heat check (hard limit)</span>
Total_Open_Risk = sum of risk across ALL open trades
<span class="result">HARD LIMIT: Total_Open_Risk must never exceed 5% of account</span>
<span class="c-dim">If adding this trade would breach 5%, reduce size or skip.</span></div>

<div class="v2-h3">Target Structure — 4 Exits</div>
<div class="code-block"><span class="c-gold">LONG TRADE (from Put Wall):</span>

Entry:  VWAP reclaim price after sweep
Stop:   max(ATR-based, structural) → calculated above
Risk:   Entry − Stop = 1R

TP1:  Entry + 1.0R  → Close 40% of position
      Move stop to: Entry (breakeven)

TP2:  Entry + 2.0R  → Close 30% of position
      Move stop to: TP1

TP3:  Max Pain level → Close 20% of position
      Move stop to: TP2

TP4:  Call Wall      → Close final 10%
      Maximum institutional target.

<span class="c-dim">// V2 Change: 4 exits (40/30/20/10) vs V1's 3 (50/25/25)
// The 10% runner captures the full move on elite setups.
// In choppy weeks TP3/TP4 rarely hit — that's fine.
// The 1:1 TP1 closes the book on risk quickly.</span></div>

<div class="v2-h3">The 25% Kelly Sizing Overlay (Advanced)</div>
<div class="info-box">
  <div class="info-title">For traders with 50+ historical trades logged</div>
  <p class="box-p">
    Once you have 50+ real trades, calculate your historical win rate (W) and
    average win/loss ratio (R). Apply 25% Kelly fraction:
    <code>Full_Kelly = W − (1−W)/R</code> then
    <code>Multiplier = 0.25 × Full_Kelly</code>.
    This adjusts the base 1% — never replaces it.
    25% Kelly is mathematically safe. Never use full Kelly.
  </p>
</div>
""")


# ══════════════════════════════════════════════════════════════
# TAB 7 — SCORING
# ══════════════════════════════════════════════════════════════
with tabs[7]:
    wrap("""
<span class="section-label">New in V2</span>
<div class="v2-h2">The Confluence Scoring System</div>
<p class="v2-p">
  V1 had no scoring — all pillars agreeing was binary. V2 assigns points to
  each factor. This answers the question V1 couldn't:
  <em>how confident should I be in this setup?</em>
  Only trade 7+. Size up at 9+.
</p>

<table class="score-table">
<thead>
  <tr><th>Factor</th><th>Condition</th><th style="text-align:right">Pts</th></tr>
</thead>
<tbody>
  <tr class="row-header"><td colspan="3">Institutional Positioning — Max 4</td></tr>
  <tr>
    <td>IPI Signal</td>
    <td>IPI &gt; 75 (strong bullish) or &lt; 25 (strong bearish)</td>
    <td class="pts">2</td>
  </tr>
  <tr>
    <td>IPI Signal</td>
    <td>IPI 55–75 or 25–45 (mild directional bias)</td>
    <td class="pts">1</td>
  </tr>
  <tr>
    <td>COT Momentum</td>
    <td>2+ consecutive weeks same-direction, accelerating</td>
    <td class="pts">1</td>
  </tr>
  <tr>
    <td>Commercial Confirmation</td>
    <td>Commercial IPI aligns with MM IPI at extreme</td>
    <td class="pts">1</td>
  </tr>
  <tr class="row-header"><td colspan="3">Macro Context — Max 2</td></tr>
  <tr>
    <td>Real Yields</td>
    <td>Falling (for longs) or rising (for shorts)</td>
    <td class="pts">1</td>
  </tr>
  <tr>
    <td>DXY Alignment</td>
    <td>DXY below 20W EMA and falling (for Gold longs)</td>
    <td class="pts">1</td>
  </tr>
  <tr class="row-header"><td colspan="3">Options Intelligence — Max 3</td></tr>
  <tr>
    <td>Wall Strength</td>
    <td>OI stable or growing since Monday</td>
    <td class="pts">1</td>
  </tr>
  <tr>
    <td>Wall Proximity</td>
    <td>Price within 0.5% of wall level</td>
    <td class="pts">1</td>
  </tr>
  <tr>
    <td>IV Skew</td>
    <td>Elevated put premium (&gt;3% skew) on a long setup</td>
    <td class="pts">1</td>
  </tr>
  <tr class="row-header"><td colspan="3">Market Structure — Max 2</td></tr>
  <tr>
    <td>Weekly Structure</td>
    <td>Trade aligns with weekly trend direction</td>
    <td class="pts">1</td>
  </tr>
  <tr>
    <td>4H Structure</td>
    <td>Trade aligns with 4H swing structure</td>
    <td class="pts">1</td>
  </tr>
  <tr class="row-header"><td colspan="3">Entry Quality — Max 2</td></tr>
  <tr>
    <td>VWAP Sweep</td>
    <td>Displacement ≥ $5 below VWAP before reclaim</td>
    <td class="pts">1</td>
  </tr>
  <tr>
    <td>Candle Pattern</td>
    <td>Engulfing, hammer, or volume spike on reversal bar</td>
    <td class="pts">1</td>
  </tr>
</tbody>
</table>

<div class="v2-h3">Score Interpretation</div>
<div class="score-grid">
  <div class="score-display">
    <div class="score-circle">
      <span class="score-num">9+</span>
      <span class="score-max">/14</span>
    </div>
    <div>
      <div class="score-lbl">Elite Setup &nbsp;<span class="pill pill-green">Trade 1.5× size</span></div>
      <div class="score-dsc">
        Rare — maybe 3–4 times per quarter. Size up and let it run to TP4.
        These setups define your quarter.
      </div>
    </div>
  </div>
  <div class="score-display">
    <div class="score-circle" style="border-color:#4A9EDB;background:rgba(74,158,219,0.08)">
      <span class="score-num" style="color:#4A9EDB">7–8</span>
      <span class="score-max">/14</span>
    </div>
    <div>
      <div class="score-lbl">Valid Setup &nbsp;<span class="pill pill-blue">Standard size</span></div>
      <div class="score-dsc">
        Your bread and butter. 1× risk, normal TP structure.
        Run the full protocol. 1–3 per week in good conditions.
      </div>
    </div>
  </div>
  <div class="score-display">
    <div class="score-circle" style="border-color:#E09A2A;background:rgba(224,154,42,0.08)">
      <span class="score-num" style="color:#E09A2A">5–6</span>
      <span class="score-max">/14</span>
    </div>
    <div>
      <div class="score-lbl">Marginal &nbsp;<span class="pill pill-amber">Do not trade</span></div>
      <div class="score-dsc">
        Too many factors missing. Paper trade only.
        Log it as an observation, not a live trade.
      </div>
    </div>
  </div>
  <div class="score-display">
    <div class="score-circle" style="border-color:#6A6660;background:rgba(100,100,100,0.05)">
      <span class="score-num" style="color:#6A6660">0–4</span>
      <span class="score-max">/14</span>
    </div>
    <div>
      <div class="score-lbl">No Setup &nbsp;<span class="pill pill-grey">Wait</span></div>
      <div class="score-dsc">
        No edge this session. Walk away. Protecting capital on bad weeks
        is how you stay in the game for the good weeks.
      </div>
    </div>
  </div>
</div>

<div class="v2-hr"></div>
<div class="v2-h3">Hard Exclusion Rules — Override Everything</div>
<div class="code-block"><span class="c-red">ABSOLUTE NO-TRADE CONDITIONS:</span>

  ✗  Within 60 minutes BEFORE or AFTER:
       FOMC rate decision
       Non-Farm Payrolls (NFP)
       US CPI  /  US PCE  /  US PPI
       Any Fed Chair speech

  ✗  VIX above 40

  ✗  IPI in neutral zone (45–55)

  ✗  Score below 7

  ✗  Total open risk already at 5% of account

  ✗  First 30 minutes of day session open
     (VWAP has insufficient data before 07:30 UTC)

  ✗  GLD options showing zero OI (data fetch error)

<span class="c-dim">// Check economic calendar every Sunday evening.
// Mark all exclusion windows before the week starts.
// These are pre-planned — not decisions made under pressure.</span></div>
""")


# ══════════════════════════════════════════════════════════════
# TAB 8 — ROUTINE
# ══════════════════════════════════════════════════════════════
with tabs[8]:
    wrap("""
<span class="section-label">Operational Framework</span>
<div class="v2-h2">The Weekly Operating Routine</div>

<div class="weekly-grid">
  <div class="week-day">
    <div class="week-day-name">Sun</div>
    <div class="week-day-items">Check econ calendar. Mark exclusion zones for the week.</div>
  </div>
  <div class="week-day active">
    <div class="week-day-name">Fri</div>
    <div class="week-day-items">COT released. Calculate IPI. Set directional bias for next week.</div>
  </div>
  <div class="week-day active">
    <div class="week-day-name">Mon</div>
    <div class="week-day-items">Full setup ritual. Mark all levels. Score pre-conditions.</div>
  </div>
  <div class="week-day">
    <div class="week-day-name">Tue</div>
    <div class="week-day-items">Update OI decay. Check wall strength. Kill zone watch.</div>
  </div>
  <div class="week-day">
    <div class="week-day-name">Wed</div>
    <div class="week-day-items">OI check. Mid-week TP adjustment if needed.</div>
  </div>
  <div class="week-day">
    <div class="week-day-name">Thu</div>
    <div class="week-day-items">Near-term OI expiring. Switch to next week's expiry levels.</div>
  </div>
  <div class="week-day">
    <div class="week-day-name">Fri</div>
    <div class="week-day-items">Close runners before 15:00 UTC. Read new COT after close.</div>
  </div>
</div>

<div class="v2-h3">Friday Evening — 15 Minutes</div>
<div class="code-block">1. Download CFTC Disaggregated COT — Gold (/GC) from cftc.gov
2. Calculate MM Net Position this week vs last week
3. Update your 52-week IPI spreadsheet
4. Calculate IPI value (0–100)
5. Check Commercial IPI for confirmation
6. Record in journal: IPI, direction, bias for next week
7. If IPI 45–55 → write "NO TRADES NEXT WEEK" and close laptop</div>

<div class="v2-h3">Monday Morning — Full Setup Ritual — 30 Minutes</div>
<div class="code-block">1. Check Weekly chart:
   → Trend direction? Above/below 200W EMA?
   → Any weekly FVGs nearby?

2. Check Daily chart:
   → PDH, PDL — mark on chart
   → Any daily FVGs in play?
   → Mark prior-day VWAP as reference

3. Pull GLD options chain (Yahoo Finance or Barchart):
   → Identify Put Wall, Call Wall, Max Pain
   → Record baseline OI at key strikes for the week
   → Note IV skew reading

4. Check macro inputs:
   → FRED: 10Y TIPS real yield vs last week
   → DXY: above or below 20W EMA?
   → VIX: what regime are we in today?

5. Check economic calendar:
   → Mark all exclusion windows this week in red

6. Score the pre-conditions (before seeing intraday price):
   IPI points:              ? / 4
   COT momentum:            ? / 1
   Commercial confirmation: ? / 1
   Real yields:             ? / 1
   DXY:                     ? / 1
   Pre-condition score:     ? / 8

7. If pre-condition score < 4 → reduced week.
   Only take 9+ setups. Size at 0.5%.</div>

<div class="v2-h3">Performance Log — What to Record Every Trade</div>
<div class="code-block"><span class="c-gold">TRADE LOG — Every Field:</span>
Date  |  Entry  |  Stop  |  TP1/TP2/TP3/TP4
Direction  |  Size  |  Score  |  IPI at entry
Result  |  R-multiple  |  Which TP hit  |  How stopped out

<span class="c-gold">POST-TRADE NOTES (write within 24 hours):</span>
→ Was the IPI reading correct for this week?
→ Did the wall hold cleanly or was there a false break first?
→ Did the VWAP entry trigger cleanly?
→ Was there an FVG or structure level I didn't score?
→ If stopped out: was stop placement logical in hindsight?

<span class="c-gold">REVIEW EVERY 20 TRADES:</span>
→ Win rate by score tier (7–8 vs 9+)
→ Win rate by IPI tier (strong vs mild)
→ Average R on winners vs average R on losers
→ Kill zone performance (London vs New York)

<span class="c-gold">CALIBRATE EVERY 50 TRADES:</span>
→ Update 25% Kelly fraction with real data
→ Identify which score factors predict wins best
→ Adjust IPI thresholds if your data suggests different cutoffs</div>

<div class="info-box">
  <div class="info-title">The Only Honest Statement About Expectancy</div>
  <p class="box-p">
    This system cannot claim a specific win rate or R-multiple until you have
    50+ documented trades. Until then: run the process faithfully, size small
    (0.5% risk per trade for first 20 trades), and collect data. The edge
    becomes provable through your own trade log — not through a document.
    That is the most important upgrade V2 makes: intellectual honesty about
    what is known and what must be discovered empirically.
  </p>
</div>
""")


# ══════════════════════════════════════════════════════════════
# TAB 9 — CHEAT SHEET
# ══════════════════════════════════════════════════════════════
with tabs[9]:
    wrap("""
<span class="section-label">Reference</span>
<div class="v2-h2">The V2 Cheat Sheet</div>

<div class="cheat">
  <div class="cheat-header">Gold Institutional Edge V2.0 — Quick Reference</div>
  <div class="cheat-body">
    <div class="cheat-row">
      <span class="cheat-step">FRI</span>
      <span class="cheat-text">
        <strong>Calculate IPI.</strong>
        Normalize MM net vs 52-week range.
        Bullish &gt;55 · Bearish &lt;45 · Neutral (45–55) = no trades this week.
      </span>
    </div>
    <div class="cheat-row">
      <span class="cheat-step">MON AM</span>
      <span class="cheat-text">
        <strong>Macro check.</strong>
        Real yields direction. DXY vs 20W EMA. VIX regime.
        Mark economic calendar exclusion windows for the week.
      </span>
    </div>
    <div class="cheat-row">
      <span class="cheat-step">MON AM</span>
      <span class="cheat-text">
        <strong>Options levels.</strong>
        Pull GLD chain. Note Put Wall, Call Wall, Max Pain.
        Record baseline OI at key strikes.
      </span>
    </div>
    <div class="cheat-row">
      <span class="cheat-step">DAILY</span>
      <span class="cheat-text">
        <strong>OI decay check.</strong>
        Is Put Wall OI stable?
        Down &gt;25% = reduce size 30%.
        Down &gt;50% = ignore level entirely.
      </span>
    </div>
    <div class="cheat-row">
      <span class="cheat-step">SESSION</span>
      <span class="cheat-text">
        <strong>MTF structure.</strong>
        Weekly trend. 4H structure. Daily FVGs. PDH / PDL.
        All must align with trade direction before continuing.
      </span>
    </div>
    <div class="cheat-row">
      <span class="cheat-step">TRIGGER</span>
      <span class="cheat-text">
        <strong>Entry checklist.</strong>
        Wall touched → price sweeps ≥$5 below VWAP →
        closes back above VWAP → candlestick confirmation.
      </span>
    </div>
    <div class="cheat-row">
      <span class="cheat-step">SCORE</span>
      <span class="cheat-text">
        <strong>Must be 7+ to trade.</strong>
        9+ = 1.5× size.
        5–6 = paper trade only.
        Below 5 = walk away completely.
      </span>
    </div>
    <div class="cheat-row">
      <span class="cheat-step">STOP</span>
      <span class="cheat-text">
        <strong>max(1.5× Daily ATR, structural swing low).</strong>
        Never fixed dollars. ×1.3 for VIX 20–30. ×1.7 for VIX &gt;30.
      </span>
    </div>
    <div class="cheat-row">
      <span class="cheat-step">TARGETS</span>
      <span class="cheat-text">
        <strong>TP1 1R → close 40%, move SL to entry.</strong>
        TP2 2R → close 30%, move SL to TP1.
        TP3 Max Pain → close 20%, move SL to TP2.
        TP4 Call Wall → close final 10%.
      </span>
    </div>
    <div class="cheat-row">
      <span class="cheat-step">JOURNAL</span>
      <span class="cheat-text">
        <strong>Every trade logged.</strong>
        IPI, score, entry, result, why it worked or failed.
        Review every 20 trades. Calibrate every 50.
      </span>
    </div>
    <div class="cheat-row">
      <span class="cheat-step">NEVER</span>
      <span class="cheat-text">
        <strong>Trade within 60 min of FOMC / NFP / CPI / PCE / PPI.</strong>
        Trade with VIX &gt;40. Move stop further away. Revenge trade.
      </span>
    </div>
  </div>
</div>

<div class="card-grid-3" style="margin-top:24px">
  <div class="v2-card">
    <div class="v2-card-title">Min Score to Trade</div>
    <div class="v2-card-value" style="color:#F0C060">7 / 14</div>
    <div class="v2-card-sub">9+ = size up 1.5×</div>
  </div>
  <div class="v2-card">
    <div class="v2-card-title">Stop Buffer</div>
    <div class="v2-card-value" style="color:#4A9EDB">1.5× ATR</div>
    <div class="v2-card-sub">or structural swing, whichever wider</div>
  </div>
  <div class="v2-card">
    <div class="v2-card-title">Max Account Heat</div>
    <div class="v2-card-value" style="color:#DD4444">5%</div>
    <div class="v2-card-sub">total open risk across all positions</div>
  </div>
  <div class="v2-card">
    <div class="v2-card-title">VWAP Min Displacement</div>
    <div class="v2-card-value" style="color:#3DAA6A">$5.00</div>
    <div class="v2-card-sub">below VWAP before reclaim counts</div>
  </div>
  <div class="v2-card">
    <div class="v2-card-title">IPI Neutral Zone</div>
    <div class="v2-card-value" style="color:#E09A2A">45 – 55</div>
    <div class="v2-card-sub">no trades when IPI falls here</div>
  </div>
  <div class="v2-card">
    <div class="v2-card-title">VIX Pause Level</div>
    <div class="v2-card-value" style="color:#DD4444">40+</div>
    <div class="v2-card-sub">stop all trading until below 30</div>
  </div>
</div>
""")