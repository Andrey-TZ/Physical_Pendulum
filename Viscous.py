import numpy as np
import matplotlib.pyplot as plt


class ViscousFriction:
    def __init__(self, h, k_resistance, angle, speed):
        self.h = h
        self.gamma = np.sqrt(
            5 / (9.81 * 1 * 4))  # sqrt(I/(g*l*m)) коэффициент для перевода времени из безразмерного вида к секундам
        self.k = k_resistance
        self.angle = [angle]  # угол в радианах
        self.speed = [speed]  # угловая скорость в безразмерном виде
        self.time = [i * self.h * self.gamma for i in range(1, round(100 / h) + 2)]  # время в секундах
        self.count()

    def count(self):
        j = 0
        while j < 100:
            i = round(j * (1 / self.h))
            c0 = self.h * self.speed[i]
            k0 = self.h * (-self.k * self.speed[i] - np.sin(self.angle[i]))
            c1 = self.h * (self.speed[i] + 0.5 * k0)
            k1 = self.h * (-self.k * (self.speed[i] + 0.5 * k0) - np.sin(self.angle[i] + 0.5 * c0))
            c2 = self.h * (self.speed[i] + 0.5 * k1)
            k2 = self.h * (-self.k * (self.speed[i] + 0.5 * k1) - np.sin(self.angle[i] + 0.5 * c1))
            c3 = self.h * (self.speed[i] + k2)
            k3 = self.h * (-self.k * (self.speed[i] + c2) - np.sin(self.angle[i] + c2))

            self.angle.append(self.angle[i] + (1 / 6) * (c0 + 2 * c1 + 2 * c2 + c3))
            self.speed.append(self.speed[i] + (1 / 6) * (k0 + 2 * k1 + 2 * k2 + k3))
            j = round(j + self.h, 1)

    def plot_angle(self):
        plt.plot(self.time, self.angle)
        angle_ticks = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1]
        plt.yticks(angle_ticks)
        plt.xlabel('t, c')
        plt.ylabel('$\phi$, рад')
        plt.show()

    def plot_phase(self):
        speed = [i / self.gamma for i in self.speed]
        plt.plot(self.angle, speed)
        plt.xlabel('$\phi$, рад')
        plt.ylabel('$\omega$, рад/с')
        plt.show()
