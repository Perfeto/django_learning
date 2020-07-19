import random

from django.http import HttpResponse

from polls.domain.BuildingStatusItemModel import BuildingStatusItemModel
from polls.domain.Group import Group
from polls.utils.ToJSONEncoder import ToJSONEncoder


def index(request):
    names_of_build = [
        "Пират",
        "Боливар",
        "Кристо",
        "Майк",
        "Джек",
        "Тонни",
        "Люци",
        "Грин",
        "Люк"
    ]

    addresses_of_build = [
        "Москва, 117997, ул. Вавилова, д. 19 ",
        "Менжинского улица, 38",
        "Минское шоссе, 66",
        "Мичуринский проспект",
        "Монтажная улица",
        "Олимпийский проспект",
        "Ореховый бульвар, 14",
        "Ореховый бульвар, 22",
        "Открытое шоссе"
    ]

    types_of_build = [
        "Промышленный",
        "Гражданский",
        "Дачный",
        "Коммунальный",
        "Военный",
        "Сельскохозяйственный",
        "Транспортный",
        "Энергетический",
        "Гидротехнический"
    ]

    list_of_building_status_models = []
    for number in range(9):
        list_of_building_status_models.append(
            BuildingStatusItemModel(
                id_ob=number,
                name_obj=names_of_build[number],
                addr_obj=addresses_of_build[number],
                cat_obj=types_of_build[number],
                count_items_oper_no=random.randint(0, 100),
                count_items_oper_breach=random.randint(0, 100),
                count_items_oper_accepted=random.randint(0, 100),
                groups_arr=[
                    Group(
                        id_group=1,
                        name_group="Квартира",
                        count_items=random.randint(0, 500),
                        count_checked=random.randint(0, 100),
                        count_breach=random.randint(0, 100),
                        count_accepted=random.randint(0, 100)
                    ),
                    Group(
                        id_group=2,
                        name_group="Дача",
                        count_items=random.randint(0, 500),
                        count_checked=random.randint(0, 100),
                        count_breach=random.randint(0, 100),
                        count_accepted=random.randint(0, 100)
                    ),
                    Group(
                        id_group=3,
                        name_group="Завод",
                        count_items=random.randint(0, 500),
                        count_checked=random.randint(0, 100),
                        count_breach=random.randint(0, 100),
                        count_accepted=random.randint(0, 100)
                    )
                ],
            )
        )

    return HttpResponse(ToJSONEncoder().encode(list_of_building_status_models), content_type="application/json")


def get_random_percents():
    percents_array = []
    for i in range(9):
        percents_array.append(random.randint(0, 100))

    return percents_array
