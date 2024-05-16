import heapq


def join_cables(cables):
    _cables_heap = []

    [heapq.heappush(_cables_heap, cable) for cable in cables]

    _cables_join_order = []

    while len(_cables_heap) != 1:
        joined_cables = [heapq.heappop(_cables_heap) for _ in range(2)]

        _cables_join_order.append(tuple(joined_cables))

        heapq.heappush(_cables_heap, sum(joined_cables))

    return _cables_join_order


cables = [i for i in range(50, 1, -3)]
# [50, 47, 44, 41, 38, 35, 32, 29, 26, 23, 20, 17, 14, 11, 8, 5, 2]

cables_join_order = join_cables(cables)
print("Порядок з'єднання кабелів:", cables_join_order)
# [(2, 5), (7, 8), (11, 14), (15, 17), (20, 23), (25, 26), (29, 32), (32, 35), (38, 41), (43, 44), (47, 50), (51, 61), (67, 79), (87, 97), (112, 146), (184, 258)]
