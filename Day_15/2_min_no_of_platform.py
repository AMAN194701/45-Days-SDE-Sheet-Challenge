class Solution:
    def countPlatforms(self, n, arr, dep):

        # Sort arrival and departure times separately
        arr.sort()
        dep.sort()

        # At least one platform is needed for the first train
        platforms_needed = 1

        # Stores the maximum platforms required at any time
        max_platforms = 1

        # i -> points to the next arriving train
        # j -> points to the next departing train
        i = 1
        j = 0

        # Process all trains
        while i < n and j < n:

            # If the next train arrives before the current train departs,
            # we need an extra platform
            if arr[i] <= dep[j]:
                platforms_needed += 1
                i += 1
            # Otherwise, a train has departed,
            # so one platform becomes free
            else:
                platforms_needed -= 1
                j += 1

            # update the maximum number of platforms needed
            max_platforms = max(max_platforms, platforms_needed)

        return max_platforms
arr = [900, 945, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130, 1150, 1900, 2000]

n = len(arr)
s1 = Solution()
print("Minimum number of platforms required:",
      s1.countPlatforms(n, arr, dep))