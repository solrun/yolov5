
To generate the new dataset run the file 
```
create_dataset.py
``` 
but before that in the create_dataset.py change the number of desired data points. 
You need to be in the yolov5 directory when calling the script.

What will be created is a folder called "dataset" that will contain a file called
"dataset.yaml". This file needs to be slightly modified. We will need to add 
one line 
```
path: ./dataset
``` 
which can be added anywhere in the file. 

At this point we are ready to train the model. Choose the wanted number of batches and epochs. 
```
python3 train.py --data 'dataset/dataset.yaml' --img 640 --batch 16 --epochs 5 --weights 'yolov5s.pt' --freeze 10
``` 






