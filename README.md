# NSE_proj

## Overview

**NSE_proj** is a comprehensive Python-based project for automated extraction of key information from scanned cheque images, utilizing state-of-the-art computer vision and OCR (Optical Character Recognition) techniques. The project combines a custom-trained YOLOv8 model for region-of-interest detection on cheques with advanced OCR preprocessing and multi-stage text recognition using Tesseract. Additionally, it features a FastAPI-based speech-to-text module powered by OpenAI's Whisper, enabling audio transcription as part of its data-processing pipeline.

---

## Main Features

### Cheque Image Processing and OCR

- **Region Detection (YOLOv8):**  
  Localizes and classifies regions of interest on cheque images, such as account number, bank name, IFSC code, and drawer/person name, using a custom-trained YOLOv8 model.

- **Advanced Image Preprocessing:**  
  Applies denoising, upscaling, contrast enhancement (CLAHE), deblurring, sharpening, and adaptive binarization (Sauvola thresholding) to optimize images for accurate OCR.

- **Robust Multi-Stage OCR Pipeline:**  
  - Crops and processes detected regions individually.
  - Runs multiple OCR strategies with varying configurations to maximize accuracy.
  - Uses regex-based validation and extraction for specific fields (e.g., IFSC code patterns, account number formats).
  - Falls back to full-image OCR if region-based extraction is unsuccessful.

- **Result Aggregation:**  
  - Outputs results to consolidated CSV files, listing each cheque's extracted fields.
  - Saves per-image TXT files detailing the detected fields for audit and review.

### Speech-to-Text Transcription

- **FastAPI Web Service:**  
  Provides a web interface to record audio via browser and transcribe it using OpenAI's Whisper model.

- **Live Microphone Integration:**  
  Records short audio samples, processes them, and returns text transcriptions.

---

## Detailed Repository Structure

```
NSE_proj/
├── cheque_pytesseract.py       # Main cheque image processing and OCR script
├── speech_2_text.py            # FastAPI server for speech-to-text
├── README.md                   # Project documentation
├── <other scripts/files>       # Any additional modules or resources
```

### Key Scripts

- **cheque_pytesseract.py**  
  - Handles cheque image loading, YOLOv8 detection, advanced preprocessing, multi-stage OCR, regex-based field extraction, and result saving.
  - Configurable to work with different datasets, model weights, and output locations.

- **speech_2_text.py**  
  - Minimal FastAPI server with endpoints to record audio and transcribe using Whisper.
  - Easy-to-use HTML interface for triggering audio recording and transcription.

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/AnshumaanSingh21/NSE_proj.git
cd NSE_proj
```

### 2. Python Dependencies

Install all required Python packages:

```bash
pip install ultralytics opencv-python-headless pytesseract fuzzywuzzy fastapi sounddevice scipy pillow whisper
```

### 3. System Dependencies

Install Tesseract OCR engine:

```bash
sudo apt-get install tesseract-ocr
```

For Google Colab, use:

```python
!apt install -y tesseract-ocr
```

### 4. Prepare Cheque Dataset and Model

- Place your cheque images in the path specified by `image_dir` (default: `/content/drive/MyDrive/cheque_project/dataset`).
- Put your trained YOLOv8 weights (`best.pt`) in the configured location.
- Adjust `image_dir`, `model_path`, and output paths in `cheque_pytesseract.py` as needed.

### 5. (Optional) Google Drive Integration

If running on Colab, the script will mount Google Drive for dataset/model access.

---

## Usage

### Cheque Information Extraction

Run the cheque information extraction script:

```bash
python cheque_pytesseract.py
```

- **Outputs:**
  - CSV file (e.g., `cheque_data1.csv`, `cheque_data_enhanced.csv`, etc.) with extracted fields for all images.
  - TXT files (e.g., in `results` or `enhanced_results_txts`) with per-image field details.

**Extracted Fields:**
- Bank Name
- Drawer/Person Name
- IFSC Code
- Account Number

### Speech-to-Text Service

Start the FastAPI server for speech transcription:

```bash
uvicorn speech_2_text:app --reload
```

- Visit [http://localhost:8000](http://localhost:8000) in your browser.
- Click "Start Recording & Transcribe" to record and transcribe your voice.

---

## Configuration

- **Expected Classes**:  
  Edit the `expected_classes` list in `cheque_pytesseract.py` to customize which cheque fields are detected and extracted.
- **Model and Directory Paths**:  
  Change `image_dir`, `model_path`, and output file paths to match your environment and data organization.

---

## Example Workflow

1. Train a YOLOv8 model on annotated cheque images for field detection.
2. Put the trained model (`best.pt`) in your drive or local path.
3. Place cheque images in the input directory.
4. Run `cheque_pytesseract.py` to extract information and save results.
5. Optionally, use `speech_2_text.py` for transcribing spoken cheque details.

---

## Advanced Details

- **Preprocessing Techniques**:  
  - Uses CLAHE for local contrast enhancement.
  - Applies noise reduction and sharpening for better text clarity.
  - Employs Sauvola adaptive binarization for robust text segmentation.

- **OCR Strategies**:  
  - Multiple configuration profiles for Tesseract (`--oem`, `--psm` options).
  - Whitelisting digits for account number extraction.
  - Pattern matching for IFSC codes and bank names.

- **Error Handling**:  
  - Skips unreadable or corrupt images.
  - Logs and prints extraction status for each field and image.

---

## Troubleshooting

- Ensure the correct Tesseract path is set in `pytesseract.pytesseract.tesseract_cmd` if not using default installation.
- Verify YOLOv8 model weights are compatible with the ultralytics library version.
- For large datasets, consider batch processing and monitoring memory usage.

---

## License

_No license specified. Please add a LICENSE file if you intend to open-source your work._

## Author

- [AnshumaanSingh21](https://github.com/AnshumaanSingh21)

---

For bug reports, feature requests, or contributions, please open an issue or submit a pull request.
