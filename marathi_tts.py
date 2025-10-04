"""
Marathi Text-to-Speech using Tortoise TTS
Custom script for cloning your mother's voice in Marathi
"""

import torch
import torchaudio
import os
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_voices

def generate_marathi_speech(text, voice_name="mom_marathi", preset="standard", output_dir="marathi_output"):
    """
    Generate speech in Marathi using the cloned voice
    
    Args:
        text (str): Marathi text to speak
        voice_name (str): Name of the voice folder in tortoise/voices/
        preset (str): Quality preset - 'ultra_fast', 'fast', 'standard', 'high_quality'
        output_dir (str): Directory to save output files
    """
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize TTS with optimizations
    print("Loading Tortoise TTS models...")
    tts = TextToSpeech(
        use_deepspeed=False,  # Set to True if you have DeepSpeed installed
        kv_cache=True,        # Speeds up generation
        half=True             # Use FP16 for faster inference
    )
    
    # Load voice samples
    print(f"Loading voice samples for: {voice_name}")
    voice_samples, conditioning_latents = load_voices([voice_name])
    
    # Generate speech
    print(f"Generating speech with preset: {preset}")
    print(f"Text: {text}")
    
    # Generate multiple candidates and pick the best
    gen = tts.tts_with_preset(
        text, 
        voice_samples=voice_samples, 
        conditioning_latents=conditioning_latents,
        preset=preset,
        k=3  # Generate 3 candidates, return best one
    )
    
    # Save output
    if isinstance(gen, list):
        # Multiple candidates returned
        for idx, audio in enumerate(gen):
            output_path = os.path.join(output_dir, f'output_{idx}.wav')
            torchaudio.save(output_path, audio.squeeze(0).cpu(), 24000)
            print(f"Saved: {output_path}")
    else:
        # Single output
        output_path = os.path.join(output_dir, 'output.wav')
        torchaudio.save(output_path, gen.squeeze(0).cpu(), 24000)
        print(f"Saved: {output_path}")
    
    print("✓ Speech generation complete!")
    return output_path


def batch_generate_marathi(texts, voice_name="mom_marathi", preset="fast"):
    """
    Generate multiple Marathi speech files from a list of texts
    
    Args:
        texts (list): List of Marathi text strings
        voice_name (str): Name of the voice folder
        preset (str): Quality preset
    """
    tts = TextToSpeech(kv_cache=True, half=True)
    voice_samples, conditioning_latents = load_voices([voice_name])
    
    for idx, text in enumerate(texts):
        print(f"\n--- Processing text {idx+1}/{len(texts)} ---")
        output_dir = f"marathi_output/batch_{idx+1}"
        os.makedirs(output_dir, exist_ok=True)
        
        gen = tts.tts_with_preset(
            text,
            voice_samples=voice_samples,
            conditioning_latents=conditioning_latents,
            preset=preset
        )
        
        output_path = os.path.join(output_dir, f'output_{idx+1}.wav')
        torchaudio.save(output_path, gen.squeeze(0).cpu(), 24000)
        print(f"Saved: {output_path}")


if __name__ == "__main__":
    # Example usage
    marathi_text = "नमस्कार, मी तुमची आई आहे. आज मी तुम्हाला एक गोष्ट सांगणार आहे."
    
    # Generate with different quality presets
    print("=" * 60)
    print("MARATHI VOICE CLONING - TORTOISE TTS")
    print("=" * 60)
    
    # Fast generation (good for testing)
    print("\n1. Fast preset (for quick testing)...")
    generate_marathi_speech(marathi_text, preset="fast", output_dir="marathi_output/fast")
    
    # Standard quality (recommended)
    print("\n2. Standard preset (recommended quality)...")
    generate_marathi_speech(marathi_text, preset="standard", output_dir="marathi_output/standard")
    
    # High quality (takes longer)
    # Uncomment below for highest quality
    # print("\n3. High quality preset (best quality, slower)...")
    # generate_marathi_speech(marathi_text, preset="high_quality", output_dir="marathi_output/high_quality")
    
    print("\n" + "=" * 60)
    print("All generations complete! Check the marathi_output folder.")
    print("=" * 60)
