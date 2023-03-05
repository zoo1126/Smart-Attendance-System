"""
The following code is intended to be run only by travis for continuius intengration and testing
purposes.
"""
import torch
import torch.nn.functional as F
import cv2
import os
from ai_model.models.mtcnn import MTCNN
from ai_model.models.inception_resnet_v1 import InceptionResnetV1

# def show_bboxes(img, bounding_boxes, facial_landmarks=[]):
#     """ Draw bounding boxes and facial landmarks. """
#     img_copy = img.copy()
#     draw = ImageDraw.Draw(img_copy)
#     person = []
#     for b in bounding_boxes:
#         b[0] = b[0] - (b[2] - b[0]) / 4
#         b[2] = b[2] + (b[2] - b[0]) / 4
#         b[1] = b[1] - (b[3] - b[1]) / 1.3
#         b[3] = b[3] + (b[3] - b[1]) / 5
#         im2 = img.crop([b[0], b[1], b[2], b[3]])
#         person.append(im2)
#         draw.rectangle([(b[0], b[1]), (b[2], b[3])],
#                        outline='red')
#
#     for p in facial_landmarks:
#         # print(p)
#         for i in range(5):
#             draw.ellipse([(p[i] - 1.0, p[i + 5] - 1.0),
#                           (p[i] + 1.0, p[i + 5] + 1.0)],
#                          outline='green')
#     return img_copy, person
#### MULTI-FACE TEST ####

'''
mtcnn = MTCNN(keep_all=True)
resnet = InceptionResnetV1(pretrained='vggface2').eval()
image = cv2.imread('./identity/1.jpg')
img1  = mtcnn(image, save_path='data/xunlian.png')
image2 = cv2.imread('./data/text.jpg')
img2 = mtcnn(image2, save_path='data/ceshi.png')
ebed1 = resnet(img1)
ebed2 = resnet(img2)
feature1 = F.normalize(ebed1)  #F.normalize只能处理两维的数据，L2归一化
feature2 = F.normalize(ebed2)
distance = feature1.mm(feature2.t())#计算余弦相似度
print(distance)
'''


dir_path = "D:\\face_project\\ai_model\\identity"
temp = 0
mtcnn = MTCNN(keep_all=True)
resnet = InceptionResnetV1(pretrained='vggface2').eval()
image1 = cv2.imread('./data/text.jpg')
img1 = mtcnn(image1, save_path='data/ceshi.png')
ebed1 = resnet(img1)
feature1 = F.normalize(ebed1)  # F.normalize只能处理两维的数据，L2归一化
files = os.listdir(dir_path)
for file in files:
    image = cv2.imread(dir_path + "\\" + file)
    img = mtcnn(image, save_path='data/xunlian.png')
    ebed = resnet(img)
    feature = F.normalize(ebed)
    distance = feature1.mm(feature.t())  # 计算余弦相似度
    if distance >= 0.6:
        temp = 1
if temp:
    print(12)
        # QMessageBox.about(self,"欢迎","打卡成功")
else:
    print(5)
        # QMessageBox.warning(self, "警告", "打卡失败，请前往申诉页面",QMessageBox.Yes)

