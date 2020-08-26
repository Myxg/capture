import pymysql
import argparse
import numpy as np
import math
import time
from multiprocessing import Process


def monitor(count_num):
    data = {'data': []}
    for count_num in range(int(count_num), int(count_num)+2):
        tt = time.time()
        zjl = []
        pjsd = []
        zgsu = []
        fb = []
        list_all = []
        db = pymysql.connect('localhost', 'root', '000000', 'data')
        cursor = db.cursor()
        sql = 'select frame_num,people_num,x,y from zb' + str(
            count_num) + ' where frame_num<"44000" and frame_num > "20000"'
        cursor.execute(sql)
        result = cursor.fetchone()
        while result != None:
            result = list(result)
            list_all.append(result)
            result = cursor.fetchone()
        db.close()
        list1 = list_all[:]
        # print(list1)
        A1 = []
        A2 = []
        B1 = []
        B2 = []
        for i in list1:
            if i[1] == 'a1':
                A1.append(i)
            elif i[1] == 'a2':
                A2.append(i)
            elif i[1] == 'b1':
                B1.append(i)
            elif i[1] == 'b2':
                B2.append(i)
        coordinate_a1 = []
        for i in A1:
            ll = [i[2], i[3]]
            coordinate_a1.append(ll)
        coordinate_a2 = []
        for i in A2:
            ll = [i[2], i[3]]
            coordinate_a2.append(ll)
        coordinate_b1 = []
        for i in B1:
            ll = [i[2], i[3]]
            coordinate_b1.append(ll)
        coordinate_b2 = []
        for i in B2:
            ll = [i[2], i[3]]
            coordinate_b2.append(ll)
        sum_a1 = []
        sum_a2 = []
        sum_b1 = []
        sum_b2 = []
        i_a1 = 0
        while True:
            if i_a1 == len(A1) - 1:
                break
            p1 = np.array([A1[i_a1][2], A1[i_a1][3]])
            p2 = np.array([A1[i_a1 + 1][2], A1[i_a1 + 1][3]])
            p3 = p2 - p1
            p4 = math.hypot(p3[0], p3[1])
            if p4 < 50:
                sum_a1.append(p4)
            i_a1 += 1
        i_a2 = 0
        while True:
            if i_a2 == len(A2) - 1:
                break
            p1 = np.array([A2[i_a2][2], A2[i_a2][3]])
            p2 = np.array([A2[i_a2 + 1][2], A2[i_a2 + 1][3]])
            p3 = p2 - p1
            p4 = math.hypot(p3[0], p3[1])
            if p4 < 50:
                sum_a2.append(p4)
            i_a2 += 1
        i_b1 = 0
        while True:
            if i_b1 == len(B1) - 1:
                break
            p1 = np.array([B1[i_b1][2], B1[i_b1][3]])
            p2 = np.array([B1[i_b1 + 1][2], B1[i_b1 + 1][3]])
            p3 = p2 - p1
            p4 = math.hypot(p3[0], p3[1])
            if p4 < 50:
                sum_b1.append(p4)
            i_b1 += 1
        i_b2 = 0
        while True:
            if i_b2 == len(B2) - 1:
                break
            p1 = np.array([B2[i_b2][2], B2[i_b2][3]])
            p2 = np.array([B2[i_b2 + 1][2], B2[i_b2 + 1][3]])
            p3 = p2 - p1
            p4 = math.hypot(p3[0], p3[1])
            if p4 < 50:
                sum_b2.append(p4)
            i_b2 += 1

        time_a1 = math.ceil(len(sum_a1) / 24)
        time_a2 = math.ceil(len(sum_a2) / 24)
        time_b1 = math.ceil(len(sum_b1) / 24)
        time_b2 = math.ceil(len(sum_b2) / 24)
        speed_a1 = []
        speed_a2 = []
        speed_b1 = []
        speed_b2 = []
        for i in range(time_a1):
            a = sum(sum_a1[i * 24:(i + 1) * 24]) * 2 / 100
            speed_a1.append(a)
        for i in range(time_a2):
            a = sum(sum_a2[i * 24:(i + 1) * 24]) * 2 / 100
            speed_a2.append(a)
        for i in range(time_b1):
            a = sum(sum_b1[i * 24:(i + 1) * 24]) * 2 / 100
            speed_b1.append(a)
        for i in range(time_b2):
            a = sum(sum_b2[i * 24:(i + 1) * 24]) * 2 / 100
            speed_b2.append(a)
        distance_a1 = round(sum(speed_a1), 2)
        distance_a2 = round(sum(speed_a2), 2)
        distance_b1 = round(sum(speed_b1), 2)
        distance_b2 = round(sum(speed_b2), 2)
        average_a1 = round(distance_a1 / time_a1, 2)
        average_a2 = round(distance_a2 / time_a2, 2)
        average_b1 = round(distance_b1 / time_b1, 2)
        average_b2 = round(distance_b2 / time_b2, 2)
        speed_a1.sort()
        speed_a2.sort()
        speed_b1.sort()
        speed_b2.sort()
        max_speed_a1 = round(speed_a1[-1], 2)
        max_speed_a2 = round(speed_a2[-1], 2)
        max_speed_b1 = round(speed_b1[-1], 2)
        max_speed_b2 = round(speed_b2[-1], 2)
        distribute_a1 = []
        distribute_a2 = []
        distribute_b1 = []
        distribute_b2 = []
        for j in range(5):
            x = [i for i in speed_a1 if j < i < j + 1]
            distribute_a1.append(len(x))
        x = [i for i in speed_a1 if 5 < i]
        distribute_a1.append(len(x))
        for j in range(5):
            x = [i for i in speed_a2 if j < i < j + 1]
            distribute_a2.append(len(x))
        x = [i for i in speed_a2 if 5 < i]
        distribute_a2.append(len(x))
        for j in range(5):
            x = [i for i in speed_b1 if j < i < j + 1]
            distribute_b1.append(len(x))
        x = [i for i in speed_b1 if 5 < i]
        distribute_b1.append(len(x))
        for j in range(5):
            x = [i for i in speed_b2 if j < i < j + 1]
            distribute_b2.append(len(x))
        x = [i for i in speed_b2 if 5 < i]
        distribute_b2.append(len(x))

        zjl = [distance_a1, distance_a2, distance_b1, distance_b2]
        pjsd = [average_a1, average_a2, average_b1, average_b2]
        zgsd = [max_speed_a1, max_speed_a2, max_speed_b1, max_speed_b2]
        fb = [{'name': 'a1', 'data': distribute_a1}, {'name': 'a2', 'data': distribute_a1},
              {'name': 'b1', 'data': distribute_a1}, {'name': 'b2', 'data': distribute_a1}]
        page = [count_num, zjl, pjsd, zgsd, fb]
        data['data'].append(page)
        ss = time.time()
        print(ss - tt)


p1 = Process(target=monitor, args=('1',))
p2 = Process(target=monitor, args=('3',))
p3 = Process(target=monitor, args=('5',))
p4 = Process(target=monitor, args=('7',))


if __name__ == '__main__':
    p1.start()
    p2.start()
    p3.start()
    p4.start()






