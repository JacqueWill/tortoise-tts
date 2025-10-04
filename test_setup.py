"""
Quick Test Script for Voice Cloning Setup
This script verifies that everything is set up correctly
"""

import os
import sys

def check_voice_files():
    """Check if voice files are in the correct location"""
    voice_dir = "tortoise/voices/mom_marathi"
    
    print("=" * 60)
    print("CHECKING VOICE FILES")
    print("=" * 60)
    
    if not os.path.exists(voice_dir):
        print(f"❌ Voice directory not found: {voice_dir}")
        print("   Please run: .\\setup_mom_voice.ps1")
        return False
    
    wav_files = [f for f in os.listdir(voice_dir) if f.endswith('.wav')]
    
    if len(wav_files) == 0:
        print(f"❌ No WAV files found in {voice_dir}")
        print("   Please run: .\\setup_mom_voice.ps1")
        return False
    
    print(f"✅ Found {len(wav_files)} voice samples in {voice_dir}")
    print("\nVoice files:")
    for f in sorted(wav_files):
        filepath = os.path.join(voice_dir, f)
        size_mb = os.path.getsize(filepath) / (1024 * 1024)
        print(f"   - {f} ({size_mb:.2f} MB)")
    
    return True

def check_dependencies():
    """Check if required Python packages are installed"""
    print("\n" + "=" * 60)
    print("CHECKING DEPENDENCIES")
    print("=" * 60)
    
    required = [
        'torch',
        'torchaudio',
        'transformers',
        'tortoise'
    ]
    
    missing = []
    
    for package in required:
        try:
            __import__(package)
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} is NOT installed")
            missing.append(package)
    
    if missing:
        print("\n⚠️  Missing packages:", ", ".join(missing))
        print("   Please run: pip install -r requirements.txt")
        print("   Then run: python setup.py install")
        return False
    
    return True

def check_gpu():
    """Check if GPU is available"""
    print("\n" + "=" * 60)
    print("CHECKING GPU")
    print("=" * 60)
    
    try:
        import torch
        
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
            gpu_memory = torch.cuda.get_device_properties(0).total_memory / (1024**3)
            print(f"✅ GPU Available: {gpu_name}")
            print(f"   Memory: {gpu_memory:.2f} GB")
            
            if gpu_memory < 4:
                print("   ⚠️  Warning: Less than 4GB VRAM. Use 'ultra_fast' or 'fast' preset")
            else:
                print("   ✅ Sufficient GPU memory for all presets")
            
            return True
        else:
            print("⚠️  No GPU detected. Will use CPU (much slower)")
            print("   This is OK but generation will take longer")
            return False
            
    except:
        print("⚠️  Could not check GPU status")
        return False

def run_quick_test():
    """Run a quick test to ensure everything works"""
    print("\n" + "=" * 60)
    print("RUNNING QUICK TEST")
    print("=" * 60)
    
    try:
        from tortoise.api import TextToSpeech
        from tortoise.utils.audio import load_voices
        
        print("✅ Tortoise TTS imports successful")
        
        # Check if voice can be loaded
        try:
            print("Attempting to load mom_marathi voice...")
            voice_samples, conditioning_latents = load_voices(['mom_marathi'])
            
            if voice_samples is not None:
                print(f"✅ Successfully loaded {len(voice_samples)} voice samples")
                return True
            else:
                print("❌ Could not load voice samples")
                return False
                
        except Exception as e:
            print(f"❌ Error loading voice: {str(e)}")
            return False
            
    except ImportError as e:
        print(f"❌ Import error: {str(e)}")
        print("   Please install dependencies: pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return False

def main():
    print("\n" + "=" * 60)
    print("  TORTOISE TTS - VOICE CLONING SETUP VERIFICATION")
    print("=" * 60)
    print()
    
    results = []
    
    # Run all checks
    results.append(("Voice Files", check_voice_files()))
    results.append(("Dependencies", check_dependencies()))
    results.append(("GPU", check_gpu()))
    results.append(("Quick Test", run_quick_test()))
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    all_passed = True
    for check_name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{check_name:15} : {status}")
        if not passed and check_name in ["Voice Files", "Dependencies", "Quick Test"]:
            all_passed = False
    
    print("\n" + "=" * 60)
    
    if all_passed:
        print("🎉 ALL CHECKS PASSED! You're ready to generate speech!")
        print("\nNext steps:")
        print("1. Run: python marathi_tts.py")
        print("   OR")
        print("2. Run: python tortoise\\do_tts.py --text \"Your Marathi text\" --voice mom_marathi --preset fast")
    else:
        print("⚠️  SOME CHECKS FAILED. Please fix the issues above.")
        print("\nQuick fixes:")
        print("1. Voice files missing: Run .\\setup_mom_voice.ps1")
        print("2. Dependencies missing: Run pip install -r requirements.txt")
        print("3. Install Tortoise: Run python setup.py install")
    
    print("=" * 60)
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
