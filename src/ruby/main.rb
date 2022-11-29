require 'ffi'

module GNOLL
  extend FFI::Library

  ffi_lib 'build/dice.so'
  attach_function :roll_and_write, [:string, :string], :void
end

module DiceNotation
  def self.roll(roll_str)
     err_code = GNOLL.roll_and_write(roll_str, "output.dice")
  end
end

DiceNotation.roll("1d20")
