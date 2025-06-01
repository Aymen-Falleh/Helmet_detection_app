import streamlit as st
from ultralytics import YOLO
import tempfile
import os
import zipfile

st.title("👷 Helmet Detection App")

uploaded_files = st.file_uploader("Upload one or more images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    model = YOLO("best.pt")
    output_files = []

    for uploaded_file in uploaded_files:
        file_extension = uploaded_file.name.split('.')[-1]

        with tempfile.NamedTemporaryFile(suffix='.' + file_extension, delete=False) as tmp:
            tmp.write(uploaded_file.read())
            image_path = tmp.name

        results = model(image_path)

        output_path = image_path.replace(f".{file_extension}", f"_output.{file_extension}")
        results[0].save(output_path)
        output_files.append((output_path, uploaded_file.name))

        st.image(output_path, caption=f"Result for {uploaded_file.name}", use_column_width=True)

        with open(output_path, "rb") as file:
            st.download_button(
                label=f"Download result for {uploaded_file.name}",
                data=file,
                file_name=f"{os.path.splitext(uploaded_file.name)[0]}_result.{file_extension}",
                mime=f"image/{file_extension}"
            )
    
    # Show "Download All Results" button if more than one file
    if len(output_files) > 1:
        with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as tmp_zip:
            zip_path = tmp_zip.name
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file_path, orig_name in output_files:
                arcname = f"{os.path.splitext(orig_name)[0]}_result{os.path.splitext(orig_name)[1]}"
                zipf.write(file_path, arcname=arcname)
        
        with open(zip_path, "rb") as fzip:
            st.download_button(
                label="Download All Results",
                data=fzip,
                file_name="all_results.zip",
                mime="application/zip"
            )
