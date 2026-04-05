import pandas as pd

# ฟังก์ชันโหลดข้อมูลเที่ยวบินจากไฟล์ CSV
def load_data(file_path="thailand_flights_updated_schedule (1) (1).csv"):
    # โหลดข้อมูลจากไฟล์ CSV
    df = pd.read_csv(file_path)
    
    # ตรวจสอบว่ามีข้อมูลอยู่หรือไม่
    if df.empty:
        print("No flight data found.")
        return None
    return df
