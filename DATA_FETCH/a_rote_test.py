import pymysql
import matplotlib.pyplot as plt
import pandas as pd
connect=pymysql.connect(host='localhost',user='root',password='334455',db='pedestrian_fix_20180506')
try:
    with connect.cursor() as curosr:
        # lsit_case=[1,2,3]
        # list_density=[0.5,0.9]
        # list_radius_core=[6,10]
        # list_steps=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        # lsit_case = [3]
        # list_density=[0.9]
        # list_radius_core=[10]
        # list_steps=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        crl_14 = []
        list_radius_ob=[20]
        list_force=[100]
        # list_force=[10,20,30,40,50,60,70,80,90,100]
        list_steps=[0,1,2,3,4]

        for l_r_o in list_radius_ob:
            for l_f in list_force:
                for l_s in list_steps:
                    single_rol=[]
                    sql='select time_s,rato  from pedestrian_fix_20180506.time_and_rote where r_o=%s and force_s=%s and step_s=%s '
                    curosr.execute(sql,[l_r_o,l_f,l_s])
                    result=curosr.fetchall()
                    connect.commit()
                    for re in result:
                        single_rol.append(re[1])
                    crl_14.append(single_rol)
        find_max_len=[]
        for c in crl_14:
            find_max_len.append(len(c))
        max_len=max(find_max_len)
        for c in crl_14:
            sub=max_len-len(c)
            for s in range(sub):
                c.append(1)
        # for c in crl_14:
        #     print(c)

            # print(r)
        main_v=[]
        for c in range(len(crl_14[0])):
            s=[]
            for r in range(len(crl_14)):
                s.append(crl_14[r][c])
            main_v.append(sum(s)/len(crl_14))
        for mv in main_v:
            print(mv)
        # list_case=[1,2,3]
        # list_density=[0.9]
        # list_radius=[6,10]
        # # list_radius_ob = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        # list_force = [50]  # 行人影响力
        # list_v=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,1.0]
        # all_plot_data=[]
        # all_plot_data.append(list_v)
        # for l_c in list_case:
        #     y_case = []
        #     for l_v in list_v:
        #         sql="select time_s from steps_test_3st.speed_and_time WHERE case_s='%s' and density='%s' and r_c='%s' and v_s='%s' and force_s='%s'"
        #         curosr.execute(sql, [l_c, list_density[0], list_radius[1],l_v,list_force[0] ])
        #         result=curosr.fetchall()
        #         evacu_time_list=[]
        #         for res in result:
        #             evacu_time_list.append(res[0])
        #         single_x_value=sum(evacu_time_list)/len(evacu_time_list)
        #         y_case.append(single_x_value)
        #     all_plot_data.append(y_case)
        # cvs_data = list(zip(all_plot_data[0], all_plot_data[1], all_plot_data[2], all_plot_data[3]))
        # df = pd.DataFrame(data=cvs_data, columns=['x_axis', 'case1', 'case2', 'case3'])
        # df.to_csv('test.csv', index=False, header=['x_axis', 'case1', 'case2', 'case3'])
        # plt.plot(all_plot_data[0],all_plot_data[1],label='case1')
        # plt.plot(all_plot_data[0], all_plot_data[2],label='case2')
        # plt.plot(all_plot_data[0], all_plot_data[3],label='case3')
        # plt.legend(loc='best')
        # plt.show()
finally:
    connect.close()