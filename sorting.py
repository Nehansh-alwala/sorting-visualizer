import random
import time
import streamlit as st

st.set_page_config(layout="wide")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")
local_css("arrow.css")

st.markdown("""
        <div class="container">
            <div class="animation">
                <span class="first">Welcome to</span>
                <span class="slide">
                    <span class="second">sorting visualizer</span>
                </span>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
        <svg class="arrows">
            <path class="a1" d="M0 0 L30 32 L60 0"></path>
            
        </svg>
    """, unsafe_allow_html=True)


def bubble_sort(numbers, draw_func):
    n = len(numbers)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                
                st.write(f"<li>Comparing {numbers[j]} and {numbers[j + 1]}</li>",
                         f"<li>Since {numbers[j]} > {numbers[j + 1]}, swapping them to arrange in ascending order.</li>",
                         f"<li>Array after swapping: {numbers}</li>",unsafe_allow_html=True)
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                draw_func(numbers, j, j + 1, n - i - 1)
                st.write("---")
                time.sleep(0.2)
                
def insertion_sort(numbers, draw_func):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        
        st.write(f"<li>Comparing {key} with the elements before it and shifting them to the right if they are greater.</li>",
                 f"<li>Inserting {key} into its correct position.</li>",
                 f"<li>Array after inserting {key}: {numbers}</li>",unsafe_allow_html=True)
        
        numbers[j + 1] = key
        draw_func(numbers, i, j + 1, i)
        
        st.write("---")
        time.sleep(0.2)

def selection_sort(numbers, draw_func):
    for i in range(len(numbers)):
        min_index = i

        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
       
        st.write(f"<li>Finding the minimum element in the unsorted part of the array.</li>",
                 f"<li>Swapping the minimum element ({numbers[min_index]}) with the current element ({numbers[i]}).</li>",
                 f"<li>Array after swapping: {numbers}</li>",unsafe_allow_html=True)
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
        draw_func(numbers, i, min_index, i)
        st.write("---")
        time.sleep(0.2)
        
def quick_sort(numbers, draw_func, low, high):
    if low < high:
        partition_index = partition(numbers, draw_func, low, high)
        quick_sort(numbers, draw_func, low, partition_index - 1)
        quick_sort(numbers, draw_func, partition_index + 1, high)

def partition(numbers, draw_func, low, high):
    pivot = numbers[high]
    i = low - 1
    st.write(f"Considering last element as the Pivot i.e {pivot}")

    for j in range(low, high):
        if numbers[j] < pivot:
            
            st.write(f"Swapping the elements {numbers[i]} and {numbers[j]} to place the smaller element on the left side of the pivot.",
                     f"Array after swapping: {numbers}",unsafe_allow_html=True)
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
            
           
            draw_func(numbers, i, j, high)
            st.write("---")
            time.sleep(0.2)
          
    numbers[i + 1], numbers[high] = numbers[high], numbers[i + 1]
    
    # Visualize the swapping process
    draw_func(numbers, i + 1, high, high)

    st.write(f"Swapped {numbers[i + 1]} and {numbers[high]}",
             f"Placing the pivot ({numbers[high]}) at its correct position in the sorted array.",
             f"Array after placing pivot: {numbers}",unsafe_allow_html=True)
    st.write("---")
    time.sleep(0.2)
    return i + 1


def merge_sort(numbers, draw_func):
    if len(numbers) > 1:
        # Divide the array into two halves
        mid = len(numbers) // 2
        left = numbers[:mid]
        right = numbers[mid:]

        # Recursively sort the two halves
        merge_sort(left, draw_func)
        merge_sort(right, draw_func)

        # Merge the sorted halves
        i = j = k = 0
        
        st.write(f"Comparing the elements {left[i-1]} and {right[j-1]}.",
                 f"The smaller element ({numbers[k]}) is added to the sorted sequence.",
                 f"Array after comparison: {numbers}",unsafe_allow_html=True)
        

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1

            # Visualize the comparison and merging process
            draw_func(numbers, k, i, j)
            st.write("---")
            
            time.sleep(0.2)
            
            # Explanation for each step
            
            
            k += 1

        while i < len(left):
            
            st.write(f"Adding the remaining elements from the left half ({left[i]}) to the sorted sequence.",
                     f"Array after adding: {numbers}",unsafe_allow_html=True)
            numbers[k] = left[i]
            
            # Visualize the adding process
            draw_func(numbers, k, i, -1)
            
            time.sleep(0.2)
            
            # Explanation for each step
            
            st.write("---")
            
            i += 1
            k += 1

        
        while j < len(right):
            
            st.write(f"Adding the remaining elements from the right half ({right[j]}) to the sorted sequence.",
                     f"Array after adding: {numbers}",unsafe_allow_html=True)
            numbers[k] = right[j]
            
            
            # Visualize the adding process
            draw_func(numbers, k, -1, j)
            
            time.sleep(0.2)
            
            # Explanation for each step
            
            st.write("---")
            
            j += 1
            k += 1


def draw_numbers(numbers, sorted_index, comparison_index, current_index):
    max_value = max(numbers)
    col1,col2=st.columns(2)
    with col2:
        html = "<p style='font-size: 20px;'>"
        for i, num in enumerate(numbers):
            if i == sorted_index:
                color = "#9370DB"  # Sorted bar,purple
            elif i == comparison_index or i == current_index:
                color = "#EA3C53"  # Comparison bar or current bar
            else:
                color = "#00ba37"  # Unsorted bar

            height = int((num / max_value) * 300)  # Scale the height based on the maximum value
            html += (
                f"<span style='background-color: {color}; color: light blue; padding: 3px; "
                f"display: inline-block; height: {height}px; margin-right: 5px;'>{num}</span>"
            )
        html += "</p>"

        st.write(html, unsafe_allow_html=True)



def steps(a,b,c,d,e):
    if a:
        st.sidebar.title("How does Bubble Sort works? 🤔")
        st.sidebar.write('''
            space complexity: `O(1)`\n
            Best case: `O(nlogn)`\n
            Average Case: `O(nlogn)`\n
            Worst case: `O(n^2)`
            ''')
        st.sidebar.write('''
    1. Start with an unsorted list of numbers.\n
    2. Get the length of the list and assign it to the variable `n`.\n
    3. Iterate through the list from index `0` to `n-2`. This loop is responsible for the number of passes.\n
    4. Within each pass, iterate through the list from index `0` to `n-i-2`. This loop compares adjacent elements.\n
    5. Compare the element at index `j` with the element at index `j+1`.\n
    6. If the element at index `j` is greater than the element at index `j+1`, swap them.\n
    7. Repeat steps 5 and 6 for each pair of adjacent elements until the end of the inner loop.\n
    8. After each pass of the outer loop, the largest element "bubbles up" to the end of the list.\n
    9. Repeat steps 3-8 until the entire list is sorted.\n
    10. The sorted list will have the smallest elements at the beginning and the largest elements at the end i.e `ascending order`.
        ''')
    
    if b:
        st.sidebar.title("How does Insertion Sort works? 🤔")
        st.sidebar.write('''
            space complexity: `O(1)`\n
            Best case: `O(nlogn)`\n
            Average Case: `O(nlogn)`\n
            Worst case: `O(n*n)`
            ''')
        st.sidebar.write('''
    1.Start with an unsorted list of numbers.\n
    2.Iterate through the list from index `1` to the length of the list `minus 1`.\n
    3.Get the current element at index `i` and assign it to the variable `key`.\n
    4.Set the index of the previous element to `j = i - 1`.\n
    5.Compare the element at index `j` with the `key`.\n
    6.If the element at index `j` is greater than the `key`, shift the element to the right by assigning `numbers[j + 1]` the value of `numbers[j]`.\n
    7.Decrement `j` by `1` to compare the `key` with the previous element.\n
    8.Repeat steps 5 and 6 until either `j` becomes less than `0` or the element at index `j` is not greater than the `key`.\n
    9.Insert the `key` at the correct position in the list by assigning `numbers[j + 1]` the value of `key`.\n
    10.Repeat steps 2-9 until the entire list is sorted.\n
    11.The sorted list will have the elements arranged in `ascending order`.
        ''')

    if c:
        st.sidebar.title("How does Selection Sort works? 🤔")
        st.sidebar.write('''
            space complexity: `O(1)`\n
            Best case: `O(nlogn)`\n
            Average Case: `O(nlogn)`\n
            Worst case: `O(n*n)`
            ''')
        st.sidebar.write('''
    1.Start iterating through the list from the `first element (index 0)` to the `second-to-last element`.\n
    2.Assume the current index as the index of the `minimum value (min_index)`.\n
    3.Compare the value at the current index with the values of the remaining elements.\n
    4.If a smaller value is found, update the min_index to the index of the new minimum value.\n
    5.After completing the inner loop, swap the value at the current index with the minimum value found `(numbers[i] and numbers[min_index]).`\n
    6.Repeat this process, incrementing the current index by `1`, until the entire list is sorted.''')
            
    if d:
        st.sidebar.title("How does Quick Sort works? 🤔")
        st.sidebar.write('''
            space complexity: `O(1)`\n
            Best case: `O(nlogn)`\n
            Average Case: `O(nlogn)`\n
            Worst case: `O(n*n)`
            ''')
        st.sidebar.write('''
    1.The `quickSort function` takes in the array `numbers`, the low index `low`, and the high index `high` as parameters.\n
    2.It first checks if the `low` index is less than the `high` index, indicating that there is more than one element to be sorted in the current `subarray`.\n
    3.Inside the `quickSort function`, the `partition function` is called to partition the array and obtain the partition index.\n
    4.The `quickSort function` is recursively called on the `left` and `right` subarrays, before and after the partition index, respectively. This step ensures that the subarrays are sorted.\n
    5.The `partition function` takes in the array `numbers`, the low index `low`, and the high index `high`.\n
    6.It selects the `pivot` element as the `last element` of the current subarray (indicated by `numbers[high]`).\n
    7.The partition index `i` is initialized to `low - 1`.\n
    8.The function iterates through the elements from `low to high - 1`.\n
    9.If an element `numbers[j]` is found to be less than the `pivot`, it is moved to the `left` side of the partition by swapping it with the element at index `i + 1`. The `i` value is then incremented.\n
    10.After the iteration is complete, all elements smaller than the `pivot` are placed on the `left` side, and the `pivot` is placed at the correct position by swapping it with the element at index `i + 1`.\n
    11.Finally, the function returns the partition index `(i + 1)`, which is the position of the `pivot` element.
        ''')

    if e:
        st.sidebar.title("How does Merge Sort works? 🤔")
        st.sidebar.write('''
            space complexity: `O(n)`\n
            Best case: `O(nlogn)`\n
            Average Case: `O(nlogn)`\n
            Worst case: `O(nlogn)`
            ''')
        st.sidebar.write('''
    1.Check if the length of the input array, `numbers`, is greater than `1`, If not, it is already sorted, so we can skip the sorting process.\n
    2.If the array has more than `1` element, calculate the middle index, `mid`, by `dividing` the `length of the array by 2`.\n
    3.Divide the array into two subarrays: the `left subarray`, left, containing elements from index `0 to mid-1`, and the `right subarray`, right, containing elements from index `mid` to the end of the array.\n
    4.Recursively call the `mergeSort function` on both the `left` and `right subarrays` to sort them.\n
    5.Initialize three pointers, `i`, `j`, and `k`, to keep track of the current positions in the `left`, `right`, and `merged arrays`, respectively.\n
    6.Compare the elements at the current positions `i` and `j` in the `left` and `right subarrays`, respectively.\n
    7.If the element in the `left subarray` is smaller than the element in the `right subarray`, place the element from the `left subarray` into the `original array` at index `k`. Otherwise, place the element from the `right subarray` into the `original array` at index `k`.\n
    8.Move the pointer `i` or `j` (depending on which subarray's element was chosen) to the next position to compare the next elements.\n
    9.Increment the pointer `k` to move to the next position in the `merged array`.\n
    10.Repeat steps 6-9 until all elements from either the `left or right subarray` have been placed into the `merged array`.\n
    11.Add any remaining elements from the `left subarray`, if any, to the `merged array`.\n
    12.Add any remaining elements from the `right subarray`, if any, to the `merged array`.\n
    13.The original array numbers is now sorted.
    
        ''')
        


def pseudo(bubble,insert,selection,quick,merge):
    if bubble:
        st.write("<h3>Algorithm ✍🏻</h3>",unsafe_allow_html=True)
        bubble=''' function bubbleSort(numbers):
        n = length(numbers)  # Get the length of the numbers list
        
        for i from 0 to n-2:  # Iterate through each element except the last one
            for j from 0 to n-i-2:  # Iterate through unsorted part of the list
                if numbers[j] > numbers[j+1]:  # Compare adjacent elements
                    swap numbers[j] and numbers[j+1]  # Swap if the current element is greater than the next one
        ''' 
        st.code(bubble,language='python')

    if insert:
        st.write("<h3>Algorithm ✍🏻</h3>",unsafe_allow_html=True)
        insert=''' function insertionSort(numbers):
        for i from 1 to length(numbers) - 1:
            key = numbers[i]  # Get the current element
            j = i - 1  # Set the index of the previous element

            while j >= 0 and numbers[j] > key:
                numbers[j + 1] = numbers[j]  # Shift elements to the right
                j = j - 1

            numbers[j + 1] = key  # Insert the current element at the correct position
        ''' 
        st.code(insert,language='python')

    if selection:
        st.write("<h3>Algorithm ✍🏻</h3>",unsafe_allow_html=True)
        selection='''
                function selectionSort(numbers):
        for i from 0 to length(numbers) - 1:
            min_index = i  # Assume the current index has the minimum value

            for j from i + 1 to length(numbers) - 1:
                if numbers[j] < numbers[min_index]:
                    min_index = j  # Update the minimum index

            swap numbers[i] and numbers[min_index]  # Swap the current element with the minimum element

                '''
        st.code(selection,language='python')

    if quick:
        st.write("<h3>Algorithm ✍🏻</h3>",unsafe_allow_html=True)
        quick='''
                function quickSort(numbers, low, high):
        if low < high:
            // Partition the array and get the partition index
            partitionIndex = partition(numbers, low, high)
            
            // Recursively sort the left and right subarrays
            quickSort(numbers, low, partitionIndex - 1)
            quickSort(numbers, partitionIndex + 1, high)

    function partition(numbers, low, high):
        // Select the pivot element
        pivot = numbers[high]
        
        // Initialize the partition index
        i = low - 1

        // Iterate through the elements from low to high-1
        for j from low to high - 1:
            if numbers[j] < pivot:
                // Move elements smaller than the pivot to the left side
                i += 1
                swap numbers[i] and numbers[j]

        // Place the pivot element at the correct position
        swap numbers[i + 1] and numbers[high]
        
        // Return the partition index
        return i + 1

                '''
        st.code(quick,language='python')

    if merge:
        st.write("<h3>Algorithm ✍🏻</h3>",unsafe_allow_html=True)
        merge='''
                function mergeSort(numbers):
        if length(numbers) > 1:  # Base case: If the array has more than 1 element
            mid = length(numbers) // 2  # Calculate the middle index
            left = numbers[:mid]  # Divide the array into left subarray
            right = numbers[mid:]  # Divide the array into right subarray

            mergeSort(left)  # Recursively call mergeSort on the left subarray
            mergeSort(right)  # Recursively call mergeSort on the right subarray

            i = j = k = 0  # Initialize pointers for left, right, and merged arrays

            while i < length(left) and j < length(right):  # Merge elements from left and right subarrays
                if left[i] < right[j]:  # Compare elements from left and right subarrays
                    numbers[k] = left[i]  # Place the smaller element in the original array
                    i += 1  # Move pointer in the left subarray
                else:
                    numbers[k] = right[j]  # Place the smaller element in the original array
                    j += 1  # Move pointer in the right subarray
                k += 1  # Move pointer in the original array

            while i < length(left):  # Add remaining elements from the left subarray
                numbers[k] = left[i]
                i += 1
                k += 1

            while j < length(right):  # Add remaining elements from the right subarray
                numbers[k] = right[j]
                j += 1
                k += 1
                '''
        st.code(merge,language='python')


def note():
    st.write("<h4>NOTE:</h4>",unsafe_allow_html=True)
    colors = [
            ("#9370DB", "Sorted Bar"),
            ("#EA3C53", "Comparison bar or Current bar"),
            ("#00BA37", "Unsorted bar"),
            
        ]
    num_colors = len(colors)
    colors_per_column = (num_colors + 2) // 3

    columns = st.columns(3)
        
    for i in range(num_colors):
        with columns[i // colors_per_column]:
            color, description = colors[i]
            st.markdown(f"<div style='display: flex; align-items: center;'>", unsafe_allow_html=True)
            st.markdown(f"<div style='background-color: {color}; width: 20px; height: 20px; margin-right: 10px;'></div>", unsafe_allow_html=True)
            st.markdown(f"<p>{description}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)




def main():

    
    st.title("Sorting Visualizer 🤖")
    algorithm = st.selectbox("Choose any sorting algorithm", ["Bubble Sort", "Insertion Sort", "Selection Sort", "Quick Sort",
                                           "Merge Sort"])
    
    select=st.radio("select the following options",('Random',"Custom"))

    if select=='Random':
        array_size = st.slider("Select array size", min_value=5, max_value=100, value=30)

        # Generate a random array
        array = [random.randint(1, 100) for _ in range(array_size)]
    else:
        array_string = st.text_input("Enter comma-separated numbers")

        # Parse the input and create an array from the numbers
        array = [int(num.strip()) for num in array_string.split(",") if num.strip()]

    if st.button("Sort"):

        

        if algorithm == "Bubble Sort":
            pseudo(bubble=1,insert=0,selection=0,quick=0,merge=0)
            b1,b2=st.columns(2)
            steps(a=1,b=0,c=0,d=0,e=0)
            st.write("<h3>Original Numbers:</h3>",unsafe_allow_html=True)
            draw_numbers(array, -1, -1, -1)
            note()
            st.title("Sorting step-by-step explanation:")
            bubble_sort(array, draw_numbers)

        elif algorithm == "Insertion Sort":
            pseudo(bubble=0,insert=1,selection=0,quick=0,merge=0)
            steps(a=0,b=1,c=0,d=0,e=0)
            st.write("<h3>Original Numbers:</h3>",unsafe_allow_html=True)
            draw_numbers(array, -1, -1, -1)
            note()
            st.title("Sorting step-by-step explanation:")
            insertion_sort(array, draw_numbers)

        elif algorithm == "Selection Sort":
            pseudo(bubble=0,insert=0,selection=1,quick=0,merge=0)
            steps(a=0,b=0,c=1,d=0,e=0)
            st.write("<h3>Original Numbers:</h3>",unsafe_allow_html=True)
            draw_numbers(array, -1, -1, -1)
            note()
            st.title("Sorting step-by-step explanation:")
            selection_sort(array, draw_numbers)

        elif algorithm == "Quick Sort":
            pseudo(bubble=0,insert=0,selection=0,quick=1,merge=0)
            steps(a=0,b=0,c=0,d=1,e=0)
            st.write("<h3>Original Numbers:</h3>",unsafe_allow_html=True)
            draw_numbers(array, -1, -1, -1)
            note()
            st.title("Sorting step-by-step explanation:")
            quick_sort(array, draw_numbers, 0, len(array) - 1)

        elif algorithm == "Merge Sort":
            pseudo(bubble=0,insert=0,selection=0,quick=0,merge=1)
            steps(a=0,b=0,c=0,d=0,e=1)
            st.write("<h3>Original Numbers:</h3>",unsafe_allow_html=True)
            draw_numbers(array, -1, -1, -1)
            note()
            st.title("Sorting step-by-step explanation:")
            merge_sort(array, draw_numbers)
        
        

if __name__ == "__main__":
    main()
    
