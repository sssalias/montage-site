def get_pricing_data(Model):
    data = Model.objects.all()
    res = {}
    radius = sorted(list(set([x.radius for x in data])))
    for el in data:
        res[el.type.name] = sorted(list(filter(lambda x: x.type == el.type, data)), key=lambda x: x.radius)
    return {
        'data': res,
        'radius': radius
    }
