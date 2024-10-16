# submarine controller
class controller:

    # created such that it is easy to change gains from the jupyter notebook
    def __init__(self, kp, kd):
        # kp = proportional gains
        # kd = derivative gains
        self.kp = kp
        self.kd = kd

    def get_controlaction(self, reference, positions, t):
        # get cave_depth current and prev
        cave_depth_curr = positions[t,1]
        cave_depth_prev = positions[t-1,1]

        # e = error = r - y
        e = reference[t] - cave_depth_curr
        e_prev = reference[t-1] - cave_depth_prev

        # pd feedback controller
        # ut: u(t) = control action
        ut = self.kp * e + self.kd* (e - e_prev)
        return ut