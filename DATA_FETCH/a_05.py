import pymysql
import matplotlib.pyplot as plt
import pandas as pd
connect=pymysql.connect(host='localhost',user='root',password='334455',db='steps_test_3st')
try:
    with connect.cursor() as curosr:
        list_case=[0]
        list_density=[0.9]
        list_radius=[6,10]
        list_radius_ob = [10, 12, 14,  16,  18, 20]
        list_force = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # 行人影响力
        all_plot_data=[]
        all_plot_data.append(list_force)
        for l_o in list_radius_ob:
            y_case = []
            for l_f in list_force:
                sql="select time_s from steps_test_3st.danger_double_for_meet WHERE case_s='%s' and density='%s' and r_c='%s' and r_o='%s' and force_s='%s'"
                curosr.execute(sql, [list_case[0], list_density[0], list_radius[1],l_o,l_f ])
                result=curosr.fetchall()
                evacu_time_list=[]
                for res in result:
                    evacu_time_list.append(res[0])
                single_x_value=sum(evacu_time_list)/len(evacu_time_list)
                y_case.append(single_x_value)
            all_plot_data.append(y_case)
        cvs_data = list(zip(all_plot_data[0], all_plot_data[1], all_plot_data[2], all_plot_data[3], all_plot_data[4], all_plot_data[5], all_plot_data[6]))
        df = pd.DataFrame(data=cvs_data, columns=['x_axis', 'ro_10', 'ro_12', 'ro_14','ro_16','ro_18','ro_20'])
        df.to_csv('test.csv', index=False, header=['x_axis', 'ro_10', 'ro_12', 'ro_14','ro_16','ro_18','ro_20'])
        plt.plot(all_plot_data[0],all_plot_data[1],label='ro_10')
        plt.plot(all_plot_data[0], all_plot_data[2],label='ro_12')
        plt.plot(all_plot_data[0], all_plot_data[3],label='ro_14')
        plt.plot(all_plot_data[0], all_plot_data[4], label='ro_16')
        plt.plot(all_plot_data[0], all_plot_data[5], label='ro_18')
        plt.plot(all_plot_data[0], all_plot_data[6], label='ro_20')
        plt.legend(loc='best')
        plt.show()
finally:
    connect.close()