import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# -------------------------------
# 1. Page configuration
# -------------------------------

st.set_page_config(
    page_title="LPBF Porosity Predictor",
    page_icon="🔬",
    layout="wide"
)

# -------------------------------
# 2. Load the trained model
# -------------------------------

MODEL_PATH = Path(__file__).parent / "lpbf_porosity_model.pkl"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


model = load_model()

# -------------------------------
# 3. Application heading
# -------------------------------

st.title("🔬 LPBF Porosity Prediction")

st.markdown(
    """
    ### Machine Learning for Additive Manufacturing

    Predict XCT-measured porosity in LPBF-manufactured AlSi10Mg
    using laser power, scanning speed, and hatch spacing.
    """
)

st.divider()

# -------------------------------
# 4. Input section
# -------------------------------

st.subheader("⚙️ Processing Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    laser_power = st.number_input(
        "Laser Power (W)",
        min_value=60.0,
        max_value=460.0,
        value=260.0,
        step=10.0
    )

with col2:
    scan_speed = st.number_input(
        "Scanning Speed (mm/s)",
        min_value=250.0,
        max_value=3000.0,
        value=500.0,
        step=50.0
    )

with col3:
    hatch_spacing = st.number_input(
        "Hatch Spacing (mm)",
        min_value=0.10,
        max_value=0.15,
        value=0.10,
        step=0.01,
        format="%.2f"
    )

st.divider()

# -------------------------------
# 5. Prediction
# -------------------------------

if st.button("Predict Porosity", type="primary"):

    input_data = pd.DataFrame(
        [[laser_power, scan_speed, hatch_spacing]],
        columns=[
            "laser_power_W",
            "scan_speed_mm_s",
            "hatch_spacing_mm"
        ]
    )

    prediction = model.predict(input_data)[0]

    st.subheader("📊 Prediction Results")

    result_col, details_col = st.columns(2)

    with result_col:
        st.metric(
            "Predicted XCT Porosity",
            f"{prediction:.4f}"
        )

    with details_col:
        st.write("**Input parameters used**")
        st.write(f"Laser Power: {laser_power:.2f} W")
        st.write(f"Scanning Speed: {scan_speed:.2f} mm/s")
        st.write(f"Hatch Spacing: {hatch_spacing:.2f} mm")

    st.info(
        "The prediction is an estimate from a Random Forest model. "
        "It is not an experimental measurement or a guarantee "
        "of manufacturing quality."
    )

# -------------------------------
# 6. Model information
# -------------------------------

st.divider()

st.subheader("About This Project")

st.markdown(
    """
    - **Material:** AlSi10Mg
    - **Manufacturing process:** Laser Powder Bed Fusion (LPBF)
    - **Machine Learning task:** Regression
    - **Algorithm:** Random Forest Regressor
    - **Target:** XCT-measured porosity
    - **Dataset size:** 60 experimental observations
    """
)

st.subheader("Model Performance")

metric1, metric2, metric3 = st.columns(3)

metric1.metric("Test MAE", "1.5188")
metric2.metric("Test RMSE", "2.5707")
metric3.metric("Test R²", "0.4357")

st.caption(
    "These are preliminary results from the original test split. "
    "Performance may vary on new experimental observations. "
    "The porosity unit should be confirmed from the source "
    "dataset documentation before interpreting these metrics."
)

st.warning(
    "This project is an educational research prototype. "
    "Predictions should not be used as manufacturing acceptance "
    "criteria or as a substitute for experimental validation."
)





