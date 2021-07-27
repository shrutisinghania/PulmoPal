Train the model:

In train_covid19.py line 41 give the path of the 'train' folder
For eg. - imagePaths = list(paths.list_images('C:/Users/ss067504/OneDrive - Cerner Corporation/Desktop/work/ship_it/2020/github_repo/ShipItVII/Analysis/train'))
Run train_covid19.py



Run the model:

In the analysis folder place the image you want to test with
In predict.py line 27 give the name of the image
for eg. - image = cv2.imread('_0_1465610.jpeg')
Run predict.py