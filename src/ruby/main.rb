require 'ffi'

module GNOLL
  extend FFI::Library

  ffi_lib 'build/dice.so'
  attach_function :roll_and_write, [:string, :string], :void
end

module DiceNotation
  def self.roll(roll_str)
     # Clear File
     df = File.open('output.dice', 'r') do |f|
     File.delete(f)

     # GNOLL
     err_code = GNOLL.roll_and_write(roll_str, "output.dice")

     # Read output
     df = File.open("output.dice", "r")
     data = df.read
     puts data
  end
end

DiceNotation.roll("1d20")
