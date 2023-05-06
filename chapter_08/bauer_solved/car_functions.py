def make_car(car_brand, model, **car_info):
    car_info['car_brand'] = car_brand
    car_info['car_model'] = model
    return car_info