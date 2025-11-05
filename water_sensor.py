import heapq

def streaming_median(nums):
    if not nums:
        return []

    # Two heaps: low (max-heap via negatives), high (min-heap)
    low, high = [], []
    result = []

    for num in nums:
        # Insert into appropriate heap
        if not low or num <= -low[0]:
            heapq.heappush(low, -num)
        else:
            heapq.heappush(high, num)

        # Balance heaps: len(low) >= len(high) and difference ≤ 1
        if len(low) > len(high) + 1:
            heapq.heappush(high, -heapq.heappop(low))
        elif len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))

        # Compute median
        if len(low) == len(high):
            median = (-low[0] + high[0]) / 2.0
        else:
            median = -low[0]

        result.append(median)

    return result