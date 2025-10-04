# PowerShell Script to Setup Voice Cloning for Marathi
# This script prepares your mother's voice samples for use with Tortoise TTS

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Voice Cloning Setup - Tortoise TTS   " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Create voice directory
Write-Host "[1/3] Creating voice directory..." -ForegroundColor Yellow
$voiceDir = "tortoise\voices\mom_marathi"
if (!(Test-Path $voiceDir)) {
    New-Item -ItemType Directory -Path $voiceDir -Force | Out-Null
    Write-Host "✓ Created directory: $voiceDir" -ForegroundColor Green
} else {
    Write-Host "✓ Directory already exists: $voiceDir" -ForegroundColor Green
}

# Step 2: Copy voice samples
Write-Host ""
Write-Host "[2/3] Copying voice samples..." -ForegroundColor Yellow
$sourceDir = "voice"
if (Test-Path $sourceDir) {
    $wavFiles = Get-ChildItem -Path $sourceDir -Filter "*.wav"
    $count = $wavFiles.Count
    
    if ($count -gt 0) {
        Copy-Item "$sourceDir\*.wav" -Destination $voiceDir -Force
        Write-Host "✓ Copied $count WAV files to $voiceDir" -ForegroundColor Green
    } else {
        Write-Host "⚠ No WAV files found in $sourceDir" -ForegroundColor Red
        Write-Host "  Please ensure your voice samples are in the 'voice' folder" -ForegroundColor Red
    }
} else {
    Write-Host "⚠ Source directory '$sourceDir' not found" -ForegroundColor Red
}

# Step 3: Verify setup
Write-Host ""
Write-Host "[3/3] Verifying setup..." -ForegroundColor Yellow
$copiedFiles = Get-ChildItem -Path $voiceDir -Filter "*.wav"
$copiedCount = $copiedFiles.Count

if ($copiedCount -gt 0) {
    Write-Host "✓ Setup complete! Found $copiedCount voice samples" -ForegroundColor Green
    Write-Host ""
    Write-Host "Voice samples:" -ForegroundColor Cyan
    $copiedFiles | ForEach-Object { Write-Host "  - $($_.Name)" -ForegroundColor Gray }
} else {
    Write-Host "✗ No voice samples found in destination" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Next Steps:" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Test the voice cloning with:" -ForegroundColor White
Write-Host "   python tortoise\do_tts.py --text `"Test text`" --voice mom_marathi --preset fast" -ForegroundColor Yellow
Write-Host ""
Write-Host "2. For Marathi text-to-speech, use:" -ForegroundColor White
Write-Host "   python marathi_tts.py" -ForegroundColor Yellow
Write-Host ""
Write-Host "3. Or generate custom text:" -ForegroundColor White
Write-Host "   python tortoise\do_tts.py --text `"Your Marathi text`" --voice mom_marathi --preset standard" -ForegroundColor Yellow
Write-Host ""
Write-Host "Quality Presets:" -ForegroundColor White
Write-Host "  - ultra_fast: Very fast, lower quality" -ForegroundColor Gray
Write-Host "  - fast:       Good balance (recommended for testing)" -ForegroundColor Gray
Write-Host "  - standard:   Better quality (recommended)" -ForegroundColor Gray
Write-Host "  - high_quality: Best quality, slower" -ForegroundColor Gray
Write-Host ""
