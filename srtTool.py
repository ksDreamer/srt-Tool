import sys
import srt

'''
A tool using [srt library](https://pypi.org/project/srt/) to convert `.srt` format subtitle file into plain text article.
Author: Kevin Stark  
Date: 2025-07-12  
Version: 1.0  
License: MIT License  
GitHub: https://github.com/ksDreamer/srt-Tool  
Email: gmy.kevinstark@gmail.com
'''

def srt_to_article(input_file_path, output_file_path):
    print(f"Reading File: {input_file_path}")
    
    try:
        with open(input_file_path, 'r', encoding='utf-8') as f:
            srt_content = f.read()

        # Parse the file and return a generator object for subtitles
        subtitles = srt.parse(srt_content)

        # Extract the content attribute, and join with a space.
        article_text = ' '.join(sub.content.replace('\n', ' ') for sub in subtitles)

        # Write the result to the output file
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(article_text)

        print(f"Conversion successful! Content saved to: {output_file_path}")
        print("\n--- Content Preview ---")
        print("\nPreview of the first 200 characters:\n" + article_text[:200] + "...")
        print("\nPreview of the last 200 characters:\n" + "... " + article_text[-200:])


    except FileNotFoundError:
        print(f"Error: File not found '{input_file_path}'")
    except Exception as e:
        print(f"Error occurred while processing the file: {e}")



def main():
    default_input = 'input.srt'
    default_output = 'output.txt'
    
    args = sys.argv[1:]  # Skip the script name
    
    input_file = default_input
    output_file = default_output
    
    if len(args) == 1:
        # Only one argument provided - need to determine if it's input or output
        arg = args[0]
        if arg.lower().endswith('.srt'):
            # If it ends with .srt, treat as input file
            input_file = arg
        else:
            output_file = arg
    elif len(args) >= 2:
        # Two or more arguments - first is input, second is output
        input_file = args[0]
        output_file = args[1]

    print("\n" + "=" * 20 + "srt Tool" + "=" * 20)
    
    if len(args) > 0 and args[0] in ['-h', '--help', 'help']:
        print("Usage:")
        print("  python srtTool.py [input.srt] [output.txt]")
        print()
        print("Examples:")
        print("  python srtTool.py                     # Use default file names: input.srt and output.txt")
        print("  python srtTool.py <inputFileName.srt>          # Custom input")
        print("  python srtTool.py <outputFileName.txt>         # Custom output")
        print("  python srtTool.py <inputFileName.srt> <outputFileName.txt>  # Custom both")

        sys.exit(0)
    
    srt_to_article(input_file, output_file)

if __name__ == "__main__":
    main()