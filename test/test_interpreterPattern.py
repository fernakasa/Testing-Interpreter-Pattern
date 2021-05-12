import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from src.interpreterPattern import Number, Add, Subtract

def test_interpreterPattern():
    # The Client
    # The sentence complies with a simple grammar of
    # Number -> Operator -> Number -> etc,
    SENTENCE = "5 + 4 - 3 + 7 - 2"
    print(SENTENCE)
    # Split the sentence into individual expressions that will be added 
    # to an Abstract Syntax Tree (AST) as Terminal and Non-Terminal 
    # expressions
    TOKENS = SENTENCE.split(" ")
    print(TOKENS)
    # Manually Creating an Abstract Syntax Tree from the tokens
    AST: list[AbstractExpression] = []  # A list of AbstractExpressions
    # 5 + 4
    AST.append(Add(Number(TOKENS[0]), Number(TOKENS[2])))
    # ^ - 3
    AST.append(Subtract(AST[0], Number(TOKENS[4])))
    # ^ + 7
    AST.append(Add(AST[1], Number(TOKENS[6])))
    # ^ - 2
    AST.append(Subtract(AST[2], Number(TOKENS[8])))
    # Use the final AST row as the root node.
    AST_ROOT = AST.pop()
    # Interpret recursively through the full AST starting from the root.
    print(AST_ROOT.interpret())
    # Print out a representation of the AST_ROOT
    print(AST_ROOT)

    assert "((((5 Add 4) Subtract 3) Add 7) Subtract 2)" == str(AST_ROOT)