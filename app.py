
import streamlit as st

st.set_page_config(page_title="Sotalcalcular", layout="centered")

st.markdown("""
<style>
/* Background and container */
body {
  background: #e9eef3;
}
.block-container {
  padding-top: 1rem;
  padding-bottom: 1rem;
  max-width: 520px;
  padding-left: 16px;
  padding-right: 16px;
}

/* Card style */
.card {
  background: #e9eef3;
  border-radius: 16px;
  padding: 12px;
  margin-bottom: 12px;
  box-shadow: 8px 8px 16px #c6ccd1, -8px -8px 16px #ffffff;
}

/* Headings */
h2 {
  margin: 0;
  padding: 0;
}

/* Inputs */
input[type="number"] {
  width: 100% !important;
  padding: 10px 12px !important;
  border-radius: 10px !important;
  border: none !important;
  background: #e9eef3 !important;
  box-shadow: inset 6px 6px 10px #c6ccd1, inset -6px -6px 10px #ffffff;
  outline: none !important;
  font-size: 16px !important;
}

/* Buttons full width */
div.stButton > button {
  width: 100%;
  height: 44px;
  border-radius: 10px;
  border: none;
  background: #e9eef3;
  box-shadow: 6px 6px 12px #c6ccd1, -6px -6px 12px #ffffff;
  font-size: 16px;
}

/* Compact metric text */
[data-testid="stMetricValue"] {
  font-size: 18px;
  font-weight: 700;
}

/* Small footer */
.small-muted {
  text-align:center;
  font-size:12px;
  color:#666;
  margin-top:6px;
}
</style>
""", unsafe_allow_html=True)

# Compact title
st.markdown("<h2 style='text-align:center; margin-bottom:6px;'>Sotalcalcular</h2>", unsafe_allow_html=True)

# Situación Actual
st.markdown("<div class='card'><b>Situación Actual</b></div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,1,1])
with col1:
    cantidad_actual = st.number_input("Cantidad", min_value=0.0, value=0.0, step=1.0, format="%.2f", key="cantidad_actual")
with col2:
    beneficio_actual = st.number_input("Beneficio", min_value=-9999999.0, value=0.0, step=1.0, format="%.2f", key="beneficio_actual")
with col3:
    yield_actual = (beneficio_actual / cantidad_actual) if cantidad_actual > 0 else 0.0
    st.metric("Yield", f"{yield_actual*100:.2f}%")

# Input card
st.markdown("<div class='card'><b>Introduce cantidad y cuota</b></div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,1,1])
with col1:
    stake_posible = st.number_input("Stake", min_value=0.0, value=10.0, step=1.0, format="%.2f", key="stake_posible")
with col2:
    cuota_posible = st.number_input("Cuota", min_value=1.0, value=2.00, step=0.01, format="%.2f", key="cuota_posible")
with col3:
    beneficio_posible = stake_posible * (cuota_posible - 1)
    st.metric("Beneficio", f"{beneficio_posible:.2f}")

# Results card
st.markdown("<div class='card'><b>Resultados</b></div>", unsafe_allow_html=True)

beneficio_acertado = beneficio_actual + beneficio_posible
cantidad_acertado = cantidad_actual + stake_posible
yield_acertado = (beneficio_acertado / cantidad_acertado) if cantidad_acertado > 0 else 0.0

beneficio_fallado = beneficio_actual - stake_posible
cantidad_fallado = cantidad_actual + stake_posible
yield_fallado = (beneficio_fallado / cantidad_fallado) if cantidad_fallado > 0 else 0.0

beneficio_nulo = beneficio_actual
cantidad_nulo = cantidad_actual + stake_posible
yield_nulo = (beneficio_nulo / cantidad_nulo) if cantidad_nulo > 0 else 0.0

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("✅ Acertado", f"{yield_acertado*100:.2f}%", delta=f"B: {beneficio_acertado:.2f}")
with col2:
    st.metric("❌ Fallado", f"{yield_fallado*100:.2f}%", delta=f"B: {beneficio_fallado:.2f}")
with col3:
    st.metric("➖ Nulo", f"{yield_nulo*100:.2f}%", delta=f"B: {beneficio_nulo:.2f}")

st.markdown("<div class='small-muted'>Compacto — diseñado para móvil</div>", unsafe_allow_html=True)
