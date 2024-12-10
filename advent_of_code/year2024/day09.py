# Day 9

# Input

from util.get_input import get_input

class DiskMap():
    def __init__(self):
        self.file_slots = []
        self.free_slots = []
    def __str__(self):
        string_builder = 'DiskMap\n\n'
        string_builder += 'File slots:\n'
        for file_slot in self.file_slots:
            string_builder += f'\t{str(file_slot)}\n'
        string_builder += '\nFree slots:\n'
        for free_slot in self.free_slots:
            string_builder += f'\t{str(free_slot)}\n'
        return string_builder

class FileSlot():
    def __init__(self, value):
        self.value = value
        self.left_to_compact = value
        self.id = None
    def __str__(self):
        return f'(id: {self.id}, value: {self.value}, left_to_compact: {self.left_to_compact})'

class FreeSlot():
    def __init__(self, value):
        self.value = value
        self.left_to_fill = value
    def __str__(self):
        return f'(value: {self.value}, left_to_fill: {self.left_to_fill})'

def get_disk_map():
    disk_map = DiskMap()
    for i, value in enumerate(get_input(2024, 9)[:-1]):
        if i % 2 == 0:
            disk_map.file_slots.append(FileSlot(int(value)))
        else:
            disk_map.free_slots.append(FreeSlot(int(value)))
    return disk_map


# Part 1

def compute_checksum(disk_map):
    l, r = 0, len(disk_map.file_slots) - 1
    position = 0
    checksum = 0
    while l < r:
        disk_map.file_slots[l].id = l
        while disk_map.file_slots[l].left_to_compact > 0:
            checksum += disk_map.file_slots[l].id * position
            disk_map.file_slots[l].left_to_compact -= 1
            position += 1
        while disk_map.free_slots[l].left_to_fill > 0 and r > l:
            if not disk_map.file_slots[r].id:
                disk_map.file_slots[r].id = r
            if disk_map.file_slots[r].left_to_compact == 0:
                r -= 1
                continue
            checksum += disk_map.file_slots[r].id * position
            disk_map.file_slots[r].left_to_compact -= 1
            disk_map.free_slots[l].left_to_fill -= 1
            position += 1
        l += 1
    while disk_map.file_slots[l].left_to_compact > 0:
        if not disk_map.file_slots[l].id:
            disk_map.file_slots[l].id = l
        checksum += disk_map.file_slots[l].id * position
        disk_map.file_slots[l].left_to_compact -= 1
        position += 1
    return checksum

print(f'The resulting filesystem checksum is {compute_checksum(get_disk_map())}.')


# Part 2

def compute_checksum_method2(disk_map):

    for i, file_slot in enumerate(disk_map.file_slots):
        file_slot.id = i
    
    checksum = 0
    
    file_slot_idx = 0
    free_slot_idx = 0

    position = 0
    compacted = 0

    min_free_space = 0

    while file_slot_idx < len(disk_map.file_slots):
        if disk_map.file_slots[file_slot_idx].left_to_compact <= 0:
            position += disk_map.file_slots[file_slot_idx].value
        while disk_map.file_slots[file_slot_idx].left_to_compact > 0:
            checksum += disk_map.file_slots[file_slot_idx].id * position
            disk_map.file_slots[file_slot_idx].left_to_compact -= 1
            position += 1
        while free_slot_idx < len(disk_map.free_slots) and disk_map.free_slots[free_slot_idx].left_to_fill > 0:
            found = False
            for i in range(len(disk_map.file_slots) - 1, file_slot_idx, -1):
                if min_free_space < disk_map.file_slots[i].left_to_compact <= disk_map.free_slots[file_slot_idx].left_to_fill:
                    while disk_map.file_slots[i].left_to_compact > 0:
                        checksum += disk_map.file_slots[i].id * position
                        disk_map.file_slots[i].left_to_compact -= 1
                        position += 1
                    disk_map.free_slots[free_slot_idx].left_to_fill -= disk_map.file_slots[i].value
                    found = True
                    break
            if not found:
                min_free_space = max(disk_map.free_slots[free_slot_idx].left_to_fill, min_free_space)
                position += disk_map.free_slots[free_slot_idx].left_to_fill
                break
        file_slot_idx += 1
        free_slot_idx += 1
    return checksum

print(f'The resulting filesystem checksum with the new method is {compute_checksum_method2(get_disk_map())}.')
