import math
import time
import pymysql
import os
import json
import cv2
import numpy as np
from multiprocessing import Process


# def func(count):
# ma = 0
# t_s = time.time()
while True:
    # if ma == 100:
    #     break
    # for count_num in range(1,9):
    # print(count_num)
    count_num = 1
    def gci(filepath):
        list = []
        files = os.listdir(filepath)
        for fi in files:
            fi_d = os.path.join(filepath, fi)
            if os.path.isdir(fi_d):
                gci(fi_d)
            else:
                a = os.path.join(filepath, fi_d)
                list.append(a)
        return list
    ROOTPATH = 'D:\openpose\out_' + str(count_num)
    lista = gci(ROOTPATH)
    text = []
    fi = []
    for i in lista[:100]:
        i.replace('\\', '\\\\')
        j = i.split('\\')[3].split('_')
        l1 = [j[0]]
        path = i
        f = open(path, encoding='utf-8')
        res = f.read()
        t = json.loads(res)
        people = t['people']
        for p in people:
            ll = p['pose_keypoints_2d']
            ll = [ll[30], ll[31], ll[39], ll[40]]
            l2 = l1 + ll
            fi.append(l2)
        f.close()

    fc = ['570', '310', '1350', '305', '390', '995', '1520', '1000']
    i = 0
    court = [0, 0, 0, 0, 0, 0, 0, 0]
    while i < 8:
        line = fc[i]
        if not line:
            exit(-1)
        court[i] = int(line.strip())
        i = i + 1
    pts1 = np.float32([[court[0], court[1]], [court[2], court[3]], [court[4], court[5]], [court[6], court[7]]])
    pts2 = np.float32([[0, 0], [305, 0], [0, 670], [305, 670]])
    M = cv2.getPerspectiveTransform(pts1, pts2)

    def fangshe_x(u, v):
        x = (M[0, 0] * u + M[0, 1] * v + M[0, 2]) / (M[2, 0] * u + M[2, 1] * v + M[2, 2])
        return int(x)

    def fangshe_y(u, v):
        y = (M[1, 0] * u + M[1, 1] * v + M[1, 2]) / (M[2, 0] * u + M[2, 1] * v + M[2, 2])
        return int(y)


    list1 = []

    for line in fi:
        l1 = []
        v = line
        if fangshe_x(float(v[1]), float(v[2])) < -10 or fangshe_x(float(v[1]), float(v[2])) > 315 \
                or fangshe_x(float(v[3]), float(v[4])) < -10 or fangshe_x(float(v[3]), float(v[4])) > 315 \
                or fangshe_y(float(v[1]), float(v[2])) < -50 or fangshe_y(float(v[1]), float(v[2])) > 720 \
                or fangshe_y(float(v[3]), float(v[4])) < -50 or fangshe_y(float(v[3]), float(v[4])) > 720:
            pass
        else:
            tmpstr = v[0] + ","
            tmpstr = tmpstr + str(fangshe_x(float(v[1]), float(v[2]))) + ','
            tmpstr = tmpstr + str(fangshe_y(float(v[1]), float(v[2]))) + ','
            tmpstr = tmpstr + str(fangshe_x(float(v[3]), float(v[4]))) + ','
            tmpstr = tmpstr + str(fangshe_y(float(v[3]), float(v[4])))
            n = tmpstr.split(',')
            l1 = [n[0], int(n[1]), int(n[2]), int(n[3]), int(n[4])]

            list1.append(l1)

    list2 = []
    for i in list1:
        # print(i)
        l1 = []
        a = i[0] + ","
        b = int((i[1] + i[3]) / 2)
        c = int((i[2] + i[4]) / 2) + 10
        if b < 0:
            b = 0
        if c < 0:
            c = 0
        l1 = [i[0], b, c]
        list2.append(l1)

    db = pymysql.connect('localhost', 'root', '000000', 'data')
    cursor = db.cursor()

    l_frame = []
    for i in list2:
        l_frame.append(int(i[0]))
    l_frame = list(set(l_frame))
    ll_frame = []
    for i in l_frame:
        ll_frame.append(str(i).zfill(7))
    for frame in ll_frame:
        l1 = []
        for i in list2:
            if i[0] == frame:
                l1.append(i)
        la = []
        lb = []
        for j in l1:
            # print(j)
            if j[2] < 335:
                la.append(j)
            else:
                lb.append(j)
        if len(la) == 1:
            a1 = la[0]
            a = a1[0] + ',' + "'a1'" + ',' + str(a1[1]) + ',' + str(a1[2])
            s1 = "insert into zb" + str(count_num) + " " + "values" + "(" + a + ")"
            try:
                cursor.execute(s1)
                db.commit()
            except:
                db.rollback()
        if len(lb) == 1:
            b1 = lb[0]
            b = b1[0] + ',' + "'b1'" + ',' + str(b1[1]) + ',' + str(b1[2])
            s1 = "insert into zb" + str(count_num) + " " + "values" + "(" + b + ")"
            try:
                cursor.execute(s1)
                db.commit()
            except:
                db.rollback()
        if len(la) == 2:
            a1 = la[0]
            a2 = la[1]
            if a1[1] < a2[1]:
                a_l = a1[0] + ',' + "'a1'" + ',' + str(a1[1]) + ',' + str(a1[2])
                a_r = a2[0] + ',' + "'a2'" + ',' + str(a2[1]) + ',' + str(a2[2])
                s1 = "insert into zb" + str(count_num) + " " + "values" + "(" + a_l + ")"
                s2 = "insert into zb" + str(count_num) + " " + "values" + "(" + a_r + ")"
            else:
                a_l = a1[0] + ',' + "'a2'" + ',' + str(a1[1]) + ',' + str(a1[2])
                a_r = a2[0] + ',' + "'a1'" + ',' + str(a2[1]) + ',' + str(a2[2])
                s1 = "insert into zb" + str(count_num) + " " + "values" + "(" + a_l + ")"
                s2 = "insert into zb" + str(count_num) + " " + "values" + "(" + a_r + ")"
            try:
                cursor.execute(s1)
                cursor.execute(s2)
                db.commit()
            except:
                db.rollback()
        if len(lb) == 2:
            b1 = lb[0]
            b2 = lb[1]
            if b1[2] < b2[2]:
                b_l = b1[0] + ',' + "'b1'" + ',' + str(b1[1]) + ',' + str(b1[2])
                b_r = b2[0] + ',' + "'b2'" + ',' + str(b2[1]) + ',' + str(b2[2])
                s1 = "insert into zb" + str(count_num) + " " + "values" + "(" + b_l + ")"
                s2 = "insert into zb" + str(count_num) + " " + "values" + "(" + b_r + ")"
            else:
                b_l = b1[0] + ',' + "'b2'" + ',' + str(b1[1]) + ',' + str(b1[2])
                b_r = b2[0] + ',' + "'b1'" + ',' + str(b2[1]) + ',' + str(b2[2])
                s1 = "insert into zb" + str(count_num) + " " + "values" + "(" + b_l + ")"
                s2 = "insert into zb" + str(count_num) + " " + "values" + "(" + b_r + ")"
            try:
                cursor.execute(s1)
                cursor.execute(s2)
                db.commit()
            except:
                db.rollback()
    db.close()
    for i in lista[:100]:
        os.remove(i)
    # ma += 1

# t_e = time.time()
# print(t_s,t_e)
# a = t_e - t_s
# aaa = math.ceil(a)
# print(aaa)


# if __name__ == '__main__':
#     p1 = Process(target=func, args=(1,))
#     p2 = Process(target=func, args=(3,))
#     p3 = Process(target=func, args=(5,))
#     p4 = Process(target=func, args=(7,))
#     s = time.time()
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#     p1.join()
#     p2.join()
#     p3.join()
#     p4.join()
#     print('~~~~~~~~~~~~~~~~')
#     e = time.time()
#     print(e-s)


