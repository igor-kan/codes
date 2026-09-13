{- ==============================================================================
 - File: languages/22_haskell/MonadicParser.hs
 - Language: Haskell (Pure Functional Programming & Category Theory)
 - Domain: Monadic Parser Combinators & Abstract Syntax Tree Compilation
 - Algorithm: Hutton-Meijer Parser Combinator Library for Arithmetic Expressions
 -
 - Rationale & Language Fit:
 -   Haskell is the definitive pure functional language, pioneering algebraic
 -   data types, typeclasses (Functor, Applicative, Monad, Alternative), and
 -   monadic composition. Monadic parser combinators (originating in Graham
 -   Hutton and Erik Meijer's seminal work) demonstrate how domain-specific
 -   grammars can be constructed from tiny, modular, referentially transparent
 -   building blocks without external lexer/parser generators like Lex/Yacc.
 - ============================================================================== -}

module Main where

import Control.Applicative
import Data.Char (isDigit, isSpace)

-- ==============================================================================
-- Monadic Parser Type Definition
-- A Parser is a function that takes an input String and returns a list of
-- candidate parses: [(parsed_result, remaining_unconsumed_string)]
-- ==============================================================================

newtype Parser a = Parser { runParser :: String -> [(a, String)] }

-- 1. Functor Instance
instance Functor Parser where
  fmap f (Parser p) = Parser (\input -> [(f x, rest) | (x, rest) <- p input])

-- 2. Applicative Instance
instance Applicative Parser where
  pure x = Parser (\input -> [(x, input)])
  (Parser pf) <*> (Parser px) = Parser (\input ->
    [(f x, rest2) | (f, rest1) <- pf input, (x, rest2) <- px rest1])

-- 3. Monad Instance
instance Monad Parser where
  (Parser p) >>= f = Parser (\input ->
    concat [runParser (f x) rest | (x, rest) <- p input])

-- 4. Alternative Instance (Choice and Failure)
instance Alternative Parser where
  empty = Parser (\_ -> [])
  (Parser p1) <|> (Parser p2) = Parser (\input ->
    case p1 input of
      []  -> p2 input
      res -> res)

-- ==============================================================================
-- Primitive Combinators
-- ==============================================================================

-- | Consumes a single character if input is non-empty
item :: Parser Char
item = Parser (\input -> case input of
  []     -> []
  (c:cs) -> [(c, cs)])

-- | Parses a character satisfying a predicate
sat :: (Char -> Bool) -> Parser Char
sat p = do
  c <- item
  if p c then pure c else empty

-- | Exact character match
char :: Char -> Parser Char
char c = sat (== c)

-- | Exact string match
string :: String -> Parser String
string []     = pure []
string (c:cs) = do
  _ <- char c
  _ <- string cs
  pure (c:cs)

-- | Consumes optional leading whitespace
whitespace :: Parser ()
whitespace = do
  _ <- many (sat isSpace)
  pure ()

-- | Wraps a parser to ignore surrounding whitespace
token :: Parser a -> Parser a
token p = do
  whitespace
  x <- p
  whitespace
  pure x

-- ==============================================================================
-- Abstract Syntax Tree (AST) for Arithmetic Expressions
-- ==============================================================================

data Expr
  = Num Double
  | Add Expr Expr
  | Sub Expr Expr
  | Mul Expr Expr
  | Div Expr Expr
  deriving (Show, Eq)

-- | Evaluates the AST to a floating-point value
eval :: Expr -> Double
eval (Num n)   = n
eval (Add l r) = eval l + eval r
eval (Sub l r) = eval l - eval r
eval (Mul l r) = eval l * eval r
eval (Div l r) = eval l / eval r

-- ==============================================================================
-- Recursive Descent Grammar with Operator Precedence:
--   Expr   ::= Term (( '+' | '-' ) Term)*
--   Term   ::= Factor (( '*' | '/' ) Factor)*
--   Factor ::= '(' Expr ')' | Number
-- ==============================================================================

parseNumber :: Parser Expr
parseNumber = token (do
  digits <- some (sat isDigit)
  pure (Num (read digits)))

parseFactor :: Parser Expr
parseFactor =
  (do
    _ <- token (char '(')
    e <- parseExpr
    _ <- token (char ')')
    pure e)
  <|> parseNumber

parseTerm :: Parser Expr
parseTerm = do
  f <- parseFactor
  rest f
  where
    rest acc =
      (do
        _ <- token (char '*')
        f <- parseFactor
        rest (Mul acc f))
      <|> (do
        _ <- token (char '/')
        f <- parseFactor
        rest (Div acc f))
      <|> pure acc

parseExpr :: Parser Expr
parseExpr = do
  t <- parseTerm
  rest t
  where
    rest acc =
      (do
        _ <- token (char '+')
        t <- parseTerm
        rest (Add acc t))
      <|> (do
        _ <- token (char '-')
        t <- parseTerm
        rest (Sub acc t))
      <|> pure acc

-- ==============================================================================
-- Top-level Evaluation Driver
-- ==============================================================================

parseAndEval :: String -> Either String (Expr, Double)
parseAndEval input =
  case runParser parseExpr input of
    [(ast, "")] -> Right (ast, eval ast)
    [(_, unparsed)] -> Left ("Parsing error: unparsed trailing tokens: " ++ unparsed)
    [] -> Left ("Parsing syntax error on input: " ++ input)
    _  -> Left "Ambiguous grammar parse tree"

main :: IO ()
main = do
  putStrLn "================================================================="
  putStrLn "Haskell Monadic Parser Combinator (Hutton-Meijer Grammar Engine)"
  putStrLn "================================================================="
  
  let testCases =
        [ "3 + 5 * 2"
        , "(10 - 4) * (2 + 3)"
        , "100 / 2 / 5"
        , "42 + (8 * 3 - (6 / 2))"
        ]
  
  mapM_ runTest testCases
  where
    runTest exprStr = do
      putStrLn ("\nExpression: " ++ exprStr)
      case parseAndEval exprStr of
        Right (ast, val) -> do
          putStrLn ("  Parsed AST: " ++ show ast)
          putStrLn ("  Evaluation: " ++ show val)
        Left err -> putStrLn ("  Error: " ++ err)
