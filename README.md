## <div>How to run the code: </div>

<details>
<summary>Install</summary>

Clone repo and install [requirements.txt](https://github.com/ultralytics/yolov5/blob/master/requirements.txt) in a
[**Python>=3.7.0**](https://www.python.org/) environment, including
[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/).

```bash
git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
```

</details>

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

## <div>Data used: </div>





Code forked from [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5) under the GNU General Public License v3.0.
See [https://ultralytics.com/yolov5](https://ultralytics.com/yolov5) for more information about the YOLOv5 🚀 family of object detection architectures and models.
