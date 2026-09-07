import streamlit as st

# ================= PAGE CONFIGURATION =================
st.set_page_config(
    page_title="Web3 & Trading Intelligence Suite",
    page_icon="🚀",
    layout="wide"
)

# ================= CUSTOM CSS & ANIMATIONS =================
st.markdown("""
    <style>
    /* Main Dashboard Background */
    .stApp {
        background: linear-gradient(135deg, #090d16 0%, #111827 50%, #1f2937 100%) !important;
        color: #f8fafc !important;
        overflow-x: hidden;
    }
    
    /* Dynamic Flying Rocket Animation Across Screen */
    @keyframes flyAcross {
        0% { transform: translate(-100px, 80vh) rotate(-35deg); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translate(105vw, -20vh) rotate(-35deg); opacity: 0; }
    }

    .flying-rocket-dynamic {
        position: fixed;
        bottom: 0px; left: 0px; font-size: 38px; z-index: 9999;
        pointer-events: none; animation: flyAcross 12s linear infinite;
        filter: drop-shadow(0 0 10px #38bdf8);
    }
    .flying-rocket-dynamic.delayed {
        animation-delay: 6s; animation-duration: 10s; font-size: 28px;
    }

    /* Glowing PCB & Blockchain Circuit Background Animation */
    @keyframes pcbCircuitFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .blockchain-pcb-box {
        background: linear-gradient(135deg, #0f172a, #1e1b4b, #0284c7, #1e1b4b, #0f172a);
        background-size: 300% 300%;
        animation: pcbCircuitFlow 8s ease infinite;
        border: 2px solid #38bdf8;
        box-shadow: 0 0 30px rgba(56, 189, 248, 0.35), inset 0 0 20px rgba(59, 130, 246, 0.4);
        padding: 28px 32px;
        border-radius: 16px;
        margin-bottom: 25px;
        position: relative;
    }

    /* Animated Sidebar Gradient */
    @keyframes sidebarGlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(135deg, #090d16, #1e1b4b, #0f172a, #172554) !important;
        background-size: 300% 300% !important;
        animation: sidebarGlow 10s ease infinite !important;
        border-right: 2px solid #38bdf8 !important;
        box-shadow: 5px 0 25px rgba(56, 189, 248, 0.2);
    }
    
    /* Neon Pulse Animation for Sidebar Containers */
    @keyframes neonPulse {
        0% { box-shadow: 0 0 12px rgba(56, 189, 248, 0.3); border-color: #38bdf8; }
        50% { box-shadow: 0 0 28px rgba(59, 130, 246, 0.75); border-color: #60a5fa; }
        100% { box-shadow: 0 0 12px rgba(56, 189, 248, 0.3); border-color: #38bdf8; }
    }

    /* Target Streamlit Native Bordered Container inside Sidebar */
    section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] [data-testid="stContainer"] {
        background: linear-gradient(145deg, #1e1b4b, #0f172a, #1e293b) !important;
        background-size: 200% 200% !important;
        animation: pcbCircuitFlow 6s ease infinite, neonPulse 4s ease infinite !important;
        border: 2px solid #38bdf8 !important;
        border-radius: 14px !important;
        padding: 14px 10px !important;
        margin-bottom: 18px !important;
    }
    
    /* Force Sidebar Text Colors */
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] label, 
    section[data-testid="stSidebar"] span, 
    section[data-testid="stSidebar"] div,
    section[data-testid="stSidebar"] p {
        color: #f8fafc !important;
    }
    
    /* Main Area Typography */
    h1, h2, h3, h4, h5, h6 { color: #38bdf8 !important; }
    p, span, label { color: #f1f5f9 !important; }
    </style>

    <div class="flying-rocket-dynamic">🚀</div>
    <div class="flying-rocket-dynamic delayed">🛸</div>
""", unsafe_allow_html=True)

# ================= HEADER BANNER =================
st.markdown("""
    <div class="blockchain-pcb-box">
        <h1 style="color: #ffffff; margin: 0; font-size: 2.3rem; text-shadow: 0 0 10px #38bdf8;">🚀 Web3 & Trading Intelligence Suite</h1>
        <p style="color: #e2e8f0; margin-top: 8px; margin-bottom: 0; font-size: 1.15rem; font-weight: 500;">
            All-in-One AI Agent Dashboard for Market Insights, Risk Management & Campaign Tracking
        </p>
    </div>
""", unsafe_allow_html=True)

# ================= SIDEBAR NAVIGATION & GLOBAL CONTROLS =================

with st.sidebar.container(border=True):
    st.markdown("### 🎛️ Navigation & Control")
    menu_option = st.radio(
        "Select Dashboard Menu:",
        [
            "📊 Live Ticker, Chart & AI Analysis", 
            "⚖️ Risk & Liquidation Calculator", 
            "🎯 Airdrop & Campaign Tracker"
        ]
    )

with st.sidebar.container(border=True):
    st.markdown("### 🪙 Asset Configuration")
    global_coin = st.text_input("Active Coin Pair", value="BTCUSDT").strip().upper()
    st.success(f"💡 Active Asset: **{global_coin}**")

# Reference dictionary for default asset prices
default_prices = {
    "BTCUSDT": 79367.52, 
    "ETHUSDT": 3450.0, 
    "SOLUSDT": 105.66, 
    "BNBUSDT": 742.27, 
    "DOGEUSDT": 0.18
}
current_price = default_prices.get(global_coin, 100.0)
tv_symbol = f"BINANCE:{global_coin}"

# ================= MAIN CONTENT RENDERED =================

if menu_option == "📊 Live Ticker, Chart & AI Analysis":
    st.subheader(f"📊 Market Intelligence & Analysis for {global_coin}")
    
    col_s1, col_s2, col_s3 = st.columns(3)
    col_s1.metric(label="Market Fear & Greed Index", value="74 (Greed)", delta="Bullish Momentum")
    col_s2.metric(label="Global 24h Volume", value="$84.5B", delta="+5.2%")
    col_s3.metric(label="BTC Dominance", value="54.2%", delta="-0.3%")
    
    st.markdown("---")
    st.markdown("##### ⚡ Live Price Ticker")
    ticker_html = f"""
    <div class="tradingview-widget-container">
      <div class="tradingview-widget-container__widget"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
      {{ "symbol": "{tv_symbol}", "width": "100%", "colorTheme": "dark", "isTransparent": false, "locale": "en" }}
      </script>
    </div>
    """
    st.components.v1.html(ticker_html, height=130)

    st.markdown(f"#### 🤖 AI Agent Technical Analysis & Trade Setup ({global_coin})")
    entry_zone_low = current_price * 0.992
    entry_zone_high = current_price * 1.000
    tp1 = current_price * 1.025
    tp2 = current_price * 1.055
    sl = current_price * 0.975

    col_a1, col_a2, col_a3 = st.columns(3)
    with col_a1:
        st.success(f"""
        **🎯 Recommended Entry Zone**
        * **Range:** ${entry_zone_low:,.2f} - ${entry_zone_high:,.2f}
        * **Bias:** Bullish Continuation
        """)
    with col_a2:
        st.info(f"""
        **🚀 Take-Profit (TP) Targets**
        * **TP 1:** ${tp1:,.2f} (+2.5%)
        * **TP 2:** ${tp2:,.2f} (+5.5%)
        """)
    with col_a3:
        st.error(f"""
        **🛑 Stop-Loss (SL) Level**
        * **SL Price:** ${sl:,.2f} (-2.5%)
        * **Risk/Reward Ratio:** 1 : 2.2
        """)

    st.markdown(f"#### 📈 Live Candlestick Chart for {global_coin}")
    chart_html = f"""
    <div class="tradingview-widget-container" style="height:500px;width:100%">
      <div id="tradingview_widget" style="height:100%;width:100%"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget({{
        "width": "100%",
        "height": "500",
        "symbol": "{tv_symbol}",
        "interval": "D",
        "timezone": "Etc/UTC",
        "theme": "dark",
        "style": "1",
        "locale": "en",
        "toolbar_bg": "#1e293b",
        "enable_publishing": false,
        "allow_symbol_change": true,
        "container_id": "tradingview_widget"
      }});
      </script>
    </div>
    """
    st.components.v1.html(chart_html, height=520)

elif menu_option == "⚖️ Risk & Liquidation Calculator":
    st.subheader(f"⚖️ Portfolio Risk & Liquidation Calculator ({global_coin})")
    st.write(f"Manage position size, risk parameters, and margin liquidation thresholds for **{global_coin}**.")
    
    st.markdown("##### ⚡ Live Market Price Feed")
    calc_ticker_html = f"""
    <div class="tradingview-widget-container">
      <div class="tradingview-widget-container__widget"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
      {{ "symbol": "{tv_symbol}", "width": "100%", "colorTheme": "dark", "isTransparent": false, "locale": "en" }}
      </script>
    </div>
    """
    st.components.v1.html(calc_ticker_html, height=120)
    
    mode = st.radio("Select Calculator Mode:", ["Spot Risk & Position Manager", "Futures Liquidation Calculator"], horizontal=True)
    
    if mode == "Spot Risk & Position Manager":
        col_r1, col_r2 = st.columns(2)
        with col_r1:
            total_capital = st.number_input("Total Wallet Capital (USDT)", value=1000.0, step=100.0)
            position_size_usd = st.number_input(f"Position Size / Capital to Invest in {global_coin} (USDT)", value=200.0, step=50.0)
            risk_pct = st.slider("Risk Tolerance per Trade (%)", 0.5, 5.0, 1.5)
        with col_r2:
            entry = st.number_input("Entry Price ($)", value=current_price, step=10.0)
            sl_pct = st.slider("Stop Loss Distance (%)", 1.0, 10.0, 3.0)
        
        coin_amount = position_size_usd / entry if entry > 0 else 0
        sl_price = entry * (1 - sl_pct / 100)
        tp_price = entry * (1 + (sl_pct * 2) / 100)
        potential_loss = position_size_usd * (sl_pct / 100)
        
        st.success(f"""
        ### 📊 Spot Position & Risk Summary ({global_coin})
        * **Allocated Investment:** **${position_size_usd:,.2f} USDT** (out of ${total_capital:,.2f} total capital)
        * **Asset Quantity Acquired:** **{coin_amount:,.4f} {global_coin.replace('USDT','')}**
        * **Suggested Entry Price:** **${entry:,.2f}**
        * **Suggested Stop-Loss Price:** **${sl_price:,.2f}** (-{sl_pct}%) $\rightarrow$ **Max Loss: ${potential_loss:,.2f} USDT**
        * **Suggested Take-Profit Price:** **${tp_price:,.2f}** (+{sl_pct*2}%, 1:2 R:R Ratio)
        """)
    else:
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            margin_usd = st.number_input("Margin / Collateral Amount (USDT)", value=100.0, step=50.0)
            margin_mode = st.selectbox("Margin Mode", ["Isolated", "Cross"])
            leverage = st.slider("Leverage (x)", 1, 150, 20)
        with col_f2:
            position_type = st.selectbox("Position Direction", ["Long (Buy)", "Short (Sell)"])
            f_entry = st.number_input("Futures Entry Price ($)", value=current_price, step=10.0)
        
        total_position_value = margin_usd * leverage
        if "Long" in position_type:
            liq_price = f_entry * (1 - (1 / leverage) + 0.005)
        else:
            liq_price = f_entry * (1 + (1 / leverage) - 0.005)
            
        st.error(f"""
        ### ⚠️ Futures Position & Liquidation Analysis ({global_coin})
        * **Margin Mode & Leverage:** **{margin_mode}** @ **{leverage}x**
        * **Margin Used:** **${margin_usd:,.2f} USDT**
        * **Total Position Exposure:** **${total_position_value:,.2f} USDT**
        * **Entry Price:** **${f_entry:,.2f}**
        * **Estimated Liquidation Price:** **${liq_price:,.2f}** ({position_type})
        """)

elif menu_option == "🎯 Airdrop & Campaign Tracker":
    st.subheader("🎯 Interactive Web3 Airdrop & Campaign Tracker Assistant")
    st.write("Manage your daily testnet interactions, smart contract deployment tasks, and community campaigns interactively.")
    
    if "custom_tasks" not in st.session_state:
        st.session_state.custom_tasks = [
            {"task": "Claim daily testnet faucet tokens", "platform": "Monad / Holesky", "link": "https://faucet.quicknode.com/"},
            {"task": "Interact with AI Agent OS smart contract", "platform": "Binance Testnet", "link": "https://testnet.binance.org/"},
            {"task": "Perform swap & liquidity provision", "platform": "DEX Testnet", "link": "https://pancakeswap.finance/"},
            {"task": "Complete daily governance vote", "platform": "DAO Portal", "link": "https://snapshot.box/"}
        ]
    
    st.markdown("#### 📋 Daily Task Checklist & Quick Links")
    
    completed_count = 0
    total_tasks = len(st.session_state.custom_tasks)
    
    for i, t in enumerate(st.session_state.custom_tasks):
        col_chk, col_btn = st.columns([4, 1])
        with col_chk:
            is_checked = st.checkbox(f"**{t['task']}** *(Platform: {t['platform']})*", key=f"task_item_{i}")
            if is_checked:
                completed_count += 1
        with col_btn:
            st.markdown(f"[🔗 Open]({t['link']})")
            
    progress = completed_count / total_tasks if total_tasks > 0 else 0
    st.markdown("---")
    st.markdown("#### 📊 Campaign Progress Overview")
    st.progress(progress)
    st.success(f"🔥 Status: Completed **{completed_count}** out of **{total_tasks}** daily tasks ({int(progress * 100)}%).")
    
    with st.expander("➕ Add New Airdrop / Testnet Task"):
        with st.form("new_task_form"):
            new_task_name = st.text_input("Task Description (e.g., Mint NFT Testnet)")
            new_task_platform = st.text_input("Platform / Network Name (e.g., Base Sepolia)")
            new_task_link = st.text_input("Platform URL (e.g., https://base.org)", value="https://")
            submit_btn = st.form_submit_button("Add Task")
            
            if submit_btn and new_task_name:
                st.session_state.custom_tasks.append({
                    "task": new_task_name,
                    "platform": new_task_platform if new_task_platform else "Web3 dApp",
                    "link": new_task_link
                })
                st.success(f"New task '{new_task_name}' added successfully! Refreshing dashboard...")
                st.rerun()

st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8; font-weight: 600;'>Web3 & Trading Intelligence Suite </p>", unsafe_allow_html=True)
