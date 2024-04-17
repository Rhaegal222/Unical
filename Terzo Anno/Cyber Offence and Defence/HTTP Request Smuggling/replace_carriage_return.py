import sys
import re

def replace_newline(input_file):
    try:
        with open(input_file, 'r') as infile:
            har_content = infile.read()

        har_content_fixed = har_content.replace('\\n', '\\r\\n')

        with open(input_file, 'w') as outfile:
            outfile.write(har_content_fixed)

        print(f"Sostituzione completata. Il file {input_file} è stato sovrascritto.")

    except FileNotFoundError:
        print(f"Errore: Il file {input_file} non è stato trovato.")
    except Exception as e:
        print(f"Errore durante l'esecuzione dello script: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilizzo: python script.py input_file.har")
    else:
        input_file = sys.argv[1]
        replace_newline(input_file)
