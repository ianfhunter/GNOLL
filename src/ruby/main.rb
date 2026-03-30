require 'ffi'

module GNOLL
  extend FFI::Library

  ffi_lib 'build/dice.so'
  attach_function :roll_and_write, [:string, :string], :int
  attach_function :gnoll_validate_roll_request, [:string], :int
end

module DiceNotation
  def self.roll(roll_str)
     filename = 'output.dice'

     # Clear File to avoid error
     File.delete(filename) if File.exist?(filename)

     rc = GNOLL.gnoll_validate_roll_request(roll_str)
     raise "GNOLL validate error #{rc}" if rc != 0

     # GNOLL
     rc = GNOLL.roll_and_write(roll_str, filename)
     raise "GNOLL roll error #{rc}" if rc != 0

     # Read output
     puts File.read(filename)
  end
end

DiceNotation.roll("1d20")
