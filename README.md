# subtitle-Tool
A command-line tool to convert `.srt` subtitle files into plain text (`.txt`/`.md`/`.doc`, etc.) documents. Built with the [srt library](https://pypi.org/project/srt/). 

Author: Kevin Stark  
Date: 2025-07-13   
Version: 1.1  
License: MIT License  
GitHub: https://github.com/ksDreamer/subtitle-Tool  
Email: gmy.kevinstark@gmail.com

## Development Notes
- V1.1 2025-07-13: 
1. Add folder support and batch processing.
2. Add stream processing to prevent crashing in case extremely large file.
3. Use argparse as command-line argument resolver to improve robustness.
4. The default output file name is now derived from the input file name.

## Prerequisites
1. Prepare python package library by `pip install srt`
2. Prepare a subtitle file in `.srt` format. (eg., `input.srt`)

## Usage
You can run the script in several ways.

1. Default Mode

If you have a subtitle file named `input.srt`, which is the default subtitle file name, just run the code and it will generate a plain subtitle file named `input.txt`.

```Bash
python main.py
# or
python main.py input.srt
```
2. Custom File Names

To specify input and output files, provide them as command-line arguments.

```Bash
python main.py <inputFileName.srt> <outputFileName.txt>
```
For example, `python main.py subtitle.srt transcript.txt` will convert `subtitle.srt` into a plain subtitle file named `transcript.txt`.

3. Folder and batch processing

If a folder having several `.srt` subtitle files.
```Bash
python main.py <folderName>
```
For example, `python main.py srtFolder` will convert all `.srt` files inside `srtFolder` into text file.

## TODO
- [x] Add batch processing and folder support.
- [x] Set default output name based on input name.
- [ ] Support other subtitle format, eg., `.ass`.
- [ ] Consider GUI layout and function using Tkinter or PyQt.
- [ ] Consider deploying online service using Flask or Nodejs.
