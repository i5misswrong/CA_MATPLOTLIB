import pymysql
import matplotlib.pyplot as plt
import pandas as pd
connect=pymysql.connect(host='localhost',user='root',password='334455',db='steps_test_3st')
try:
    with connect.cursor() as curosr:
        list_case=[1,2,3]
        list_density=[0.9]
        list_radius=[6,10]
        # list_radius_ob = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        list_force = [50]  # 行人影响力
        list_v=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,1.0]
        all_plot_data=[]
        all_plot_data.append(list_v)
        for l_c in list_case:
            y_case = []
            for l_v in list_v:
                sql="select time_s from steps_test_3st.speed_and_time WHERE case_s='%s' and density='%s' and r_c='%s' and v_s='%s' and force_s='%s'"
                curosr.execute(sql, [l_c, list_density[0], list_radius[1],l_v,list_force[0] ])
                result=curosr.fetchall()
                evacu_time_list=[]
                for res in result:
                    evacu_time_list.append(res[0])
                single_x_value=sum(evacu_time_list)/len(evacu_time_list)
                y_case.append(single_x_value)
            all_plot_data.append(y_case)
        cvs_data = list(zip(all_plot_data[0], all_plot_data[1], all_plot_data[2], all_plot_data[3]))
        df = pd.DataFrame(data=cvs_data, columns=['x_axis', 'case1', 'case2', 'case3'])
        df.to_csv('test.csv', index=False, header=['x_axis', 'case1', 'case2', 'case3'])
        plt.plot(all_plot_data[0],all_plot_data[1],label='case1')
        plt.plot(all_plot_data[0], all_plot_data[2],label='case2')
        plt.plot(all_plot_data[0], all_plot_data[3],label='case3')
        plt.legend(loc='best')
        plt.show()
finally:
    connect.close()