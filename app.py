
import streamlit as st

st.set_page_config(page_title="Tipster Dashboard", layout="wide")

st.title("Dashboard Tipster — Situación vs Apuesta posible")
st.write("Interfaz sencilla para calcular cómo afecta una apuesta a tu yield actual. Introduce 'Cantidad apostada' y 'Beneficio' en Situación Actual (beneficio = ganancia neta acumulada). En Caja Posible indica la apuesta que estudias. Por defecto el beneficio posible se calcula como stake*(cuota-1) (ganancia neta).")

# Situación Actual
st.header("Situación Actual")
col1, col2 = st.columns([1,2])
with col1:
    cantidad_actual = st.number_input("Cantidad apostada (total hasta ahora)", min_value=0.0, value=0.0, step=1.0, format="%.2f", key="cantidad_actual")
    beneficio_actual = st.number_input("Beneficio neto (total hasta ahora)", value=0.0, step=1.0, format="%.2f", key="beneficio_actual")
with col2:
    if cantidad_actual > 0:
        yield_actual = beneficio_actual / cantidad_actual
    else:
        yield_actual = 0.0
    st.metric("Yield actual", f"{yield_actual*100:.2f} %")
    st.write("Interpretación: Yield = Beneficio (neto) / Cantidad apostada (total). Si tu definición de 'beneficio' es distinta, usa la caja posible en modo 'Introducir beneficio manual' para ajustar.")

st.markdown("---")

# Caja Posible
st.header("Caja Posible (apuesta que evalúas)")
col1, col2 = st.columns([1,2])
with col1:
    stake_posible = st.number_input("Cantidad apostada (apuesta)", min_value=0.0, value=10.0, step=1.0, format="%.2f", key="stake_posible")
    cuota_posible = st.number_input("Cuota", min_value=1.0, value=2.0, step=0.01, format="%.3f", key="cuota_posible")
    modo_beneficio = st.radio("Modo de cálculo del beneficio posible", 
                              ("Calcular ganancia neta automáticamente (recomendado)", "Introducir beneficio neto manualmente"),
                              index=0)
    if modo_beneficio.startswith("Calcular"):
        beneficio_posible_calc = stake_posible * (cuota_posible - 1)
        beneficio_posible = beneficio_posible_calc
        st.write(f"Ganancia neta calculada: {beneficio_posible_calc:.2f} (stake * (cuota - 1)).")
        st.write(f"Retorno bruto (stake * cuota): {stake_posible * cuota_posible:.2f}.")
    else:
        beneficio_posible = st.number_input("Beneficio neto (introducido manualmente)", value=0.0, format="%.2f", key="beneficio_posible_manual")
        beneficio_posible_calc = beneficio_posible
        st.write("Has elegido introducir el beneficio neto manualmente. Asegúrate de que es la ganancia neta (no el retorno bruto).")

st.markdown("---")

# Escenarios
st.header("Escenarios (resultado tras evaluar la apuesta)")

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
    st.subheader("Acertado")
    st.metric("Yield", f"{yield_acertado*100:.2f} %")
    st.write(f"Beneficio neto total: {beneficio_acertado:.2f}")
    st.write(f"Cantidad apostada total: {cantidad_acertado:.2f}")
with col2:
    st.subheader("Fallado")
    st.metric("Yield", f"{yield_fallado*100:.2f} %")
    st.write(f"Beneficio neto total: {beneficio_fallado:.2f}")
    st.write(f"Cantidad apostada total: {cantidad_fallado:.2f}")
with col3:
    st.subheader("Nulo")
    st.metric("Yield", f"{yield_nulo*100:.2f} %")
    st.write(f"Beneficio neto total: {beneficio_nulo:.2f}")
    st.write(f"Cantidad apostada total: {cantidad_nulo:.2f}")

st.markdown("---")
st.write("Notas: 1) El app trata 'Beneficio' como ganancia neta acumulada. 2) Si quieres que la 'Situación Actual' sea compartida en tiempo real entre dos usuarios, hay que conectar el app a una hoja de cálculo (Google Sheets) o a una pequeña base de datos; dímelo y lo implemento. 3) Para desplegar en Streamlit Cloud necesitas un repositorio en GitHub con este fichero y un requirements.txt con 'streamlit'.")
