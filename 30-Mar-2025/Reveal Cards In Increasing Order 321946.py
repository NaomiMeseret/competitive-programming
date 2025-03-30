# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res=[0]*len(deck)
        queue=deque(range(len(deck)))
        for n in deck:
            i=queue.popleft()
            res[i]=n
            if queue:
                queue.append(queue.popleft())
        return res


        
        

        