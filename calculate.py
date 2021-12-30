def calculate(**kwargs):
    if kwargs["make_float"] == False:
        if "message" in kwargs:
            if kwargs["operation"] == "add":
                return kwargs["message"] +" "+ str(int(kwargs["first"]+kwargs["second"]))
            elif kwargs["operation"] == "subtract":
                return kwargs["message"] +" "+ str(int(kwargs["first"]-kwargs["second"]))
            elif kwargs["operation"] == "multiply":
                return kwargs["message"] +" "+ str(int(kwargs["first"]*kwargs["second"]))
            return kwargs["message"] +" "+ str(int(kwargs["first"]/kwargs["second"]))
        else:
            if kwargs["operation"] == "add":
                return "The result is " + str(int(kwargs["first"]+kwargs["second"]))
            elif kwargs["operation"] == "subtract":
                return "The result is " + str(int(kwargs["first"]-kwargs["second"]))
            elif kwargs["operation"] == "multiply":
                return "The result is " + str(int(kwargs["first"]*kwargs["second"]))
            return "The result is " + str(int(kwargs["first"]/kwargs["second"]))
    elif kwargs["make_float"] == True:
        if "message" in kwargs:
            if kwargs["operation"] == "add":
                return kwargs["message"] + " "+str(float(kwargs["first"]+kwargs["second"]))
            elif kwargs["operation"] == "subtract":
                return kwargs["message"] +" "+ str(float(kwargs["first"]-kwargs["second"]))
            elif kwargs["operation"] == "multiply":
                return kwargs["message"] +" "+ str(float(kwargs["first"]*kwargs["second"]))
            return kwargs["message"] +" "+ str(float(kwargs["first"]/kwargs["second"]))
        else:
            if kwargs["operation"] == "add":
                return "The result is " + str(float(kwargs["first"]+kwargs["second"]))
            elif kwargs["operation"] == "subtract":
                return "The result is " + str(float(kwargs["first"]-kwargs["second"]))
            elif kwargs["operation"] == "multiply":
                return "The result is " + str(float(kwargs["first"]*kwargs["second"]))
            return "The result is " + str(float(kwargs["first"]/kwargs["second"]))

def better_calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final

print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))

print(better_calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(better_calculate(make_float=True, operation='divide', first=3.5, second=5))