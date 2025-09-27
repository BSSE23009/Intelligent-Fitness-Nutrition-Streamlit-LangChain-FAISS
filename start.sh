#!/bin/bash

# Install Streamlit at runtime (no caching to save space)
pip install --no-cache-dir streamlit

# Run your app
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
