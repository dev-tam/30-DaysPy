import datetime

default_names = ["Justin","john","Emille","Jim","ron","sandra","verinica","whitney"]
default_amounts=[123.32,94.65,124.56,323.4,23,322.122333,32.4,99.99]

unf_message = """Hi {name}! 
Thank you for the purchase on {date}.
Porttitor accumsan eros faucibus morbi hendrerit 
leo sagittis erat sapien massa lacinia parturient 
nascetur viverra enim, orci justo facilisi litora 
sed eget nisl integer venenatis mollis posuere ${total}

Habitasse dui nunc!
"""


def make_messages(names, amounts):
	messages = []
	if len(names) == len(amounts):
		i = 0
		today = datetime.date.today()
		text = '{today.month}/{today.day}/{today.year}'.format(today=today)
		
		for name in names:
			name=name.capitalize()
			new_amount = "%.2f"%(amounts[i])
			new_msg=unf_message.format(
				name=name,
				date=text,
				total=new_amount
				)
			i += 1
			print(new_msg)


make_messages(default_names,default_amounts)