{-# LANGUAGE ForeignFunctionInterface #-}
{-# LANGUAGE BangPatterns #-}

module Main where
import System.Environment (getArgs)
import Control.Monad (when)
import Control.Monad.IO.Class (liftIO)
import System.IO (openTempFile, hClose, hGetLine)
import System.Directory (removeFile)
import Data.Either (fromLeft, fromRight)
import Foreign.C.Types
import Foreign.C.String

foreign import ccall "shared_header.h gnoll_validate_roll_request"
     c_gnoll_validate_roll_request :: CString -> CInt

foreign import ccall "shared_header.h roll_and_write"
     c_roll_and_write :: CString -> CString -> CInt

main :: IO ()
main = do
  args <- getArgs
  when (length args == 0) ( error "Needs one argument")
  roll (head args)

roll :: String -> IO ()
roll input = do
     putStrLn $ "Rolling: " ++ input
     let fileName = "gnoll_roll_die"
     (file, handle) <- openTempFile "/tmp" fileName
     putStrLn $ "File: " ++ file
     cstr1 <- newCString input
     cstr2 <- newCString file

     v <- c_gnoll_validate_roll_request cstr1
     when (v /= 0) ( error $ "GNOLL validate error: " ++ show v )

     -- call roll_and_write
     rc <- c_roll_and_write cstr1 cstr2
     when (rc /= 0) ( error $ "GNOLL roll error: " ++ show rc )

     -- get line from the file
     output <- hGetLine handle
     putStrLn ("Result: " ++ output)

     -- close handle 
     hClose handle
     -- delete /tmp/gnoll_roll_die* file
     removeFile file