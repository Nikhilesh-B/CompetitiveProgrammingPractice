import bisect


class XOUR_solution():
    def __init__(self, arr: list):
        self.arr = arr
        self.set_of_elements = set(arr)
        self.positions_of_elements = {}
        self.last_position_of_elements = {}
        self.sorted_unique_elements = []

    def sorted_unique_set_of_elements(self):
        self.sorted_unique_elements = sorted(
            list(self.set_of_elements), reverse=True)
        self.idxs_of_sorted_unique_elements = {
            element: i for i, element in enumerate(self.sorted_unique_elements)}

    def create_positions_of_elements(self):
        for i, element in enumerate(self.arr):
            if element in self.positions_of_elements:
                self.positions_of_elements[element].append(i)
            else:
                self.positions_of_elements[element] = [i]

    def create_last_positions_of_elements(self):
        for element in self.set_of_elements:
            self.last_position_of_elements[element] = self.positions_of_elements[element][-1]

    def insert_and_preserve_order(self, ordered_lst, insertion_val):
        insertion_idx = bisect.bisect_left(ordered_lst, insertion_val)
        ordered_lst.insert(insertion_idx, insertion_val)
        return ordered_lst

    def remove_and_preserveOrder(self, ordered_lst, removal_val):
        removal_idx = bisect.bisect_left(ordered_lst, removal_val)
        ordered_lst.pop(removal_idx)
        return ordered_lst

    def make_updates_to_stored_positions(self, larger_val, larger_idx, smaller_val, smaller_idx):
        print("swapping", larger_val, "at", larger_idx,
              "with", smaller_val, "at", smaller_idx)
        self.positions_of_elements[larger_val] = self.remove_and_preserveOrder(
            self.positions_of_elements[larger_val], larger_idx)
        self.positions_of_elements[smaller_val] = self.remove_and_preserveOrder(
            self.positions_of_elements[smaller_val], smaller_idx)
        self.positions_of_elements[larger_val] = self.insert_and_preserve_order(
            self.positions_of_elements[larger_val], smaller_idx)
        self.positions_of_elements[smaller_val] = self.insert_and_preserve_order(
            self.positions_of_elements[smaller_val], larger_idx)
        self.last_position_of_elements[larger_val] = self.positions_of_elements[larger_val][-1]
        self.last_position_of_elements[smaller_val] = self.positions_of_elements[smaller_val][-1]

    def sort_arr_XOUR(self):
        i = 0
        n = len(self.arr)

        while i < n:
            curr_element = self.arr[i]
            for j in range(3, 0, -1):
                new_candidate = curr_element-j
                print(new_candidate)
                if new_candidate in self.set_of_elements:
                    last_position_of_new_candidate = self.last_position_of_elements[new_candidate]
                    if last_position_of_new_candidate > i:
                        self.arr[i], self.arr[last_position_of_new_candidate] = self.arr[last_position_of_new_candidate], self.arr[i]
                        self.make_updates_to_stored_positions(
                            curr_element, i, new_candidate, last_position_of_new_candidate)
                        break
            i += 1
        return self.arr


if __name__ == "__main__":
    t = int(input())
    all_lsts = []
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        all_lsts.append(arr)

    for lst in all_lsts:
        xour = XOUR_solution(lst)
        xour.sorted_unique_set_of_elements()
        xour.create_positions_of_elements()
        xour.create_last_positions_of_elements()
        sorted_arr = xour.sort_arr_XOUR()
        print(" ".join(map(str, sorted_arr)))
