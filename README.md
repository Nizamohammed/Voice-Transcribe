<img width="1056" height="520" alt="Gemini_Generated_Image_ev2kv9ev2kv9ev2k" src="https://github.com/user-attachments/assets/58bfb2c5-76d0-4b1f-9116-355d3e8060f8" />

# 🎙️ voice-transcribe

Turn long audio into text from your terminal — fast setup, simple commands, no UI needed.

This is a student-friendly CLI tool using **OpenAI Whisper** that helps you transcribe:
- lecture recordings
- voice memos
- meetings / interviews
- “I’ll write notes later” moments 😅

> ⚡ Current goal: get a reliable transcription tool out now.  
> 🧠 Future goal: evolve this into a full student notes workflow (better structure, timing, performance, features).

---
## 📟 Try it in your browser (No installation required)
1. Click the **Open in GitHub Codespaces** badge above
2. Wait for the environment to finish setting up
3. In the terminal, run:

```bash
transcribe --help
```

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Nizamohammed/Voice-Transcribe)

---

## ✅ What this tool does (Currently)

- Transcribes common audio formats: `.m4a`, `.mp3`, `.wav`, etc.
- Saves output to a `.txt` file automatically (or to your chosen path)
- Lets you pick a Whisper model (accuracy vs speed)

---

## 🧩 Requirements

### 1) Python
- **Python 3.10+** recommended

Check:
```bash
python3 --version
```
### 2) ffmpeg

#### MacOS (Homebrew)
```bash
brew install ffmpeg
```
#### Ubentu/Debian
```bash
sudo apt update && sudo apt install ffmpeg
```
#### Windows
Install ffmpeg and make sure it’s on PATH. (Windows support docs coming later.)

---

## 🚀 Installation
### Install pipx
```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```
Restart your terminal (or open a new one)

### Install this tool from GitHub
```bash
pipx install git+https://github.com/Nizamohammed/Voice-Transcribe.git
```
✅ After installing, you should have a global command:
```bash
transcribe --help
```

---

## 🎛️ Usage
### Basic
```bash
transcribe lecture.m4a
```
this will create:
lecture_transcription.txt in the current directory

### Choose output file
```bash
transcribe lecture.m4a notes.txt
```

### Choose model (speed vs accuracy)
```bash
transcribe lecture.m4a notes.txt turbo
```

---

## 🧠 Model choices (how to pick)

### Whisper models trade speed for accuracy:
- **tiny** → fastest, lowest accuracy
- **base / small** → decent for quick drafts
- **medium / large** → best accuracy, slower
- **turbo** → usually a great balance (default)

If you're unsure, start with:
```bash
transcribe lecture.m4a notes.txt turbo
```

---

## 🛣️ Future Roadmap 

### This project is actively evolving. Ideas I’m exploring:

- structured lecture notes output
- faster processing + performance improvements
- exporting to Markdown / PDF / Notion formats
- speaker separation and cleanup tools

---

## 🤝 Contributing (students welcome)

### If you’re a student and want to contribute:

1. Fork the repo 
2. Create a new branch
3.	Submit a pull request

Even small improvements (README fixes, bug reports, setup tips) help a lot :)

---

## 📜 License

MIT License — use it, improve it, share it.

---

## ⭐ If this helped you

Star the repo so other students can find it, and feel free to open an issue with feature ideas or bugs!

