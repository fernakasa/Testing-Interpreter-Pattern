"""
The Interpreter Pattern Concept
https://sbcode.net/python/interpreter/#interpreterinterpreter_conceptpy
"""
class AbstractExpression():
    """
    All Terminal and Non-Terminal expressions will implement
    an `interpret` method
    """
    @staticmethod
    def interpret():
        """
        The `interpret` method gets called recursively for each 
        AbstractExpression
        """
class Number(AbstractExpression):
    "Terminal Expression"
    def __init__(self, value):
        self.value = int(value)
    def interpret(self):
        return self.value
    def __repr__(self):
        return str(self.value)
class Add(AbstractExpression):
    "Non-Terminal Expression."
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def interpret(self):
        return self.left.interpret() + self.right.interpret()
    def __repr__(self):
        return f"({self.left} Add {self.right})"
class Subtract(AbstractExpression):
    "Non-Terminal Expression"
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def interpret(self):
        return self.left.interpret() - self.right.interpret()
    def __repr__(self):
        return f"({self.left} Subtract {self.right})"