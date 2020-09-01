import cv2
from PIL import Image
import numpy as np
import pymysql


for count_num in range(1, 9):
    list_all = []
    db = pymysql.connect('localhost', 'root', '000000', 'data')
    cursor = db.cursor()
    # sql = 'select frame_num,people_num,x,y from zb1 where frame_num>"10755" and frame_num<"10995"'
    sql = 'select frame_num,people_num,x,y from zb' + str(
        count_num) + ' where frame_num<' + str(count_num) + "1500" + ' and frame_num > ' + str(count_num) + "0000"
    cursor.execute(sql)
    result = cursor.fetchone()
    while result != None:
        result = list(result)
        list_all.append(result)
        result = cursor.fetchone()
    db.close()
    list1 = list_all[:]

    list_dataa1 = []
    list_dataa2 = []
    list_datab1 = []
    list_datab2 = []
    for i in list1:
        if i[1] == 'a1':
            j = (int(i[2]),int(i[3]))
            list_dataa1.append(j)
        if i[1] == 'a2':
            j = (int(i[2]), int(i[3]))
            list_dataa2.append(j)
        if i[1] == 'b1':
            j = (int(i[2]), int(i[3]))
            list_datab1.append(j)
        if i[1] == 'b2':
            j = (int(i[2]), int(i[3]))
            list_datab2.append(j)
    # for i in list_data:
    #     print(i)
    list_len = [len(list_dataa1), len(list_dataa2), len(list_datab1), len(list_datab2)]
    list_len.sort()
    length = list_len[0]-1
    canvas = np.zeros((670,305,3), dtype='uint8')
    image = Image.open('D:\\monitor\\playground.jpg')
    image_data = np.asarray(image)
    green = (0,255,0)
    balck = (65,105,225)
    blue = (144,238,144)
    red = (255,0,0)
    n = 0
    while n < length:
        img = cv2.line(image_data,list_dataa1[n],list_dataa1[n+1],red)
        img = cv2.line(image_data,list_dataa2[n],list_dataa2[n+1],blue)
        img = cv2.line(image_data,list_datab1[n],list_datab1[n+1],green)
        img = cv2.line(image_data,list_datab2[n],list_datab2[n+1],balck)

        print(img)
        n += 1
    # for i in list_data:
    #     cv2.circle(canvas,i,1,green,1)
    cv2.imshow("luxian",img)
    cv2.waitKey(0)
    filepath = "D:\\monitor\\playground_" + str(count_num) + ".jpg"

    cv2.imwrite(filepath, img)