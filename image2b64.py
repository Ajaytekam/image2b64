#!/usr/bin/python3  

import base64
import argparse
import re  
import os, sys

def encodeImage(imageFile):
    with open(imageFile, "rb") as img_file:
        b64String = base64.b64encode(img_file.read()).decode('utf-8') 
    return b64String

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="markdown file name to process", required=True)
    parser.add_argument("-o", help="Output Filename")
    args = parser.parse_args()
    # output filename
    if args.o:
        OPFile = args.o
    else:
        OPFile = 'EncodedREADME.md'
    # open the file 
    tempfile = open(OPFile, 'w')
    encoded_images = []
    for line in open(args.file):
        if re.match(r"!\[\]\(*.*\)", line):
            # get the file name
            filename = re.search(r"[_a-zA-Z0-9]*\.[a-zA-Z]{3}", line).group(0)
            # check if file exists or not
            if not os.path.isfile(filename):
                print("[-] File {} does not exists".format(filename))
                # writing the original line to the file 
                tempfile.write(line)
                continue
            FileExtension = filename.split('.')[1].lower()
            # filtering the extensions
            # allowd extensions are png, jpg and gif
            extens = ['png', 'jpg', 'jpeg', 'gif']
            Matched = False
            for ext in extens:
                if FileExtension == ext:
                    Matched = True
                    encodedText = encodeImage(filename)
                    line2write = "![](data:image/{};base64,{})".format(ext, encodedText)
                    tempfile.write(line2write+'\n')
                    encoded_images.append(filename)
                    break
            if not Matched:
                print("[-] Extension is not allowd: {}".format(FileExtension))
                print("[-] Filename {} is not written into Output file.".format(filename))
        else:
            # write the data into a new file 
            tempfile.write(line)
    # close the file 
    tempfile.close()
    # print all the encoded images 
    if encoded_images:
        print("[+] Encodeed Images : ")
        for i in encoded_images:
            print("{} ".format(i))
    print("\n[+] Data written into : {}\n".format(OPFile)) 

if __name__ == "__main__":
    main()

