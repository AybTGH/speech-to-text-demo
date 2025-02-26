# Speech-to-Text Prototype Using French Audio Data

## 📌 Project Overview
This project demonstrates a **speech-to-text** pipeline using **French audio recordings** from the OpenSLR dataset. The goal is to process `.flac` audio files, convert them into text, and compare the predicted transcriptions with the provided ground truth transcripts.

## 📂 Dataset Information
We are using the **OpenSLR MediaSpeech dataset** from [OpenSLR](https://www.openslr.org/108/). This dataset contains:
- **French audio recordings** in `.flac` format
- **Manual transcriptions** in `.txt` format
- **Metadata** including speaker and environment information

### 🗂 Example File Structure
```
/data
├── sample.flac  # Audio file (French speech)
├── sample.txt   # Ground truth transcription
```

## 🛠 Script Overview
The script processes `.flac` audio files and extracts speech using **Google Speech Recognition API**.

### **Main Features**
✅ Reads `.flac` files from the dataset
✅ Converts speech to text using **`speech_recognition`**
✅ Compares predictions with ground truth transcripts
✅ Uses `mutagen` to extract metadata from FLAC files

### **Dependencies**
Install the required libraries before running the script:
```bash
pip install mutagen speechrecognition numpy
```

### **How to Run the Script**
Run the Python script to test speech-to-text conversion:
```bash
python speech_to_text.py
```

### **Expected Output**
```
🔹 Predicted Text:
"Bonjour, bienvenue dans notre test de reconnaissance vocale."

✅ Actual Transcript:
"Bonjour, bienvenue dans notre test de reconnaissance vocale."

🎉 Perfect match!
```

## 📌 Next Steps
- Improve transcription accuracy using a **custom speech model**
- Evaluate **error rate (WER - Word Error Rate)**
- Experiment with **different speech recognition APIs** (Whisper, Vosk, etc.)

📌 Stay tuned for more updates! 🚀

