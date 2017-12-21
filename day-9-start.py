import datetime


class MessageUser():
    user_details = []
    messages = []
    base_message = """Hi {name}! 
Thank you for the purchase on {date}.
Porttitor accumsan eros faucibus morbi hendrerit 
leo sagittis erat sapien massa lacinia parturient 
nascetur viverra enim, orci justo facilisi litora 
sed eget nisl integer venenatis mollis posuere ${total}

Habitasse dui nunc!
"""

    def add_user(self, name, amount):
        # name=name.capitalize()
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" % (amount)
        detail = {
            "name": name,
            "amount": amount,
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        self.user_details.append(detail)

    def get_details(self):
        return self.user_details

    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                self.messages.append(new_msg)
            return self.messages
        return []


obj = MessageUser()
obj.add_user("Justin", 123.32)
obj.add_user("joHn", 94.65)
obj.add_user("Emille", 124.56)
obj.add_user("Jim", 323.4)
obj.add_user("ron", 23)
obj.add_user("sandra", 322.122333)
obj.add_user("verinica", 32.4)
obj.add_user("whitney", 99.99)
gt = obj.get_details()
print(gt)
msg = obj.make_messages()
print(msg)
