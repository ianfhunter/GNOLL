require 'ffi'

module GNOLL
  extend FFI::Library

  ffi_lib 'build/dice.so'
  attach_function :roll_and_write, [:string, :string], :void
end

module DiceNotation
  def self.roll(roll_str)
     filename = 'output.dice'

     # Clear File to avoid error
     File.delete(filename) if File.exist?(filename)

     # GNOLL
     GNOLL.roll_and_write(roll_str, filename)

     # Read output
     puts File.read(filename)
  end
end

DiceNotation.roll("1d20")
