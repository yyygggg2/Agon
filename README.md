### 📌 中文描述
本仓库收录了对伊戈尔·斯特拉文斯基(Igor Stravinsky)晚期芭蕾作品《Agon》中多个片段的定量分析资料。内容包括用于提取音高类别(Pitch Class)数据的 Python 脚本、处理后的原始数据(CSV 文件)以及相应的统计图表，旨在辅助对该作品和作曲技法的结构性理解与分析。

---

### 📌 English Description
This repository contains quantitative analysis resources for selected sections of Igor Stravinsky’s late ballet *Agon*. It includes Python scripts for pitch class extraction, processed data in CSV format, and accompanying statistical visualizations. The project aims to facilitate structural and theoretical analysis of Stravinsky’s compositional techniques.

---

## 📖 README
### Agon Quantitative Analysis Project

This project provides a framework for analyzing pitch-class usage in Stravinsky’s *Agon*, focusing on selected reductions of key sections. It consists of:
* 🎼 MusicXML input files (e.g., `1_pas_de_quatre_reduction.musicxml`)
* 🐍 Python scripts for processing and summarizing pitch class usage
* 📊 CSV datasets and ready-to-use statistical summaries

---

### 📂 Project Structure
├── 1_pas_de_quatre_reduction.musicxml     # MusicXML file (others also follow same naming)\
├── 8_parse_pitch_class.py                 # Extract pitch class data from MusicXML to CSV\
├── 9_parse_pitch_class_summary.py         # Summarize pitch class data (per measure, cumulative)\
├── *_pitch_classes.csv                    # Output: Raw pitch class counts by measure\
├── *_summary.csv                          # Output: Used pitch classes and cumulative stats

---

### 🧠 Key Features
* Accurate pitch class tracking: Handles tied notes and chords across measures
* Measure-by-measure analysis: Captures dynamic evolution of pitch-class material
* Cumulative tracking: Shows how the harmonic vocabulary builds over time
* Modular design: Easy to adapt to other works or sections

---

### ▶️ Usage

#### 1. Pitch Class Extraction
Run `8_parse_pitch_class.py` to process MusicXML files:
This generates multiple `*_pitch_classes.csv` files, one for each section.

#### 2. Summary Generation
Run `9_parse_pitch_class_summary.py` to compute cumulative stats:
This produces summary CSVs, each including:

* Used pitch classes per measure
* Cumulative used pitch classes
* Measure-wise and cumulative counts

---

### 📌 Dependencies

* `music21` (for parsing MusicXML)
* `csv` (standard Python module)

---

### 📝 License

This project is released under the MIT License.
