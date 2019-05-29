import numpy as np
import matplotlib.pyplot as plt

def main():
    deadNode1 = np.loadtxt("/Users/yhc/Code/WirlessSensor/result/TSP+_only_dead(2_cars,5000nodes).txt")
    deadNode2 = np.loadtxt("/Users/yhc/Code/WirlessSensor/result/TSP_plus+_only_dead(2_cars,5000nodes).txt")
    deadNode3 = np.loadtxt("/Users/yhc/Code/WirlessSensor/result/value(0.5*0.5)+_only_dead(2_cars,5000nodes).txt")
    energy1 = \
        np.loadtxt("/Users/yhc/Code/WirlessSensor/result/TSP+_only_energy(2_cars,5000nodes).txt")
    energy2 = \
        np.loadtxt("/Users/yhc/Code/WirlessSensor/result/TSP_plus+_only_energy(2_cars,5000nodes).txt")
    energy3 = \
        np.loadtxt("/Users/yhc/Code/WirlessSensor/result/value(0.5*0.5)+_only_energy(2_cars,5000nodes).txt")

    x1 = np.arange(0, deadNode1.size, 10000)
    plt.plot(x1, deadNode1[::10000], marker="^", label="TSP", linewidth=1, color="r")

    x2 = np.arange(0, deadNode2.size, 10000)
    plt.plot(x2, deadNode2[::10000], marker="*", label="TSP_plus", linewidth=1, color="b")

    x3 = np.arange(0, deadNode3.size, 10000)
    plt.plot(x3, deadNode3[::10000], marker="x", label="value(0.5*0.5)", linewidth=1, color="g")

    plt.grid(color="k", linestyle=":")
    plt.xlabel("Time")
    plt.ylabel("Dead Node")
    plt.legend()
    plt.show()

    # x1 = np.arange(0, energy1.size, 36000)
    # plt.plot(x1, energy1[::36000], marker="^", label="TSP", linewidth=1, color="r")
    #
    # x2 = np.arange(0, energy2.size, 36000)
    # plt.plot(x2, energy2[::36000], marker="*", label="TSP_plus", linewidth=1, color="b")
    #
    # x3 = np.arange(0, energy3.size, 36000)
    # plt.plot(x3, energy3[::36000], marker="x", label="value(0.5*0.5)", linewidth=1, color="g")
    #
    # plt.ylim(0.1, 1.0)
    # plt.grid(color="k", linestyle=":")
    #
    # plt.xlabel("Time")
    # plt.ylabel("Energy Utilization")
    # plt.legend()
    # plt.show()


    # x_list = ['TADP(0.5*0.5)', 'TSP']
    # y_chargeQueue = [2000, 450]
    # plt.title('charge queue length')
    # plt.bar(range(len(y_chargeQueue)), y_chargeQueue, 0.35, color='rgb', tick_label=x_list)
    # plt.show()

    # x_list = ['4000nodes', '5000nodes', '6000nodes']
    # y_TSP_deadNode = [10, 100, 280]
    # y_value_deadNode = [3600, 4600, 5600]
    # x = list(range(len(y_TSP_deadNode)))
    # total_width, n = 0.8, 2
    # width = total_width / n
    # plt.title('dead nodes')
    # plt.bar(x, y_TSP_deadNode, width=width, label='TSP', fc='g')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # plt.bar(x, y_value_deadNode, width=width, label='TADP(0.5*0.5)', tick_label=x_list, fc='r')
    # plt.legend()
    # plt.show()

    # x_list1 = [100, 150, 200, 250, 300]
    # y_list1 = [900, 1000, 1500, 1900, 2200]
    # x_list2 = [100, 150, 200, 250, 300]
    # y_list2 = [1100, 1600, 2000, 2300, 2400]
    #
    # plt.xlabel("num")
    # plt.ylabel("charge energy (KJ)")
    # plt.plot(x_list1, y_list1, marker="^", linewidth=1, color="r", label="Omnidirectional")
    # plt.plot(x_list2, y_list2, marker="*", linewidth=1, color="b", label="Orientation")
    # plt.legend()
    # plt.show()


if __name__ == '__main__':
    main()