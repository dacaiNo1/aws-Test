import boto3
import pandas as pd
import streamlit as st
from io import StringIO

# Streamlit UI
st.title("Preview CSV from S3")

# User input for S3 file details
bucket_name = st.text_input("S3 Bucket Name", value="hannahtest12345")
file_key = st.text_input("S3 File Key (e.g. folder/file.csv)", value="Anomaly Testing - Amount.csv.csv")
region = st.text_input("AWS Region", value="us-east-2")

# Button to load and preview
if st.button("Load and Preview File"):

    try:
        # Create S3 client
        s3 = boto3.client('s3', region_name=region)

        # Read object from S3
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        content = response['Body'].read().decode('utf-8')

        # Load CSV into pandas
        df = pd.read_csv(StringIO(content))

        # Show preview
        st.success("File loaded successfully!")
        st.dataframe(df)

    except Exception as e:
        st.error(f"Failed to load file: {e}")
