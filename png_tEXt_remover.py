import os
import re

print("PNG tEXt embeded data remover by yellowZedman")
print("================================")

input_dir = os.path.join(".", "pngDataIni")
output_dir = os.path.join(".", "pngDataRemoved")

match_start = 0
match_end = 0

CHUNK_BYTE_OFFSET = 4

for filename in os.listdir(input_dir):
    input_file = os.path.join(input_dir, filename)
    newfile = os.path.join(output_dir, filename[:-4] + "_strip.png")

    with open(input_file, 'rb') as f:
        content = f.read()
        # print(content[0:2048])
        re_pattern_ini = re.compile(b"\x74\x45\x58\x74")
        re_pattern_end = re.compile(b"\x00\x01\x00\x00")

        match = re_pattern_ini.search(content)
        print(match.span())
        match_start = match.start() - CHUNK_BYTE_OFFSET
        match = re_pattern_end.search(content)
        match_end = match.start()# - CHUNK_BYTE_OFFSET

    print("Chunk start: " + str(match_start))
    print("Chunk end: " + str(match_end))

    print("Chunk start text : " + str(content[match_start:match_start + 8]))
    print("Chunk end text : " + str(content[match_end - 8:match_end]))

    with open(newfile, 'xb') as f:
        f.write(content[:match_start] + content[match_end:])
        print("New file created at " + newfile)

    os.remove(input_file)

input("Program ended. Press Enter to continue...")
