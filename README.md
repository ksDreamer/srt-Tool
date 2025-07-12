# subtitle-Tool
A command-line tool to convert `.srt` subtitle files into plain text (`.txt`/`.md`/`.doc`, etc.) documents. Built with the [srt library](https://pypi.org/project/srt/). 

Author: Kevin Stark  
Date: 2025-07-12  
Version: 1.0  
License: MIT License  
GitHub: https://github.com/ksDreamer/subtitle-Tool  
Email: gmy.kevinstark@gmail.com

## Prerequisites
1. Prepare python package library by `pip install srt`
2. Prepare a subtitle file in `.srt` format. (eg., `input.srt`)

## Usage
You can run the script in two ways.

1. Default Mode

If you have a subtitle file named `input.srt`, just run the code and it will generate an `output.txt` file.

```Bash
python main.py
```
2. Custom File Names

To specify your input and output files, provide them as command-line arguments.

```Bash
python main.py <input_file.srt> <output_file.txt>
```
Example: `python main.py my_subtitle.srt transcript.txt` will convert `my_subtitle.srt` into a text file named `transcript.txt`.