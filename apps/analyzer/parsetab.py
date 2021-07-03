
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT ADD_ALL_FUNC AND ARROW AS ASIGDIV ASIGMINUS ASIGSUM ASIGTIMES ASSERT ASSIGN ASYNC AWAIT BOOLEAN BREAK CASE CATCH CLASS CLEAR_FUNC COMMA CONST CONTAINS_DICT_FUNC CONTAINS_FUNC CONTAINS_VALUE_FUNC CONTINUE DDOTS DIVISION DO DOT DOUBLE_TYPE DYNAMIC ELEMENTAT_FUNC ELSE ENDSWITH_FUNC ENUM EQ EQ_V EXPORT EXTENDS FALSE FINALLY FLOAT FOR FUNCTION GT GTE IDENT IF IMPLEMENTS INT INTERFACE INT_TYPE JOIN_FUNC LBRACE LBRACKET LIST LPAREN LT LTE MAP MINUS MINUSMINUS MOD NE NEGATION OR PLUS PLUSPLUS PRINT RBRACE RBRACKET REMOVE_FUNC RETURN RPAREN SEMICOLON SET STRING STRING_TYPE SUBSTRING_FUNC SUPER SWITCH TIMES TOSTRING_FUNC TRIM_FUNC TRUE TYPEDEF VAR VIR VOID WHILEbody : colstmsempty :nonColtypes : ifstm\n                 | elstm\n                 | whilestm\n\t\t             | forstmt\n                 | funccolstms : nonColtypes\n             | nonColtypes colstmscoltypes : idmap\n              | stringstm\n              | listfunc\n              | varfunc\n              | dicfunc\n              | stringfunc\n              | listassign\n              | operation\n              | siuprintcolstms : coltypes SEMICOLON\n             | coltypes SEMICOLON colstmssiuprint : PRINT LPAREN printable RPARENprintable : STRING\n               | IDENTifstm : ifelse LPAREN condition RPAREN LBRACE RBRACE\n           | ifelse LPAREN condition RPAREN LBRACE body RBRACEelstm : ELSE LBRACE body RBRACEifelse : IF\n            | ELSE IFwhilestm : WHILE LPAREN condition RPAREN LBRACE RBRACE\n            | WHILE LPAREN condition RPAREN LBRACE body RBRACEcondition : prepositioncondition : preposition operator prepositioncondition :  preposition operator preposition morecondmorecond : operator preposition\n              | operator preposition morecond\n  operator : EQ\n              | NE\n              | AND\n              | OR\n              | GT\n              | GTE\n              | LT\n              | LTE\n  preposition : typrepreposition : NEGATION typretypre : STRING\n           | INT\n           | TRUE\n           | FALSE\n           | FLOAT\n           | IDENT\n  idmap : tymap IDENT EQ_V dictionarytymap : MAP\n           | MAP LT tykey COMMA tyvalue GTtykey : STRING_TYPE\n           | DOUBLE_TYPE\n           | INT_TYPEtyvalue : STRING_TYPE\n             | DOUBLE_TYPE\n             | INT_TYPE\n             | BOOLEAN\n             | IDENT\n             | iterable\n             | tymapiterable : LIST\n              | SET\n              | STRINGstringstm : STRING_TYPE IDENT EQ_V STRINGdicfunc : dictionary DOT functiondictionary : LBRACE item RBRACEitem : key DDOTS value\n          | key DDOTS value COMMA itemkey : STRING\n         | INT\n         | FLOATvalue : STRING\n           | FLOAT\n           | INT\n           | FALSE\n           | TRUE\n           | IDENT\n           | iterable\n           | tymap\n           | listassigntypelistassign : VAR IDENT EQ_V list\n    listassign : LIST LT typedata GT IDENT EQ_V list\n    listassigntype : LIST LT typedata GT IDENT EQ_V list\n    typedata : INT_TYPE\n                | DOUBLE_TYPE\n                | BOOLEAN\n                | STRING_TYPE\n    retornable : INT_TYPE\n                | DOUBLE_TYPE\n                | BOOLEAN\n                | STRING_TYPE\n                | VOID\n                | LIST\n                | MAP\n                | SET\n  listassign : LIST IDENT EQ_V list\n    list : LBRACKET element RBRACKET \n    list : LBRACKET RBRACKET\n    element : typre\n    element : typre COMMA typre\n    element : typre COMMA typre moreelements\n    moreelements : COMMA typre\n                    | COMMA typre moreelements\n    forstmt : FOR LPAREN INT_TYPE assign SEMICOLON comparisonint SEMICOLON varincredecre RPAREN LBRACE RBRACE\n                | FOR LPAREN INT_TYPE assign SEMICOLON comparisonint SEMICOLON varincredecre RPAREN LBRACE body RBRACE\n    assign : IDENT EQ_V INT\n    comparisonint : IDENT comparisonop INT\n    varincredecre : incredecre IDENT\n                     | IDENT incredecre\n    incredecre : PLUSPLUS\n                  | MINUSMINUS\n    comparisonop : EQ\n                    | GT\n                    | GTE\n                    | LT\n                    | LTE\n                    | NE\n    func : retornable IDENT LPAREN param RPAREN LBRACE RBRACE\n          |  retornable IDENT LPAREN param RPAREN LBRACE body RBRACE \n          | retornable IDENT LPAREN RPAREN LBRACE RBRACE\n          |  retornable IDENT LPAREN RPAREN LBRACE body RBRACE\n  param : typedata IDENT\n  param : typedata IDENT COMMA typedata IDENT\n  param : typedata IDENT COMMA typedata IDENT moreparam\n  moreparam : COMMA typedata IDENT\n                | COMMA typedata IDENT moreparam\n  varfunc : IDENT DOT functionstringfunc : STRING DOT functionlistfunc : list DOT functionfunction : CLEAR_FUNC LPAREN RPARENfunction : ADD_ALL_FUNC LPAREN dictionary  RPARENfunction : CONTAINS_DICT_FUNC LPAREN key RPARENfunction : CONTAINS_VALUE_FUNC LPAREN value RPARENfunction : REMOVE_FUNC LPAREN STRING RPARENfunction : TOSTRING_FUNC LPAREN RPARENfunction : TRIM_FUNC LPAREN RPARENfunction : ENDSWITH_FUNC LPAREN STRING RPARENfunction : SUBSTRING_FUNC LPAREN INT RPARENfunction : SUBSTRING_FUNC LPAREN INT COMMA INT RPARENfunction : JOIN_FUNC LPAREN STRING RPARENfunction : CONTAINS_FUNC LPAREN  typre RPARENfunction : ELEMENTAT_FUNC LPAREN INT RPARENoperation : arit oparit arit\n  operation : LPAREN arit oparit arit RPAREN\n  operation : arit oparit arit moreArit\n  operation : LPAREN arit oparit arit moreAritP\n  moreArit : oparit arit\n              | oparit arit moreArit\n              | empty\n  moreAritP : oparit arit RPAREN\n               | oparit arit moreAritP\n               | empty\n  arit : FLOAT\n          | INT\n          | IDENT\n          | operation\n  oparit : PLUS\n            | MINUS\n            | TIMES\n            | DIVISION\n  '
    
_lr_action_items = {'ELSE':([0,3,5,6,7,8,9,47,57,159,189,197,201,229,236,241,242,259,266,275,277,291,301,303,306,],[22,22,-3,-4,-5,-6,-7,22,22,-26,22,22,22,-24,-29,22,-124,-25,-30,-122,-125,-123,22,-108,-109,]),'WHILE':([0,3,5,6,7,8,9,47,57,159,189,197,201,229,236,241,242,259,266,275,277,291,301,303,306,],[23,23,-3,-4,-5,-6,-7,23,23,-26,23,23,23,-24,-29,23,-124,-25,-30,-122,-125,-123,23,-108,-109,]),'FOR':([0,3,5,6,7,8,9,47,57,159,189,197,201,229,236,241,242,259,266,275,277,291,301,303,306,],[24,24,-3,-4,-5,-6,-7,24,24,-26,24,24,24,-24,-29,24,-124,-25,-30,-122,-125,-123,24,-108,-109,]),'STRING_TYPE':([0,3,5,6,7,8,9,47,57,69,77,98,159,187,189,196,197,201,229,236,241,242,244,259,266,275,277,291,298,301,303,306,],[30,30,-3,-4,-5,-6,-7,30,30,122,129,122,-26,218,30,122,30,30,-24,-29,30,-124,122,-25,-30,-122,-125,-123,122,30,-108,-109,]),'IDENT':([0,3,5,6,7,8,9,20,25,26,28,30,33,34,38,39,40,41,42,43,47,48,57,59,71,72,73,74,75,76,91,92,94,97,119,120,121,122,133,135,136,137,138,139,140,141,142,143,159,165,169,176,181,183,187,189,191,197,198,201,227,229,231,236,241,242,257,259,261,265,266,267,275,277,278,286,288,289,291,301,302,303,306,],[27,27,-3,-4,-5,-6,-7,50,-92,61,63,65,68,70,-93,-94,-96,-53,-99,86,27,86,27,86,50,-161,-162,-163,-164,127,86,50,152,162,-88,-89,-90,-91,86,86,-36,-37,-38,-39,-40,-41,-42,-43,-26,202,152,86,215,50,222,27,50,27,239,27,86,-24,86,-29,27,-124,-54,-25,50,284,-30,287,-122,-125,292,296,-114,-115,-123,27,305,-108,-109,]),'STRING':([0,3,5,6,7,8,9,21,43,47,48,57,59,76,91,94,114,133,135,136,137,138,139,140,141,142,143,159,168,169,170,173,175,176,187,189,195,197,201,227,229,231,236,241,242,259,266,275,277,291,301,303,306,],[31,31,-3,-4,-5,-6,-7,54,81,31,81,31,81,126,81,147,179,81,81,-36,-37,-38,-39,-40,-41,-42,-43,-26,54,147,207,210,212,81,226,31,54,31,31,81,-24,81,-29,31,-124,-25,-30,-122,-125,-123,31,-108,-109,]),'VAR':([0,3,5,6,7,8,9,47,57,159,189,197,201,229,236,241,242,259,266,275,277,291,301,303,306,],[33,33,-3,-4,-5,-6,-7,33,33,-26,33,33,33,-24,-29,33,-124,-25,-30,-122,-125,-123,33,-108,-109,]),'LIST':([0,3,5,6,7,8,9,47,57,94,159,169,187,189,197,201,229,236,241,242,259,266,275,277,291,301,303,306,],[34,34,-3,-4,-5,-6,-7,34,34,156,-26,156,225,34,34,34,-24,-29,34,-124,-25,-30,-122,-125,-123,34,-108,-109,]),'LPAREN':([0,3,5,6,7,8,9,19,20,23,24,36,37,47,57,58,61,71,72,73,74,75,92,100,101,102,103,104,105,106,107,108,109,110,111,159,183,189,191,197,201,229,236,241,242,259,261,266,275,277,291,301,303,306,],[20,20,-3,-4,-5,-6,-7,48,20,59,60,76,-27,20,20,-28,98,20,-161,-162,-163,-164,20,166,167,168,169,170,171,172,173,174,175,176,177,-26,20,20,20,20,20,-24,-29,20,-124,-25,20,-30,-122,-125,-123,20,-108,-109,]),'PRINT':([0,3,5,6,7,8,9,47,57,159,189,197,201,229,236,241,242,259,266,275,277,291,301,303,306,],[36,36,-3,-4,-5,-6,-7,36,36,-26,36,36,36,-24,-29,36,-124,-25,-30,-122,-125,-123,36,-108,-109,]),'IF':([0,3,5,6,7,8,9,22,47,57,159,189,197,201,229,236,241,242,259,266,275,277,291,301,303,306,],[37,37,-3,-4,-5,-6,-7,58,37,37,-26,37,37,37,-24,-29,37,-124,-25,-30,-122,-125,-123,37,-108,-109,]),'INT_TYPE':([0,3,5,6,7,8,9,47,57,60,69,77,98,159,187,189,196,197,201,229,236,241,242,244,259,266,275,277,291,298,301,303,306,],[25,25,-3,-4,-5,-6,-7,25,25,97,119,131,119,-26,220,25,119,25,25,-24,-29,25,-124,119,-25,-30,-122,-125,-123,119,25,-108,-109,]),'DOUBLE_TYPE':([0,3,5,6,7,8,9,47,57,69,77,98,159,187,189,196,197,201,229,236,241,242,244,259,266,275,277,291,298,301,303,306,],[38,38,-3,-4,-5,-6,-7,38,38,120,130,120,-26,219,38,120,38,38,-24,-29,38,-124,120,-25,-30,-122,-125,-123,120,38,-108,-109,]),'BOOLEAN':([0,3,5,6,7,8,9,47,57,69,98,159,187,189,196,197,201,229,236,241,242,244,259,266,275,277,291,298,301,303,306,],[39,39,-3,-4,-5,-6,-7,39,39,121,121,-26,221,39,121,39,39,-24,-29,39,-124,121,-25,-30,-122,-125,-123,121,39,-108,-109,]),'VOID':([0,3,5,6,7,8,9,47,57,159,189,197,201,229,236,241,242,259,266,275,277,291,301,303,306,],[40,40,-3,-4,-5,-6,-7,40,40,-26,40,40,40,-24,-29,40,-124,-25,-30,-122,-125,-123,40,-108,-109,]),'MAP':([0,3,5,6,7,8,9,47,57,94,159,169,187,189,197,201,229,236,241,242,259,266,275,277,291,301,303,306,],[41,41,-3,-4,-5,-6,-7,41,41,158,-26,158,158,41,41,41,-24,-29,41,-124,-25,-30,-122,-125,-123,41,-108,-109,]),'SET':([0,3,5,6,7,8,9,47,57,94,159,169,187,189,197,201,229,236,241,242,259,266,275,277,291,301,303,306,],[42,42,-3,-4,-5,-6,-7,42,42,157,-26,157,157,42,42,42,-24,-29,42,-124,-25,-30,-122,-125,-123,42,-108,-109,]),'LBRACKET':([0,3,5,6,7,8,9,47,57,117,123,159,189,197,201,229,236,241,242,255,259,266,275,277,291,294,301,303,306,],[43,43,-3,-4,-5,-6,-7,43,43,43,43,-26,43,43,43,-24,-29,43,-124,43,-25,-30,-122,-125,-123,43,43,-108,-109,]),'LBRACE':([0,3,5,6,7,8,9,22,47,57,112,134,159,160,164,167,189,197,200,201,229,236,241,242,259,266,275,277,291,295,301,303,306,],[21,21,-3,-4,-5,-6,-7,57,21,21,21,189,-26,197,201,21,21,21,241,21,-24,-29,21,-124,-25,-30,-122,-125,-123,301,21,-108,-109,]),'FLOAT':([0,3,5,6,7,8,9,20,21,43,47,48,57,59,71,72,73,74,75,91,92,94,133,135,136,137,138,139,140,141,142,143,159,168,169,176,183,189,191,195,197,201,227,229,231,236,241,242,259,261,266,275,277,291,301,303,306,],[44,44,-3,-4,-5,-6,-7,44,56,85,44,85,44,85,44,-161,-162,-163,-164,85,44,148,85,85,-36,-37,-38,-39,-40,-41,-42,-43,-26,56,148,85,44,44,44,56,44,44,85,-24,85,-29,44,-124,-25,44,-30,-122,-125,-123,44,-108,-109,]),'INT':([0,3,5,6,7,8,9,20,21,43,47,48,57,59,71,72,73,74,75,91,92,94,133,135,136,137,138,139,140,141,142,143,159,168,169,174,176,177,183,189,191,195,197,199,201,227,229,231,236,241,242,251,259,261,266,268,269,270,271,272,273,274,275,277,291,301,303,306,],[45,45,-3,-4,-5,-6,-7,45,55,82,45,82,45,82,45,-161,-162,-163,-164,82,45,149,82,82,-36,-37,-38,-39,-40,-41,-42,-43,-26,55,149,211,82,214,45,45,45,55,45,240,45,82,-24,82,-29,45,-124,279,-25,45,-30,290,-116,-117,-118,-119,-120,-121,-122,-125,-123,45,-108,-109,]),'$end':([1,2,3,5,6,7,8,9,46,47,87,159,229,236,242,259,266,275,277,291,303,306,],[0,-1,-8,-3,-4,-5,-6,-7,-9,-19,-20,-26,-24,-29,-124,-25,-30,-122,-125,-123,-108,-109,]),'RBRACE':([2,3,5,6,7,8,9,46,47,52,79,87,95,132,146,147,148,149,150,151,152,153,154,155,156,157,158,159,189,197,201,229,230,234,236,237,241,242,243,257,259,266,275,276,277,291,300,301,303,304,306,],[-1,-8,-3,-4,-5,-6,-7,-9,-19,93,-102,-20,159,-101,-71,-67,-77,-78,-79,-80,-81,-82,-83,-84,-65,-66,-53,-26,229,236,242,-24,259,-72,-29,266,275,-124,277,-54,-25,-30,-122,291,-125,-123,-87,303,-108,306,-109,]),'SEMICOLON':([4,10,11,12,13,14,15,16,17,18,44,45,50,51,79,93,99,113,115,116,124,132,145,161,178,179,180,182,184,185,186,192,193,194,203,208,209,216,233,238,240,245,246,247,248,249,250,252,253,254,256,262,263,264,280,283,290,293,],[47,-10,-11,-12,-13,-14,-15,-16,-17,-18,-157,-158,-159,-160,-102,-70,-131,-69,-132,-133,-2,-101,-2,198,-52,-68,-85,-100,-149,-153,-21,-148,-150,-153,-134,-139,-140,-2,-2,267,-110,-135,-136,-137,-138,-141,-142,-144,-145,-146,-149,-154,-155,-153,-86,-2,-111,-143,]),'PLUS':([17,27,35,44,45,49,50,51,124,145,184,185,192,193,194,216,233,256,262,263,264,283,],[-160,-159,72,-157,-158,72,-159,-160,72,72,-149,-153,-148,-150,-153,72,72,-149,-154,-155,-153,72,]),'MINUS':([17,27,35,44,45,49,50,51,124,145,184,185,192,193,194,216,233,256,262,263,264,283,],[-160,-159,73,-157,-158,73,-159,-160,73,73,-149,-153,-148,-150,-153,73,73,-149,-154,-155,-153,73,]),'TIMES':([17,27,35,44,45,49,50,51,124,145,184,185,192,193,194,216,233,256,262,263,264,283,],[-160,-159,74,-157,-158,74,-159,-160,74,74,-149,-153,-148,-150,-153,74,74,-149,-154,-155,-153,74,]),'DIVISION':([17,27,35,44,45,49,50,51,124,145,184,185,192,193,194,216,233,256,262,263,264,283,],[-160,-159,75,-157,-158,75,-159,-160,75,75,-149,-153,-148,-150,-153,75,75,-149,-154,-155,-153,75,]),'DOT':([27,29,31,32,79,93,132,],[62,64,66,67,-102,-70,-101,]),'LT':([34,41,81,82,83,84,85,86,89,90,144,156,158,190,239,260,],[69,77,-46,-47,-48,-49,-50,-51,142,-44,-45,196,77,142,272,142,]),'RBRACKET':([43,78,80,81,82,83,84,85,86,188,228,258,281,],[79,132,-103,-46,-47,-48,-49,-50,-51,-104,-105,-106,-107,]),'TRUE':([43,48,59,91,94,133,135,136,137,138,139,140,141,142,143,169,176,227,231,],[83,83,83,83,151,83,83,-36,-37,-38,-39,-40,-41,-42,-43,151,83,83,83,]),'FALSE':([43,48,59,91,94,133,135,136,137,138,139,140,141,142,143,169,176,227,231,],[84,84,84,84,150,84,84,-36,-37,-38,-39,-40,-41,-42,-43,150,84,84,84,]),'RPAREN':([44,45,50,51,54,55,56,79,81,82,83,84,85,86,88,89,90,93,96,98,125,126,127,132,144,145,147,148,149,150,151,152,153,154,155,156,157,158,163,166,171,172,190,192,193,194,202,204,205,206,207,210,211,212,213,214,232,233,256,257,260,262,263,264,279,282,283,285,288,289,292,296,297,299,300,305,307,],[-157,-158,-159,-160,-73,-74,-75,-102,-46,-47,-48,-49,-50,-51,134,-31,-44,-70,160,164,186,-22,-23,-101,-45,192,-67,-77,-78,-79,-80,-81,-82,-83,-84,-65,-66,-53,200,203,208,209,-32,-148,-150,-153,-126,245,246,247,248,249,250,252,253,254,-33,262,-149,-54,-34,-154,-155,-153,293,-35,262,295,-114,-115,-127,-112,-113,-128,-87,-129,-130,]),'NEGATION':([48,59,135,136,137,138,139,140,141,142,143,231,],[91,91,91,-36,-37,-38,-39,-40,-41,-42,-43,91,]),'DDOTS':([53,54,55,56,],[94,-73,-74,-75,]),'CLEAR_FUNC':([62,64,66,67,],[100,100,100,100,]),'ADD_ALL_FUNC':([62,64,66,67,],[101,101,101,101,]),'CONTAINS_DICT_FUNC':([62,64,66,67,],[102,102,102,102,]),'CONTAINS_VALUE_FUNC':([62,64,66,67,],[103,103,103,103,]),'REMOVE_FUNC':([62,64,66,67,],[104,104,104,104,]),'TOSTRING_FUNC':([62,64,66,67,],[105,105,105,105,]),'TRIM_FUNC':([62,64,66,67,],[106,106,106,106,]),'ENDSWITH_FUNC':([62,64,66,67,],[107,107,107,107,]),'SUBSTRING_FUNC':([62,64,66,67,],[108,108,108,108,]),'JOIN_FUNC':([62,64,66,67,],[109,109,109,109,]),'CONTAINS_FUNC':([62,64,66,67,],[110,110,110,110,]),'ELEMENTAT_FUNC':([62,64,66,67,],[111,111,111,111,]),'EQ_V':([63,65,68,70,162,215,284,],[112,114,117,123,199,255,294,]),'COMMA':([79,80,81,82,83,84,85,86,128,129,130,131,132,146,147,148,149,150,151,152,153,154,155,156,157,158,188,202,211,257,258,292,300,305,],[-102,133,-46,-47,-48,-49,-50,-51,187,-55,-56,-57,-101,195,-67,-77,-78,-79,-80,-81,-82,-83,-84,-65,-66,-53,227,244,251,-54,227,298,-87,298,]),'EQ':([81,82,83,84,85,86,89,90,144,190,239,260,],[-46,-47,-48,-49,-50,-51,136,-44,-45,136,269,136,]),'NE':([81,82,83,84,85,86,89,90,144,190,239,260,],[-46,-47,-48,-49,-50,-51,137,-44,-45,137,274,137,]),'AND':([81,82,83,84,85,86,89,90,144,190,260,],[-46,-47,-48,-49,-50,-51,138,-44,-45,138,138,]),'OR':([81,82,83,84,85,86,89,90,144,190,260,],[-46,-47,-48,-49,-50,-51,139,-44,-45,139,139,]),'GT':([81,82,83,84,85,86,89,90,118,119,120,121,122,144,157,158,190,217,218,219,220,221,222,223,224,225,226,235,239,257,260,],[-46,-47,-48,-49,-50,-51,140,-44,181,-88,-89,-90,-91,-45,-66,-53,140,257,-58,-59,-60,-61,-62,-63,-64,-65,-67,265,270,-54,140,]),'GTE':([81,82,83,84,85,86,89,90,144,190,239,260,],[-46,-47,-48,-49,-50,-51,141,-44,-45,141,271,141,]),'LTE':([81,82,83,84,85,86,89,90,144,190,239,260,],[-46,-47,-48,-49,-50,-51,143,-44,-45,143,273,143,]),'PLUSPLUS':([267,287,],[288,288,]),'MINUSMINUS':([267,287,],[289,289,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'body':([0,57,189,197,201,241,301,],[1,95,230,237,243,276,304,]),'colstms':([0,3,47,57,189,197,201,241,301,],[2,46,87,2,2,2,2,2,2,]),'nonColtypes':([0,3,47,57,189,197,201,241,301,],[3,3,3,3,3,3,3,3,3,]),'coltypes':([0,3,47,57,189,197,201,241,301,],[4,4,4,4,4,4,4,4,4,]),'ifstm':([0,3,47,57,189,197,201,241,301,],[5,5,5,5,5,5,5,5,5,]),'elstm':([0,3,47,57,189,197,201,241,301,],[6,6,6,6,6,6,6,6,6,]),'whilestm':([0,3,47,57,189,197,201,241,301,],[7,7,7,7,7,7,7,7,7,]),'forstmt':([0,3,47,57,189,197,201,241,301,],[8,8,8,8,8,8,8,8,8,]),'func':([0,3,47,57,189,197,201,241,301,],[9,9,9,9,9,9,9,9,9,]),'idmap':([0,3,47,57,189,197,201,241,301,],[10,10,10,10,10,10,10,10,10,]),'stringstm':([0,3,47,57,189,197,201,241,301,],[11,11,11,11,11,11,11,11,11,]),'listfunc':([0,3,47,57,189,197,201,241,301,],[12,12,12,12,12,12,12,12,12,]),'varfunc':([0,3,47,57,189,197,201,241,301,],[13,13,13,13,13,13,13,13,13,]),'dicfunc':([0,3,47,57,189,197,201,241,301,],[14,14,14,14,14,14,14,14,14,]),'stringfunc':([0,3,47,57,189,197,201,241,301,],[15,15,15,15,15,15,15,15,15,]),'listassign':([0,3,47,57,189,197,201,241,301,],[16,16,16,16,16,16,16,16,16,]),'operation':([0,3,20,47,57,71,92,183,189,191,197,201,241,261,301,],[17,17,51,17,17,51,51,51,17,51,17,17,17,51,17,]),'siuprint':([0,3,47,57,189,197,201,241,301,],[18,18,18,18,18,18,18,18,18,]),'ifelse':([0,3,47,57,189,197,201,241,301,],[19,19,19,19,19,19,19,19,19,]),'retornable':([0,3,47,57,189,197,201,241,301,],[26,26,26,26,26,26,26,26,26,]),'tymap':([0,3,47,57,94,169,187,189,197,201,241,301,],[28,28,28,28,154,154,224,28,28,28,28,28,]),'dictionary':([0,3,47,57,112,167,189,197,201,241,301,],[29,29,29,29,178,204,29,29,29,29,29,]),'list':([0,3,47,57,117,123,189,197,201,241,255,294,301,],[32,32,32,32,180,182,32,32,32,32,280,300,32,]),'arit':([0,3,20,47,57,71,92,183,189,191,197,201,241,261,301,],[35,35,49,35,35,124,145,216,35,233,35,35,35,283,35,]),'item':([21,195,],[52,234,]),'key':([21,168,195,],[53,205,53,]),'oparit':([35,49,124,145,216,233,283,],[71,92,183,191,183,261,261,]),'element':([43,],[78,]),'typre':([43,48,59,91,133,135,176,227,231,],[80,90,90,144,188,90,213,258,90,]),'condition':([48,59,],[88,96,]),'preposition':([48,59,135,231,],[89,89,190,260,]),'function':([62,64,66,67,],[99,113,115,116,]),'typedata':([69,98,196,244,298,],[118,165,235,278,302,]),'printable':([76,],[125,]),'tykey':([77,],[128,]),'operator':([89,190,260,],[135,231,231,]),'value':([94,169,],[146,206,]),'iterable':([94,169,187,],[153,153,223,]),'listassigntype':([94,169,],[155,155,]),'assign':([97,],[161,]),'param':([98,],[163,]),'moreArit':([124,145,216,233,283,],[184,184,256,256,256,]),'empty':([124,145,216,233,283,],[185,194,185,264,264,]),'moreAritP':([145,233,283,],[193,263,263,]),'tyvalue':([187,],[217,]),'moreelements':([188,258,],[228,281,]),'morecond':([190,260,],[232,282,]),'comparisonint':([198,],[238,]),'comparisonop':([239,],[268,]),'varincredecre':([267,],[285,]),'incredecre':([267,287,],[286,297,]),'moreparam':([292,305,],[299,307,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> body","S'",1,None,None,None),
  ('body -> colstms','body',1,'p_body','yacc.py',5),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',8),
  ('nonColtypes -> ifstm','nonColtypes',1,'p_nonColtypes','yacc.py',12),
  ('nonColtypes -> elstm','nonColtypes',1,'p_nonColtypes','yacc.py',13),
  ('nonColtypes -> whilestm','nonColtypes',1,'p_nonColtypes','yacc.py',14),
  ('nonColtypes -> forstmt','nonColtypes',1,'p_nonColtypes','yacc.py',15),
  ('nonColtypes -> func','nonColtypes',1,'p_nonColtypes','yacc.py',16),
  ('colstms -> nonColtypes','colstms',1,'p_colstms_no','yacc.py',19),
  ('colstms -> nonColtypes colstms','colstms',2,'p_colstms_no','yacc.py',20),
  ('coltypes -> idmap','coltypes',1,'p_coltypes','yacc.py',23),
  ('coltypes -> stringstm','coltypes',1,'p_coltypes','yacc.py',24),
  ('coltypes -> listfunc','coltypes',1,'p_coltypes','yacc.py',25),
  ('coltypes -> varfunc','coltypes',1,'p_coltypes','yacc.py',26),
  ('coltypes -> dicfunc','coltypes',1,'p_coltypes','yacc.py',27),
  ('coltypes -> stringfunc','coltypes',1,'p_coltypes','yacc.py',28),
  ('coltypes -> listassign','coltypes',1,'p_coltypes','yacc.py',29),
  ('coltypes -> operation','coltypes',1,'p_coltypes','yacc.py',30),
  ('coltypes -> siuprint','coltypes',1,'p_coltypes','yacc.py',31),
  ('colstms -> coltypes SEMICOLON','colstms',2,'p_colstms','yacc.py',34),
  ('colstms -> coltypes SEMICOLON colstms','colstms',3,'p_colstms','yacc.py',35),
  ('siuprint -> PRINT LPAREN printable RPAREN','siuprint',4,'p_siuprint','yacc.py',38),
  ('printable -> STRING','printable',1,'p_printable','yacc.py',41),
  ('printable -> IDENT','printable',1,'p_printable','yacc.py',42),
  ('ifstm -> ifelse LPAREN condition RPAREN LBRACE RBRACE','ifstm',6,'p_ifstm','yacc.py',45),
  ('ifstm -> ifelse LPAREN condition RPAREN LBRACE body RBRACE','ifstm',7,'p_ifstm','yacc.py',46),
  ('elstm -> ELSE LBRACE body RBRACE','elstm',4,'p_elstm','yacc.py',49),
  ('ifelse -> IF','ifelse',1,'p_ifelse','yacc.py',52),
  ('ifelse -> ELSE IF','ifelse',2,'p_ifelse','yacc.py',53),
  ('whilestm -> WHILE LPAREN condition RPAREN LBRACE RBRACE','whilestm',6,'p_whilestm','yacc.py',56),
  ('whilestm -> WHILE LPAREN condition RPAREN LBRACE body RBRACE','whilestm',7,'p_whilestm','yacc.py',57),
  ('condition -> preposition','condition',1,'p_condition_single','yacc.py',60),
  ('condition -> preposition operator preposition','condition',3,'p_condition','yacc.py',63),
  ('condition -> preposition operator preposition morecond','condition',4,'p_condition_more','yacc.py',66),
  ('morecond -> operator preposition','morecond',2,'p_morecond','yacc.py',69),
  ('morecond -> operator preposition morecond','morecond',3,'p_morecond','yacc.py',70),
  ('operator -> EQ','operator',1,'p_operator','yacc.py',74),
  ('operator -> NE','operator',1,'p_operator','yacc.py',75),
  ('operator -> AND','operator',1,'p_operator','yacc.py',76),
  ('operator -> OR','operator',1,'p_operator','yacc.py',77),
  ('operator -> GT','operator',1,'p_operator','yacc.py',78),
  ('operator -> GTE','operator',1,'p_operator','yacc.py',79),
  ('operator -> LT','operator',1,'p_operator','yacc.py',80),
  ('operator -> LTE','operator',1,'p_operator','yacc.py',81),
  ('preposition -> typre','preposition',1,'p_preposition','yacc.py',85),
  ('preposition -> NEGATION typre','preposition',2,'p_preposition_not','yacc.py',88),
  ('typre -> STRING','typre',1,'p_typre','yacc.py',91),
  ('typre -> INT','typre',1,'p_typre','yacc.py',92),
  ('typre -> TRUE','typre',1,'p_typre','yacc.py',93),
  ('typre -> FALSE','typre',1,'p_typre','yacc.py',94),
  ('typre -> FLOAT','typre',1,'p_typre','yacc.py',95),
  ('typre -> IDENT','typre',1,'p_typre','yacc.py',96),
  ('idmap -> tymap IDENT EQ_V dictionary','idmap',4,'p_idmap','yacc.py',100),
  ('tymap -> MAP','tymap',1,'p_tymap','yacc.py',103),
  ('tymap -> MAP LT tykey COMMA tyvalue GT','tymap',6,'p_tymap','yacc.py',104),
  ('tykey -> STRING_TYPE','tykey',1,'p_tykey','yacc.py',107),
  ('tykey -> DOUBLE_TYPE','tykey',1,'p_tykey','yacc.py',108),
  ('tykey -> INT_TYPE','tykey',1,'p_tykey','yacc.py',109),
  ('tyvalue -> STRING_TYPE','tyvalue',1,'p_tyvalue','yacc.py',112),
  ('tyvalue -> DOUBLE_TYPE','tyvalue',1,'p_tyvalue','yacc.py',113),
  ('tyvalue -> INT_TYPE','tyvalue',1,'p_tyvalue','yacc.py',114),
  ('tyvalue -> BOOLEAN','tyvalue',1,'p_tyvalue','yacc.py',115),
  ('tyvalue -> IDENT','tyvalue',1,'p_tyvalue','yacc.py',116),
  ('tyvalue -> iterable','tyvalue',1,'p_tyvalue','yacc.py',117),
  ('tyvalue -> tymap','tyvalue',1,'p_tyvalue','yacc.py',118),
  ('iterable -> LIST','iterable',1,'p_iterable','yacc.py',121),
  ('iterable -> SET','iterable',1,'p_iterable','yacc.py',122),
  ('iterable -> STRING','iterable',1,'p_iterable','yacc.py',123),
  ('stringstm -> STRING_TYPE IDENT EQ_V STRING','stringstm',4,'p_string','yacc.py',126),
  ('dicfunc -> dictionary DOT function','dicfunc',3,'p_dicfunc','yacc.py',129),
  ('dictionary -> LBRACE item RBRACE','dictionary',3,'p_dictionary','yacc.py',132),
  ('item -> key DDOTS value','item',3,'p_item','yacc.py',135),
  ('item -> key DDOTS value COMMA item','item',5,'p_item','yacc.py',136),
  ('key -> STRING','key',1,'p_key','yacc.py',139),
  ('key -> INT','key',1,'p_key','yacc.py',140),
  ('key -> FLOAT','key',1,'p_key','yacc.py',141),
  ('value -> STRING','value',1,'p_value','yacc.py',144),
  ('value -> FLOAT','value',1,'p_value','yacc.py',145),
  ('value -> INT','value',1,'p_value','yacc.py',146),
  ('value -> FALSE','value',1,'p_value','yacc.py',147),
  ('value -> TRUE','value',1,'p_value','yacc.py',148),
  ('value -> IDENT','value',1,'p_value','yacc.py',149),
  ('value -> iterable','value',1,'p_value','yacc.py',150),
  ('value -> tymap','value',1,'p_value','yacc.py',151),
  ('value -> listassigntype','value',1,'p_value','yacc.py',152),
  ('listassign -> VAR IDENT EQ_V list','listassign',4,'p_listassign','yacc.py',155),
  ('listassign -> LIST LT typedata GT IDENT EQ_V list','listassign',7,'p_listassign_diamonds','yacc.py',159),
  ('listassigntype -> LIST LT typedata GT IDENT EQ_V list','listassigntype',7,'p_listassigntype','yacc.py',163),
  ('typedata -> INT_TYPE','typedata',1,'p_typedata','yacc.py',167),
  ('typedata -> DOUBLE_TYPE','typedata',1,'p_typedata','yacc.py',168),
  ('typedata -> BOOLEAN','typedata',1,'p_typedata','yacc.py',169),
  ('typedata -> STRING_TYPE','typedata',1,'p_typedata','yacc.py',170),
  ('retornable -> INT_TYPE','retornable',1,'p_retornable','yacc.py',174),
  ('retornable -> DOUBLE_TYPE','retornable',1,'p_retornable','yacc.py',175),
  ('retornable -> BOOLEAN','retornable',1,'p_retornable','yacc.py',176),
  ('retornable -> STRING_TYPE','retornable',1,'p_retornable','yacc.py',177),
  ('retornable -> VOID','retornable',1,'p_retornable','yacc.py',178),
  ('retornable -> LIST','retornable',1,'p_retornable','yacc.py',179),
  ('retornable -> MAP','retornable',1,'p_retornable','yacc.py',180),
  ('retornable -> SET','retornable',1,'p_retornable','yacc.py',181),
  ('listassign -> LIST IDENT EQ_V list','listassign',4,'p_listassign_list','yacc.py',185),
  ('list -> LBRACKET element RBRACKET','list',3,'p_list','yacc.py',189),
  ('list -> LBRACKET RBRACKET','list',2,'p_list_void','yacc.py',192),
  ('element -> typre','element',1,'p_element_single','yacc.py',196),
  ('element -> typre COMMA typre','element',3,'p_element','yacc.py',199),
  ('element -> typre COMMA typre moreelements','element',4,'p_element_more','yacc.py',203),
  ('moreelements -> COMMA typre','moreelements',2,'p_moreelements','yacc.py',207),
  ('moreelements -> COMMA typre moreelements','moreelements',3,'p_moreelements','yacc.py',208),
  ('forstmt -> FOR LPAREN INT_TYPE assign SEMICOLON comparisonint SEMICOLON varincredecre RPAREN LBRACE RBRACE','forstmt',11,'p_forstmt','yacc.py',212),
  ('forstmt -> FOR LPAREN INT_TYPE assign SEMICOLON comparisonint SEMICOLON varincredecre RPAREN LBRACE body RBRACE','forstmt',12,'p_forstmt','yacc.py',213),
  ('assign -> IDENT EQ_V INT','assign',3,'p_assign','yacc.py',217),
  ('comparisonint -> IDENT comparisonop INT','comparisonint',3,'p_comparisonint','yacc.py',221),
  ('varincredecre -> incredecre IDENT','varincredecre',2,'p_varincredecre','yacc.py',225),
  ('varincredecre -> IDENT incredecre','varincredecre',2,'p_varincredecre','yacc.py',226),
  ('incredecre -> PLUSPLUS','incredecre',1,'p_incredecre','yacc.py',230),
  ('incredecre -> MINUSMINUS','incredecre',1,'p_incredecre','yacc.py',231),
  ('comparisonop -> EQ','comparisonop',1,'p_comparisonop','yacc.py',235),
  ('comparisonop -> GT','comparisonop',1,'p_comparisonop','yacc.py',236),
  ('comparisonop -> GTE','comparisonop',1,'p_comparisonop','yacc.py',237),
  ('comparisonop -> LT','comparisonop',1,'p_comparisonop','yacc.py',238),
  ('comparisonop -> LTE','comparisonop',1,'p_comparisonop','yacc.py',239),
  ('comparisonop -> NE','comparisonop',1,'p_comparisonop','yacc.py',240),
  ('func -> retornable IDENT LPAREN param RPAREN LBRACE RBRACE','func',7,'p_func','yacc.py',244),
  ('func -> retornable IDENT LPAREN param RPAREN LBRACE body RBRACE','func',8,'p_func','yacc.py',245),
  ('func -> retornable IDENT LPAREN RPAREN LBRACE RBRACE','func',6,'p_func','yacc.py',246),
  ('func -> retornable IDENT LPAREN RPAREN LBRACE body RBRACE','func',7,'p_func','yacc.py',247),
  ('param -> typedata IDENT','param',2,'p_param_single','yacc.py',251),
  ('param -> typedata IDENT COMMA typedata IDENT','param',5,'p_param','yacc.py',255),
  ('param -> typedata IDENT COMMA typedata IDENT moreparam','param',6,'p_param_more','yacc.py',259),
  ('moreparam -> COMMA typedata IDENT','moreparam',3,'p_more_params','yacc.py',263),
  ('moreparam -> COMMA typedata IDENT moreparam','moreparam',4,'p_more_params','yacc.py',264),
  ('varfunc -> IDENT DOT function','varfunc',3,'p_varfunc','yacc.py',268),
  ('stringfunc -> STRING DOT function','stringfunc',3,'p_stringfunc','yacc.py',271),
  ('listfunc -> list DOT function','listfunc',3,'p_listfunc','yacc.py',274),
  ('function -> CLEAR_FUNC LPAREN RPAREN','function',3,'p_function_clear','yacc.py',277),
  ('function -> ADD_ALL_FUNC LPAREN dictionary RPAREN','function',4,'p_function_addAll','yacc.py',280),
  ('function -> CONTAINS_DICT_FUNC LPAREN key RPAREN','function',4,'p_function_containsKey','yacc.py',283),
  ('function -> CONTAINS_VALUE_FUNC LPAREN value RPAREN','function',4,'p_function_containsValue','yacc.py',286),
  ('function -> REMOVE_FUNC LPAREN STRING RPAREN','function',4,'p_function_remove','yacc.py',289),
  ('function -> TOSTRING_FUNC LPAREN RPAREN','function',3,'p_function_tostring','yacc.py',292),
  ('function -> TRIM_FUNC LPAREN RPAREN','function',3,'p_function_trim','yacc.py',295),
  ('function -> ENDSWITH_FUNC LPAREN STRING RPAREN','function',4,'p_function_endsWith','yacc.py',298),
  ('function -> SUBSTRING_FUNC LPAREN INT RPAREN','function',4,'p_function_substring','yacc.py',301),
  ('function -> SUBSTRING_FUNC LPAREN INT COMMA INT RPAREN','function',6,'p_function_substring_2','yacc.py',304),
  ('function -> JOIN_FUNC LPAREN STRING RPAREN','function',4,'p_function_join','yacc.py',307),
  ('function -> CONTAINS_FUNC LPAREN typre RPAREN','function',4,'p_function_contains','yacc.py',310),
  ('function -> ELEMENTAT_FUNC LPAREN INT RPAREN','function',4,'p_function_elementat','yacc.py',313),
  ('operation -> arit oparit arit','operation',3,'p_operation','yacc.py',316),
  ('operation -> LPAREN arit oparit arit RPAREN','operation',5,'p_operation_p','yacc.py',320),
  ('operation -> arit oparit arit moreArit','operation',4,'p_operation_m','yacc.py',324),
  ('operation -> LPAREN arit oparit arit moreAritP','operation',5,'p_operation_mp','yacc.py',328),
  ('moreArit -> oparit arit','moreArit',2,'p_moreArit','yacc.py',332),
  ('moreArit -> oparit arit moreArit','moreArit',3,'p_moreArit','yacc.py',333),
  ('moreArit -> empty','moreArit',1,'p_moreArit','yacc.py',334),
  ('moreAritP -> oparit arit RPAREN','moreAritP',3,'p_moreAritP','yacc.py',338),
  ('moreAritP -> oparit arit moreAritP','moreAritP',3,'p_moreAritP','yacc.py',339),
  ('moreAritP -> empty','moreAritP',1,'p_moreAritP','yacc.py',340),
  ('arit -> FLOAT','arit',1,'p_arit','yacc.py',344),
  ('arit -> INT','arit',1,'p_arit','yacc.py',345),
  ('arit -> IDENT','arit',1,'p_arit','yacc.py',346),
  ('arit -> operation','arit',1,'p_arit','yacc.py',347),
  ('oparit -> PLUS','oparit',1,'p_oparit','yacc.py',351),
  ('oparit -> MINUS','oparit',1,'p_oparit','yacc.py',352),
  ('oparit -> TIMES','oparit',1,'p_oparit','yacc.py',353),
  ('oparit -> DIVISION','oparit',1,'p_oparit','yacc.py',354),
]
