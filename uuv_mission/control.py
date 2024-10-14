# submarine controller
class controller:

    def get_controlaction(cls, reference, positions, t):
        # kp = proportional gains
        kp = 0.15
        # kd = derivative gains
        kd = 0.6

        # get cave_depth current and prev
        cave_depth_curr = positions[t,1]
        cave_depth_prev = positions[t-1,1]

        # e = error = r - y
        e = reference(t) - cave_depth_curr
        e_prev = reference(t-1) - cave_depth_prev

        # pd feedback controller
        # ut: u(t) = control action
        ut = kp * e + kd* (e - e_prev)
        return ut