import datetime as dt
from datetime import timedelta


class Record:
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment
        if date == '':
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        for r in self.records:
            if r.date == dt.datetime.now().date():
                today_stats += r.amount
        print(today_stats)
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        now = dt.datetime.now().date()
        week_ago = now - timedelta(7)
        for r in self.records:
            if week_ago <= r.date <= now:
                week_stats += r.amount
        print(week_stats)
        return week_stats


class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        conversion_rates = {
            'BYN': 1,
            'USD': 0.31,
            'RUB': 31.56,
            'EUR': 0.29
        }

        balance = self.limit - self.get_today_stats()
        balance *= conversion_rates.get(currency, 1)

        if balance > 0:
            print(f'На сегодня осталось {balance} {currency}')
        elif balance == 0:
            print('Денег нет, держись')
        else:
            print(f'Денег нет, держись: твой долг: {balance} {currency}')


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        today_stats = self.get_today_stats()
        remains = self.limit - today_stats
        if remains > 0:
            print(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {remains} кКал')
        else:
            print('Харэ жрать!')


def main():
    r1 = Record(11, 'Мясная у Мамуки', '17.12.2024')
    r2 = Record(15, '', '08.12.2024')
    cash = CashCalculator(10)
    cash.add_record(r1)
    cash.add_record(r2)

    cash.get_week_stats()


pass

if __name__ == '__main__':
    main()
