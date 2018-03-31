import pymysql


def force_data():

    average_list = []
    '''设置循环参数'''
    list_case = [0, 1, 2]  # 危险源位置
    list_density = [0.8, 0.9]  # 行人密度
    list_radius_core = [9, 18, 27]  # 危险源半径
    list_radius_ob = [30, 40, 50, 60, 70, 80, 90, 100]  # 危险源边缘半径
    list_radius_v_increase = [0]  # 危险源边缘增长速度
    list_force = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # 行人影响力
    list_force_tyoe = [1, 2]  # 行人影响力类型
    list_people_view = [10]  # 行人视野半径
    list_steps = [0, 1, 2, 3, 4]
    '''参数设置结束'''
    connect = pymysql.connect(host='localhost', user='root', password='334455', db='pedestrian')  # 获取链接
    try:
        with connect.cursor() as cursor:
            for l_c in list_case:
                for s in list_radius_ob:
                    time_list = []
                    average = 0
                    sql = "select time_logo from pedestrian.danger_double where radius_v=0 and density=0.9 and peo_view=10 and case_s='%s' and  radius=27 and radius_ob='%s' and  force_s=100 and force_type=1 "
                    cursor.execute(sql, [l_c,s])
                    result = cursor.fetchall()
                    for i in result:
                        time_list.append(i[0])

                    average = sum(time_list) / 5
                    average_list.append(average)
                    print(s,"---",average)
                print('-----')
                # print(average_list)

            connect.commit()
    finally:
        connect.close()


if __name__ == '__main__':
    force_data()