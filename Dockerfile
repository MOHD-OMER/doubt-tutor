# ---- Base Python Image ----
FROM python:3.10-slim

# ---- Set Work Directory ----
WORKDIR /app

# ---- Install System Dependencies ----
# (Needed for Pillow, PDFs, ReportLab)
RUN apt-get update && apt-get install -y \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# ---- Copy Project Files ----
COPY . /app

# ---- Install Python Dependencies ----
RUN pip install --no-cache-dir -r requirements.txt

# ---- Expose Streamlit Port ----
EXPOSE 8501

# ---- Run the Streamlit App ----
CMD ["streamlit", "run", "ui/app.py", "--server.address=0.0.0.0", "--server.port=8501"]
