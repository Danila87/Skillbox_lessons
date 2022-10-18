#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distances = {}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

Moscow = sites['Moscow']
London = sites['London']
Paris = sites['Paris']

Moscow_to_London = ((Moscow[0] - London[0]) ** 2 + (Moscow[1] - London[1]) ** 2) ** .5
Moscow_to_Paris = ((Moscow[0] - Paris[0]) ** 2 + (Moscow[1] - Paris[1]) ** 2) ** .5
London_to_Paris = ((London[0] - Paris[0]) ** 2 + (London[1] - Paris[1]) ** 2) ** .5

# TODO здесь заполнение словаря

distances['Moscow'] = {'London': Moscow_to_London, 'Paris': Moscow_to_Paris}
distances['London'] = {'Moscow': Moscow_to_London, 'Paris': London_to_Paris}
distances['Paris'] = {'London': London_to_Paris, 'Moscow': Moscow_to_Paris}

print(distances)




