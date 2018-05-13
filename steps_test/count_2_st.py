import pymysql
import matplotlib.pyplot as plt
import pandas as pd
connect = pymysql.connect(host='localhost', user='root', password='334455', db='steps_test_3st')
try:
    with connect.cursor() as curosr:
        list_case = [1, 2, 0]
        list_density = [0.9]
        list_radius = [6, 8, 10]
        list_radius_ob = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        list_force = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # 行人影响力
        for l_r in list_radius:
            all_plot_data = []
            all_plot_data.append(list_radius_ob)
            for l_c in list_case:
                y_case = []
                for l_r_o in list_radius_ob:
                    sql = "select time_s from steps_test_3st.danger_double_for_meet WHERE case_s='%s' and density='%s' and r_c='%s' and r_o='%s' and force_s='10'"
                    curosr.execute(sql, [l_c, list_density[0], l_r, l_r_o])
                    result = curosr.fetchall()
                    evacu_time_list = []
                    for res in result:
                        evacu_time_list.append(res[0])
                    single_x_value = sum(evacu_time_list) / len(evacu_time_list)
                    y_case.append(single_x_value)
                all_plot_data.append(y_case)
            plt.plot(all_plot_data[0], all_plot_data[1], label='case1')
            plt.plot(all_plot_data[0], all_plot_data[2], label='case2')
            plt.plot(all_plot_data[0], all_plot_data[3], label='case3')
            plt.legend(loc='best')
            plt.show()
finally:
    connect.close()