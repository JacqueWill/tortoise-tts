# Quick Start - Marathi Voice Cloning

## 🎯 Goal
Clone your mother's voice (19 WAV files, ~3 minutes) for Marathi text-to-speech.

## ⚡ 3-Step Quick Start

### 1️⃣ Setup Voice Files
```powershell
.\setup_mom_voice.ps1
```

### 2️⃣ Install Dependencies (First Time Only)
```powershell
pip install -r requirements.txt
python setup.py install
```

### 3️⃣ Verify Setup
```powershell
python test_setup.py
```

## 🚀 Generate Speech

### Option A: Use the Custom Script
```powershell
python marathi_tts.py
```

### Option B: Command Line
```powershell
# Fast test
python tortoise\do_tts.py --text "नमस्कार" --voice mom_marathi --preset fast

# Better quality
python tortoise\do_tts.py --text "तुमचा मराठी मजकूर" --voice mom_marathi --preset standard --candidates 3
```

## 📖 Full Documentation
See **MARATHI_GUIDE.md** for complete instructions, troubleshooting, and advanced features.

## ⚙️ Quality Presets
- `ultra_fast` - Quick test (10-20 sec)
- `fast` - Good for testing (30-60 sec) ⭐ Start here
- `standard` - Recommended quality (1-3 min) ⭐⭐ Best balance
- `high_quality` - Best quality (3-6 min)

## 🎵 Output Location
Generated audio files will be in:
- `results/` (default)
- `marathi_output/` (when using marathi_tts.py)

## ❤️ Important Note
This is a beautiful way to preserve your mother's voice. The 19 clips you have should work well. First generation will download ~4GB of models.

**Good luck!** 🙏
