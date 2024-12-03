def get_card_number(self):
    card_num = self.cardData.text()
    return card_num


def double(self, x):
    res = x * 2
    if res > 9:
        res = res - 9
    return res


def luhn_algorithm(self, card):
    odd = map(lambda x: self.double(int(x)), card[::2])
    even = map(int, card[1::2])
    return (sum(odd) + sum(even)) % 10 == 0


def process_data(self):
    number = self.get_card_number()
    if self.luhn_algorithm(number):
        self.errorLabel.setText("Ваша карта обрабатывается...")