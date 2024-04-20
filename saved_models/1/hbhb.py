import os

model_path = "../saved_models/1"
if os.path.exists(model_path):
    print(f"Model file exists at {os.path.abspath(model_path)}")
else:
    print(f"Model file does not exist at {os.path.abspath(model_path)}")
