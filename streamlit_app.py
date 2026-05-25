# =========================================================
# STREAMLIT DASHBOARD
# SIMULASI SISTEM ANTRIAN SORTIR PAKET
# PREMIUM DARK VERSION — FIXED & COMPLETE
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Dashboard Simulasi Antrian Paket",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# COLOR PALETTE
# =========================================================

PRIMARY    = "#FF6B00"
SECONDARY  = "#FF8C42"
RED        = "#D62828"
WHITE      = "#FFFFFF"
CARD       = "#151515"
CARD2      = "#1E1E1E"
BORDER     = "#2B2B2B"

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif !important;
}

/* ---- APP BACKGROUND ---- */
.stApp {
    background: linear-gradient(135deg, #0D0D0D 0%, #1A1A1A 35%, #2B0B0B 100%);
}

.block-container {
    padding-top: 1.2rem !important;
    padding-bottom: 1rem !important;
    max-width: 100% !important;
}

/* ---- SIDEBAR ---- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0D0D0D 0%, #1A0808 100%) !important;
    border-right: 1px solid rgba(255,255,255,0.08) !important;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* ---- SELECTBOX FIX ---- */

.stSelectbox label {
    color: white !important;
    font-weight: 600 !important;
}

/* box utama */
.stSelectbox > div > div {

    background-color: #1E1E1E !important;

    border: 1px solid #FF6B00 !important;

    border-radius: 14px !important;

    min-height: 45px !important;
}

/* text selected */
.stSelectbox div[data-baseweb="select"] span {

    color: white !important;

    font-size: 14px !important;

    font-weight: 500 !important;
}

/* dropdown popup */
div[data-baseweb="popover"] {

    background-color: #1A1A1A !important;
}

/* option item */
div[role="option"] {

    background-color: #1A1A1A !important;

    color: white !important;
}

/* hover option */
div[role="option"]:hover {

    background-color: #FF6B00 !important;

    color: white !important;
}
/* ---- SLIDER ---- */
.stSlider > div > div { color: #FF6B00 !important; }

/* ---- SIDEBAR CARDS ---- */
.sidebar-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.04), rgba(255,255,255,0.01));
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 16px;
    margin-bottom: 16px;
    transition: 0.3s;
}

.sidebar-card:hover {
    transform: translateY(-2px);
    border: 1px solid #FF6B00;
    box-shadow: 0 6px 18px rgba(255,107,0,0.18);
}

.sidebar-title {
    color: white;
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: 12px;
}

.sidebar-info {
    color: #C9C9C9;
    font-size: 0.85rem;
    line-height: 1.8;
}

/* ---- SYSTEM STATUS ---- */
.system-status {
    background: linear-gradient(135deg, rgba(255,107,0,0.15), rgba(214,40,40,0.12));
    border: 1px solid rgba(255,107,0,0.25);
    border-radius: 16px;
    padding: 14px;
    margin-top: 12px;
}

.status-title {
    color: #FFB067;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 4px;
}

.status-value {
    color: white;
    font-size: 1.2rem;
    font-weight: 700;
}

/* ---- DASHBOARD HEADER ---- */
.dashboard-header {
    margin-bottom: 18px;
}

.dashboard-title {
    font-size: clamp(18px, 2.5vw, 28px);
    font-weight: 800;
    color: white;
    line-height: 1.2;
    margin-bottom: 4px;
}

.dashboard-subtitle {
    font-size: clamp(11px, 1.2vw, 14px);
    color: #C9C9C9;
    font-weight: 400;
}

/* ---- METRIC CARDS ---- */
.metric-card {
    background: linear-gradient(145deg, #1E1E1E, #151515);
    border: 1px solid #2B2B2B;
    border-radius: 18px;
    padding: 18px 16px;
    min-height: 110px;
    transition: 0.3s;
    position: relative;
    overflow: hidden;
}

.metric-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #FF6B00, #D62828);
    border-radius: 18px 18px 0 0;
}

.metric-card:hover {
    transform: translateY(-3px);
    border-color: #FF6B00;
    box-shadow: 0 8px 24px rgba(255,107,0,0.2);
}

.metric-title {
    font-size: 10px;
    font-weight: 700;
    color: #FF8C42;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.metric-value {
    font-size: clamp(24px, 3vw, 36px);
    font-weight: 800;
    color: white;
    line-height: 1;
    margin-bottom: 5px;
}

.metric-desc {
    font-size: 12px;
    color: #C9C9C9;
    font-weight: 500;
}

/* ---- SECTION CARDS ---- */
.section-card {
    background: linear-gradient(145deg, #1A1A1A, #141414);
    border: 1px solid #2B2B2B;
    border-radius: 20px;
    padding: 18px;
    margin-bottom: 0;
}

.section-title {
    font-size: 14px;
    font-weight: 700;
    color: white;
    margin-bottom: 12px;
    letter-spacing: 0.02em;
}

/* ---- INSIGHT CARD ---- */
.insight-card {
    background: linear-gradient(145deg, #1E1E1E, #151515);
    border: 1px solid #2B2B2B;
    border-radius: 18px;
    padding: 18px 16px;
    min-height: 90px;
    transition: 0.3s;
}

.insight-card:hover {
    border-color: #FF6B00;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(255,107,0,0.15);
}

/* ---- FOOTER ---- */
.custom-footer {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 14px 20px;
    margin-top: 12px;
    text-align: center;
    color: #C9C9C9;
    font-size: 13px;
    font-weight: 500;
}

.footer-highlight {
    color: #FF6B00;
    font-weight: 600;
}

/* ---- HIDE STREAMLIT DEFAULTS ---- */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }

/* ---- OVERRIDE STREAMLIT METRIC ---- */
[data-testid="stMetricValue"] { color: white !important; }
[data-testid="stMetricLabel"] { color: #C9C9C9 !important; }

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():
    DATA_FILENAME = Path(__file__).parent / "data" / "hasil_simulasi_antrian_Paket.csv"
    return pd.read_csv(DATA_FILENAME)

df = load_data()

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-card">
        <div class="sidebar-title">📦 FILTER &amp; KONTROL</div>
    </div>
    """, unsafe_allow_html=True)

    scenario_list = ["Semua Skenario"] + list(df["Scenario"].unique())

    selected_scenario = st.selectbox("Pilih Skenario", scenario_list)

    iteration_range = st.slider(
        "Rentang Iterasi",
        int(df["Iteration"].min()),
        int(df["Iteration"].max()),
        (int(df["Iteration"].min()), int(df["Iteration"].max()))
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-card">
        <div class="sidebar-title">ℹ️ INFORMASI SIMULASI</div>
        <div class="sidebar-info">
            <b>Model:</b> M/M/c Priority Queue<br>
            <b>Pendekatan:</b> Discrete Event Simulation<br>
            <b>Distribusi Kedatangan:</b> Poisson<br>
            <b>Distribusi Pelayanan:</b> Eksponensial<br>
            <b>Library:</b> SimPy<br>
            <b>Durasi Simulasi:</b> 480 menit
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-card">
        <div class="sidebar-title">🎨 KETERANGAN WARNA</div>
        <div class="sidebar-info">
            🟧 Orange → Wait Express<br>
            🟥 Red → Wait Reguler<br>
            🟨 Gold → Queue Length<br>
            ⚪ White → Utilisasi
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# FILTER DATA
# =========================================================

filtered_df = df.copy()

if selected_scenario != "Semua Skenario":
    filtered_df = filtered_df[filtered_df["Scenario"] == selected_scenario]

filtered_df = filtered_df[
    (filtered_df["Iteration"] >= iteration_range[0]) &
    (filtered_df["Iteration"] <= iteration_range[1])
]

scenario_df = filtered_df.groupby("Scenario").mean(numeric_only=True).reset_index()

# =========================================================
# METRICS
# =========================================================

avg_wait_express = filtered_df["Avg Wait Express"].mean()
avg_wait_reguler = filtered_df["Avg Wait Reguler"].mean()
avg_queue        = filtered_df["Avg Queue Length"].mean()
avg_util         = filtered_df["Utilisasi"].mean()
total_paket      = filtered_df["Total Paket"].sum()

# =========================================================
# SIDEBAR — STATUS (after avg_util is defined)
# =========================================================

with st.sidebar:
    status_label = "🟢 STABIL" if avg_util < 1 else "🔴 OVERLOAD"
    st.markdown(f"""
    <div class="system-status">
        <div class="status-title">STATUS SISTEM</div>
        <div class="status-value">{status_label}</div>
        <div style="color:#CFCFCF;font-size:0.85rem;margin-top:6px;">
            Utilisasi: {avg_util:.2f}
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

hcol1, hcol2 = st.columns([4, 1.2])

with hcol1:
    st.markdown("""
    <div class="dashboard-header">
        <div class="dashboard-title">📦 DASHBOARD SIMULASI SISTEM ANTRIAN SORTIR PAKET</div>
        <div class="dashboard-subtitle">
            Simulasi dan Analisis Kinerja Sistem Antrian Sortir Paket pada Layanan Ekspedisi Menggunakan SimPy
        </div>
    </div>
    """, unsafe_allow_html=True)

with hcol2:
    mc1, mc2 = st.columns(2)
    with mc1:
        st.metric("Total Iterasi",  f"{df['Iteration'].max():,}")
    with mc2:
        st.metric("Total Skenario", f"{df['Scenario'].nunique()}")

# =========================================================
# METRIC CARDS
# =========================================================

c1, c2, c3, c4, c5 = st.columns(5, gap="small")

card_data = [
    ("AVG WAIT EXPRESS",     f"{avg_wait_express:.2f}", "menit"),
    ("AVG WAIT REGULER",     f"{avg_wait_reguler:.2f}", "menit"),
    ("AVG QUEUE LENGTH",     f"{avg_queue:.2f}",        "paket"),
    ("UTILISASI PETUGAS",    f"{avg_util:.2f}",         f"({avg_util*100:.0f}%)"),
    ("TOTAL PAKET DIPROSES", f"{total_paket:,.0f}",     "paket"),
]

for col, (title, value, desc) in zip([c1, c2, c3, c4, c5], card_data):
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

# =========================================================
# ROW 1 — Bar Chart | Gauge | Histogram
# =========================================================

left, middle, right = st.columns([2.2, 1, 1.2], gap="small")

# ---- BAR CHART ----
with left:
    st.markdown('<div class="section-card"><div class="section-title">📊 PERBANDINGAN KINERJA SKENARIO</div>', unsafe_allow_html=True)

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Bar(
        x=scenario_df["Scenario"], y=scenario_df["Avg Wait Express"],
        name="Wait Express", marker_color=PRIMARY,
        text=scenario_df["Avg Wait Express"].round(2),
        textposition="outside", textfont=dict(color="white", size=10)
    ), secondary_y=False)

    fig.add_trace(go.Bar(
        x=scenario_df["Scenario"], y=scenario_df["Avg Wait Reguler"],
        name="Wait Reguler", marker_color=RED,
        text=scenario_df["Avg Wait Reguler"].round(2),
        textposition="outside", textfont=dict(color="white", size=10)
    ), secondary_y=False)

    fig.add_trace(go.Bar(
        x=scenario_df["Scenario"], y=scenario_df["Avg Queue Length"],
        name="Queue Length", marker_color="#FFD700",
        text=scenario_df["Avg Queue Length"].round(2),
        textposition="outside", textfont=dict(color="white", size=10)
    ), secondary_y=False)

    fig.add_trace(go.Scatter(
        x=scenario_df["Scenario"], y=scenario_df["Utilisasi"],
        mode="lines+markers", name="Utilisasi",
        line=dict(color="white", width=3),
        marker=dict(size=8, color="white")
    ), secondary_y=True)

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=CARD, plot_bgcolor=CARD,
        font=dict(color="white", family="Poppins"),
        height=440,
        margin=dict(l=10, r=10, t=10, b=10),
        barmode="group",
        legend=dict(orientation="h", y=1.05, font=dict(size=11)),
    )
    fig.update_yaxes(title_text="Nilai",     secondary_y=False, gridcolor="rgba(255,255,255,0.05)")
    fig.update_yaxes(title_text="Utilisasi", secondary_y=True,  range=[0, 1.5], showgrid=False)

    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---- GAUGE ----
with middle:
    st.markdown('<div class="section-card"><div class="section-title">⚡ UTILISASI SISTEM (RATA-RATA)</div>', unsafe_allow_html=True)

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=avg_util,
        number={"suffix": f" ({avg_util*100:.0f}%)", "font": {"size": 20, "color": "white"}},
        title={"text": "Tingkat Utilisasi Petugas Sortir", "font": {"size": 11, "color": "#C9C9C9"}},
        gauge={
            "axis": {"range": [0, 1], "tickfont": {"size": 10, "color": "white"}},
            "bar":  {"color": PRIMARY, "thickness": 0.3},
            "bgcolor": "rgba(0,0,0,0)",
            "borderwidth": 0,
            "steps": [
                {"range": [0,   0.5], "color": "#1a3d1a"},
                {"range": [0.5, 0.8], "color": "#4a3500"},
                {"range": [0.8, 1.0], "color": "#4a0a0a"},
            ],
            "threshold": {
                "line": {"color": "white", "width": 2},
                "thickness": 0.8,
                "value": avg_util
            },
        }
    ))

    gauge.update_layout(
        template="plotly_dark",
        paper_bgcolor=CARD,
        font=dict(color="white", family="Poppins"),
        height=440,
        margin=dict(l=20, r=20, t=30, b=20),
    )

    st.plotly_chart(gauge, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---- HISTOGRAM ----
with right:
    st.markdown('<div class="section-card"><div class="section-title">📈 DISTRIBUSI WAITING TIME REGULER</div>', unsafe_allow_html=True)

    hist = px.histogram(
        filtered_df, x="Avg Wait Reguler", nbins=30,
        labels={"Avg Wait Reguler": "Waiting Time (menit)", "count": "Frekuensi"}
    )
    hist.update_traces(marker_color=PRIMARY, marker_line_color="#FF8C42", marker_line_width=0.5)
    hist.update_layout(
        template="plotly_dark",
        paper_bgcolor=CARD, plot_bgcolor=CARD,
        font=dict(color="white", family="Poppins"),
        height=440,
        margin=dict(l=10, r=10, t=10, b=10),
        yaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
    )

    st.plotly_chart(hist, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

# =========================================================
# ROW 2 — Trend | Heatmap | Correlation
# =========================================================

left2, middle2, right2 = st.columns([2, 1.3, 1.3], gap="small")

# ---- TREND ----
with left2:
    st.markdown('<div class="section-card"><div class="section-title">📉 TREND WAITING TIME REGULER PER ITERASI</div>', unsafe_allow_html=True)

    trend_fig = go.Figure()
    line_colors = [PRIMARY, RED, "#FFD700", WHITE]

    for sc, color in zip(filtered_df["Scenario"].unique(), line_colors):
        temp = filtered_df[filtered_df["Scenario"] == sc]
        trend_fig.add_trace(go.Scatter(
            x=temp["Iteration"], y=temp["Avg Wait Reguler"],
            mode="lines", name=sc,
            line=dict(color=color, width=1.5)
        ))

    trend_fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=CARD, plot_bgcolor=CARD,
        font=dict(color="white", family="Poppins"),
        height=400,
        margin=dict(l=10, r=10, t=10, b=10),
        legend=dict(orientation="h", y=1.05, font=dict(size=10)),
        xaxis=dict(title="Iterasi", gridcolor="rgba(255,255,255,0.05)"),
        yaxis=dict(title="Waiting Time (menit)", gridcolor="rgba(255,255,255,0.05)"),
    )

    st.plotly_chart(trend_fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---- HEATMAP ----
with middle2:
    st.markdown('<div class="section-card"><div class="section-title">🔥 HEATMAP KINERJA SKENARIO</div>', unsafe_allow_html=True)

    heatmap_cols = ["Avg Wait Express", "Avg Wait Reguler", "Avg Queue Length", "Utilisasi"]
    heatmap_data = scenario_df.set_index("Scenario")[heatmap_cols]

    heatmap = px.imshow(
        heatmap_data,
        text_auto=".2f",
        color_continuous_scale="OrRd",
        aspect="auto"
    )
    heatmap.update_layout(
        template="plotly_dark",
        paper_bgcolor=CARD,
        font=dict(color="white", family="Poppins"),
        height=400,
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis=dict(tickangle=-20, tickfont=dict(size=10)),
        coloraxis_showscale=False,
    )

    st.plotly_chart(heatmap, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---- CORRELATION ----
with right2:
    st.markdown('<div class="section-card"><div class="section-title">🔗 KORELASI ANTAR VARIABEL</div>', unsafe_allow_html=True)

    corr_cols = ["Avg Wait Express", "Avg Wait Reguler", "Avg Queue Length", "Utilisasi"]
    corr = filtered_df[corr_cols].corr()
    corr.index   = ["Wait\nExpress", "Wait\nReguler", "Queue\nLength", "Utilisasi"]
    corr.columns = ["Wait\nExpress", "Wait\nReguler", "Queue\nLength", "Utilisasi"]

    corr_fig = px.imshow(
        corr, text_auto=".2f",
        color_continuous_scale="Oranges",
        zmin=-1, zmax=1
    )
    corr_fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=CARD,
        font=dict(color="white", family="Poppins"),
        height=400,
        margin=dict(l=10, r=10, t=10, b=10),
        coloraxis_showscale=False,
    )

    st.plotly_chart(corr_fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

# =========================================================
# BOTTOM INSIGHT ROW
# =========================================================

best_scenario  = scenario_df.loc[scenario_df["Avg Wait Reguler"].idxmin(), "Scenario"]
worst_scenario = scenario_df.loc[scenario_df["Avg Wait Reguler"].idxmax(), "Scenario"]
best_val       = scenario_df["Avg Wait Reguler"].min()
worst_val      = scenario_df["Avg Wait Reguler"].max()

b1, b2, b3, b4 = st.columns(4, gap="small")

insight_cards = [
    ("🏆 SKENARIO TERBAIK",  best_scenario,  f"Wait reguler: {best_val:.2f} menit",  "#1a3d1a", "#86efac"),
    ("⚠️ SKENARIO TERBURUK", worst_scenario, f"Wait reguler: {worst_val:.2f} menit", "#4a0a0a", "#fca5a5"),
    ("📌 INSIGHT UTAMA",     "Tambah Petugas", "Efektif turunkan queue & waiting",   "#1a1a3d", "#93c5fd"),
    ("✅ STATUS SISTEM",      "STABIL" if avg_util < 1 else "OVERLOAD",
     f"Utilisasi rata-rata: {avg_util:.2f}",
     "#1a3d1a" if avg_util < 1 else "#4a0a0a",
     "#86efac" if avg_util < 1 else "#fca5a5"),
]

for col, (title, value, desc, bg, accent) in zip([b1, b2, b3, b4], insight_cards):
    with col:
        st.markdown(f"""
        <div class="insight-card" style="border-color:{accent}33;">
            <div style="font-size:10px;font-weight:700;color:{accent};
                 letter-spacing:.07em;text-transform:uppercase;margin-bottom:8px;">{title}</div>
            <div style="font-size:16px;font-weight:800;color:white;margin-bottom:5px;">{value}</div>
            <div style="font-size:12px;color:#C9C9C9;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

st.markdown(f"""
<div class="custom-footer">
    Simulasi menggunakan <span class="footer-highlight">SimPy</span>
    &nbsp;|&nbsp;
    Model: <span class="footer-highlight">M/M/c Priority Queue</span>
    &nbsp;|&nbsp;
    Iterasi: <span class="footer-highlight">{int(df['Iteration'].max()):,}</span> per skenario
    &nbsp;|&nbsp;
    Durasi Simulasi: <span class="footer-highlight">480 menit</span>
</div>
""", unsafe_allow_html=True)
