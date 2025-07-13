import argparse
import sys
from pathlib import Path
from typing import TextIO, List, Tuple

import srt

'''
A command-line tool to convert `.srt` subtitle files into plain text (`.txt`/`.md`/`.doc`, etc.) documents. Built with the [srt library](https://pypi.org/project/srt/). 

Author: Kevin Stark  
Date: 2025-07-13
Version: 1.1
License: MIT License  
GitHub: https://github.com/ksDreamer/subtitle-Tool  
Email: gmy.kevinstark@gmail.com
'''



def convert_srt_stream(input_stream: TextIO, output_stream: TextIO) -> None:
    """
    Reads SRT content and converts to output streams.
    """
    try:
        subtitles = srt.parse(input_stream.read())
        processed_text = ' '.join(sub.content.replace('\n', ' ') for sub in subtitles)
        output_stream.write(processed_text)
    except Exception as e:
        raise IOError(f"Failed during stream conversion: {e}") from e

def process_single_file(input_path: Path, output_path: Path) -> bool:
    """
    Processes a single SRT file conversion.
    
    Returns:
        True if conversion was successful, False otherwise.
    """
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(input_path, 'r', encoding='utf-8') as infile, \
             open(output_path, 'w', encoding='utf-8') as outfile:
            convert_srt_stream(infile, outfile)
        
        print("Conversion successful!")
        return True

    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_path}'", file=sys.stderr)
    except (IOError, OSError) as e:
        print(f"Error: Failed to process file. {e}", file=sys.stderr)
    return False

def resolve_conversion_tasks(files: List[str]) -> List[Tuple[Path, Path]]:
    """
    Resolves command-line arguments into a list of (input, output) path tuples.
    """
    num_args = len(files)
    tasks = []

    if num_args == 0:
        # Case 1: No arguments. Default single file task.
        input_path = Path("input.srt")
        tasks.append((input_path, input_path.with_suffix('.txt')))
    
    elif num_args == 1:
        arg_path = Path(files[0])
        if arg_path.is_dir():
            # Case 2: Argument is a directory. Create tasks for all .srt files within.
            print(f"Directory mode activated for: {arg_path}")
            srt_files = sorted(arg_path.glob('*.srt')) # sorted() for consistent order
            if not srt_files:
                print(f"No .srt files found in '{arg_path}'.")
                return []
            for srt_file in srt_files:
                tasks.append((srt_file, srt_file.with_suffix('.txt')))
        else:
            # Case 3: Argument is a single file.
            if arg_path.suffix.lower() == '.srt':
                tasks.append((arg_path, arg_path.with_suffix('.txt')))
            else:
                input_path = Path("input.srt")
                tasks.append((input_path, arg_path))
    
    else: # 2 or more arguments
        # Case 4: Explicit input and output files. Directory processing is disabled.
        if Path(files[0]).is_dir():
            print("Error: Directory input is not supported when an output file is specified.", file=sys.stderr)
            return []
        input_path = Path(files[0])
        output_path = Path(files[1])
        tasks.append((input_path, output_path))
        if num_args > 2:
            print(f"Warning: Extra arguments {files[2:]} are ignored in two-argument mode.", file=sys.stderr)
            
    return tasks

def create_arg_parser() -> argparse.ArgumentParser:
    """Creates and configures the argument parser."""
    parser = argparse.ArgumentParser(
        description="A tool to convert SRT subtitle files or directories to plain text.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        'files',
        nargs='*', # 0 or more arguments
        help=(
            "Accepts a file path, a directory path, or combinations.\n\n"
            "Usage Scenarios:\n"
            "1. Directory: python main.py <folder_path>\n"
            "   - Converts all .srt files inside the folder.\n"
            "2. Single File (Default output): python main.py <file.srt>\n"
            "   - Converts 'file.srt' to 'file.txt'.\n"
            "3. Single File (Custom output): python main.py <file.srt> <out.txt>\n"
            "   - Converts as specified.\n"
            "4. Default: python main.py\n"
            "   - Converts 'input.srt' to 'input.txt'."
        )
    )
    return parser

def main() -> None:

    parser = create_arg_parser()
    args = parser.parse_args()
    
    tasks = resolve_conversion_tasks(args.files)
    
    if not tasks:
        sys.exit(1) # Exit if no tasks were generated (e.g., error or no files found)

    success_count = 0
    total_count = len(tasks)
    
    print("-" * 55)
    for i, (input_path, output_path) in enumerate(tasks, 1):
        if total_count > 1:
            print(f"Processing task {i} of {total_count}...")
        if process_single_file(input_path, output_path):
            success_count += 1
        print("-" * 55)

    if total_count > 1:
        print("All tasks completed!")
        print(f"Summary: {success_count} succeeded, {total_count - success_count} failed.")

if __name__ == "__main__":
    main()