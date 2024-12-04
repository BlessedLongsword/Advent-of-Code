# Day 2

# Input

def get_box_list(file):
    dimensions_list = open(file).read().splitlines()
    return [list(map(int, dimensions.split('x'))) for dimensions in dimensions_list]
    

# Part 1

def compute_box_wrapping_paper(l, w, h):
    face_surfaces = [w * l, h * l, w * h]
    return 2 * sum(face_surfaces) + min(face_surfaces)

def compute_total_wrapping_paper(dimensions_list):
    return sum([compute_box_wrapping_paper(*dimensions) for dimensions in dimensions_list])
    
print(f"The total amount of square feet of wrapping paper the elves should order is {compute_total_wrapping_paper(get_box_list('input.txt'))}")


# Part 2

def compute_ribbon_length(l, w, h):
    volume = l * w * h
    side_pair_sums = [l + w, w + h, h + l]
    return 2 * min(side_pair_sums) + volume

def compute_total_ribbon_length(dimensions_list):
    return sum([compute_ribbon_length(*dimensions) for dimensions in dimensions_list])

print(f"They should order {compute_total_ribbon_length(get_box_list("input.txt"))} feet of ribbon")
