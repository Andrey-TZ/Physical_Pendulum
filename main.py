from Viscous import ViscousFriction
from Dry import DryFriction

if __name__ == '__main__':
    viscous = ViscousFriction(0.1, 0.1, 0.25, 1)
    viscous.plot_angle()
    viscous.plot_phase()

    dry = DryFriction(0.1, 0.02, 0, 1)
    dry.plot_angle()
    dry.plot_phase()

