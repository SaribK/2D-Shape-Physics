## @file test_driver.py
#  @author Sarib Kashif (kashis2)
#  @brief Contains test cases for CircleT,
#  BodyT, Scene and Plot.
#  @date Feb 12 2021
#  @details Uses pytest to display number of
#  cases that passed and failed. Plot.py file
#  is tested manually.

import pytest
from CircleT import CircleT
from TriangleT import TriangleT
from BodyT import BodyT
from Scene import Scene
from Plot import plot
import math

g = 9.81  # accel due to gravity (m/s^2)
epsilon = 0.0000001


def Fx(t):
    return 0


def Fy(t):
    return -g * 4


def Fx2(t):
    return 0


def Fy2(t):
    return -g * 1


class TestCircleT:

    # edge/boundary case for c2
    def setup_method(self, method):
        self.c1 = CircleT(5, 5, 1, 2)
        self.c2 = CircleT(-1, -1, 1, 1)

    def teardown_method(self, method):
        self.c1 = None
        self.c2 = None

    def test_cm_x(self):
        assert self.c1.cm_x() == 5

    def test_cm_x2(self):
        assert self.c2.cm_x() == -1

    def test_cm_y(self):
        assert self.c1.cm_y() == 5

    def test_cm_y2(self):
        assert self.c2.cm_y() == -1

    def test_mass(self):
        assert self.c1.mass() == 2

    def test_mass2(self):
        assert self.c2.mass() == 1

    def test_m_inert(self):
        assert self.c1.m_inert() == 1

    def test_m_inert2(self):
        assert self.c2.m_inert() == 0.5

    # testing exception cases
    # tested negative values for both m and r
    def test_value_error1(self):
        with pytest.raises(ValueError):
            self.c2 = CircleT(5, 5, -1, 2)

    def test_value_error2(self):
        with pytest.raises(ValueError):
            self.c2 = CircleT(5, 5, 1, -2)

    # tested 0 value for m and r
    def test_value_error3(self):
        with pytest.raises(ValueError):
            self.c2 = CircleT(5, 5, 0, 0)


class TestTriangleT:

    # t2 is big numbers and really small numbers (-500)
    def setup_method(self, method):
        self.t1 = TriangleT(5, 5, 1, 2)
        self.t2 = TriangleT(-500, 100, 2, 2)

    def teardown_method(self, method):
        self.t1 = None
        self.t2 = None

    def test_cm_x(self):
        assert self.t1.cm_x() == 5

    def test_cm_x2(self):
        assert self.t2.cm_x() == -500

    def test_cm_y(self):
        assert self.t1.cm_y() == 5

    def test_cm_y2(self):
        assert self.t2.cm_y() == 100

    def test_mass(self):
        assert self.t1.mass() == 2

    def test_mass2(self):
        assert self.t2.mass() == 2

    def test_m_inert(self):
        assert math.isclose(self.t1.m_inert(), 0.16666666666)

    def test_m_inert2(self):
        assert math.isclose(self.t2.m_inert(), 2 / 3)

    # testing exception cases
    def test_value_error1(self):
        with pytest.raises(ValueError):
            self.t2 = TriangleT(5, 5, -1, 2)

    def test_value_error2(self):
        with pytest.raises(ValueError):
            self.t2 = TriangleT(5, 5, 1, -2)

    def test_value_error3(self):
        with pytest.raises(ValueError):
            self.t2 = TriangleT(5, 5, 0, 0)


class TestBodyT:

    def setup_method(self, method):
        x = [2, 0, -1]
        y = [1, -2, 3]
        m = [3, 3, 3]
        self.b1 = BodyT(x, y, m)

    def teardown_method(self, method):
        self.b1 = None

    def test_cm_x(self):
        assert math.isclose(self.b1.cm_x(), 1 / 3)

    def test_cm_y(self):
        assert math.isclose(self.b1.cm_y(), 2 / 3)

    def test_mass(self):
        assert self.b1.mass() == 9

    def test_m_inert(self):
        assert self.b1.m_inert() == 52

    # testing exception cases
    # tested different types of exception cases
    # (e.g mass is 0 and unequal list lengths)
    def test_value_error1(self):
        with pytest.raises(ValueError):
            self.b2 = BodyT([1, 1, 1], [1, 1, 1], [1, 1, 1, 1])

    def test_value_error2(self):
        with pytest.raises(ValueError):
            self.b2 = BodyT([1, 1, 1], [1, 1, 1], [1, 1, 0])


class TestScene:

    def setup_method(self, method):
        self.c1 = CircleT(5, 5, 1, 2)
        self.s1 = Scene(self.c1, Fx, Fy, 0, 0)

    def teardown_method(self, method):
        self.c1 = None
        self.s1 = None

    def test_get_shape(self):
        assert self.s1.get_shape() == self.c1

    def test_get_unbal_forces(self):
        assert self.s1.get_unbal_forces() == (Fx, Fy)

    def test_get_init_velo(self):
        assert self.s1.get_init_velo() == (0, 0)

    def test_set_shape(self):
        c2 = CircleT(-1, 2, 3, 6)
        self.s1.set_shape(c2)
        assert self.s1.get_shape() == c2

    def test_set_unbal_forces(self):
        self.s1.set_unbal_forces(Fx2, Fy2)
        assert self.s1.get_unbal_forces() == (Fx2, Fy2)

    def test_set_init_velo(self):
        self.s1.set_init_velo(5, 5)
        assert self.s1.get_init_velo() == (5, 5)

    def test_sim(self):
        t, wsol = self.s1.sim(5, 5)
        expected_t = [0, 5 / 4, 5 / 2, 15 / 4, 5]
        expected_wsol = [[5, 5, 0, 0], [5, -10.328125, 0, -24.525],
                         [5, -56.3125, 0, -49.05], [5, -132.953125, 0, -73.575],
                         [5, -240.25, 0, -98.1]]

        for i in range(len(t)):
            if t[i] == expected_t[i]:
                assert t[i] == expected_t[i]
            else:
                assert abs((t[i] - expected_t[i]) / expected_t[i]) < epsilon

        for i in range(len(wsol)):
            for j in range(len(wsol[i])):
                if wsol[i][j] == expected_wsol[i][j]:
                    assert wsol[i][j] == expected_wsol[i][j]
                else:
                    assert abs((t[i] - expected_t[i]) / expected_t[i]) \
                           < epsilon


class TestPlot:

    def setup_method(self, method):
        self.c = CircleT(0, 0, 1, 4)
        self.t = TriangleT(1, 1, 1, 1)
        self.b = BodyT([1, -1, 2, -1], [2, 1, 3, -1], [1, 1, 1, 1])
        self.S = Scene(self.c, Fx, Fy, 0, 0)

    def teardown_method(self, method):
        self.c = None
        self.t = None
        self.b = None
        self.S = None

    def test_plot(self):
        t, wsol = self.S.sim(10, 100)
        plot(wsol, t)

        self.S.set_shape(self.b)
        t, wsol = self.S.sim(10, 100)
        plot(wsol, t)

        self.S.set_init_velo(5 * math.cos(math.pi), 5 * math.sin(-math.pi))
        self.S.set_unbal_forces(Fx2, Fy2)
        self.S.set_shape(self.t)
        t, wsol = self.S.sim(10, 100)
        plot(wsol, t)

        with pytest.raises(ValueError):
            plot([0, 0, 0], [0, 0])
