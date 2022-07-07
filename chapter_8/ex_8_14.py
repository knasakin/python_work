# 8.14. Автомобили
def make_car(company, model, **other_info):
    information = {'company': company, 'model': model}

    if other_info:
        for key, value in other_info.items():
            information[key] = value

    return information


car_1 = make_car('subaru', 'outback', color='blue', tow_package=True)
car_2 = make_car('toyota', 'camry', color='black', tow_package=False)
print(car_1)
print(car_2)
