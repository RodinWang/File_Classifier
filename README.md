# File_Classifier

> This is a file classifier write in python.

## Usage       

- This Classifier can sperate file with different prefix and file extension.

  ![image-filelist.jpg](/img/image-filelist.jpg)

## How to use

- This Classifier needs to use the required file name format for classification.

  ```
  Required File name Format:
  
  	<Prefix>_<KeyWord>_*.<file extension>
  	
  	Prefix : This is a prefix string to determine the range of file.
  	Keyword : This is the keyword for classification, and will be used for folder name. ex: Date(20200131 or 20210429) or Word(Dog or Cat).
  	* : This can be any string you like.
  	file extension : This is the file type going to classify.
  ```

- Usage:

  ```
  python file_classification.py -d <directory> -p <file prefix> -e <file extend> -m <copy or move>
  
  arguments:
  	-h, --help			show the help message and exit.
  	-d, --dir			the directory for classification. Default is current work directory.
  	-p, --prefix		the file prefix going to classify. Default is ''.
  	-e, --extend		the file extension going to classify. Default is 'jpg'.
  	-m, --mode 			the operation mode while processing file, copy or move. default is copy mode.
  ```

  

