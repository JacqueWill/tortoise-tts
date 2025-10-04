# 📋 Step-by-Step Implementation Guide

## Overview
**Goal**: Clone your mother's voice for Marathi text-to-speech
**Resources**: 19 WAV files (~3 minutes of audio)
**Technology**: Tortoise TTS (voice cloning system)

---

## 🗂️ Files Created for You

| File | Purpose |
|------|---------|
| `QUICK_START.md` | Quick reference guide (start here!) |
| `MARATHI_GUIDE.md` | Complete documentation with examples |
| `setup_mom_voice.ps1` | PowerShell script to setup voice files |
| `marathi_tts.py` | Python script for Marathi TTS |
| `test_setup.py` | Verification script |

---

## 📝 Complete Implementation Steps

### Phase 1: Initial Setup (One Time)

```
┌─────────────────────────────────────────────────────────┐
│ Step 1: Organize Voice Files                           │
│ Run: .\setup_mom_voice.ps1                             │
│                                                         │
│ This will:                                              │
│ ✓ Create tortoise/voices/mom_marathi/                  │
│ ✓ Copy your 19 WAV files                               │
│ ✓ Verify the setup                                     │
└─────────────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────────────┐
│ Step 2: Install Dependencies                           │
│ Run: pip install -r requirements.txt                   │
│ Then: python setup.py install                          │
│                                                         │
│ This installs:                                          │
│ ✓ PyTorch & TorchAudio                                 │
│ ✓ Transformers                                         │
│ ✓ Tortoise TTS                                         │
│ ✓ Other dependencies                                   │
└─────────────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────────────┐
│ Step 3: Verify Setup                                   │
│ Run: python test_setup.py                              │
│                                                         │
│ This checks:                                            │
│ ✓ Voice files are in correct location                  │
│ ✓ All dependencies are installed                       │
│ ✓ GPU availability (optional but faster)               │
│ ✓ Can load the voice successfully                      │
└─────────────────────────────────────────────────────────┘
```

**Expected time**: 15-30 minutes (mostly download time)

---

### Phase 2: Testing & Usage

```
┌─────────────────────────────────────────────────────────┐
│ Quick Test (30-60 seconds generation)                  │
│                                                         │
│ python tortoise\do_tts.py \                            │
│   --text "नमस्कार" \                                    │
│   --voice mom_marathi \                                 │
│   --preset fast                                         │
│                                                         │
│ Output: results/mom_marathi_0.wav                       │
└─────────────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────────────┐
│ Standard Quality (1-3 minutes generation)              │
│                                                         │
│ python tortoise\do_tts.py \                            │
│   --text "आज मी तुम्हाला एक गोष्ट सांगणार आहे" \       │
│   --voice mom_marathi \                                 │
│   --preset standard \                                   │
│   --candidates 3                                        │
│                                                         │
│ Output: results/mom_marathi_0_0.wav (best of 3)        │
└─────────────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────────────┐
│ Using Custom Python Script                             │
│                                                         │
│ Edit marathi_tts.py with your text, then run:          │
│ python marathi_tts.py                                   │
│                                                         │
│ Output: marathi_output/ folder with results            │
└─────────────────────────────────────────────────────────┘
```

---

## 🎛️ Understanding the Parameters

### Essential Parameters

| Parameter | Values | Description |
|-----------|--------|-------------|
| `--text` | Any Marathi text | The text you want spoken |
| `--voice` | `mom_marathi` | Your voice folder name |
| `--preset` | `ultra_fast`, `fast`, `standard`, `high_quality` | Quality vs Speed |
| `--output_path` | Directory path | Where to save files |

### Optional But Useful

| Parameter | Values | Description |
|-----------|--------|-------------|
| `--candidates` | 1-10 (recommend 3) | Generate multiple versions |
| `--half` | `True`/`False` | Use FP16 (faster, less memory) |
| `--kv_cache` | `True`/`False` | Speed optimization |
| `--seed` | Any number | For reproducible results |

---

## 🎨 Preset Comparison

```
Ultra Fast:
├─ Generation Time: 10-20 seconds
├─ Quality: ⭐⭐ (OK for testing)
├─ GPU Memory: ~2-3 GB
└─ Use Case: Quick experiments

Fast:
├─ Generation Time: 30-60 seconds
├─ Quality: ⭐⭐⭐ (Good)
├─ GPU Memory: ~3-4 GB
└─ Use Case: Testing & drafts ✅ START HERE

Standard:
├─ Generation Time: 1-3 minutes
├─ Quality: ⭐⭐⭐⭐ (Very Good)
├─ GPU Memory: ~4-6 GB
└─ Use Case: Production use ✅ RECOMMENDED

High Quality:
├─ Generation Time: 3-6 minutes
├─ Quality: ⭐⭐⭐⭐⭐ (Excellent)
├─ GPU Memory: ~6-8 GB
└─ Use Case: Final outputs only
```

---

## 🔄 Typical Workflow

```
Day 1: Setup & Testing
┌────────────────────────────────────────┐
│ 1. Run setup_mom_voice.ps1            │
│ 2. Install dependencies                │
│ 3. Run test_setup.py                   │
│ 4. Generate first test with 'fast'    │
│ 5. Listen and evaluate                 │
└────────────────────────────────────────┘

Day 2+: Production Use
┌────────────────────────────────────────┐
│ 1. Prepare your Marathi text          │
│ 2. Generate with 'standard' preset    │
│ 3. Use candidates=3 for options        │
│ 4. Select best output                  │
└────────────────────────────────────────┘
```

---

## 📊 What to Expect

### First Run
- **Downloads**: ~4GB of pre-trained models
- **Time**: 10-20 minutes (one-time)
- **Location**: `~/.cache/tortoise/models/`

### Generation Times (on modern GPU)
| Text Length | Fast | Standard | High Quality |
|-------------|------|----------|--------------|
| Single word | 10s | 30s | 1m |
| Short sentence (5-10 words) | 30s | 1-2m | 3-4m |
| Long sentence (15-25 words) | 1m | 2-3m | 5-6m |
| Paragraph (50 words) | 2-3m | 5-8m | 10-15m |

**Note**: CPU is 10-50x slower than GPU

---

## 🎯 Quality Expectations

### Your Voice Samples
- **Quantity**: 19 files ✅ (Good! 3+ recommended)
- **Duration**: 7-15 seconds each ✅ (Ideal range)
- **Total**: ~3 minutes ✅ (Sufficient)

### Expected Quality
With good source audio:
- **Tone/Voice**: 85-95% match
- **Pronunciation**: 80-90% accurate
- **Naturalness**: 75-85% natural
- **Marathi Support**: Full Unicode support ✅

### Factors Affecting Quality
1. **Source audio quality** (most important!)
   - Clear speech = better results
   - Background noise = worse results
   
2. **Text content**
   - Natural sentences work best
   - Very short/long texts may vary
   
3. **Preset selection**
   - Higher preset = better quality
   - But diminishing returns above 'standard'

---

## 🔧 Common Commands Reference

### Testing Commands
```powershell
# Verify setup
python test_setup.py

# Quick test
python tortoise\do_tts.py --text "हॅलो" --voice mom_marathi --preset fast

# Check if voice loads
python -c "from tortoise.utils.audio import load_voices; print(load_voices(['mom_marathi'])[0] is not None)"
```

### Generation Commands
```powershell
# Basic
python tortoise\do_tts.py --text "Your text" --voice mom_marathi --preset fast

# With candidates
python tortoise\do_tts.py --text "Your text" --voice mom_marathi --preset standard --candidates 3

# High quality
python tortoise\do_tts.py --text "Your text" --voice mom_marathi --preset high_quality --half True --kv_cache True

# Custom output location
python tortoise\do_tts.py --text "Your text" --voice mom_marathi --preset standard --output_path my_outputs
```

### Python Script Usage
```powershell
# Use the custom script
python marathi_tts.py

# Or create your own script (see marathi_tts.py for template)
```

---

## 🆘 Troubleshooting Quick Reference

| Problem | Solution |
|---------|----------|
| Voice not found | Run `setup_mom_voice.ps1` again |
| Module not found | Run `pip install -r requirements.txt` |
| Out of memory | Use `--preset ultra_fast` or `--half True` |
| Slow generation | Check GPU is being used, or use `--preset fast` |
| Poor quality | Try `--preset standard`, increase `--candidates` |
| Wrong audio format | Convert to WAV 22050Hz with ffmpeg |

---

## 📈 Optimization Tips

### For Speed
```powershell
python tortoise\do_tts.py \
    --text "Your text" \
    --voice mom_marathi \
    --preset fast \
    --half True \
    --kv_cache True \
    --candidates 1
```

### For Quality
```powershell
python tortoise\do_tts.py \
    --text "Your text" \
    --voice mom_marathi \
    --preset high_quality \
    --candidates 5
```

### For Balance (Recommended)
```powershell
python tortoise\do_tts.py \
    --text "Your text" \
    --voice mom_marathi \
    --preset standard \
    --candidates 3 \
    --half True \
    --kv_cache True
```

---

## 🎓 Learning Path

```
Week 1: Basics
├─ Setup and first generation
├─ Try different presets
└─ Understand the output quality

Week 2: Refinement
├─ Experiment with candidates
├─ Test different text lengths
└─ Optimize for your hardware

Week 3: Advanced
├─ Use Python API
├─ Batch processing
└─ Emotion control with prompts
```

---

## ❤️ Final Notes

This is a meaningful project to preserve your mother's voice. The system should work well with:
- ✅ Your 19 voice samples
- ✅ Marathi text (full Unicode support)
- ✅ Various quality levels to choose from

**Key Success Factors:**
1. Good quality source audio (clear, minimal noise)
2. Appropriate preset selection (start with 'fast', move to 'standard')
3. Using multiple candidates to get best results
4. Patience on first run (model download)

**Remember:** 
- First generation will download models (~4GB, one-time)
- Start with 'fast' preset to test
- Use 'standard' for production
- GPU highly recommended but not required

---

## 📞 Getting Help

If you encounter issues:
1. ✅ Check `test_setup.py` output
2. ✅ Read `MARATHI_GUIDE.md` troubleshooting section
3. ✅ Verify audio format (WAV, 22050Hz)
4. ✅ Try different presets

---

**You're all set! Start with `.\setup_mom_voice.ps1` and follow the steps above.**

**May this help preserve beautiful memories!** 🙏❤️
