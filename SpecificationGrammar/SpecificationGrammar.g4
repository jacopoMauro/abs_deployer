grammar SpecificationGrammar;

// Resource constraints should be added only inside DC

spec :
	spec bool2Op spec 	# AspecBool2Op |
	bool1Op spec 		# AspecBool1Op |
	'(' spec ')' 		# AspecBrackets |
	boolFact			# AspecBoolFact |
	expr op expr		# AspecOp ;
	
expr :
  'DC[' resourceFilter '|'  specNoDC ']' 	# AexprDC |
  'DC['  specNoDC ']' 						# AexprDCNoFilter |
  expr arithmetic_op expr					# AexprArithmetic |
  exprNoDC									# AexprNoDC ;

resourceFilter :
  ID op INT 								# AresourceFilterOp	|
  resourceFilter ';' resourceFilter		# AresourceFilterBool2Op ;
	 
specNoDC:
	specNoDC bool2Op specNoDC 	# AspecNoDCBool2Op |
	bool1Op specNoDC 			# AspecNoDCBool1Op |
	'(' specNoDC ')' 			# AspecNoDCBrackets |
	boolFact 					# AspecNoDCBoolFact |
	exprNoDC op exprNoDC 		# AspecNoDCOp ;

exprNoDC :
  INT 						# AexprNoDCInt	|
  'INTERFACE[' ID ']' 		# AexprNoDCInterface	|
  'CLASS[' ID ':' ID ']'	# AexprNoDCClassScenario	|
  'CLASS[' ID ']'		    # AexprNoDCClass ;
	
op : LEQ | EQ | GEQ | LT | GT | NEQ ;

arithmetic_op : PLUS | MINUS | TIMES ;

bool2Op : AND | OR;
bool1Op : NOT;
boolFact : TRUE;

AND : 'and';
OR : 'or';
NOT : 'not';
TRUE : 'true';
FALSE : 'false';

LEQ : '<=';
EQ : '=';
GEQ : '>=';
LT : '<';
GT : '>';
NEQ : '!=';

PLUS : '+';
MINUS : '-';
TIMES : '*';
      
ID : [a-zA-Z_][a-zA-Z0-9._]+ ;    // match letters, numbers, dot, underscore
INT : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
