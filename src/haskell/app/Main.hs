{-# LANGUAGE ForeignFunctionInterface #-}

module Main where
import System.Environment
import Control.Monad (when)
import Foreign.C.Types
import Foreign.C.String

foreign import ccall "shared_header.h roll"
     c_roll :: CString -> CInt

main :: IO ()
main = do
  args <- getArgs
  when (length args == 0) ( error "Needs one argument")
  putStrLn ("Running roll(" ++ head args ++ ")")
  cstr <- newCString (head args)
  let ans = c_roll cstr
  putStrLn (show ans)
