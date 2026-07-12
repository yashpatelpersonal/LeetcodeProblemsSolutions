class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # If array is empty, return empty list
        if not arr:
            return []

        # Step 1: Sort unique values
        # Using set() removes duplicates → reduces memory and speeds up sorting
        sorted_unique = sorted(set(arr))

        # Step 2: Assign rank to each unique value
        # Rank starts at 1, so we use i + 1
        rank = {value: i + 1 for i, value in enumerate(sorted_unique)}

        # Step 3: Replace each element in arr with its rank
        # Lookup is O(1) because rank is a dictionary
        return [rank[value] for value in arr]