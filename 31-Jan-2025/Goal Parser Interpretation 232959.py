# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

  def interpret(self, command: str) -> str:
        res=command.replace("()","o").replace("(al)","al")
        return res
        