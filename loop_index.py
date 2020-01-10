# -*- coding: utf-8 -*-

class LoopIndex:

    def __init__(self, limit, jump=1, start=0, skip_last=False):
        if jump == 0:
            raise ValueError("Incrementing by 0 does not make sense.")

        self._jump = jump
        self._start = start
        self.set_limit(limit)

        self.reset()
        self.skip_last_iter(skip_last)

    def __repr__(self):
        return "LoopIndex(" + str(self._limit) + ", "\
                + str(self._jump) + ", " + str(self._start) + ", "\
                + str(self._skip_last_iter) + ")"

    def check_bounds(self):
        return self._lambda_check_bounds()

    def get_value(self):
        return self._index

    def increment(self):
        self._index += self._jump

    def iterate(self):
        if self._first_iteration:
            self._first_iteration = False
        else:
            self.increment()
        return self.check_bounds()

    def _limit_is_reachable(self):
        return (self._limit - self._start) * self._jump > 0

    def reset(self):
        self._first_iteration = True
        self._index = self._start

    def _set_lambda_check_bounds(self):
        if self._skip_last_iter:
            if self._jump > 0:
                self._lambda_check_bounds = lambda:\
                    self._index + self._jump - 1 < self._limit
            else:
                self._lambda_check_bounds = lambda:\
                    self._index + self._jump + 1 >= self._limit
        else:
            if self._jump > 0:
                self._lambda_check_bounds = lambda: self._index < self._limit
            else:
                self._lambda_check_bounds = lambda: self._index >= self._limit

    def set_limit(self, limit):
        self._limit = limit
        if not self._limit_is_reachable():
            raise ValueError("The limit will never be reached. limit = "
                             + str(limit) + ", jump = " + str(jump)
                             + ", start = " + str(start))

    def skip_last_iter(self, skip_last=True):
        self._skip_last_iter = skip_last
        self._set_lambda_check_bounds()