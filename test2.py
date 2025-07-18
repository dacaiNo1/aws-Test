import boto3
import pandas as pd
import streamlit as st
from io import StringIO

# Read secrets
aws_access_key = st.secrets["aws_access_key"]
aws_secret_key = st.secrets["aws_secret_key"]
aws_region = st.secrets["aws_region"]

# UI inputs
st.title("Preview CSV from S3")
bucket_name = st.text_input("S3 Bucket Name", value="hannahtest12345")
file_key = st.text_input("S3 File Key", value="Anomaly Testing - Amount.csv.csv")

if st.button("Load and Preview File"):
    try:
        s3 = boto3.client(
            's3',
            region_name=aws_region,
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )

        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        content = response['Body'].read().decode('utf-8')
        df = pd.read_csv(StringIO(content))

        st.success("File loaded successfully!")
        st.dataframe(df)

    except Exception as e:
        st.error(f"Failed to load file: {e}")
