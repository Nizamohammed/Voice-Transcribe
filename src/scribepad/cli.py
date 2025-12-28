#!/usr/bin/env python3
"""
Large File Voice Transcription Script
Handles files of any size with high accuracy using OpenAI Whisper
Fixed for Mac externally-managed environments
"""

import sys
import os
import argparse

def transcribe_file(audio_path, output_path= None, model_size="turbo"):
    """
    Transcribe an audio file using Whisper

    Args:
        audio_path: Path to audio file
        output_path: Path for output text file (optional)
        model_size: Model size (tiny, base, small, medium, large, turbo) {default: turbo}
    """
    try:
        import whisper
    except ImportError:
        print("\n❌ Whisper not found in current Python environment")
        print("\nPlease Install it via this package install (pipx) or:")
        print("  pip3 install --user openai-whisper")
        print("\nThen run this script again.")
        sys.exit(1)

    print(f"Loading Whisper model: {model_size}")
    print("(First run will download the model, ~1.5GB)\n")
    model = whisper.load_model(model_size)

    print(f"Transcribing: {audio_path}")
    print("This may take several minutes for large files...\n")

    # Transcribe with progress
    result = model.transcribe(audio_path, verbose=True)

    # Get transcription text
    transcription = result["text"]

    # Determine output path
    if output_path is None:
        base_name = os.path.splitext(audio_path)[0]
        output_path = f"{base_name}_transcription.txt"

    # Save transcription
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(transcription)

    print(f"\n✅ Transcription complete!")
    print(f"✅ Saved to: {output_path}")
    print(f"✅ Word count: {len(transcription.split())}")

    return transcription


def main():
    parser = argparse.ArgumentParser(prog="transcribe", description="Transcribe audio using OpenAI Whisper")
    parser.add_argument("audio_file", help="Path to audio file (m4a, mp3, wav, etc.)")
    parser.add_argument("output_path", nargs ="?", default=None, help="Optional output-text file path")
    parser.add_argument("model_size", nargs="?", default="turbo", help="Model size: tiny, base, small, medium, large, turbo (default: turbo)")
    args = parser.parse_args()

    if not os.path.exists(args.audio_file):
        print(f"Error: File '{args.audio_file}' not found")
        sys.exit(1)
    transcribe_file(args.audio_file, args.output_path, args.model_size)


if __name__ == "__main__":
    main()
