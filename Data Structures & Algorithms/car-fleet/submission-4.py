class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleet = 0    
        current_time = 0
        for pos, spd in cars:         
            # 当前车单独到达终点需要的时间         
            time = (target - pos) / spd          
            # 当前车比前面的车队慢，追不上，形成新车队         
            if time > current_time:             
                fleet += 1             
                current_time = time 
        
            # 如果 time <= current_time         
            # 说明它会追上前面的车队，不增加fleet
        return fleet
        