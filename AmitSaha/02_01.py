from pylab import plot, show, legend, xlabel, ylabel


hrs = ['04:00', '07:00', '10:00', '13:00', '16:00', '19:00', '22:00', '01:00']
temps_01 = [17, 16, 19, 24, 26, 25, 22, 19]
temps_02 = [16, 16, 21, 23, 26, 27, 23, 18]

plot(hrs, temps_01)
plot(hrs, temps_02)
xlabel('Godzina')
ylabel('Temperatura [°C]')
legend(['Mielec', 'Szczecin'])
show()
