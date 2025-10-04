# Marathi Voice Cloning Guide - Your Mother's Voice

This guide will help you clone your mother's voice for Marathi text-to-speech using Tortoise TTS.

## 📋 What You Have

- **19 voice samples** (1.wav to 19.wav) ranging from 7-15 seconds each
- **~3 minutes total audio** - This is sufficient for voice cloning!
- **Voice folder**: `voice/` directory with all samples

## 🎯 Your Goal

Create a Marathi text-to-speech system that speaks in your mother's voice.

---

## 🚀 Quick Start (3 Steps)

### Step 1: Setup Voice Files

Run the setup script to prepare your voice samples:

```powershell
.\setup_mom_voice.ps1
```

This will:
- Create `tortoise/voices/mom_marathi/` directory
- Copy all 19 WAV files to the correct location
- Verify the setup

### Step 2: Install Dependencies (First Time Only)

```powershell
# Install required packages
pip install -r requirements.txt

# Install Tortoise TTS
python setup.py install
```

**Note**: The first run will download pre-trained models (~4GB) automatically.

### Step 3: Generate Speech!

**Option A - Using the custom Marathi script:**
```powershell
python marathi_tts.py
```

**Option B - Using command line:**
```powershell
python tortoise\do_tts.py --text "तुमचा मराठी मजकूर" --voice mom_marathi --preset standard --output_path results
```

---

## 📝 Detailed Usage

### Understanding Quality Presets

| Preset | Speed | Quality | Use Case |
|--------|-------|---------|----------|
| `ultra_fast` | ⚡⚡⚡ | ⭐⭐ | Quick testing |
| `fast` | ⚡⚡ | ⭐⭐⭐ | Testing & drafts |
| `standard` | ⚡ | ⭐⭐⭐⭐ | **Recommended** |
| `high_quality` | 🐌 | ⭐⭐⭐⭐⭐ | Final outputs |

### Command Line Usage

**Basic command:**
```powershell
python tortoise\do_tts.py --text "Your text" --voice mom_marathi --preset fast
```

**With all options:**
```powershell
python tortoise\do_tts.py `
    --text "नमस्कार, मी तुमची आई आहे" `
    --voice mom_marathi `
    --preset standard `
    --output_path marathi_output `
    --candidates 3 `
    --half True `
    --kv_cache True
```

**Parameters explained:**
- `--text`: Your Marathi text to speak
- `--voice`: Voice name (mom_marathi)
- `--preset`: Quality level (fast, standard, high_quality)
- `--output_path`: Where to save audio files
- `--candidates`: Generate multiple versions (3 recommended)
- `--half`: Use FP16 for faster generation
- `--kv_cache`: Speed optimization

### Python Script Usage

Edit `marathi_tts.py` and modify the main section:

```python
# Your Marathi text
marathi_text = "तुमचा मराठी संवाद"

# Generate speech
generate_marathi_speech(
    text=marathi_text,
    voice_name="mom_marathi",
    preset="standard",
    output_dir="marathi_output"
)
```

Then run:
```powershell
python marathi_tts.py
```

### Batch Processing Multiple Texts

Add multiple texts to `marathi_tts.py`:

```python
texts = [
    "पहिला वाक्य",
    "दुसरा वाक्य",
    "तिसरा वाक्य"
]

batch_generate_marathi(texts, voice_name="mom_marathi", preset="fast")
```

---

## 🎨 Advanced Techniques

### 1. Emotion Control (Prompt Engineering)

Add emotional context in brackets - it will be redacted from output but affect the tone:

```python
text = "[I am very happy] आज खूप छान दिवस आहे"
# Will speak with happy emotion but only say the Marathi text
```

### 2. Extract Conditioning Latents (For Experimentation)

```powershell
python tortoise\get_conditioning_latents.py --voice mom_marathi
```

This creates a `.pth` file with voice characteristics that you can modify or blend with other voices.

### 3. Combine Multiple Voices

```powershell
# Blend two voices together
python tortoise\do_tts.py --text "Text" --voice mom_marathi&another_voice --preset fast
```

---

## 💡 Tips for Best Results

### Audio Quality Recommendations

Your source audio should ideally have:
- ✅ **Clear speech** with minimal background noise
- ✅ **Natural speaking pace** (not too fast/slow)
- ✅ **Consistent volume** across clips
- ✅ **Varied content** (different words/phrases)
- ❌ **Avoid**: Music, phone quality, echoes, "um/uh" sounds

### If Quality is Not Good

If the generated voice doesn't sound right:

1. **Check your audio samples**:
   - Remove clips with background noise
   - Remove clips with music
   - Keep only clear speech clips

2. **Try different presets**:
   - Start with `fast` for quick tests
   - Use `standard` for production
   - Try `high_quality` for best results

3. **Adjust candidates**:
   - Increase `--candidates` to 5 or 7
   - Listen to all candidates and pick the best

4. **Use more samples**:
   - The more good quality samples, the better
   - Aim for 2-5 minutes of clear speech

---

## 🔧 Troubleshooting

### Problem: Models not downloading
**Solution**: Check internet connection. Models download to `~/.cache/tortoise/models/`

### Problem: CUDA out of memory
**Solution**: 
```powershell
# Reduce batch size or use CPU
python tortoise\do_tts.py --text "Text" --voice mom_marathi --preset ultra_fast
```

### Problem: Voice doesn't sound right
**Solution**:
1. Check audio quality of source samples
2. Try different presets (standard or high_quality)
3. Increase candidates to get more options
4. Ensure WAV files are 22.05kHz sample rate

### Problem: Slow generation
**Solution**:
```powershell
# Use optimizations
python tortoise\do_tts.py --text "Text" --voice mom_marathi --preset fast --half True --kv_cache True
```

### Convert audio to correct format
If your files are not in the right format:
```powershell
# Using ffmpeg
ffmpeg -i input.mp3 -ar 22050 -ac 1 output.wav
```

---

## 📊 Expected Performance

### Generation Times (approximate)

| Preset | Time for 1 sentence | GPU Required |
|--------|-------------------|--------------|
| ultra_fast | 10-20 seconds | 4GB VRAM |
| fast | 30-60 seconds | 4GB VRAM |
| standard | 1-3 minutes | 6GB VRAM |
| high_quality | 3-6 minutes | 8GB VRAM |

*Note: Times vary based on hardware and text length*

---

## 📁 File Structure

```
tortoise-tts/
├── voice/                      # Your original voice files
│   ├── 1.wav
│   ├── 2.wav
│   └── ... (19 files)
│
├── tortoise/
│   └── voices/
│       └── mom_marathi/        # Voice files copied here
│           ├── 1.wav
│           ├── 2.wav
│           └── ... (19 files)
│
├── marathi_output/             # Generated speech files
│   ├── fast/
│   │   └── output.wav
│   ├── standard/
│   │   └── output.wav
│   └── high_quality/
│       └── output.wav
│
├── marathi_tts.py             # Custom Marathi TTS script
└── setup_mom_voice.ps1        # Setup script
```

---

## 🎯 Complete Workflow Example

```powershell
# 1. Setup (one time)
.\setup_mom_voice.ps1
pip install -r requirements.txt
python setup.py install

# 2. Quick test
python tortoise\do_tts.py --text "हॅलो" --voice mom_marathi --preset fast

# 3. Generate quality output
python tortoise\do_tts.py --text "नमस्कार, आज मी तुम्हाला एक गोष्ट सांगणार आहे" --voice mom_marathi --preset standard --candidates 3

# 4. Check outputs in results/ folder
```

---

## 🌟 Important Notes

1. **First Run**: Will download ~4GB of models - be patient!
2. **GPU Recommended**: Much faster than CPU (10-50x)
3. **Text Length**: Keep individual texts under ~200 words for best results
4. **Marathi Support**: Model works with Marathi text (Unicode support)
5. **Voice Rights**: Use responsibly and ethically

---

## 📚 Additional Resources

- **Original Repo**: https://github.com/neonbjb/tortoise-tts
- **Paper**: https://arxiv.org/abs/2305.07243
- **Voice Customization Guide**: See `voice_customization_guide.md`
- **Advanced Usage**: See `Advanced_Usage.md`

---

## ❤️ Preserving Memories

This is a beautiful way to preserve your mother's voice. The 19 clips you have (3 minutes total) should work well with Tortoise TTS. Remember:

- The quality of output depends heavily on the quality of input samples
- More diverse speech samples = better results
- Experiment with different presets and candidates
- The model will learn the voice characteristics, speaking style, and tone

**Best of luck with preserving these precious memories!** 🙏

---

## 🆘 Need Help?

If you encounter issues:
1. Check the Troubleshooting section above
2. Verify your audio files are in correct format (WAV, 22050Hz)
3. Try different quality presets
4. Check GPU/CUDA installation if using GPU

---

*Generated with care for preserving precious memories* ❤️
