# srt-Tool
A command-line tool to convert `.srt` subtitle files into plain text (`.txt`/`.md`/`.doc`, etc.) documents. Built with the [srt library](https://pypi.org/project/srt/). 

Author: Kevin Stark  
Date: 2025-07-12  
Version: 1.0  
License: MIT License  
GitHub: https://github.com/ksDreamer/srtTool  
Email: gmy.kevinstark@gmail.com

## Prerequisites
1. Prepare python package 
```pip install srt```  
2. Prepare a subtitle file in `.srt` format.  
For example, `input.srt` or `example.srt`

## Usage
You can run the script in two ways.

1. Default Mode

If you have a subtitle file named `input.srt`, just run the code and it will generate an `output.txt` file.

```Bash
python srtTool.py
```
2. Custom File Names

To specify your input and output files, provide them as command-line arguments.

```Bash
python srtTool.py <input_file.srt> <output_file.txt>
```
Example:
Following command will convert `my_subtitle.srt` into a text file named `transcript.txt`.

```Bash
python srtTool.py my_subtitle.srt transcript.txt
```