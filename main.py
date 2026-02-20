import os
from pdf2docx import Converter
from docx2pdf import convert as docx_to_pdf
from PIL import Image
from moviepy.editor import VideoFileClip
import pandas as pd

class UniversalConverter:
    # 1. PDF -> WORD
    @staticmethod
    def pdf_to_word(pdf_path, docx_path):
        cv = Converter(pdf_path)
        cv.convert(docx_path)
        cv.close()
        print(f"✅ Word fayl tayyor: {docx_path}")

    # 2. WORD -> PDF
    @staticmethod
    def word_to_pdf(docx_path, pdf_path):
        docx_to_pdf(docx_path, pdf_path)
        print(f"✅ PDF fayl tayyor: {pdf_path}")

    # 3. RASM FORMATINI O'ZGARTIRISH (masalan PNG -> JPG)
    @staticmethod
    def convert_image(input_img, output_img, format="JPEG"):
        img = Image.open(input_img)
        if format == "JPEG":
            img = img.convert("RGB")
        img.save(output_img, format=format)
        print(f"✅ Rasm saqlandi: {output_img}")

    # 4. VIDEO -> AUDIO (MP4 -> MP3)
    @staticmethod
    def video_to_audio(video_path, audio_path):
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(audio_path)
        print(f"✅ Ovoz fayli ajratib olindi: {audio_path}")

    # 5. EXCEL -> CSV
    @staticmethod
    def excel_to_csv(excel_path, csv_path):
        df = pd.read_excel(excel_path)
        df.to_csv(csv_path, index=False)
        print(f"✅ CSV fayl tayyor: {csv_path}")

# --- ISHLATIB KO'RISH ---
if __name__ == "__main__":
    conv = UniversalConverter()
    
    # Misollar (fayl nomlarini o'zingiznikiga almashtiring):
    # conv.pdf_to_word("test.pdf", "test.docx")
    # conv.word_to_pdf("test.docx", "test.pdf")
    # conv.convert_image("logo.png", "logo.jpg", "JPEG")
    # conv.video_to_audio("kino.mp4", "music.mp3")
    # conv.excel_to_csv("hisobot.xlsx", "hisobot.csv")
