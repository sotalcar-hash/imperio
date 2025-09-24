
import streamlit as st

st.set_page_config(page_title="Tipster Dashboard", layout="centered")

st.markdown(
    """
    <style>
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        font-size: 1em;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📊 Tipster Dashboard")

# Situación Actual
st.subheader("Situación Actual")
col1, col2, col3 = st.columns(3)
with col1:
    cantidad_actual = st.number_input("Cantidad", min_value=0.0, value=0.0, step=1.0, format="%.2f", key="cantidad_actual")
with col2:
    beneficio_actual = st.number_input("Beneficio", value=0.0, step=1.0, format="%.2f", key="beneficio_actual")
with col3:
    yield_actual = (beneficio_actual / cantidad_actual) if cantidad_actual > 0 else 0.0
    st.metric("Yield", f"{yield_actual*100:.2f}%")

st.markdown("---")

# Caja Posible
st.subheader("Caja Posible")
col1, col2, col3 = st.columns(3)
with col1:
    stake_posible = st.number_input("Stake", min_value=0.0, value=0.0, step=1.0, format="%.2f", key="stake_posible")
with col2:
    cuota_posible = st.number_input("Cuota", min_value=1.0, value=1.0, step=0.01, format="%.2f", key="cuota_posible")
with col3:
    beneficio_posible = stake_posible * (cuota_posible - 1)
    st.metric("Beneficio", f"{beneficio_posible:.2f}")

st.markdown("---")

# Escenarios
st.subheader("Escenarios")

# Acertado
beneficio_acertado = beneficio_actual + beneficio_posible
cantidad_acertado = cantidad_actual + stake_posible
yield_acertado = (beneficio_acertado / cantidad_acertado) if cantidad_acertado > 0 else 0.0

# Fallado
beneficio_fallado = beneficio_actual - stake_posible
cantidad_fallado = cantidad_actual + stake_posible
yield_fallado = (beneficio_fallado / cantidad_fallado) if cantidad_fallado > 0 else 0.0

# Nulo
beneficio_nulo = beneficio_actual
cantidad_nulo = cantidad_actual + stake_posible
yield_nulo = (beneficio_nulo / cantidad_nulo) if cantidad_nulo > 0 else 0.0

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("✅ Acertado", f"{yield_acertado*100:.2f}%", f"B:{beneficio_acertado:.2f} / C:{cantidad_acertado:.2f}")
with col2:
    st.metric("❌ Fallado", f"{yield_fallado*100:.2f}%", f"B:{beneficio_fallado:.2f} / C:{cantidad_fallado:.2f}")
with col3:
    st.metric("➖ Nulo", f"{yield_nulo*100:.2f}%", f"B:{beneficio_nulo:.2f} / C:{cantidad_nulo:.2f}")
