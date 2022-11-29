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
     err_code = GNOLL.roll_and_write(roll_str, filename)

     # Read output
     df = File.open(filename, "r") do |f|
       data = df.read
       puts data
     end
  end
end

DiceNotation.roll("1d20")
