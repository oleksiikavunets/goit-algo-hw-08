import heapq


def heap_sort(iterable, descending=False):
    sign = -1 if descending else 1
    h = [sign * el for el in iterable]
    heapq.heapify(h)
    return [sign * heapq.heappop(h) for _ in range(len(h))]


def join_cables(cables):
    def _join(_cables_heap):
        join_order = []
        total_sum = 0
        while len(_cables_heap) != 1:
            joined_cables = [heapq.heappop(_cables_heap) for _ in range(2)]

            join_order.append(tuple(joined_cables))

            total_sum += sum(joined_cables)
            heapq.heappush(_cables_heap, sum(joined_cables))
        return total_sum, join_order

    _cables_heap_1 = heap_sort(cables)
    sum_1, _cables_join_order_1 = _join(_cables_heap_1)

    _cables_heap_2 = heap_sort(cables, descending=True)
    sum_2, _cables_join_order_2 = _join(_cables_heap_2)

    return _cables_join_order_1 if sum_1 < sum_2 else _cables_join_order_2


cables = [i for i in range(50, 1, -3)]
# [50, 47, 44, 41, 38, 35, 32, 29, 26, 23, 20, 17, 14, 11, 8, 5, 2]

cables_join_order = join_cables(cables)
print("Порядок з'єднання кабелів:", cables_join_order)
# [(2, 5), (7, 8), (11, 14), (15, 17), (20, 23), (25, 26), (29, 32), (32, 35), (38, 41), (43, 44), (47, 50), (51, 61), (67, 79), (87, 97), (112, 146), (184, 258)]
