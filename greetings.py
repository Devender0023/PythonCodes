def special_greetings(**kwargs):
	if "David" in kwargs and kwargs["David"] == "special":
		return "You get a special greeting David!"
	elif "David" in kwargs:
		return f"{kwargs['David']} David!"
	return "Not sure who this is...."

print(special_greetings(David = 'Hello'))
print(special_greetings(Bob = 'hello'))
print(special_greetings(David = 'special'))