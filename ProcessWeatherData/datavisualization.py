import matplotlib.pyplot as plt


def plot_temperatures(temperatures, average, highest, lowest):
    days =(range(1, len(temperatures)))

    plt.plot(temperatures, label='Daily Temperature', marker='o')
    plt.plot(highest, label='Highest', marker='o', color='g')
    plt.plot(lowest, label='Lowest', marker='o', color='r')

    plt.xticks(days,)
    plt.xlabel('Days')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Trend')
    plt.legend()

    plt.show()
    return

