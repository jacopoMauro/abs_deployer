/**
 * Copyright (c) 2016, Jacopo Mauro. All rights reserved. 
 * This file is licensed under the terms of the ISC License.
 */

grammar DeclSpecLanguage;

// To generate files run antlr4 -Dlanguage=Python2 -visitor -no-listener


statement : b_expr EOF;

b_expr : b_term (bool_binary_op b_term )* ;

b_term : (unaryOp)? b_factor ;

b_factor : boolFact | relation ; 

relation : expr (comparison_op expr)? ;

expr : term (arith_binary_op term)* ;

term :
  (EXISTS | FORALL) variable 'in' typeV ':' b_expr    # AtermQuantifier |
  INT                                                 # AtermInt |
  objId                                               # AtermId |
  dcId '.' objId                                      # AtermDCObj |
  SUM variable 'in' typeV ':' expr                    # AtermSum |
  arith_unary_op expr                                 # AexprUnaryArithmetic |  
  '(' b_expr ')'                                      # AtermBrackets ;

typeV : OBJ | DC | RE;

dcId :
  ID                                # AdcIDID | // DC[0]
  variable                          # AdcIDVar |
  ID '[' INT ']'                    # AdcIDNum ;

objId :
  // default scenario 
  ID                              # AobjIDID |
  // variable to capture all the obj
  variable                        # AobjIDVar |
  // id with non default scenario
  ID '[' ID ']'                   # AobjIDScenario |
  ID '[' RE ']'                   # AobjIDRE ; 

variable : VARIABLE   # Avariable;
	
bool_binary_op : AND | OR | IMPL | IFF ;
arith_binary_op : PLUS | MINUS | TIMES ;
arith_unary_op : ABS ;

comparison_op : LEQ | EQ | GEQ | LT | GT | NEQ;
unaryOp : NOT;
boolFact : TRUE;

RE : '\'' ([a-zA-Z0-9_] | '-' | '*' | '\\' | '+' | '?' | '[' | ']' | '|' )+ '\''; 
  // match regular expression           

AND : 'and';
OR : 'or';
NOT : 'not';
TRUE : 'true';
FALSE : 'false';
IMPL: 'impl';
IFF: 'iff';
EXISTS: 'exists';
FORALL: 'forall';
SUM: 'sum';
COST: 'cost';

LEQ : '<=';
EQ : '=';
GEQ : '>=';
LT : '<';
GT : '>';
NEQ : '!=';

PLUS : '+';
MINUS : '-';
TIMES : '*';
ABS : 'abs';

OBJ: 'obj';
DC: 'DC';

VARIABLE : '?'[a-zA-Z_][a-zA-Z0-9_]*;
 
ID : [a-zA-Z_][a-zA-Z0-9_]* ;    // match letters, numbers, underscore
INT : [-]?[0-9]+ ;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
