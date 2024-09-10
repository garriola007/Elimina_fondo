import os
from PIL import Image
from rembg import remove
import streamlit as st

def save_upload_file(upload_file):
  upload_dir = "uploads"
  if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)
  file_path = os.path.join(upload_dir, uploaded_file.name)
  with open(file_path, "wb") as f:
    f.write(uploaded_file.getbuffer())
  return file_path

def run_background_remover(input_img_file):
  input_img_path = save_uploaded_file(input_img_file)
  output_img_path = input_img_path.replace(_old:'.', __new:'__rmbg.').replace(__old:'jpeg', __new:'png')
  try:
    image = Image.open(input_img_path)
  
  
    
  
