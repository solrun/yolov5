import fiftyone as fo
import fiftyone.zoo as foz
import os
# These will be multiplied with number of classes.
N_DATAPOINTS_TRAIN = 10
N_DATAPOINTS_TEST = 10
N_DATAPOINTS_VAL = 10
# these paths need to be changed

path_to_yolov5 = os.getcwd()
print('path', path_to_yolov5)
export_path = path_to_yolov5+"/dataset/"
labels_path = path_to_yolov5+"/dataset/labels"

dataset_type = fo.types.dataset_types.YOLOv5Dataset

label_field = "ground_truth" 

class_list = ['person', 'cat', 'dog', 'backpack', 'umbrella', 'handbag', 'suitcase', 'bottle', 'wine glass',
             'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'chair', 'couch', 
             'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 
             'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 
             'scissors', 'hair drier', 'toothbrush']

n_classes = len(class_list)

dataset_coco_train = foz.load_zoo_dataset(
    "coco-2017",
    label_types=["detections"],
    classes=class_list,
    max_samples=N_DATAPOINTS_TRAIN*n_classes,
    seed=51,
    split='train',
    shuffle=True,
)

dataset_coco_val = foz.load_zoo_dataset(
    "coco-2017",
    label_types=["detections"],
    classes=class_list,
    max_samples=(N_DATAPOINTS_TEST+N_DATAPOINTS_VAL)*n_classes,
    seed=51,
    split='validation',
    shuffle=True,
)

# Set default classes
dataset_coco_train.default_classes = class_list
dataset_coco_val.default_classes = class_list

# Edit the default classes
dataset_coco_train.default_classes.append("Teapot")
dataset_coco_train.save()  # must save after edits

dataset_coco_val.default_classes.append("Teapot")
dataset_coco_val.save()  # must save after edits


dataset_oi_train = foz.load_zoo_dataset(
    "open-images-v6",
    label_types=["detections"],
    classes=["Teapot"],
    split='train',
    max_samples=N_DATAPOINTS_TRAIN,
    seed=51,
    shuffle=True,
)


dataset_oi_val = foz.load_zoo_dataset(
    "open-images-v6",
    label_types=["detections"],
    classes=["Teapot"],
    split='validation',
    max_samples=(N_DATAPOINTS_TEST+N_DATAPOINTS_VAL),
    seed=51,
    shuffle=True,
)


dataset_oi_train.default_classes = ["Teapot"]
dataset_oi_train.default_classes.extend(class_list)
dataset_oi_train.rename_sample_fields({"detections": label_field})
dataset_oi_train.save()  # must save after edits

dataset_oi_val.default_classes = ["Teapot"]
dataset_oi_val.default_classes.extend(class_list)
dataset_oi_val.rename_sample_fields({"detections": label_field})
dataset_oi_val.save()  # must save after edits

dataset_coco_train.merge_samples(dataset_oi_train)
dataset_coco_val.merge_samples(dataset_oi_val)

dataset_coco_test = dataset_coco_val.take(N_DATAPOINTS_TEST*n_classes)
dataset_coco_val.delete_samples(dataset_coco_test)


# Export dataset
dataset_coco_train.export(
    dataset_type=dataset_type,
    export_dir=export_path,
    label_field=label_field,
    classes=dataset_coco_train.default_classes,
    split='train',
    path='./dataset'
)


dataset_coco_val.export(
    dataset_type=dataset_type,
    export_dir=export_path,
    label_field=label_field,
    classes=dataset_coco_val.default_classes,
    split='val',
    path='./dataset'
)

dataset_coco_test.export(
    dataset_type=dataset_type,
    export_dir=export_path,
    label_field=label_field,
    classes=dataset_coco_test.default_classes,
    split='test',
)

print('export done')

# Visualize the dataset in the FiftyOne App
#session = fo.launch_app(dataset_cocooi)
#session.wait()
