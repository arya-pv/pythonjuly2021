def vaccine_age(func):
    def wrapper(a,b):
        if a<=18:
            raise Exception("you are not eligible")
        else:
            return func(a,b)
    return wrapper

@vaccine_age
def age_limit(age,name):
    return "eligible"
print(age_limit(45,"arya"))