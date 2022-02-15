from typing import Tuple
import random
import datetime
from abc import ABC, abstractmethod


class DummyData(ABC):
    def __init__(self, random_seed=None):
        self.first_names = ['Bishwajit', 'Tsubaki', 'Arin', 'Harry', 'Ram', 'Shyam', 'Jodu', 'Modu', 'Sayan', 'Velma']
        self.last_names = ['Ghosh', 'Cullen', 'Potter', 'Dey', 'Roy', 'Sawabe', 'Dinkley']
        self.depts = {
            1: 'CSE',
            2: 'ECE',
            3: 'ME',
            4: 'MME',
            5: 'BT',
            6: 'PHD',
            7: 'CE',
            8: 'MCA',
            9: 'IT',
            10: 'EE',
        }
        self.start_date = '2020-01-01'
        self.end_date = '2021-10-31'
        self.random_seed = random_seed
        self.additional_setters()

        random.seed(self.random_seed)

    def additional_setters(self):
        pass

    def get_dept(self) -> Tuple[str, int]:
        x = random.randint(1, len(self.depts))
        return self.depts[x], x

    @staticmethod
    def get_cgpa(precision=2) -> float:
        return round(random.randint(5, 9) + random.random(), precision)

    def get_date(self) -> str:
        start_date = datetime.datetime.strptime(self.start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(self.end_date, '%Y-%m-%d')
        if self.start_date > self.end_date:
            raise ValueError('Start date if after End date')
        date_diff = random.randint(0, (end_date - start_date).days)
        date = start_date + datetime.timedelta(days=date_diff)
        return datetime.datetime.strftime(date, '%Y-%m-%d')

    def get_name(self, max_len=15, pad=10) -> str:
        a, b = map(random.choice, (self.first_names, self.last_names))
        iter_count = 0
        while len(a) + len(b) + 1 > max_len:
            a, b = map(random.choice, (self.first_names, self.last_names))
            iter_count += 1
            if iter_count > len(self.first_names) * len(self.last_names) + pad:
                raise ValueError('max_len given is probably too low to make any names')
        return "{} {}".format(a, b)

    @abstractmethod
    def get_single_data(self, index=1, *args, **kwargs) -> str:
        pass

    def get_multiple_data(self, n=15, start_index=1) -> str:
        arr = [
            self.get_single_data(index=i)
            for i in range(start_index, start_index + n)
        ]
        return ',\n'.join(arr)

    def dummy(self, n=15):
        print(self.get_multiple_data(n=n))
