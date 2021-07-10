def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

danh_sach_sap_xep = [16,6,2002,2021]
bubble_sort(danh_sach_sap_xep)
print(danh_sach_sap_xep)