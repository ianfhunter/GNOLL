-- Load the FFI library
local ffi = require("ffi")

-- Load the shared library
local libdice = ffi.load("../../build/libdice.so")  -- Replace with the actual path to your library

-- Define the C function signature
ffi.cdef[[
    void roll_and_write(const char* param1, const char* param2);
]]

-- Function to call roll_and_write
local function call_roll_and_write(param1, param2)
    libdice.roll_and_write(param1, param2)
end

-- Example parameters
local param1 = "34d42"
local param2 = "output.txt"

-- Call the C function
call_roll_and_write(param1, param2)

-- Read the result from the output file
local file = io.open("output.txt", "r")
local result = file:read("*number")
file:close()

-- Print the result
print("Result from roll_and_write: " .. result)

if result and result > 33 then
    os.exit(0)
else
    os.exit(1)
end
