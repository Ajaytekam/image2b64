## image2b64  

Convert all images into base64 encoded string on markdown '.md' files. It basically grabs the image tag, generate base64 string of image and then replace image path with base64 string, so its easy to use/move/blog markdown files without being hassaled by moving all image files. It works on png, jpg, jpeg and gif files.  

**Usage :**  

```shell   
./image2b64.py -f <Input_Markdown_File> 
```  

With output file name 

```shell   
./image2b64.py -f <Input_Markdown_File> -o <Output_Markdown_File>  
```  

Examples :  

```shell  
./image2b64.py -f README.md  

[+] Encodeed Images :
bsp1_1.png
bsp1_2.png
bsp1_3.png

[+] Data written into : EncodedREADME.md
```  

```shell  
./image2b64.py -f README.md -o MyFile.md 

[+] Encodeed Images : 
bsp1_1.png 
bsp1_2.png 
bsp1_3.png 

[+] Data written into : MyFile.md
```  

