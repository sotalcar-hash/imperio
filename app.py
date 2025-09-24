
import streamlit as st

st.set_page_config(page_title="Sotalcalcular", layout="centered")

# Minimal, safe CSS: only adjust button width and metric text.
st.markdown(
    """
    <style>
    /* Make Streamlit buttons full width (safe selector) */
    div.stButton > button {
        width: 100%;
        height: 44px;
        border-radius: 10px;
    }
    /* Slightly larger metric value */
    [data-testid="stMetricValue"] {
        font-size: 18px;
        font-weight: 700;
    }
    /* Small spacing adjustments */
    .stAlert, .stException {
        max-width: 520px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown("<h2 style='text-align:center; margin: 6px 0 10px 0;'>Sotalcalcular</h2>", unsafe_allow_html=True)

# --- Situación Actual (compact) ---
st.markdown("**Situación Actual**")
col1, col2, col3 = st.columns([1,1,1])
with col1:
    cantidad_actual = st.number_input("Cantidad", min_value=0.0, value=0.0, step=1.0, format="%.2f", key="cantidad_actual")
with col2:
    beneficio_actual = st.number_input("Beneficio", min_value=-1e9, value=0.0, step=1.0, format="%.2f", key="beneficio_actual")
with col3:
    yield_actual = (beneficio_actual / cantidad_actual) if cantidad_actual > 0 else 0.0
    st.metric("Yield", f"{yield_actual*100:.2f}%")

st.markdown("---")

# --- Caja Posible ---
st.markdown("**Introduce cantidad y cuota**")
col1, col2 = st.columns([1,1])
with col1:
    stake_posible = st.number_input("Stake", min_value=0.0, value=10.0, step=1.0, format="%.2f", key="stake_posible")
with col2:
    cuota_posible = st.number_input("Cuota", min_value=1.0, value=2.00, step=0.01, format="%.2f", key="cuota_posible")

beneficio_posible = stake_posible * (cuota_posible - 1)
st.metric("Beneficio posible", f"{beneficio_posible:.2f} €")

st.markdown("---")

# --- Resultados ---
st.markdown("**Resultados**")

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

st.markdown("<div style='text-align:center; font-size:12px; color:#666; margin-top:8px;'>Si los campos no se pueden editar, reemplaza app.py por este archivo y haz un Rerun en Streamlit Cloud.</div>", unsafe_allow_html=True)
