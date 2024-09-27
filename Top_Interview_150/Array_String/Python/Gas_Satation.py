class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0 # net gas from completing circuit
        curr_gas = 0 # net gas from current starting station
        starting_station = 0 # starting index

        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            curr_gas += gas[i] - cost[i]

            if curr_gas < 0:
                starting_station = i + 1 
                curr_gas = 0
        return starting_station if total_gas >= 0 else -1
