"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0]*8 #stores 8 registers
        self.ram = [0]*256 # stores program on load
        self.pc = 0 #current address/location

    def load(self):
        """Load a program into memory."""
        program = sys.argv[1]
        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        if len(sys.argv) < 2:
            print('please pass in a second filename')
            sys.exit()
        try:
            address = 0
            with open(sys.argv[1]) as files:
                for line in files:
                    split_line = line.split('#')
                    command = split_line[0].strip()
                    if command == '':
                        continue
                    num_command = int(command, 2)

                    self.ram[address] = num_command
                    address += 1
        except FileNotFoundError:
            print(f'{sys.argv[0]}{sys.argv[1]}file was not found')
            sys.exit()



    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
                self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value):
        self.ram[address] = value

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
     
        while self.pc < len(self.ram):
            command = self.ram[self.pc]
            HLT = 0b00000001

            if command == HLT:  # stops program
                break

            if command == 0b10000010:  # registers the next line as the index inserting the line after that one as the value
                self.ram_write(self.ram[self.pc+1], self.ram[self.pc+2])

            if command == 0b01000111:  # prints next line
                print(self.ram_read(self.ram[self.pc+1]))

            if command == 0b10100010:  # multiplies the numbers of the indexes of the next 2 lines
                print(self.ram_read(self.ram[self.pc+1])
                      * self.ram_read(self.ram[self.pc+2]))

            self.pc += command >> 6
            self.pc += 1